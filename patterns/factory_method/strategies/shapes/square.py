from dataclasses import dataclass
from decimal import Decimal

from .interface import IShape


@dataclass
class SquareShape(IShape):
    side: Decimal

    def area(self) -> Decimal:
        return self.side * self.side
