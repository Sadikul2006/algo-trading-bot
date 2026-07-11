import pandas as pd
from strategy.base_strategy import BaseStrategy
from indicators.supertrend import calculate_supertrend


class TrendFollowingStrategy(BaseStrategy):
    """
    A strategy that follows the Supertrend indicator, entering a trade
    only when the trend direction has just changed.
    """

    def __init__(self, period: int = 10, multiplier: float = 3.0) -> None:
        self.period = period
        self.multiplier = multiplier

    def generate_signal(self, data: pd.DataFrame) -> str:
        """
        Generates a BUY/SELL/HOLD signal based on a Supertrend direction change.

        Args:
            data: A pandas DataFrame with 'high', 'low', 'close' columns.

        Returns:
            BaseStrategy.BUY, BaseStrategy.SELL, or BaseStrategy.HOLD
        """
        if len(data) < self.period + 2:
            return self.HOLD

        supertrend_data = calculate_supertrend(
            data["high"], data["low"], data["close"],
            self.period, self.multiplier
        )

        latest_direction = supertrend_data["direction"].iloc[-1]
        previous_direction = supertrend_data["direction"].iloc[-2]

        if previous_direction == -1 and latest_direction == 1:
            return self.BUY
        elif previous_direction == 1 and latest_direction == -1:
            return self.SELL
        else:
            return self.HOLD