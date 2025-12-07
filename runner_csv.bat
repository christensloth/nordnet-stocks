@echo off

set file_location=C:\users\chris\OneDrive\Dokumenter\finanshuset

del C:\users\chris\OneDrive\Dokumenter\finanshuset\stock_fetcher\output.csv
del C:\users\chris\OneDrive\Dokumenter\finanshuset\stock_fetcher\tjek_file.txt

cd C:\users\chris\OneDrive\Dokumenter\finanshuset\stock_fetcher

rem python "%cd%\main.py -t C:\users\chris\OneDrive\Dokumenter\finanshuset\stock_fetcher\tickers.txt -o C:\users\chris\OneDrive\Dokumenter\finanshuset\stock_fetcher\output.csv"

python .\main.py -t tickers.txt -o output.csv



rem pause