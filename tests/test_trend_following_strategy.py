import pandas as pd
from strategy.trend_following_strategy import TrendFollowingStrategy

if __name__ == "__main__":
    high = pd.Series([100, 99, 98, 97, 96, 90, 85, 80, 75, 70, 65, 75])
    low  = pd.Series([95, 94, 93, 92, 91, 85, 80, 75, 70, 65, 60, 70])
    close = pd.Series([97, 96, 95, 94, 93, 87, 82, 77, 72, 67, 62, 72])

    data = pd.DataFrame({"high": high, "low": low, "close": close})

    strategy = TrendFollowingStrategy(period=5, multiplier=1.0)
    signal = strategy.generate_signal(data)

    print(f"Generated signal: {signal}")