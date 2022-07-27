from dataclasses import dataclass
from typing import Dict


def is_singleton(cls):
    instances: Dict = {}

    def get_instance(*args, **kwargs):
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]

    return get_instance


@is_singleton
@dataclass
class DatabaseManager:
    database_url: str

    def connect(self) -> str:
        return "Conecting to database..."
