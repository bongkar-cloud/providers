import typer
from pprint import pp

from data import *
from data.filters import filter_cloud_provider

def get_cloud_by_provider(name: str):
  print(f"Services for {name}:")
  pp(
    filter_cloud_provider(name),
    indent=4
  )

if __name__ == "__main__":
    typer.run(get_cloud_by_provider)