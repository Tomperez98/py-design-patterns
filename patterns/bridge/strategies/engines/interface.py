from abc import ABC, abstractmethod


class IEngine(ABC):
    @abstractmethod
    def charge_engine(self) -> str:
        pass
