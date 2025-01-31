import requests
from api_key import api_key

def getStocks(time,equity):
   base_url = "https://www.alphavantage.co/query?"
   url = base_url + 'function=TIME_SERIES_' + time + '&symbol=' + equity + '&interval=5min&apikey=' + api_key
   response = requests.get(url).json()
   return response

def main():
   equity = input("Enter the equity of choice: ")
   time = input("Enter time series: ")
   return (getStocks(time.upper(), equity))

if __name__ == "__main__":
   print(main())