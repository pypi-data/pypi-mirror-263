import typer
from typing_extensions import Annotated
from typing import Optional
import importlib.metadata

def main(command: Annotated[Optional[str], typer.Argument()] = None,
         version: Annotated[bool, typer.Option(help="Output the version number")] = False):
    if version:
        print(importlib.metadata.metadata('goshawk')["Version"])
    if command:
        print(f"The command is {command}")
    else:
        print("No command supplied")    

def run():
    typer.run(main)

if __name__ == "__main__":
    run()
