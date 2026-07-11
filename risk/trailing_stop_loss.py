class TrailingStopLoss:
    """
    Tracks a trailing stop loss for an open position. The stop loss
    only moves in the favorable direction (up for a BUY position),
    locking in profit as the price moves favorably, and never moves
    backward even if the price temporarily pulls back.
    """

    def __init__(self, entry_price: float, trail_percentage: float) -> None:
        """
        Args:
            entry_price: The price at which the position was entered.
            trail_percentage: The trailing distance as a percentage
                               (e.g. 5 for 5%).
        """
        if entry_price <= 0:
            raise ValueError("Entry price must be positive.")
        if trail_percentage <= 0:
            raise ValueError("Trail percentage must be positive.")

        self.entry_price = entry_price
        self.trail_percentage = trail_percentage
        self.highest_price = entry_price
        self.stop_loss_price = self._calculate_stop_loss(entry_price)

    def _calculate_stop_loss(self, price: float) -> float:
        """Internal helper: calculates stop loss based on a given price."""
        return round(price * (1 - self.trail_percentage / 100), 2)

    def update(self, current_price: float) -> float:
        """
        Updates the trailing stop loss based on the latest price.
        Should be called on every new price tick/candle.

        Args:
            current_price: The latest market price.

        Returns:
            The current stop loss price (updated if price made a new high).
        """
        if current_price > self.highest_price:
            self.highest_price = current_price
            self.stop_loss_price = self._calculate_stop_loss(current_price)

        return self.stop_loss_price

    def is_triggered(self, current_price: float) -> bool:
        """
        Checks whether the current price has hit the trailing stop loss.

        Args:
            current_price: The latest market price.

        Returns:
            True if the stop loss has been triggered (price <= stop loss).
        """
        return current_price <= self.stop_loss_price