import logging
from paper_trading.trade import Trade

logger = logging.getLogger(__name__)


class Portfolio:
    """
    Manages a virtual trading account: balance, open positions,
    and trade history. This is the core of the paper trading engine.
    """

    def __init__(self, starting_balance: float) -> None:
        """
        Args:
            starting_balance: The initial virtual cash balance.
        """
        if starting_balance <= 0:
            raise ValueError("Starting balance must be positive.")

        self.starting_balance = starting_balance
        self.cash_balance = starting_balance
        self.open_positions: dict[str, Trade] = {}
        self.trade_history: list[Trade] = []

    def open_position(self, symbol: str, quantity: int, entry_price: float,
                       stop_loss_price: float, target_price: float,
                       direction: str = "BUY") -> bool:
        """
        Opens a new virtual position, if sufficient balance is available.

        Args:
            symbol: The stock symbol (e.g. "RELIANCE").
            quantity: Number of shares to trade.
            entry_price: The price at which to enter.
            stop_loss_price: The stop loss level.
            target_price: The target level.
            direction: "BUY" or "SELL". Defaults to "BUY".

        Returns:
            True if the position was opened successfully, False otherwise
            (e.g. insufficient balance, or a position already open for this symbol).
        """
        if symbol in self.open_positions:
            logger.warning(f"Position already open for {symbol}. Skipping.")
            return False

        cost = quantity * entry_price

        if direction == "BUY" and cost > self.cash_balance:
            logger.warning(f"Insufficient balance to open {symbol}: need {cost}, have {self.cash_balance}")
            return False

        trade = Trade(
            symbol=symbol,
            quantity=quantity,
            entry_price=entry_price,
            stop_loss_price=stop_loss_price,
            target_price=target_price,
            direction=direction,
        )

        self.open_positions[symbol] = trade

        if direction == "BUY":
            self.cash_balance = round(self.cash_balance - cost, 2)

        logger.info(f"Opened {direction} position: {symbol} x{quantity} @ {entry_price}")
        return True

    def close_position(self, symbol: str, exit_price: float, exit_reason: str) -> float:
        """
        Closes an open position and records the result.

        Args:
            symbol: The stock symbol to close.
            exit_price: The price at which the position is being closed.
            exit_reason: Why it's being closed ("TARGET", "STOP_LOSS", "MANUAL").

        Returns:
            The P&L from this trade. Returns 0.0 if no open position existed.
        """
        if symbol not in self.open_positions:
            logger.warning(f"No open position found for {symbol}.")
            return 0.0

        trade = self.open_positions.pop(symbol)
        trade.close(exit_price, exit_reason)

        pnl = trade.calculate_pnl()

        # Return the capital (plus/minus P&L) to the cash balance
        if trade.direction == "BUY":
            self.cash_balance = round(self.cash_balance + trade.quantity * exit_price, 2)
        else:  # SELL (short) — capital was never deducted, so just add P&L
            self.cash_balance = round(self.cash_balance + pnl, 2)

        self.trade_history.append(trade)

        logger.info(f"Closed {symbol} @ {exit_price} ({exit_reason}) | P&L: {pnl}")
        return pnl

    def get_total_pnl(self) -> float:
        """Returns the total realized P&L from all closed trades."""
        return round(sum(trade.calculate_pnl() for trade in self.trade_history), 2)

    def get_portfolio_value(self) -> float:
        """
        Returns the current total portfolio value: cash balance plus
        the value of any open positions (at their entry price, since
        we don't have live prices here).
        """
        open_value = sum(pos.quantity * pos.entry_price for pos in self.open_positions.values())
        return round(self.cash_balance + open_value, 2)