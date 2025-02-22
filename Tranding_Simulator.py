import requests
from api_key import api_key

def getStocks(time,equity):
   base_url = "https://www.alphavantage.co/query?"
   url = base_url + 'function=TIME_SERIES_' + time + '&symbol=' + equity + '&interval=5min&apikey=' + api_key
   response = requests.get(url).json()
   return response

def main():
   equity_name = input("Enter the equity of choice: ")
   time = input("Enter time series: ")
   equity_dict = {
    'Tesla': 'TSLA',
    'NVIDIA': 'NVDA',
    'Super Micro Computer': 'SMCI',
    'Quantum Computing': 'QUBT',
    'Rigetti Computing': 'RGTI',
    'MicroStrategy': 'MSTR',
    'Nukkleus': 'NUKK',
    'Broadcom': 'AVGO',
    'CleanSpark': 'CLSK',
    'Advanced Micro Devices': 'AMD',
    'Eli Lilly and Company': 'LLY',
    'SEALSQ Corp': 'LAES',
    'Micron Technology': 'MU',
    'D-Wave Quantum': 'QBTS',
    'Dell Technologies': 'DELL',
    'Walmart': 'WMT',
    'Invesco QQQ Trust': 'QQQ',
    'Apple': 'AAPL',
    'Amazon.com': 'AMZN',
    'Palantir Technologies': 'PLTR',
    'Google': 'GOOGL',
    'IBM': 'IBM',
    'Microsoft': 'MSFT',
    'Meta': 'META'
   }

   if equity_name in equity_dict.values():
      equity = equity_name
   elif equity_name.capitalize() in equity_dict.keys():
      equity = equity_dict[equity_name.capitalize()]
   else:
      print("Data Not available:") 
      return
   
   return (getStocks(time.upper(), equity))

if __name__ == "__main__":
   print(main())