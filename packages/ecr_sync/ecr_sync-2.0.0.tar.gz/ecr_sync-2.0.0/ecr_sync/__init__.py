# pylint: disable = missing-module-docstring
from typing import List, Optional
from dataclasses import dataclass
from concurrent.futures import ThreadPoolExecutor

import time
import base64
import fnmatch
import json
import os
import subprocess
import sys
import boto3
import click

from mypy_boto3_ecr_public import ECRPublicClient
from mypy_boto3_ecr import ECRClient
from mypy_boto3_ecr.type_defs import RepositoryTypeDef


@dataclass()
class Context:
    """
    Cli context object.
    Represents the context for ECR synchronization.

    Attributes:
        client (ECRPublicClient | ECRClient): The ECR client to use for synchronization.
        registry_id (str): The ID of the ECR registry.
        override_os (str): The override operating system for synchronization.
        override_arch (str): The override architecture for synchronization.
        verbose (bool): Flag indicating whether to display verbose output.
        dry_run (bool): Flag indicating whether to perform a dry run without making any changes.
        debug (bool): Flag indicating whether to enable debug mode.
        public (bool): Flag indicating whether to synchronize with the public ECR registry.
        docker_username (str): The username for authenticating with the Docker registry.
        docker_password (str): The password for authenticating with the Docker registry.
        threads (int): The number of threads to use for synchronization.
    """
    client: ECRPublicClient | ECRClient
    registry_id: str
    override_os: str
    override_arch: str
    verbose: bool
    dry_run: bool
    debug: bool
    public: bool
    docker_username: str
    docker_password: str
    threads: int


@dataclass()
class MirroredRepo:
    """
    Represents a mirrored repository.

    Attributes:
        upstream_image (str): The name of the upstream image.
        repository_uri (str): The URI of the mirrored repository.
        upstream_tags (List[str]): A list of tags from the upstream repository.
        ignore_tags (List[str]): A list of tags to ignore during synchronization.
    """
    upstream_image: str
    repository_uri: str
    upstream_tags: List[str]
    ignore_tags: List[str]


@click.group()
@click.option(
    "--registry-id",
    "--reg",
    required=True,
    help="The registry ID. This is usually your AWS account ID.",
)
@click.option("--role-name", help="Assume a specific role to push to AWS")
@click.option(
    "--override-os",
    default="linux",
    help='Specify the OS of images, default to "linux"',
)
@click.option(
    "--override-arch",
    type=click.Choice(["amd64", "arm64", "windows-amd64", "all"]),
    default="amd64",
    help='Specify the ARCH of images, default to "amd64". If set to "all" - all architectures will be synced',
)
@click.option("--profile-name", help="The name of the AWS profile to use")
@click.option("--verbose", is_flag=True, help="Enable verbose output")
@click.option("--dry-run", is_flag=True, help="Enable dry run")
@click.option("--debug", is_flag=True, help="Enable debug output")
@click.option("--public", is_flag=True, help="Use ECR Public instead of ECR")
@click.option("--docker-username", help="The username to use for docker login")
@click.option("--docker-password", help="The password to use for docker login")
@click.option(
    "--threads", default=5, help="The number of threads to use for copying images"
)
@click.pass_context
def cli(
    ctx,
    registry_id,
    profile_name,
    role_name,
    override_os,
    override_arch,
    public,
    verbose,
    dry_run,
    debug,
    docker_username,
    docker_password,
    threads,
):
    """
    Click entrypoint.
    Synchronize OCI Docker repositories to ECR using ECR tags.
    """
    service_name = "ecr" if not public else "ecr-public"

    # Authenticate
    if not profile_name:
        print("No profile name specified. Falling back to environment variables.")
        if "AWS_ACCESS_KEY_ID" not in os.environ:
            raise ValueError(
                "No AWS_ACCESS_KEY_ID environment variable set. Please set credentials or use Profile name."
            )
        my_session = boto3.Session(
            aws_access_key_id=os.environ["AWS_ACCESS_KEY_ID"],
            aws_secret_access_key=os.environ["AWS_SECRET_ACCESS_KEY"],
            aws_session_token=os.environ["AWS_SESSION_TOKEN"],
        )
    else:
        my_session = boto3.session.Session(profile_name=profile_name)

    # Assume the desired role
    if role_name:
        print(f"Assuming role {role_name}")
        sts_connection = my_session.client("sts")
        account_id = sts_connection.get_caller_identity()["Account"]
        assumed_role_object = sts_connection.assume_role(
            RoleArn=f"arn:aws:iam::{account_id}:role/{role_name}",
            RoleSessionName=f"ecr-mirror{role_name}@{account_id}",
        )["Credentials"]
        my_session = boto3.Session(
            aws_access_key_id=assumed_role_object["AccessKeyId"],
            aws_secret_access_key=assumed_role_object["SecretAccessKey"],
            aws_session_token=assumed_role_object["SessionToken"],
        )
    client = my_session.client(service_name)

    ctx.obj = Context(
        client=client,
        registry_id=registry_id,
        override_os=override_os,
        override_arch=override_arch,
        verbose=verbose,
        dry_run=dry_run,
        debug=debug,
        public=public,
        docker_username=docker_username,
        docker_password=docker_password,
        threads=threads,
    )


@cli.command()
@click.pass_context
def sync(ctx):
    """
    Synchronize OCI Docker repository to ECR using ECR tags. Image tags, that are not already in the destination will be copied.
    """
    repositories = find_repositories(ctx.obj.client, ctx.obj.registry_id)
    copy_repositories(ctx.obj.client, ctx.obj.registry_id, list(repositories))


@cli.command()
@click.argument("source")
@click.argument("destination-repository")
@click.pass_context
def copy(ctx, source, destination_repository):
    """
    Copy all tags that match a given glob expression into ECR
    """
    upstream_image, upstream_tag = source.split(":")
    repositories = [
        MirroredRepo(
            upstream_image=upstream_image,
            upstream_tags=[upstream_tag],
            repository_uri=destination_repository,
            ignore_tags=[],
        )
    ]
    copy_repositories(ctx.obj.client, ctx.obj.registry_id, repositories)


@cli.command()
@click.pass_context
def list_repos(ctx):
    """
    List all repositories that will be synced
    """
    click.echo("Repositories to mirror:")
    for repo in find_repositories(ctx.obj.client, ctx.obj.registry_id):
        click.secho(f"- upstream: {repo.upstream_image}", fg="green")
        click.secho(f"  mirror: {repo.repository_uri}", fg="red")
        if repo.upstream_tags:
            click.secho(f"  tags: {repo.upstream_tags}", fg="yellow")


@click.pass_context
def ecr_login(ctx, client: ECRPublicClient | ECRClient, registry_id: str) -> str:
    """
    Authenticate with ECR, returning a `username:password` pair
    """
    if ctx.obj.public:
        auth_response = client.get_authorization_token()["authorizationData"][
            "authorizationToken"
        ].encode()
    else:
        auth_response = client.get_authorization_token(registryIds=[registry_id])[
            "authorizationData"
        ][0]["authorizationToken"].encode()

    return base64.decodebytes(auth_response).decode()


@click.pass_context
def copy_repositories(
    ctx,
    client: ECRPublicClient | ECRClient,
    registry_id: str,
    repositories: List[MirroredRepo],
):
    """
    Perform the actual, concurrent copy of the images
    """
    token = ecr_login(client, registry_id)
    click.echo("Finding all tags to copy...")

    # destination repository tags. This is a dictionary with the key being the repository uri and the value being a list of tags
    destination_tags = {
        repo.repository_uri: get_repo_tags(repo.repository_uri) for repo in repositories
    }

    items = [
        (repo, tag)
        for repo in repositories
        for tag in find_tags_to_copy(
            repo.upstream_image, repo.upstream_tags, repo.ignore_tags
        )
    ]

    items_to_copy = []

    # remove items that are exist in the destination repository
    for item in items:
        if item[0].repository_uri in destination_tags:
            # pylint: disable = W0106
            if item[1] in destination_tags[item[0].repository_uri]:
                (
                    click.echo(f"Removing {item[1]} from list of tags to copy")
                    if ctx.obj.verbose
                    else None
                )
            else:
                items_to_copy.append(item)

    if items_to_copy:
        click.echo(f"Beginning the copy of {len(items_to_copy)} images")
    else:
        click.echo("No images to copy")
        return

    with ThreadPoolExecutor(max_workers=ctx.obj.threads) as pool:
        # This code aint' beautiful, but whatever 🤷‍
        pool.map(
            lambda item: copy_image(
                ctx.obj,
                f"{item[0].upstream_image}:{item[1]}",
                f"{item[0].repository_uri}:{item[1]}",
                token,
                sleep_time=1,
            ),
            items_to_copy,
        )


@click.pass_context
def get_repo_tags(ctx: click.Context, repo_name: str) -> List[str]:
    """
    Get all tags for a given repository
    """
    cmd = [
        "skopeo",
        "list-tags",
        f"docker://{repo_name}",
        f"--override-os={ctx.obj.override_os}",
    ]
    if ctx.obj.override_arch != "all":
        cmd = cmd + [f"--override-arch={ctx.obj.override_arch}"]
    output = subprocess.check_output(cmd)
    all_tags = json.loads(output)["Tags"]

    return all_tags


def copy_image(ctx: Context, source_image, dest_image, token, sleep_time):
    """
    Copy a single image using Skopeo
    """
    click.echo(
        f"Copying {click.style(source_image, fg='green')} to {click.style(dest_image, fg='blue')}"
    )
    args = [
        "skopeo",
        "copy",
        f"--dest-creds={token}",
        f"docker://{source_image}",
        f"docker://{dest_image}",
        f"--override-os={ctx.override_os}",
    ]

    if ctx.docker_username and ctx.docker_password:
        args.insert(2, f"--src-creds={ctx.docker_username}:{ctx.docker_password}")
    if ctx.dry_run:
        args = args + ["--dry-run"]
    if ctx.override_arch == "all":
        args = args + ["--multi-arch=all"]
    else:
        args = args + [f"--override-arch={ctx.override_arch}"]
    try:
        subprocess.check_output(args, stderr=subprocess.STDOUT)
    except subprocess.CalledProcessError as e:
        click.secho(f'{" ".join(args)} raised an error: {e.returncode}', fg="red")
        click.secho(f"Last output: {e.output[100:]}", fg="red")

    time.sleep(sleep_time)


def find_tags_to_copy(image_name, tag_patterns, ignore_tags):
    """
    Use Skopeo to list all available tags for an image
    """
    all_tags = get_repo_tags(image_name)

    def does_match(tag):
        any_matches = any(fnmatch.fnmatch(tag, pattern) for pattern in tag_patterns)
        any_negates = any(fnmatch.fnmatch(tag, pattern) for pattern in ignore_tags)

        # Copy all tags if only ignored tags are given
        if not tag_patterns and not any_negates:
            return True

        # Else if something has negated it, skip
        if any_negates:
            return False

        return any_matches

    yield from (tag for tag in all_tags if does_match(tag))


def find_repositories(client: ECRPublicClient | ECRClient, registry_id: str):
    """
    List all ECR repositories that have an `upstream-image` tag set.
    """
    paginator = client.get_paginator("describe_repositories")
    all_repositories = [
        repo
        for result in paginator.paginate(registryId=registry_id)
        for repo in result["repositories"]
    ]

    def filter_repo(repo: RepositoryTypeDef) -> Optional[MirroredRepo]:
        tags = client.list_tags_for_resource(resourceArn=repo["repositoryArn"])
        tags_dict = {tag_item["Key"]: tag_item["Value"] for tag_item in tags["tags"]}

        if "upstream-image" in tags_dict:
            return MirroredRepo(
                upstream_image=tags_dict["upstream-image"],
                upstream_tags=tags_dict.get("upstream-tags", "")
                .replace("+", "*")
                .split("/"),
                ignore_tags=tags_dict.get("ignore-tags", "")
                .replace("+", "*")
                .split("/"),
                repository_uri=repo["repositoryUri"],
            )

    with ThreadPoolExecutor() as pool:
        for item in pool.map(filter_repo, all_repositories):
            if item is not None:
                yield item

# pylint: disable = missing-module-docstring
if __name__ == "__main__":
    #pylint: disable = no-value-for-parameter
    cli()
    sys.exit(0)
