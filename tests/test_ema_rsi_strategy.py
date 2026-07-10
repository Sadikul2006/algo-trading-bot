import pandas as pd
from strategy.ema_rsi_strategy import EmaRsiStrategy
from indicators.ema import calculate_ema
from indicators.rsi import calculate_rsi

if __name__ == "__main__":
    close_prices = [100, 102, 104, 106, 108, 110, 112, 114, 116, 118,
                     120, 122, 124, 126, 128, 130, 128, 125, 122, 119,
                     117, 115, 114, 113, 112]

    data = pd.DataFrame({"close": close_prices})
    close = data["close"]

    # Debug: print actual indicator values
    short_ema = calculate_ema(close, 9)
    long_ema = calculate_ema(close, 21)
    rsi = calculate_rsi(close, 14)

    print(f"Latest Short EMA (9): {short_ema.iloc[-1]:.2f}")
    print(f"Latest Long EMA (21): {long_ema.iloc[-1]:.2f}")
    print(f"Latest RSI (14): {rsi.iloc[-1]:.2f}")

    strategy = EmaRsiStrategy()
    signal = strategy.generate_signal(data)
    print(f"\nGenerated signal: {signal}")