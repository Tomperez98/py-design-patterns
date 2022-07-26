from abc import ABC, abstractmethod


class IPunchBehavior(ABC):
    @abstractmethod
    def punch(self) -> str:
        pass
