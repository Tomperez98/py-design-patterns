import shutil
from pathlib import Path

import typer
from cookiecutter.main import cookiecutter


def move_new_pattern_folder(pattern_slug: str, base_dir: Path) -> None:

    try:
        (base_dir / "patterns" / pattern_slug).mkdir(
            parents=True, exist_ok=False
        )
    except FileExistsError:
        shutil.rmtree(base_dir / "patterns" / pattern_slug)

    (base_dir / pattern_slug).rename(base_dir / "patterns" / pattern_slug)


def move_test_file(pattern_slug: str, base_dir: Path) -> None:

    try:
        (base_dir / "tests" / pattern_slug).mkdir(parents=True, exist_ok=False)
    except FileExistsError:
        shutil.rmtree(base_dir / "tests" / pattern_slug)

    (base_dir / "tests" / pattern_slug).mkdir(parents=True, exist_ok=True)

    (base_dir / pattern_slug / "test_main.py").rename(
        base_dir / "tests" / pattern_slug / "test_main.py"
    )

    (base_dir / "tests" / pattern_slug / "__init__.py").touch()


def main(
    pattern_name: str = typer.Option(
        default=...,
        prompt="What's the name of the pattern you want to build",
        confirmation_prompt=False,
    )
):
    pattern_name = pattern_name.strip()

    pattern_slug = (
        pattern_name.strip().lower().replace(" ", "_").replace("-", "_")
    )
    pattern_name = pattern_name.capitalize()

    base_dir = Path(__file__).parent.parent
    new_pattern_template = (
        base_dir / "scripts" / "resources" / "new_pattern.zip"
    )

    cookiecutter(
        str(new_pattern_template),
        extra_context={
            "pattern_name": pattern_name,
            "project_slug": pattern_slug,
        },
        no_input=True,
        overwrite_if_exists=True,
    )

    move_test_file(pattern_slug=pattern_slug, base_dir=base_dir)

    move_new_pattern_folder(pattern_slug=pattern_slug, base_dir=base_dir)


if __name__ == "__main__":
    typer.run(main)
