from abc import ABC, abstractmethod
from decimal import Decimal


class IShape(ABC):
    @abstractmethod
    def area(self) -> Decimal:
        pass
