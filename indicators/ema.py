import pandas as pd


def calculate_ema(data: pd.Series, period: int) -> pd.Series:
    """
    Calculates the Exponential Moving Average (EMA) for a given price series.

    Args:
        data: A pandas Series of prices (e.g. closing prices), ordered oldest to newest.
        period: The number of periods (days/candles) to use for the EMA.

    Returns:
        A pandas Series containing the EMA values, same length as input.
    """
    return data.ewm(span=period, adjust=False).mean()