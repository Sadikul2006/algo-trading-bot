import pandas as pd
from indicators.ema import calculate_ema

if __name__ == "__main__":
    # Sample closing prices (imagine these are 10 days of stock prices)
    sample_prices = pd.Series([100, 102, 101, 105, 107, 110, 108, 111, 115, 117])

    print("Price data:")
    print(sample_prices)

    ema_values = calculate_ema(sample_prices, period=5)

    print("\n5-period EMA:")
    print(ema_values)