from typing import Type

import pytest

from patterns import state


@pytest.mark.parametrize(
    "initial_state, action, expected_state",
    [
        (
            state.OpenDoorState,
            "pay_ok",
            state.OpenDoorState,
        ),
        (
            state.OpenDoorState,
            "enter",
            state.CloseDoorState,
        ),
        (
            state.OpenDoorState,
            "pay_failed",
            state.OpenDoorState,
        ),
        (
            state.CloseDoorState,
            "pay_failed",
            state.CloseDoorState,
        ),
        (
            state.CloseDoorState,
            "enter",
            state.CloseDoorState,
        ),
        (
            state.CloseDoorState,
            "pay_ok",
            state.OpenDoorState,
        ),
    ],
)
def test_pattern_name(
    initial_state: Type[state.BaseDoorState],
    action: str,
    expected_state: Type[state.BaseDoorState],
):
    door = state.GlassDoor()
    door.change_state(new_state=initial_state(door=door))
    if action == "pay_ok":
        door.pay_ok()
    elif action == "enter":
        door.enter()
    elif action == "pay_failed":
        door.pay_failed()

    assert isinstance(door.state, expected_state)
