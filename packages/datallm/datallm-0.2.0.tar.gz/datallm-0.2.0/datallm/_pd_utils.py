from typing import Iterable, List

import pandas as pd

from datallm._types import (
    DtypeEnum,
    RowCompletionsResponse,
)


def _convert_values_to_series(
    values: List[str],
    dtype: DtypeEnum,
) -> pd.Series:
    dtype_map = {
        DtypeEnum.integer: "int64[pyarrow]",
        DtypeEnum.float: "float[pyarrow]",
        DtypeEnum.boolean: "bool[pyarrow]",  # bool_coerce
        DtypeEnum.category: "category",
        DtypeEnum.string: "string[pyarrow]",
        DtypeEnum.date: "datetime64[s]",  # pd.DatetimeIndex,
        DtypeEnum.datetime: "datetime64[s]",  # pd.DatetimeIndex
    }
    str_series = pd.Series(values, dtype="string[pyarrow]")
    series = str_series.astype(dtype_map[dtype])
    if dtype == DtypeEnum.boolean:
        series = pd.Series(values, dtype="bool[pyarrow]")
    elif dtype in [DtypeEnum.date, DtypeEnum.datetime]:
        try:
            series = pd.to_datetime(
                pd.Series(values, dtype="string[pyarrow]")
            )
        except ValueError:
            series = pd.Series(values, dtype="string[pyarrow]")
    elif dtype == DtypeEnum.category:
        series = pd.Series(values, dtype="category")
    elif dtype == DtypeEnum.integer:
        series = pd.Series(values, dtype="int64[pyarrow]")
    elif dtype == DtypeEnum.float:
        series = pd.Series(values, dtype="float64[pyarrow]")
    elif dtype == DtypeEnum.string:
        series = pd.Series(values, dtype="string[pyarrow]")
    return series


def _log_usage(batch: Iterable[RowCompletionsResponse]):
    print(list(batch)[-1].full_prompt)
    total_prompt_tokens = sum(completion.usage.prompt_tokens for completion in batch)
    total_completion_tokens = sum(
        completion.usage.completion_tokens for completion in batch
    )
    print(f"Total prompt tokens processed: {total_prompt_tokens}")
    print(f"Total tokens generated: {total_completion_tokens}\n")
