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

    def __make_request(self, datatypes: DataType, ticker: str, interval: str, observations):
        max_retries = 3
        retry_delay = 2  # seconds
        request = self.__parse_request(datatypes, ticker, interval, observations)
        print("Trying request: " + request)

        for attempt in range(max_retries):
            try:
                response = self._session.get(request)
                response.raise_for_status()
                data = response.json()
                if data['status'] != '200':
                    exit(f"Errorcode was: {data['status']}, reason: {data['data']}")
                print("API Request for " + ticker + " was successful")
                return data

            except ConnectionError as e:
                print(f"Connection failed (attempt {attempt + 1}/{max_retries}): {str(e)}")
                if attempt < max_retries - 1:
                    print(f"Retrying in {retry_delay} seconds...")
                    time.sleep(retry_delay)
                continue

            except Exception as e:
                print(f"An unexpected error occurred: {str(e)}")
                break

        print("Failed to establish connection after multiple attempts")
        return None

    def call(self, datatypes: DataType, ticker: str, interval: str, observations, destination: str):
        parser = DataParser(self.__combine_enums(datatypes))
        data = self.__make_request(datatypes, ticker, interval, observations)
        parser.parse_data(data, ticker, destination)