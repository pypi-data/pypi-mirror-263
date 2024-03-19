import pandas as pd
from statistics import mode
from typing import Iterable, Any

class Impute:
    def _is__(self, val: Any, cls: object) -> bool: #  Checks if a value is an instance of a given class.
        return isinstance(val, cls)

    def _notnaVal(self, column: Iterable[Any]) -> list[Any]: # Extracts non-NA values from a column.
        return [val for val in column if not pd.isna(val)]

    # Determines the value to fill missing values based on the data type of non-missing values.
    def _whattofill(self, column: Iterable[Any]) -> Any:
        if self._is__(self._notnaVal(column)[0], str):
            return mode(column)
        
        return int(sum(self._notnaVal(column))/len(column))

    # Fills missing values in a column using the value determined by _whattofill().
    def fill_missing_val(self, column: Iterable[Any]) -> Iterable[Any]:
        return column.fillna(self._whattofill(column))