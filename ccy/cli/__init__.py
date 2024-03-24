import click
import pandas as pd
from rich.console import Console

import ccy

from .console import df_to_rich


@click.group()
def ccys() -> None:
    """Currency commands."""


@ccys.command()
def show() -> None:
    """Show table with all currencies."""
    df = pd.DataFrame(ccy.dump_currency_table())
    console = Console()
    console.print(df_to_rich(df, exclude=("symbol_raw",)))
