@echo off

set file_location=C:\users\chris\OneDrive\Dokumenter\finanshuset

del C:\users\chris\OneDrive\Dokumenter\finanshuset\stock_fetcher\output.csv

c:
cd C:\users\chris\OneDrive\Dokumenter\finanshuset\stock_fetcher

rem python "%cd%\main.py -t C:\users\chris\OneDrive\Dokumenter\finanshuset\stock_fetcher\tickers.txt -o C:\users\chris\OneDrive\Dokumenter\finanshuset\stock_fetcher\output.csv"

python3 .\main.py -t tickers.txt -o output.csv

pause