import math
from dataclasses import dataclass
from decimal import Decimal

from .interface import IShape


@dataclass
class CircleShape(IShape):
    radius: Decimal

    def area(self) -> Decimal:
        return Decimal(math.pow(self.radius, 2) * math.pi)
