import pandas as pd
from rich.table import Table

set_alike = set[str] | frozenset[str] | tuple[str] | list[str] | None


def df_to_rich(
    df: pd.DataFrame, *, exclude: set_alike = None, **columns: dict
) -> Table:
    table = Table()
    if exclude_columns := set(exclude or ()):
        df = df.drop(columns=exclude_columns)
    for column in df.columns:
        config = dict(justify="right", style="cyan", no_wrap=True)
        config.update(columns.get(column) or {})
        table.add_column(column, **config)  # type: ignore[arg-type]
    for row in df.values:
        table.add_row(*[str(item) for item in row])
    return table
