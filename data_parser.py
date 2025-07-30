import csv
import os
from datetime import datetime
from datatypes import DataType

class DataParser:

    def __init__(self, datatype_str: str, output: str):
        self.requested_types = self.__parse_datatype_str(datatype_str)
        self._output_file = output
        
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

    def parse_data(self, json_data, ticker: str):
        data = json_data['data']
        new_rows = []
        print("Writing " + ticker + " to: " + self._output_file)
        print("")
        
        if not os.path.exists(self._output_file):
            print(f"File {self._output_file} doesn't exist, creating file with header")
            with open(self._output_file, 'w', newline='') as csvfile:
                writer = csv.writer(csvfile)
                header = ["Date", "Ticker", "Open Price", "High Price", "Low Price", "Close Price", "Volume"]
                writer.writerow(header)

        with open(self._output_file, 'a', newline='') as csvfile:
            for row in reversed(data):
                formatted_row = []
                for i, value in enumerate(row):
                    if self.requested_types[i] == DataType.Date:
                        formatted_row.insert(0, self.__parse_timestamp(value))
                    if self.requested_types[i] == DataType.OpenPrice:
                        formatted_row.insert(2, value)
                    if self.requested_types[i] == DataType.HighPrice:
                        formatted_row.insert(3, value)
                    if self.requested_types[i] == DataType.LowPrice:
                        formatted_row.insert(4, value)
                    if self.requested_types[i] == DataType.ClosePrice:
                        formatted_row.insert(5, value)
                    if self.requested_types[i] == DataType.Volume:
                        formatted_row.insert(6, value)
                formatted_row.insert(1, ticker)
                csv.writer(csvfile).writerow(formatted_row)