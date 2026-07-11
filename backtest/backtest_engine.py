import logging
import pandas as pd
from paper_trading.engine import PaperTradingEngine
from paper_trading.portfolio import Portfolio
from strategy.base_strategy import BaseStrategy

logger = logging.getLogger(__name__)


class BacktestEngine:
    """
    Runs a strategy against historical data, simulating trades day by day,
    and produces a Portfolio with the full trade history for analysis.
    """

    def __init__(self, strategy: BaseStrategy, historical_data: pd.DataFrame,
                 symbol: str, starting_balance: float,
                 min_amount: float, max_amount: float,
                 target_percentage: float = 10, stop_loss_percentage: float = 5,
                 warmup_period: int = 30) -> None:
        """
        Args:
            strategy: Any strategy implementing BaseStrategy.
            historical_data: Full historical OHLCV data to backtest on.
            symbol: The stock symbol being tested.
            starting_balance: Initial virtual capital.
            min_amount: Minimum capital to deploy per trade.
            max_amount: Maximum capital to deploy per trade.
            target_percentage: Take-profit percentage.
            stop_loss_percentage: Stop-loss percentage.
            warmup_period: Number of initial candles to skip before trading
                            starts, so indicators have enough data to be valid.
        """
        self.historical_data = historical_data
        self.symbol = symbol
        self.warmup_period = warmup_period

        self.portfolio = Portfolio(starting_balance=starting_balance)
        self.engine = PaperTradingEngine(
            strategy=strategy,
            portfolio=self.portfolio,
            symbol=symbol,
            min_amount=min_amount,
            max_amount=max_amount,
            target_percentage=target_percentage,
            stop_loss_percentage=stop_loss_percentage,
        )

        self.equity_curve: list[float] = []

    def run(self) -> None:
        """
        Runs the backtest: iterates through the historical data one candle
        at a time, feeding progressively larger windows to the engine,
        and recording the portfolio value at each step.
        """
        total_rows = len(self.historical_data)

        for i in range(self.warmup_period, total_rows):
            window = self.historical_data.iloc[:i + 1]
            self.engine.process_candle(window)

            current_price = window["close"].iloc[-1]
            portfolio_value = self._calculate_current_value(current_price)
            self.equity_curve.append(portfolio_value)

        logger.info(f"Backtest complete: {len(self.portfolio.trade_history)} trades executed.")

    def _calculate_current_value(self, current_price: float) -> float:
        """
        Calculates portfolio value using the CURRENT market price for any
        open position (more accurate than entry price for the equity curve).
        """
        open_value = 0.0
        if self.symbol in self.portfolio.open_positions:
            position = self.portfolio.open_positions[self.symbol]
            open_value = position.quantity * current_price

        return round(self.portfolio.cash_balance + open_value, 2)