import pandas as pd


def calculate_sma(data: pd.Series, period: int) -> pd.Series:
    """
    Calculates the Simple Moving Average (SMA) for a given price series.

    Args:
        data: A pandas Series of prices (e.g. closing prices), ordered oldest to newest.
        period: The number of periods (days/candles) to average over.

    Returns:
        A pandas Series containing the SMA values, same length as input.
        The first (period - 1) values will be NaN, since there isn't
        enough data yet to calculate a full window average.
    """
    return data.rolling(window=period).mean()