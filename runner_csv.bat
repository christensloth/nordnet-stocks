@echo off

c:
cd C:\users\chris\OneDrive\Dokumenter\finanshuset\stock_fetcher

del C:\users\chris\OneDrive\Dokumenter\finanshuset\stock_fetcher\output.csv

python "%cd%\main.py"
pause