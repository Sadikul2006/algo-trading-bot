import pandas as pd
from strategy.base_strategy import BaseStrategy
from indicators.ema import calculate_ema
from indicators.rsi import calculate_rsi


class EmaRsiStrategy(BaseStrategy):
    """
    A strategy that combines EMA crossover (for trend direction)
    with RSI (for entry timing).
    """

    def __init__(self, short_period: int = 9, long_period: int = 21,
                 rsi_period: int = 14, rsi_buy_threshold: float = 40,
                 rsi_sell_threshold: float = 60) -> None:
        self.short_period = short_period
        self.long_period = long_period
        self.rsi_period = rsi_period
        self.rsi_buy_threshold = rsi_buy_threshold
        self.rsi_sell_threshold = rsi_sell_threshold

    def generate_signal(self, data: pd.DataFrame) -> str:
        """
        Generates a BUY/SELL/HOLD signal based on EMA crossover and RSI.

        Args:
            data: A pandas DataFrame with a 'close' column.

        Returns:
            BaseStrategy.BUY, BaseStrategy.SELL, or BaseStrategy.HOLD
        """
        close = data["close"]

        short_ema = calculate_ema(close, self.short_period)
        long_ema = calculate_ema(close, self.long_period)
        rsi = calculate_rsi(close, self.rsi_period)

        # Look at the most recent (last) values only, since that's "now"
        latest_short_ema = short_ema.iloc[-1]
        latest_long_ema = long_ema.iloc[-1]
        latest_rsi = rsi.iloc[-1]

        is_uptrend = latest_short_ema > latest_long_ema
        is_downtrend = latest_short_ema < latest_long_ema

        if is_uptrend and latest_rsi < self.rsi_buy_threshold:
            return self.BUY
        elif is_downtrend and latest_rsi > self.rsi_sell_threshold:
            return self.SELL
        else:
            return self.HOLD