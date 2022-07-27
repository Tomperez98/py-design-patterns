from abc import ABC, abstractmethod


class IRunBehavior(ABC):
    @abstractmethod
    def run(self) -> str:
        pass
