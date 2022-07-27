from .interface import IPunchBehavior


class HardPunchBehavior(IPunchBehavior):
    def punch(self) -> str:
        return "Hard punch"
