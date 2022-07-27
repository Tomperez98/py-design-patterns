from .base import BaseNotify


class WhatsAppNotify(BaseNotify):
    def notify(self) -> str:
        return super().notify() + ", also notified via WhatsApp"
