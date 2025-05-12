import requests
from datatypes import DataType

class NewtonApi:
    _base_api = "https://api.newtonanalytics.com/price/?"
    _session = requests.Session()
    _session.headers['Origin'] = _base_api
    def __combine_enums(self, enums: DataType):
        return ''.join(str(enum.int_value) for enum in enums)

    def __init__(self):
        return
    
    def __parse_list(self):
        with open('tickers.txt', 'r') as file:
            return [line.strip() for line in file if line.strip()]

    def __parse_request(self, datatypes: DataType, ticker: str, interval: str, observations):
        datatypes = "&dataType="+self.__combine_enums(datatypes)
        ticker = "&ticker="+ticker
        interval = "&interval="+interval
        observations = "&observations="+str(observations)
        return self._base_api+datatypes+ticker+interval+observations

    """
    Request for newton API
    interval is used like: 1mo, 2d, 3w etc..
    """
    def make_request(self, datatypes: DataType, ticker: str, interval: str, observations):
        request = self.__parse_request(datatypes, ticker, interval, observations)
        return self._session.get(request).json()
