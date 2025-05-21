import csv
import os
from datetime import datetime
from datatypes import DataType

class DataParser:

    _output_file = "output.csv"

    def __init__(self, datatype_str: str):
        self.requested_types = self.__parse_datatype_str(datatype_str)
        
    def __parse_datatype_str(self, datatype_str: str) -> list[DataType]:
        type_map = {
            '0': DataType.Date,
            '1': DataType.OpenPrice,
            '2': DataType.HighPrice,
            '3': DataType.LowPrice,
            '4': DataType.ClosePrice,
            '5': DataType.Volume,
            '6': DataType.AdjustedClose
        }
        return [type_map[char] for char in datatype_str]

    def __parse_timestamp(self, timestamp):
        return datetime.utcfromtimestamp(timestamp).strftime('%Y-%m-%d %H:%M:%S')

    def __parse_header(self):
        fields = [dtype.str_value for dtype in self.requested_types]
        fields.insert(1, "Ticker")
        return fields

    def parse_data(self, json_data, ticker: str, destination: str):
        data = json_data['data']
        new_rows = []
        print("Writing " + ticker + " to: " + self._output_file)
        print("")
        
        if not os.path.exists(self._output_file):
            print(f"File {self._output_file} doesn't exist, creating file with header")
            with open(self._output_file, 'w', newline='') as csvfile:
                writer = csv.writer(csvfile)
                writer.writerow(self.__parse_header())

        with open(self._output_file, 'a', newline='') as csvfile:
            for row in reversed(data):
                formatted_row = []
                for i, value in enumerate(row):
                    if self.requested_types[i] == DataType.Date:
                        formatted_row.insert(0, self.__parse_timestamp(value))
                    if self.requested_types[i] == DataType.LowPrice:
                        formatted_row.insert(2, value)
                    if self.requested_types[i] == DataType.HighPrice:
                        formatted_row.insert(3, value)
                    if self.requested_types[i] == DataType.OpenPrice:
                        formatted_row.insert(4, value)
                    if self.requested_types[i] == DataType.ClosePrice:
                        formatted_row.insert(5, value)
                    if self.requested_types[i] == DataType.Volume:
                        formatted_row.insert(6, value)
                formatted_row.insert(1, ticker)
                csv.writer(csvfile).writerow(formatted_row)