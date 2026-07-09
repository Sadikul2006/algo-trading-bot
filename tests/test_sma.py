import pandas as pd
from indicators.sma import calculate_sma

if __name__ == "__main__":
    sample_prices = pd.Series([100, 102, 101, 105, 107, 110, 108, 111, 115, 117])

    print("Price data:")
    print(sample_prices)

    sma_values = calculate_sma(sample_prices, period=5)

    print("\n5-period SMA:")
    print(sma_values)