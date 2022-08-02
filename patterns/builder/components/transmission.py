from __future__ import annotations

import enum


class Transmission(str, enum.Enum):
    MANUAL = "MANUAL"
    AUTOMATIC = "AUTOMATIC"
    SEMI_AUTOMATIC = "SEMI_AUTOMATIC"
