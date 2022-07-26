import pytest

from patterns import strategy


@pytest.mark.parametrize(
    "run_strategy, jump_strategy, punch_strategy, expected_performance",
    [
        (
            strategy.FastRunBehavior(),
            strategy.HighJumpBehavior(),
            strategy.SoftPunchBehavior(),
            strategy.ExerciseResults(
                jump_perfomance="Jumping high!",
                punch_performance="Soft punch",
                run_performance="Wow that was fast!",
            ),
        ),
        (
            strategy.SlowRunBehavior(),
            strategy.HighJumpBehavior(),
            strategy.SoftPunchBehavior(),
            strategy.ExerciseResults(
                jump_perfomance="Jumping high!",
                punch_performance="Soft punch",
                run_performance="Too slow",
            ),
        ),
        (
            strategy.SlowRunBehavior(),
            strategy.LowJumpBehavior(),
            strategy.SoftPunchBehavior(),
            strategy.ExerciseResults(
                jump_perfomance="Jumping low...",
                punch_performance="Soft punch",
                run_performance="Too slow",
            ),
        ),
        (
            strategy.SlowRunBehavior(),
            strategy.LowJumpBehavior(),
            strategy.HardPunchBehavior(),
            strategy.ExerciseResults(
                jump_perfomance="Jumping low...",
                punch_performance="Hard punch",
                run_performance="Too slow",
            ),
        ),
    ],
)
def test_pattern_name(
    run_strategy: strategy.IRunBehavior,
    jump_strategy: strategy.IJumpBehavior,
    punch_strategy: strategy.IPunchBehavior,
    expected_performance: strategy.ExerciseResults,
):
    a_person = strategy.Person(
        jump=jump_strategy, punch=punch_strategy, run=run_strategy
    )
    assert a_person.exercise() == expected_performance
