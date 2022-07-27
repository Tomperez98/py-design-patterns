from .decorators import INotify


class BusinessProcess(INotify):
    def execute(self) -> str:
        return "Executing some business process"

    def notify(self) -> str:
        return "Default notification of the business process"
