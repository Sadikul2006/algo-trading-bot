import pandas as pd
from indicators.rsi import calculate_rsi

if __name__ == "__main__":
    # More data points needed since RSI default period is 14
    sample_prices = pd.Series([
        44, 44.34, 44.09, 44.15, 43.61, 44.33, 44.83, 45.10, 45.42,
        45.84, 46.08, 45.89, 46.03, 45.61, 46.28, 46.28, 46.00,
        46.03, 46.41, 46.22
    ])

    print("Price data:")
    print(sample_prices)

    rsi_values = calculate_rsi(sample_prices, period=14)

    print("\n14-period RSI:")
    print(rsi_values)