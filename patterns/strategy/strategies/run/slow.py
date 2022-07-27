from .interface import IRunBehavior


class SlowRunBehavior(IRunBehavior):
    def run(self) -> str:
        return "Too slow"
