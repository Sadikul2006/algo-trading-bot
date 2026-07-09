import pandas as pd


def calculate_bollinger_bands(data: pd.Series, period: int = 20, std_dev: float = 2.0) -> pd.DataFrame:
    """Calculates Bollinger Bands: Middle (SMA), Upper, and Lower bands."""
    middle_band = data.rolling(window=period).mean()
    rolling_std = data.rolling(window=period).std()
    upper_band = middle_band + (std_dev * rolling_std)
    lower_band = middle_band - (std_dev * rolling_std)
    return pd.DataFrame({
        "middle": middle_band,
        "upper": upper_band,
        "lower": lower_band
    })