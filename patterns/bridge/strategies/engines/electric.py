from .interface import IEngine


class ElectricEngine(IEngine):
    def charge_engine(self) -> str:
        return "Charged in an hour"
