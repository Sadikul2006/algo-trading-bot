from abc import ABC, abstractmethod
import pandas as pd


class BaseStrategy(ABC):
    """
    Abstract base class that all trading strategies must inherit from.
    This defines a common contract: every strategy must implement
    a `generate_signal` method that returns BUY, SELL, or HOLD.
    """

    BUY = "BUY"
    SELL = "SELL"
    HOLD = "HOLD"

    @abstractmethod
    def generate_signal(self, data: pd.DataFrame) -> str:
        """
        Analyzes the given price data and returns a trading signal.

        Args:
            data: A pandas DataFrame with at least 'open', 'high', 'low',
                  'close' columns, ordered oldest to newest.

        Returns:
            One of: BaseStrategy.BUY, BaseStrategy.SELL, BaseStrategy.HOLD
        """
        pass