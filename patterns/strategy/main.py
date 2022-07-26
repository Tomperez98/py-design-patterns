from dataclasses import dataclass

from .strategies import IJumpBehavior, IPunchBehavior, IRunBehavior


@dataclass
class ExerciseResults:
    jump_perfomance: str
    punch_performance: str
    run_performance: str


@dataclass
class Person:
    jump: IJumpBehavior
    punch: IPunchBehavior
    run: IRunBehavior

    def exercise(self) -> ExerciseResults:
        jump_performance = self.jump.jump()
        punch_performance = self.punch.punch()
        run_performance = self.run.run()
        return ExerciseResults(
            jump_perfomance=jump_performance,
            punch_performance=punch_performance,
            run_performance=run_performance,
        )
