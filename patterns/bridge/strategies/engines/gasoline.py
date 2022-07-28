from .interface import IEngine


class GasolineEngine(IEngine):
    def charge_engine(self) -> str:
        return "The fuel is so expensive"
