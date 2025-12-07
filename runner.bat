@echo off

set file_location=C:\users\chris\OneDrive\Dokumenter\finanshuset

del C:\users\chris\OneDrive\Dokumenter\finanshuset\stock_fetcher\output.csv
del C:\users\chris\OneDrive\Dokumenter\finanshuset\stock_fetcher\tjek_file.txt

cd C:\users\chris\OneDrive\Dokumenter\finanshuset\stock_fetcher

rem python "%cd%\main.py -t C:\users\chris\OneDrive\Dokumenter\finanshuset\stock_fetcher\tickers.txt -o C:\users\chris\OneDrive\Dokumenter\finanshuset\stock_fetcher\output"

rem python .\main.py -t tickers.txt -o output

@echo off
setlocal enabledelayedexpansion

set first=1
for %%F in (output\*.csv) do (
    if !first! == 1 (
        type "%%F" > merged.csv
        set first=0
    ) else (
        more +1 "%%F" >> merged.csv
    )
)


rem pause