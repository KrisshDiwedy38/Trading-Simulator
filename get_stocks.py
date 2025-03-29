import json
import random
import datetime

# Function to generate synthetic non-stationary stock data
def generate_stock_data(symbol="IBM", start_date="2023-01-01", num_days=100):
    stock_data = {
        "Meta Data": {
            "1. Information": "Daily Prices (open, high, low, close) and Volumes",
            "2. Symbol": symbol,
            "3. Last Refreshed": start_date,
            "4. Output Size": "Compact",
            "5. Time Zone": "US/Eastern",
        },
        "Time Series (5min)": {}
    }

    # Convert start date to datetime object
    current_date = datetime.datetime.strptime(start_date, "%Y-%m-%d")
    
    # Initial price
    open_price = 130.0  

    for _ in range(num_days):
        # Introduce trend (slow upward movement)
        open_price += random.uniform(-1.5, 2.0)

        # Simulate daily high, low, close, and volume
        high_price = open_price + random.uniform(0.5, 2.5)
        low_price = open_price - random.uniform(0.5, 2.5)
        close_price = random.uniform(low_price, high_price)
        volume = random.randint(1000000, 10000000)

        # Store in dictionary
        stock_data["Time Series (5min)"][current_date.strftime("%Y-%m-%d")] = {
            "1. open": f"{open_price:.2f}",
            "2. high": f"{high_price:.2f}",
            "3. low": f"{low_price:.2f}",
            "4. close": f"{close_price:.2f}",
            "5. volume": str(volume)
        }

        # Move to the previous day
        current_date -= datetime.timedelta(days=1)

    return stock_data

# Generate and save the data
stock_data = generate_stock_data(num_days=100)

# Save to a JSON file
with open("stock_data.json", "w") as file:
    json.dump(stock_data, file, indent=4)

print("Generated non-stationary stock data!")
