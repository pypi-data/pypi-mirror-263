import typer
from typing_extensions import Annotated

app = typer.Typer()


@app.command(name='new')
def new(file: Annotated[str, typer.Option(help='name of config.')]) -> None:
    """
    Generate new config file.
    """
    print(f'Hello {file}')


@app.command('check')
def check(file: str) -> None:
    """
    Validate config consistency.
    :param file: name of config
    """
    print(f'validate {file}')


def main():
    app()


if __name__ == "__main__":
    main()


def func1(a: int, b: int):
    return a + b
