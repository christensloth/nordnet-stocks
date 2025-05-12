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