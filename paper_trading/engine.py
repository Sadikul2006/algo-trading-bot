import logging
import pandas as pd
from paper_trading.portfolio import Portfolio
from risk.position_sizing import calculate_quantity_in_range
from strategy.base_strategy import BaseStrategy

logger = logging.getLogger(__name__)


class PaperTradingEngine:
    """
    Ties together a Strategy, Risk Management, and Portfolio to run
    a full paper trading simulation on historical or live price data.
    """

    def __init__(self, strategy: BaseStrategy, portfolio: Portfolio,
                 symbol: str, min_amount: float, max_amount: float,
                 target_percentage: float = 10, stop_loss_percentage: float = 5) -> None:
        """
        Args:
            strategy: Any strategy implementing BaseStrategy.
            portfolio: The virtual portfolio to trade with.
            symbol: The stock symbol being traded.
            min_amount: Minimum capital to deploy per trade.
            max_amount: Maximum capital to deploy per trade.
            target_percentage: Take-profit percentage.
            stop_loss_percentage: Stop-loss percentage.
        """
        self.strategy = strategy
        self.portfolio = portfolio
        self.symbol = symbol
        self.min_amount = min_amount
        self.max_amount = max_amount
        self.target_percentage = target_percentage
        self.stop_loss_percentage = stop_loss_percentage

    def process_candle(self, data: pd.DataFrame) -> None:
        """
        Processes a single new candle/price update: checks for exits on
        open positions first, then checks for new entry signals.

        Args:
            data: A DataFrame of historical data up to and including "now",
                  with at least a 'close' column (and 'high'/'low' if the
                  strategy requires them).
        """
        current_price = data["close"].iloc[-1]

        # Step 1: Check if an open position should be closed
        if self.symbol in self.portfolio.open_positions:
            self._check_exit(current_price)
            return  # Don't open a new position in the same candle we exit

        # Step 2: No open position — check for a new entry signal
        signal = self.strategy.generate_signal(data)

        if signal == BaseStrategy.BUY:
            self._open_new_position(current_price)
        # SELL signals for entry (shorting) are not handled in this basic engine

    def _check_exit(self, current_price: float) -> None:
        """Checks whether the open position's target or stop loss has been hit."""
        trade = self.portfolio.open_positions[self.symbol]

        if current_price >= trade.target_price:
            self.portfolio.close_position(self.symbol, current_price, "TARGET")
        elif current_price <= trade.stop_loss_price:
            self.portfolio.close_position(self.symbol, current_price, "STOP_LOSS")

    def _open_new_position(self, entry_price: float) -> None:
        """Calculates position size and opens a new BUY position."""
        quantity = calculate_quantity_in_range(self.min_amount, self.max_amount, entry_price)

        if quantity == 0:
            logger.info(f"Skipping entry for {self.symbol}: price {entry_price} doesn't fit budget range.")
            return

        target_price = round(entry_price * (1 + self.target_percentage / 100), 2)
        stop_loss_price = round(entry_price * (1 - self.stop_loss_percentage / 100), 2)

        self.portfolio.open_position(
            symbol=self.symbol,
            quantity=quantity,
            entry_price=entry_price,
            stop_loss_price=stop_loss_price,
            target_price=target_price,
            direction="BUY",
        )