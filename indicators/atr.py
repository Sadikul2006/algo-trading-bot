import pandas as pd


def calculate_atr(high: pd.Series, low: pd.Series, close: pd.Series, period: int = 14) -> pd.Series:
    """Calculates Average True Range (ATR) — measures volatility."""
    previous_close = close.shift(1)
    range1 = high - low
    range2 = (high - previous_close).abs()
    range3 = (low - previous_close).abs()
    true_range = pd.concat([range1, range2, range3], axis=1).max(axis=1)
    return true_range.rolling(window=period).mean()