import requests
from datatypes import DataType
from data_parser import DataParser

class NewtonApi:
    _base_api = "https://api.newtonanalytics.com/price/?"
    _session = requests.Session()
    _session.headers['Origin'] = _base_api
    
    def __init__(self):
        return

    def _combine_enums(self, enums: DataType):
        return ''.join(str(enum.int_value) for enum in enums)
    
    def _parse_request(self, datatypes: DataType, ticker: str, interval: str, observations):
        datatypes = "&dataType=" + self._combine_enums(datatypes)
        ticker = "&ticker=" + ticker
        interval = "&interval=" + interval
        observations = "&observations=" + str(observations)
        return self._base_api + datatypes + ticker + interval + observations

    def _make_request(self, datatypes: DataType, ticker: str, interval: str, observations):
        max_retries = 3
        retry_delay = 2  # seconds
        request = self._parse_request(datatypes, ticker, interval, observations)

        for attempt in range(max_retries):
            try:
                response = self._session.get(request)
                response.raise_for_status()
                data = response.json()
                if data['status'] != '200':
                    exit(f"Errorcode was: {data['status']}, reason: {data['data']}")
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

    def call(self, datatypes: DataType, ticker: str, interval: str, observations, output: str):
        parser = DataParser(self._combine_enums(datatypes), output)
        data = self._make_request(datatypes, ticker, interval, observations)
        parser.parse_data(data, ticker)