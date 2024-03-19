import importlib.metadata
import sys

import click

from noti.pypi import PyPI

from loguru import logger

from noti.slack import send_slack
try:
    version = importlib.metadata.version("noti2")
except importlib.metadata.PackageNotFoundError:
    version = "0.0.0"


def check_upgrade():
    latest_version = PyPI.get_instance().get_latest_version("noti2")
    if latest_version is not None and version != latest_version:
        logger.warning(
            f"You are using an outdated version of noti (noti2). The latest version is {latest_version}, while you are using {version}."
        )
    else:
        logger.trace("You are using the latest version of noti (noti2).")




@click.group(
    help=f"Noti ({version}) -- a simple notification tool for long-running tasks"
)
@click.version_option(version)
def cli():
    check_upgrade()


cli.add_command(send_slack, name='slack')

if __name__ == "__main__":
    cli()

