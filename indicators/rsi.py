import pandas as pd


def calculate_rsi(data: pd.Series, period: int = 14) -> pd.Series:
    """
    Calculates the Relative Strength Index (RSI) for a given price series.

    Args:
        data: A pandas Series of prices (e.g. closing prices), ordered oldest to newest.
        period: The number of periods to use for averaging gains/losses. Default is 14,
                which is the standard period used across most trading platforms.

    Returns:
        A pandas Series containing the RSI values (range 0-100), same length as input.
    """
    # Step 1: Calculate day-to-day price change
    delta = data.diff()

    # Step 2: Split into gains (positive changes) and losses (negative changes, made positive)
    gain = delta.where(delta > 0, 0.0)
    loss = -delta.where(delta < 0, 0.0)

    # Step 3: Calculate the rolling average gain and average loss
    avg_gain = gain.rolling(window=period).mean()
    avg_loss = loss.rolling(window=period).mean()

    # Step 4: Calculate Relative Strength (RS)
    rs = avg_gain / avg_loss

    # Step 5: Calculate RSI
    rsi = 100 - (100 / (1 + rs))

    return rsi