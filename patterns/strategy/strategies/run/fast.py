from .interface import IRunBehavior


class FastRunBehavior(IRunBehavior):
    def run(self) -> str:
        return "Wow that was fast!"
