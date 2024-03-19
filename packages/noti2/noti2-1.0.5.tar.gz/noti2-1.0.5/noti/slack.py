import socket
import time
from contextlib import contextmanager

import click
import requests

from noti.config import NotiConfig

DEFAULT_MSG = "Task completed"


class Slack:
    def __init__(self, prefix: str = ""):
        self.noti = NotiConfig.load()
        self.prefix = prefix
        if len(self.prefix) > 0:
            self.prefix += " "

    @contextmanager
    def watch(self, msg: str = DEFAULT_MSG):
        start = time.time()
        try:
            yield None
        finally:
            end = time.time()
            self(f"{msg} (took {end - start:.2f}s)")

    def __call__(self, msg: str = DEFAULT_MSG):
        requests.post(self.noti.slack_webhook_url, json={"text": self.prefix + msg})


slack = Slack(prefix=f"`{socket.gethostname()}`")


@click.command()
@click.argument("msg", nargs=-1)
def send_slack(msg: list[str]):
    if len(msg) == 0:
        slack(DEFAULT_MSG)
    else:
        slack(" ".join(msg))


if __name__ == "__main__":
    send_slack()
