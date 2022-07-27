from .interface import IJumpBehavior


class HighJumpBehavior(IJumpBehavior):
    def jump(self) -> str:
        return "Jumping high!"
