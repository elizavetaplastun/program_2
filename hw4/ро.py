import yfinance as yf
f = "APPL"
start_time = "2000-09-09"
finish_time = "2022-09-09"
data = yf.download(f, start_time, finish_time)
print(data)