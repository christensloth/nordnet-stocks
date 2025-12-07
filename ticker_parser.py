from datatypes import DataType
from api_handler import NewtonApi
import os
from multiprocessing import Process

class TickerParser:
    _api = NewtonApi()

    def __init__(self, datatypes: DataType, interval: str, observations):
        self._datatypes = datatypes
        self._interval = interval
        self._observations = observations

    def _parse_list(self, ticker_list):
        with open(ticker_list, 'r') as file:
            return [line.strip() for line in file if line.strip()]

    def _fetch_ticker_process(self, ticker: str, output: str):
        self._api.call(self._datatypes, ticker, self._interval, self._observations, output)

    def fetch_tickers(self, ticker_list, output: str):
        tickers = self._parse_list(ticker_list)
        processes = []
        
        for ticker in tickers:
            process = Process(target=self._fetch_ticker_process, args=(ticker, output))
            process.start()
            processes.append(process)
        
        for process in processes:
            process.join()