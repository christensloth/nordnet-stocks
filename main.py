from ticker_parser import TickerParser
from  datatypes  import DataType

"""
Interval should be in format 1d (1 day), 1wk (1 week), 1m (1 month)
"""
data_interval = "1d"
observations =  30

"""
Available datatypes an be seen in datatypes.py
"""
datatypes = [DataType.Date, DataType.LowPrice, DataType.HighPrice, DataType.OpenPrice, DataType.ClosePrice, DataType.AdjustedClose, DataType.Volume]

parser = TickerParser(datatypes, data_interval, observations)
parser.fetch_tickers()
