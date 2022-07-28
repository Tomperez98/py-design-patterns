from abc import ABC, abstractmethod


class IJumpBehavior(ABC):
    @abstractmethod
    def jump(self) -> str:
        pass
