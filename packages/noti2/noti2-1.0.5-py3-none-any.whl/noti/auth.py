import getpass
import click
from noti.config import NotiConfig, CONFIG_FILE

@click.command()
def auth():
    slack_webhook_url = getpass.getpass("Enter the slack webhook url: ")
    slack_webhook_url = slack_webhook_url.strip()

    # now we need to save this url to a file.
    print(f"Save the hook URL to: {CONFIG_FILE}")
    NotiConfig(slack_webhook_url=slack_webhook_url).save()


if __name__ == "__main__":
    auth()
