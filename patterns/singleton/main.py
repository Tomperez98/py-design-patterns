from dataclasses import dataclass
from typing import Dict


class Singleton(type):
    _instances: Dict = {}

    def __call__(cls, *args, **kwargs):

        if cls in cls._instances:
            raise Exception(
                "This class is a singleton. Use the already created instance "
                "or delete it before instanciating a new one"
            )
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(
                *args, **kwargs
            )

        return cls._instances[cls]


@dataclass
class DatabaseManager(metaclass=Singleton):
    database_url: str

    def connect(self) -> str:
        return "Conecting to database..."
