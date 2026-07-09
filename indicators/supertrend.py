import pandas as pd
from indicators.atr import calculate_atr


def calculate_supertrend(high: pd.Series, low: pd.Series, close: pd.Series,
                          period: int = 10, multiplier: float = 3.0) -> pd.DataFrame:
    """Calculates the Supertrend indicator and trend direction."""
    atr = calculate_atr(high, low, close, period)
    hl2 = (high + low) / 2

    upper_band = hl2 + (multiplier * atr)
    lower_band = hl2 - (multiplier * atr)

    supertrend = pd.Series(index=close.index, dtype="float64")
    direction = pd.Series(index=close.index, dtype="int64")

    for i in range(len(close)):
        if i == 0:
            supertrend.iloc[i] = upper_band.iloc[i]
            direction.iloc[i] = 1
            continue

        if close.iloc[i] > upper_band.iloc[i - 1]:
            direction.iloc[i] = 1
        elif close.iloc[i] < lower_band.iloc[i - 1]:
            direction.iloc[i] = -1
        else:
            direction.iloc[i] = direction.iloc[i - 1]

        supertrend.iloc[i] = lower_band.iloc[i] if direction.iloc[i] == 1 else upper_band.iloc[i]

    return pd.DataFrame({"supertrend": supertrend, "direction": direction})