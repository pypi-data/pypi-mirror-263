from __future__ import annotations
import os
from dataclasses import dataclass
import serde.yaml

CONFIG_FILE = os.path.expanduser("~/.config/noti2.yaml")
INSTANCE = None

@dataclass
class NotiConfig:
    slack_webhook_url: str

    @staticmethod
    def get_instance() -> NotiConfig:
        global INSTANCE
        if INSTANCE is None:
            INSTANCE = NotiConfig.load()
        return INSTANCE

    @staticmethod
    def load() -> NotiConfig:
        obj = serde.yaml.deser(CONFIG_FILE)
        return NotiConfig(slack_webhook_url=obj["slack_webhook_url"])
    
    def save(self) -> None:
        serde.yaml.ser({
            "slack_webhook_url": self.slack_webhook_url
        }, CONFIG_FILE)



