from .base import BaseNotify


class FacebookNotify(BaseNotify):
    def notify(self) -> str:
        return super().notify() + ", also notified via Facebook"
