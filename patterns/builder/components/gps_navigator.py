from __future__ import annotations

import dataclasses


@dataclasses.dataclass
class GPSNavigator:
    route: str = dataclasses.field(
        init=False,
        default=(
            "221b, Baker Street, London  to Scotland Yard, "
            "8-10 Broadway, London"
        ),
    )
