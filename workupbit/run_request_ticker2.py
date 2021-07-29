

import requests

url_market = "https://api.upbit.com/v1/market/all"
resp = requests.get(url_market)
data = resp.json()


krw_tickers = []

for coin in data:
    ticker = coin['market']
    
    if ticker.startswith("KRW"):
        krw_tickers.append(ticker)

print(krw_tickers)


