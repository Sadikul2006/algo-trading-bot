import pandas as pd
from indicators.atr import calculate_atr


def calculate_supertrend(high: pd.Series, low: pd.Series, close: pd.Series,
                          period: int = 10, multiplier: float = 3.0) -> pd.DataFrame:
    """
    Calculates the Supertrend indicator and trend direction.
    Uses trailing (locked-in) bands, matching the standard Supertrend algorithm.
    """
    atr = calculate_atr(high, low, close, period)
    hl2 = (high + low) / 2

    basic_upper = hl2 + (multiplier * atr)
    basic_lower = hl2 - (multiplier * atr)

    final_upper = pd.Series(index=close.index, dtype="float64")
    final_lower = pd.Series(index=close.index, dtype="float64")
    supertrend = pd.Series(index=close.index, dtype="float64")
    direction = pd.Series(index=close.index, dtype="int64")

    for i in range(len(close)):
        is_fresh_start = (
            i == 0
            or pd.isna(atr.iloc[i])
            or pd.isna(final_upper.iloc[i - 1])
            or pd.isna(final_lower.iloc[i - 1])
        )

        if is_fresh_start:
            final_upper.iloc[i] = basic_upper.iloc[i]
            final_lower.iloc[i] = basic_lower.iloc[i]
            direction.iloc[i] = 1
            supertrend.iloc[i] = final_lower.iloc[i]
            continue

        if basic_upper.iloc[i] < final_upper.iloc[i - 1] or close.iloc[i - 1] > final_upper.iloc[i - 1]:
            final_upper.iloc[i] = basic_upper.iloc[i]
        else:
            final_upper.iloc[i] = final_upper.iloc[i - 1]

        if basic_lower.iloc[i] > final_lower.iloc[i - 1] or close.iloc[i - 1] < final_lower.iloc[i - 1]:
            final_lower.iloc[i] = basic_lower.iloc[i]
        else:
            final_lower.iloc[i] = final_lower.iloc[i - 1]

        if close.iloc[i] > final_upper.iloc[i - 1]:
            direction.iloc[i] = 1
        elif close.iloc[i] < final_lower.iloc[i - 1]:
            direction.iloc[i] = -1
        else:
            direction.iloc[i] = direction.iloc[i - 1]

        supertrend.iloc[i] = final_lower.iloc[i] if direction.iloc[i] == 1 else final_upper.iloc[i]

    return pd.DataFrame({"supertrend": supertrend, "direction": direction})