from abc import ABC, abstractmethod


class INotify(ABC):
    @abstractmethod
    def notify(self) -> str:
        pass
