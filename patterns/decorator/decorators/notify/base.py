from dataclasses import dataclass

from .interface import INotify


@dataclass
class BaseNotify(INotify):
    _wrappe: INotify

    def notify(self) -> str:
        return self.wrappe.notify()

    @property
    def wrappe(self) -> INotify:
        return self._wrappe
