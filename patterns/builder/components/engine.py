from __future__ import annotations

import dataclasses
import decimal


@dataclasses.dataclass
class Engine:
    volume: decimal.Decimal
    mileage: decimal.Decimal
    started: bool = dataclasses.field(init=False, default=False)

    def on(self) -> None:
        self.started = True

    def off(self) -> None:
        self.started = False

    def is_started(self) -> bool:
        return self.started

    def go(self, mileage: decimal.Decimal) -> None:
        if self.is_started():
            self.mileage += mileage
        else:
            raise Exception
