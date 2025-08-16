from enum import Enum

class DataType(Enum):
    Date = (0, "Date")
    OpenPrice = (3, "Open Price")
    HighPrice = (2, "High Price")
    LowPrice = (1, "Low Price")
    ClosePrice = (4, "Close Price")
    Volume = (5, "Volume")
    AdjustedClose = (6, "Adjusted Close")

    def __init__(self, int_value, str_value):
        self._int_value = int_value
        self._str_value = str_value

    @property
    def int_value(self):
        return self._int_value

    @property
    def str_value(self):
        return self._str_value