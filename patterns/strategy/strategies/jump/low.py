from .interface import IJumpBehavior


class LowJumpBehavior(IJumpBehavior):
    def jump(self) -> str:
        return "Jumping low..."
