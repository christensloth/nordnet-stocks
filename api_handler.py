import requests
from datatypes import DataType
from data_parser import DataParser

class NewtonApi:
    _base_api = "https://api.newtonanalytics.com/price/?"
    _session = requests.Session()
    _session.headers['Origin'] = _base_api
    
    def __init__(self):
        return

    def __combine_enums(self, enums: DataType):
        return ''.join(str(enum.int_value) for enum in enums)
    
    def __parse_request(self, datatypes: DataType, ticker: str, interval: str, observations):
        datatypes = "&dataType=" + self.__combine_enums(datatypes)
        ticker = "&ticker=" + ticker
        interval = "&interval=" + interval
        observations = "&observations=" + str(observations)
        return self._base_api + datatypes + ticker + interval + observations

    def make_request(self, datatypes: DataType, ticker: str, interval: str, observations, destination: str):
        request = self.__parse_request(datatypes, ticker, interval, observations)
        parser = DataParser(self.__combine_enums(datatypes))
        print("Request: " + request)
        data = self._session.get(request).json()
        if data['status'] != '200':
            exit(f"Errorcode was: {data['status']}, reason: {data['data']}")
        print("API Request for " + ticker + " was successful")
        parser.parse_data(self._session.get(request).json(), ticker, destination)