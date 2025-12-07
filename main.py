from ticker_parser import TickerParser
from  datatypes  import DataType
import argparse

parser = argparse.ArgumentParser()

parser.add_argument("-t", "--tickers", required = True, help = "Absolute path to .txt file with tickers")
parser.add_argument("-o", "--output", required = True, help = "Absolute path to .csv file for output")

args = parser.parse_args()
"""
Interval should be in format 1d (1 day), 1wk (1 week), 1m (1 month)
"""
data_interval = "1d"
observations =  265

"""
Available datatypes an be seen in datatypes.py
"""
datatypes = [DataType.Date, DataType.OpenPrice, DataType.HighPrice, DataType.LowPrice, DataType.ClosePrice, DataType.Volume]

parser = TickerParser(datatypes, data_interval, observations)
parser.fetch_tickers(args.tickers, args.output)

with open("tjek_file.txt", "w") as file:
    file.write("Rates are all collected")

