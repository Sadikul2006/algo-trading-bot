from dataclasses import dataclass, field
from datetime import datetime


@dataclass
class Trade:
    """
    Represents a single paper trade (position) — either open or closed.
    Using a dataclass here since this is primarily a data container,
    with minimal behavior of its own.
    """

    symbol: str
    quantity: int
    entry_price: float
    stop_loss_price: float
    target_price: float
    direction: str  # "BUY" or "SELL"
    entry_time: datetime = field(default_factory=datetime.now)

    exit_price: float | None = None
    exit_time: datetime | None = None
    exit_reason: str | None = None  # "TARGET", "STOP_LOSS", "MANUAL"
    is_open: bool = True

    def close(self, exit_price: float, exit_reason: str) -> None:
        """
        Marks the trade as closed, recording the exit details.

        Args:
            exit_price: The price at which the trade was exited.
            exit_reason: Why the trade was closed (e.g. "TARGET", "STOP_LOSS").
        """
        self.exit_price = exit_price
        self.exit_reason = exit_reason
        self.exit_time = datetime.now()
        self.is_open = False

    def calculate_pnl(self) -> float:
        """
        Calculates the profit or loss for this trade.
        Returns 0 if the trade is still open (no exit price yet).
        """
        if self.exit_price is None:
            return 0.0

        if self.direction == "BUY":
            return round((self.exit_price - self.entry_price) * self.quantity, 2)
        else:  # SELL (short position)
            return round((self.entry_price - self.exit_price) * self.quantity, 2)