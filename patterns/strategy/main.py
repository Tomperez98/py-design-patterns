from dataclasses import dataclass

from .strategies import IJumpBehavior, IPunchBehavior, IRunBehavior


@dataclass
class ExerciseResults:
    jump_perfomance: str
    punch_performance: str
    run_performance: str


@dataclass
class Person:
    jump_strategy: IJumpBehavior
    punch_strategy: IPunchBehavior
    run_strategy: IRunBehavior

    def exercise(self) -> ExerciseResults:
        jump_performance = self.jump_strategy.jump()
        punch_performance = self.punch_strategy.punch()
        run_performance = self.run_strategy.run()
        return ExerciseResults(
            jump_perfomance=jump_performance,
            punch_performance=punch_performance,
            run_performance=run_performance,
        )
