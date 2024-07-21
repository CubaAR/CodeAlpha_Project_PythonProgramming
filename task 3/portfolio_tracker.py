import requests
import pandas as pd
import matplotlib.pyplot as plt

api_key = '6FXKJRA59HEZCQJ9'

def get_stock_data(symbol):
    url = f'https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol={symbol}&interval=5min&apikey={api_key}'
    response = requests.get(url)
    data = response.json()
    if "Time Series (5min)" in data:
        time_series = data["Time Series (5min)"]
        df = pd.DataFrame.from_dict(time_series, orient='index', dtype=float)
        df.columns = ['Open', 'High', 'Low', 'Close', 'Volume']
        df.index = pd.to_datetime(df.index)
        return df
    else:
        print(f"Error fetching data for {symbol}: {data.get('Note', 'Unknown error')}")
        return None

portfolio = {}

def add_stock(symbol, shares):
    if symbol in portfolio:
        portfolio[symbol] += shares
    else:
        portfolio[symbol] = shares
    print(f"Added {shares} shares of {symbol} to the portfolio.")

def remove_stock(symbol, shares):
    if symbol in portfolio:
        if portfolio[symbol] > shares:
            portfolio[symbol] -= shares
            print(f"Removed {shares} shares of {symbol} from the portfolio.")
        elif portfolio[symbol] == shares:
            del portfolio[symbol]
            print(f"Removed all shares of {symbol} from the portfolio.")
        else:
            print(f"Cannot remove {shares} shares of {symbol}. You only have {portfolio[symbol]} shares.")
    else:
        print(f"{symbol} is not in the portfolio.")

def display_portfolio():
    if not portfolio:
        print("The portfolio is empty.")
        return
    print("Current Portfolio:")
    for symbol, shares in portfolio.items():
        print(f"{symbol}: {shares} shares")

def calculate_portfolio_value():
    total_value = 0
    for symbol, shares in portfolio.items():
        stock_data = get_stock_data(symbol)
        if stock_data is not None:
            latest_price = stock_data.iloc[0]['Close']
            total_value += latest_price * shares
            print(f"{symbol}: {shares} shares @ {latest_price:.2f} = {latest_price * shares:.2f}")
        else:
            print(f"Could not fetch data for {symbol}.")
    print(f"Total Portfolio Value: {total_value:.2f}")

def plot_portfolio():
    fig, ax = plt.subplots()
    for symbol in portfolio.keys():
        stock_data = get_stock_data(symbol)
        if stock_data is not None:
            stock_data['Close'].plot(ax=ax, label=symbol)
        else:
            print(f"Could not fetch data for {symbol}.")
    plt.title('Portfolio Performance')
    plt.xlabel('Time')
    plt.ylabel('Stock Price')
    plt.legend()
    plt.show()

def main():
    while True:
        print("\nStock Portfolio Tracker")
        print("1. Add Stock")
        print("2. Remove Stock")
        print("3. Display Portfolio")
        print("4. Calculate Portfolio Value")
        print("5. Plot Portfolio Performance")
        print("6. Exit")
        choice = input("Enter your choice: ")
        
        if choice == '1':
            symbol = input("Enter stock symbol: ").upper()
            shares = int(input("Enter number of shares: "))
            add_stock(symbol, shares)
        elif choice == '2':
            symbol = input("Enter stock symbol: ").upper()
            shares = int(input("Enter number of shares to remove: "))
            remove_stock(symbol, shares)
        elif choice == '3':
            display_portfolio()
        elif choice == '4':
            calculate_portfolio_value()
        elif choice == '5':
            plot_portfolio()
        elif choice == '6':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()

