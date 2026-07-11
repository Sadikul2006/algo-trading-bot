class DailyRiskManager:
    """
    Tracks daily trading activity and enforces two safety limits:
    - Maximum loss allowed per day
    - Maximum number of trades allowed per day

    This class should be reset at the start of every new trading day.
    """

    def __init__(self, max_daily_loss: float, max_trades_per_day: int) -> None:
        """
        Args:
            max_daily_loss: Maximum amount of money allowed to lose in a day
                             (e.g. 2000 for ₹2,000). Should be a positive number.
            max_trades_per_day: Maximum number of trades allowed in a day.
        """
        if max_daily_loss <= 0:
            raise ValueError("Max daily loss must be positive.")
        if max_trades_per_day <= 0:
            raise ValueError("Max trades per day must be positive.")

        self.max_daily_loss = max_daily_loss
        self.max_trades_per_day = max_trades_per_day

        self.trades_today = 0
        self.total_pnl_today = 0.0

    def record_trade(self, pnl: float) -> None:
        """
        Records the result of a completed trade.

        Args:
            pnl: Profit or loss from the trade (negative for a loss).
        """
        self.trades_today += 1
        self.total_pnl_today += pnl

    def can_trade(self) -> bool:
        """
        Checks whether a new trade is allowed, based on today's activity.

        Returns:
            True if trading is still allowed, False if a limit has been hit.
        """
        if self.trades_today >= self.max_trades_per_day:
            return False

        if self.total_pnl_today <= -abs(self.max_daily_loss):
            return False

        return True

    def reset(self) -> None:
        """Resets the daily counters. Should be called at the start of a new trading day."""
        self.trades_today = 0
        self.total_pnl_today = 0.0