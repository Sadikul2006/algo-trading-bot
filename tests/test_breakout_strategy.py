import pandas as pd
from strategy.breakout_strategy import BreakoutStrategy

if __name__ == "__main__":
    # 20 days of sideways movement (range: 95-105), then a breakout above 105
    high = [102, 104, 103, 105, 104, 103, 102, 104, 105, 103,
             104, 102, 103, 105, 104, 103, 102, 104, 105, 103, 110]
    low = [98, 99, 97, 100, 99, 98, 97, 99, 100, 98,
            99, 97, 98, 100, 99, 98, 97, 99, 100, 98, 106]
    close = [100, 101, 99, 102, 101, 100, 99, 101, 102, 100,
              101, 99, 100, 102, 101, 100, 99, 101, 102, 100, 108]

    data = pd.DataFrame({"high": high, "low": low, "close": close})

    strategy = BreakoutStrategy(lookback_period=20)
    signal = strategy.generate_signal(data)

    print(f"Generated signal: {signal}")