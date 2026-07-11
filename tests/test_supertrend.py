import pandas as pd
from indicators.supertrend import calculate_supertrend

if __name__ == "__main__":
    high = pd.Series([100, 99, 98, 97, 96, 90, 85, 80, 75, 70, 65, 75, 85, 95])
    low  = pd.Series([95, 94, 93, 92, 91, 85, 80, 75, 70, 65, 60, 70, 80, 90])
    close = pd.Series([97, 96, 95, 94, 93, 87, 82, 77, 72, 67, 62, 72, 82, 92])

    result = calculate_supertrend(high, low, close, period=5, multiplier=1.0)
    print(result)