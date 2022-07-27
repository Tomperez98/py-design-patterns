from .interface import IPunchBehavior


class SoftPunchBehavior(IPunchBehavior):
    def punch(self) -> str:
        return "Soft punch"
