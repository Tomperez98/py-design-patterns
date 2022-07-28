from .base import BaseNotify


class SMSNotify(BaseNotify):
    def notify(self) -> str:
        return super().notify() + ", also notified via SMS"
