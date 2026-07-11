import pandas as pd
from strategy.base_strategy import BaseStrategy
from indicators.bollinger_bands import calculate_bollinger_bands


class MeanReversionStrategy(BaseStrategy):
    """
    A strategy that assumes price reverts to its average after
    moving too far away, using Bollinger Bands.
    """

    def __init__(self, period: int = 20, std_dev: float = 2.0) -> None:
        self.period = period
        self.std_dev = std_dev

    def generate_signal(self, data: pd.DataFrame) -> str:
        """
        Generates a BUY/SELL/HOLD signal based on price position
        relative to Bollinger Bands.

        Args:
            data: A pandas DataFrame with a 'close' column.

        Returns:
            BaseStrategy.BUY, BaseStrategy.SELL, or BaseStrategy.HOLD
        """
        close = data["close"]
        bands = calculate_bollinger_bands(close, self.period, self.std_dev)

        latest_close = close.iloc[-1]
        latest_upper = bands["upper"].iloc[-1]
        latest_lower = bands["lower"].iloc[-1]

        if pd.isna(latest_upper) or pd.isna(latest_lower):
            # Not enough data yet to calculate bands
            return self.HOLD

        if latest_close <= latest_lower:
            return self.BUY
        elif latest_close >= latest_upper:
            return self.SELL
        else:
            return self.HOLD