from ticker_parser import TickerParser
from  datatypes  import DataType



# copy of ticker_parse.py

from datatypes import DataType
from api_handler import NewtonApi
import os

class TickerParser:
    _api = NewtonApi()
    _outputdir = "output/"

    def __init__(self, datatypes: DataType, interval: str, observations):
        self._datatypes = datatypes
        self._interval = interval
        self._observations = observations

    def __parse_list(self):
        with open('tickers.txt', 'r') as file:
            return [line.strip() for line in file if line.strip()]

    def fetch_tickers(self):
        tickers = self.__parse_list()
        os.makedirs(self._outputdir, exist_ok=True)
        for ticker in tickers:
            self._api.call(self._datatypes, str(ticker), self._interval, self._observations, self._outputdir)


# copy of datatypes.py

from enum import Enum

class DataType(Enum):
    Date = (0, "Date")
    OpenPrice = (1, "Open Price").replace(".", ",")
    HighPrice = (2, "High Price")
    LowPrice = (3, "Low Price")
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


"""
Interval should be in format 1d (1 day), 1wk (1 week), 1m (1 month)
"""
data_interval = "1d"
observations =  260

"""
Available datatypes an be seen in datatypes.py
"""
datatypes = [DataType.Date, DataType.OpenPrice, DataType.HighPrice, DataType.LowPrice, DataType.ClosePrice, DataType.AdjustedClose, DataType.Volume]

parser = TickerParser(datatypes, data_interval, observations)
parser.fetch_tickers()
