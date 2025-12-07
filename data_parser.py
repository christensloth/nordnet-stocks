import csv
import os
from datetime import datetime
from datatypes import DataType

class DataParser:

    def __init__(self, datatype_str: str, output: str):
        self.requested_types = self._parse_datatype_str(datatype_str)
        self._output_dir = output
        
    def _parse_datatype_str(self, datatype_str: str) -> list[DataType]:
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

    def _parse_timestamp(self, timestamp):
        return datetime.utcfromtimestamp(timestamp).strftime('%Y-%m-%d %H:%M:%S')

    def parse_data(self, json_data, ticker: str):
        data = json_data['data']
        new_rows = []
        output_file = os.path.join(self._output_dir, f"{ticker}_data.csv")
        
        if not os.path.exists(output_file):
            with open(output_file, 'w', newline='') as csvfile:
                writer = csv.writer(csvfile)
                header = ["Date", "Ticker", "Open Price", "High Price", "Low Price", "Close Price", "Volume"]
                writer.writerow(header)

        with open(output_file, 'a', newline='') as csvfile:
            for row in reversed(data):
                formatted_row = []
                for i, value in enumerate(row):
                    if self.requested_types[i] == DataType.Date:
                        formatted_row.insert(0, self._parse_timestamp(value))
                    if self.requested_types[i] == DataType.OpenPrice:
                        formatted_row.insert(4, value)
                    if self.requested_types[i] == DataType.HighPrice:
                        formatted_row.insert(3, value)
                    if self.requested_types[i] == DataType.LowPrice:
                        formatted_row.insert(2, value)
                    if self.requested_types[i] == DataType.ClosePrice:
                        formatted_row.insert(5, value)
                    if self.requested_types[i] == DataType.Volume:
                        formatted_row.insert(6, value)
                formatted_row.insert(1, ticker)
                csv.writer(csvfile).writerow(formatted_row)
        
        print(f"Data for {ticker} written to {output_file}")

