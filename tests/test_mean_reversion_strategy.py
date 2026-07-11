import pandas as pd
from strategy.mean_reversion_strategy import MeanReversionStrategy

if __name__ == "__main__":
    # Prices oscillating around 100, then a sharp drop at the end
    close_prices = [100, 101, 99, 100, 102, 98, 101, 100, 99, 100,
                     101, 99, 100, 102, 98, 101, 100, 99, 100, 85]

    data = pd.DataFrame({"close": close_prices})

    strategy = MeanReversionStrategy(period=15, std_dev=2.0)
    signal = strategy.generate_signal(data)

    print(f"Generated signal: {signal}")