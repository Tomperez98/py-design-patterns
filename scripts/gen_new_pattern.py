from pathlib import Path

import typer
from cookiecutter.main import cookiecutter


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
    )


if __name__ == "__main__":
    typer.run(main)
