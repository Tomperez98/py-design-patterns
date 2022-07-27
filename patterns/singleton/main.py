from dataclasses import dataclass
from typing import Dict


def is_singleton(cls):
    _instances: Dict = {}

    def get_instance(*args, **kwargs):
        if cls in _instances:
            raise Exception(
                "This class is a singleton. Use the already created instance"
                " or delete it before instanciating a new one"
            )
        if cls not in _instances:
            _instances[cls] = cls(*args, **kwargs)
        return _instances[cls]

    return get_instance


@is_singleton
@dataclass
class DatabaseManager:
    database_url: str

    def connect(self) -> str:
        return "Conecting to database..."
