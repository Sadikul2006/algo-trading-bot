import pandas as pd


def calculate_vwap(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Calculates VWAP — the average price weighted by trading volume."""
    typical_price = (high + low + close) / 3
    cumulative_tp_volume = (typical_price * volume).cumsum()
    cumulative_volume = volume.cumsum()
    return cumulative_tp_volume / cumulative_volume