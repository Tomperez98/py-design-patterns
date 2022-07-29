from __future__ import annotations

import abc
import dataclasses


class _DoorStateActivities(abc.ABC):
    """
    Defines all possible actions to manage BaseDoor objects as State Machines
    """

    @abc.abstractmethod
    def pay_ok(self) -> None:
        pass

    @abc.abstractmethod
    def enter(self) -> None:
        pass

    @abc.abstractmethod
    def pay_failed(self) -> None:
        pass


@dataclasses.dataclass
class BaseDoorState(_DoorStateActivities, abc.ABC):
    """
    BaseDoorState abstract class that is implemented by different
    states

    Args:
        door (BaseDoor): Reference to door with current state
    """

    door: BaseDoor


class OpenDoorState(BaseDoorState):
    """
    OpenDoorState implementation
    """

    def pay_failed(self) -> None:
        """
        When Door is Open and pay fails
        """
        self.door.change_state(new_state=OpenDoorState(door=self.door))

    def pay_ok(self) -> None:
        """
        When Door is Open and pay is OK
        """
        self.door.change_state(new_state=OpenDoorState(door=self.door))

    def enter(self) -> None:
        """
        When Door is Open and door is entered
        """
        self.door.change_state(new_state=CloseDoorState(door=self.door))


class CloseDoorState(BaseDoorState):
    """
    CloseDoorState implementation
    """

    def pay_failed(self) -> None:
        """
        When Door is Closed and pay fails
        """
        self.door.change_state(new_state=CloseDoorState(door=self.door))

    def pay_ok(self) -> None:
        """
        When Door is Closed and pay is OK
        """
        self.door.change_state(new_state=OpenDoorState(door=self.door))

    def enter(self) -> None:
        """
        When Door is Closed and door is entered
        """
        self.door.change_state(new_state=CloseDoorState(door=self.door))


@dataclasses.dataclass
class BaseDoor(_DoorStateActivities, abc.ABC):
    state: BaseDoorState = dataclasses.field(init=False)

    def __post_init__(self):
        self.state = CloseDoorState(door=self)

    def change_state(self, new_state: BaseDoorState):
        self.state = new_state

    def pay_failed(self) -> None:
        return self.state.pay_failed()

    def pay_ok(self) -> None:
        return self.state.pay_ok()

    def enter(self) -> None:
        return self.state.enter()
