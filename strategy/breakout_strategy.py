import pandas as pd
from strategy.base_strategy import BaseStrategy


class BreakoutStrategy(BaseStrategy):
    """
    A strategy that generates signals when the price breaks out of
    the recent high/low range.
    """

    def __init__(self, lookback_period: int = 20) -> None:
        """
        Args:
            lookback_period: Number of past candles to consider for
                              determining the recent high/low range.
        """
        self.lookback_period = lookback_period

    def generate_signal(self, data: pd.DataFrame) -> str:
        """
        Generates a BUY/SELL/HOLD signal based on price breakout.

        Args:
            data: A pandas DataFrame with 'high', 'low', 'close' columns.

        Returns:
            BaseStrategy.BUY, BaseStrategy.SELL, or BaseStrategy.HOLD
        """
        if len(data) < self.lookback_period + 1:
            # Not enough data to determine a breakout range
            return self.HOLD

        # Exclude the most recent candle from the range calculation,
        # since we're checking if the CURRENT price breaks the PAST range
        past_data = data.iloc[-(self.lookback_period + 1):-1]
        recent_high = past_data["high"].max()
        recent_low = past_data["low"].min()

        current_close = data["close"].iloc[-1]

        if current_close > recent_high:
            return self.BUY
        elif current_close < recent_low:
            return self.SELL
        else:
            return self.HOLD