#!/usr/bin/env python

import logging
import shlex
import os
import click
import sys

from .metadata_utils import lab_version
from .docker import (
    DockerDaemonInfo,
    RootlessDockerContainer,
    DockerRunBuilder,
    ROOTLESS_DOCKER_NAME
)


def loglevel() -> str:
    return os.environ.get('LOGLEVEL', 'INFO').upper()


logging.basicConfig(level=loglevel())


DISPLAY = os.environ.get('DISPLAY', '')
WORKSPACE = os.environ['LAB_WORKSPACE']
WORKSPACE_DATA = os.path.join(WORKSPACE, 'data')
NETWORK_NAME = 'lab'


@click.command()
def start_cli():
    docker_daemon_info = DockerDaemonInfo.build()
    if not docker_daemon_info.network_exists(NETWORK_NAME):
        docker_daemon_info.create_network(NETWORK_NAME)

    rootless = RootlessDockerContainer(ROOTLESS_DOCKER_NAME, docker_daemon_info)
    if not docker_daemon_info.is_rootless():
        docker_daemon_info = rootless.start_rootless_container(WORKSPACE, NETWORK_NAME)

    cli_cmd = DockerRunBuilder(f'enclarify/lab-partner-cli:{lab_version()}')
    cli_cmd.options() \
        .with_tty() \
        .with_env('ENVIRONMENT', 'LOCAL') \
        .with_env('HOST_DOCKER_SOCKET', docker_daemon_info.docker_internal_socket()) \
        .with_env('LAB_WORKSPACE', os.environ.get('LAB_WORKSPACE')) \
        .with_env('LAB_WORKSPACE', WORKSPACE) \
        .with_env('LAB_WORKSPACE_DATA', WORKSPACE_DATA) \
        .with_env('LAB_NETWORK_NAME', NETWORK_NAME) \
        .with_env('LAB_VERSION', lab_version()) \
        .with_home_dir_bind_mount('.gitconfig', '/opt/lab/home/.gitconfig') \
        .with_home_dir_bind_mount('.vim', '/opt/lab/home/.vim') \
        .with_home_dir_bind_mount('.vimrc', '/opt/lab/home/.vimrc') \
        .with_home_dir_bind_mount('.actrc', '/opt/lab/home/.actrc') \
        .with_home_dir_bind_mount('.aws', '/opt/lab/home/.aws') \
        .with_home_dir_bind_mount('.ssh', '/opt/lab/home/.ssh') \
        .with_bind_mount(WORKSPACE, WORKSPACE) \
        .with_bind_mount('/opt/lab/cicd/artifacts', '/opt/lab/cicd/artifacts') \
        .with_bind_mount(docker_daemon_info.docker_socket(), '/var/run/docker.sock') \
        .with_workdir(WORKSPACE)

    cmd = shlex.split(cli_cmd.build())
    os.execvpe(cmd[0], cmd, {'DOCKER_HOST': f'unix://{docker_daemon_info.docker_socket()}'})


if __name__ == '__main__':
    start_cli()
