from .main import ExerciseResults, Person
from .strategies.jump import HighJumpBehavior, LowJumpBehavior
from .strategies.jump.interface import IJumpBehavior
from .strategies.punch import HardPunchBehavior, SoftPunchBehavior
from .strategies.punch.interface import IPunchBehavior
from .strategies.run import FastRunBehavior, SlowRunBehavior
from .strategies.run.interface import IRunBehavior

__all__ = [
    "Person",
    "HighJumpBehavior",
    "IJumpBehavior",
    "LowJumpBehavior",
    "HardPunchBehavior",
    "SoftPunchBehavior",
    "FastRunBehavior",
    "SlowRunBehavior",
    "IPunchBehavior",
    "IRunBehavior",
    "ExerciseResults",
]
