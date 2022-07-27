from .base import BaseNotify


class SlackNotify(BaseNotify):
    def notify(self) -> str:
        return super().notify() + ", also notified via Slack"
