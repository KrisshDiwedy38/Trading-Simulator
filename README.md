# Stock Price Analysis & Forecasting Tool

This project provides a comprehensive toolset for analyzing and forecasting stock prices using time series analysis and ARIMA models. It leverages the Alpha Vantage API to fetch real-time intraday data and implements statistical methods to predict future price movements.

## Features

- **Real-time Data Retrieval**: Fetch 5-minute interval stock data from Alpha Vantage API
- **Interactive Visualization**: Plot stock price trends using Plotly
- **Statistical Analysis**: 
  - Time series stationarity testing using Augmented Dickey-Fuller
  - Automatic determination of differencing parameter (d)
- **Automated Model Selection**: Iterative testing of ARIMA(p,d,q) parameters
- **Stock Forecasting**: Generate and visualize price predictions
- **Performance Evaluation**: Compare forecast against test data
- **Equity Reference**: Built-in list of popular stocks with sentiment indicators

## Data Sources

- [Alpha Vantage API](https://www.alphavantage.co/) for intraday stock data
- Local reference database of top 20 equities with sentiment analysis

## Requirements

- Python 3.6+
- Libraries:
  - requests
  - pandas
  - numpy
  - plotly.express
  - matplotlib
  - statsmodels
  - math
  - json
  - warnings

## Project Structure

```
Stock_Analysis/
│
├── Trading_Sim.ipynb        # Main script with all functionality
├── requirements.txt         # install all the required libraries
├── get_stocks.py            # Script to create sample stock data
├── stock_data.json          # Sample stock data for offline testing
├── README.md                # Project documentation
```

## How It Works

1. **Data Collection**  
   Intraday stock data is fetched from Alpha Vantage API with 5-minute intervals.

2. **Data Preprocessing**  
   Time series data is formatted, visualized, and split into training and testing sets.

3. **Stationarity Analysis**  
   The Augmented Dickey-Fuller test is applied to check for time series stationarity.

4. **Differencing**  
   If data is non-stationary, differencing is applied iteratively until stationarity is achieved.

5. **Model Selection**  
   Multiple ARIMA models with different p and q parameters are tested to find the optimal configuration based on AIC.

6. **Forecasting**  
   The optimal model is used to forecast future stock prices.

7. **Visualization**  
   Original data and forecasts are plotted for comparison and analysis.

## Usage Instructions

1. Clone the repository
2. Install required packages: `pip install -r requirements.txt`
3. Replace the API key in the script with your Alpha Vantage API key
4. Run the script: `python Trading_Sim.ipynb`
5. Enter the stock symbol when prompted (e.g., AAPL, MSFT, TSLA)

## Limitations

- Alpha Vantage API has rate limits (5 calls/minute, 500 calls/day on free tier)
- ARIMA models assume past patterns will continue in the future
- Market volatility and unexpected events can significantly impact forecast accuracy
- Model computation becomes more intensive with increased historical data

## Future Work

- Implement machine learning models (LSTM, Random Forest) for comparison
- Add sentiment analysis from financial news
- Create a web interface for easier interaction
- Incorporate fundamental analysis metrics
- Include options for different forecasting horizons
- Implement backtesting functionality to measure model performance