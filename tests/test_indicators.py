import pandas as pd
from indicators.atr import calculate_atr
from indicators.vwap import calculate_vwap
from indicators.macd import calculate_macd
from indicators.supertrend import calculate_supertrend
from indicators.bollinger_bands import calculate_bollinger_bands

if __name__ == "__main__":
    high = pd.Series([48.70, 48.72, 48.90, 48.87, 48.82, 49.05, 49.20, 49.35, 49.92, 50.19,
                       50.12, 49.66, 49.88, 50.19, 50.36, 50.57, 50.65, 50.43, 49.63, 50.33])
    low = pd.Series([47.79, 48.14, 48.39, 48.37, 48.24, 48.64, 48.94, 48.86, 49.50, 49.87,
                      49.20, 48.90, 49.43, 49.73, 49.26, 50.09, 50.30, 49.21, 48.98, 49.61])
    close = pd.Series([48.16, 48.61, 48.75, 48.63, 48.74, 49.03, 49.07, 49.32, 49.91, 50.13,
                        49.53, 49.50, 49.75, 50.03, 50.31, 50.52, 50.41, 49.34, 49.37, 50.23])
    volume = pd.Series([1000, 1200, 1100, 900, 1300, 1250, 1400, 1150, 1600, 1700,
                         1500, 1100, 1250, 1350, 1450, 1600, 1550, 1300, 1200, 1400])

    print("ATR:\n", calculate_atr(high, low, close), "\n")
    print("VWAP:\n", calculate_vwap(high, low, close, volume), "\n")
    print("MACD:\n", calculate_macd(close), "\n")
    print("Supertrend:\n", calculate_supertrend(high, low, close), "\n")
    print("Bollinger Bands:\n", calculate_bollinger_bands(close, period=10), "\n")