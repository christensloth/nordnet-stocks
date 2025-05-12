import csv
from datetime import datetime
from datatypes import DataType

class DataParser:

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

    def parse_data(self, json_data, ticker: str, destination: str):
        data = json_data['data']
        
        filename = destination + ticker + ".csv"
        print("Writing " + ticker + " to: " + filename)
        print("")
        
        existing_rows = []
        try:
            with open(filename, 'r', newline='') as csvfile:
                reader = csv.reader(csvfile)
                headers = next(reader, None)
                if headers:
                    date_column = headers.index(DataType.Date.str_value)
                    existing_rows = list(reader)
        except FileNotFoundError:
            pass 
        
        existing_dates = {row[date_column] for row in existing_rows} if existing_rows else set()
        
        new_rows = []
        date_column_index = None
        for i, dtype in enumerate(self.requested_types):
            if dtype == DataType.Date:
                date_column_index = i
                break
        
        if date_column_index is None:
            raise ValueError("Date column not found in requested data types")
        
        for row in reversed(data):
            formatted_row = []
            for i, value in enumerate(row):
                if self.requested_types[i] == DataType.Date:
                    formatted_date = self.__parse_timestamp(value)
                    formatted_row.append(formatted_date)
                else:
                    formatted_row.append(value)
            
            if formatted_row[date_column_index] not in existing_dates:
                new_rows.append(formatted_row)
        
        all_rows = existing_rows + new_rows
        
        with open(filename, 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow([dtype.str_value for dtype in self.requested_types])
            writer.writerows(all_rows)