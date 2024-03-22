import importlib.metadata
from typing import List, Optional

import typer
from typing_extensions import Annotated

app = typer.Typer()


def main(
    command: Annotated[Optional[str], typer.Argument()] = None,
    version: Annotated[bool, typer.Option(help="Output the version number")] = False,
) -> None:
    if version:
        print(importlib.metadata.metadata("goshawk")["Version"])
    if command:
        print(f"The command is {command}")
    else:
        print("No command supplied")


@app.command()
def view_model_tree(mask: Annotated[Optional[List[str]], typer.Option(help="Mask to deploy")] = None) -> None:
    print("View model tree")


@app.command()
def data_refresh(
    db_env: Annotated[str, typer.Option(help="Name of db environment")] = "",
    mask: Annotated[Optional[List[str]], typer.Option(help="Mask to deploy")] = None,
) -> None:
    print("Data refresh")


@app.command()
def model_deploy(
    db_env: Annotated[str, typer.Option(help="Name of db environment")] = "",
    mask: Annotated[Optional[List[str]], typer.Option(help="Mask to deploy")] = None,
) -> None:
    print(f"Model deploy dbenv={db_env},mask={mask} ")


@app.command()
def init_env(envname: str) -> None:
    print(f"Creating environment: {envname}")


@app.command()
def destroy_env(envname: str) -> None:
    print(f"Destroying environment: {envname}")


if __name__ == "__main__":
    app()
