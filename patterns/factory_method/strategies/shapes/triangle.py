from dataclasses import dataclass
from decimal import Decimal

from .interface import IShape


@dataclass
class TriangleShape(IShape):
    base: Decimal
    height: Decimal

    def area(self) -> Decimal:
        return self.base * self.height * Decimal(0.5)
