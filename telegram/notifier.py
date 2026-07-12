import logging
import requests
from config.settings import settings

logger = logging.getLogger(__name__)


class TelegramNotifier:
    """
    Sends notifications to a configured Telegram chat using the
    Telegram Bot API. Used for trade alerts, error alerts, and
    daily reports.
    """

    def __init__(self) -> None:
        self.bot_token = settings.TELEGRAM_BOT_TOKEN
        self.chat_id = settings.TELEGRAM_CHAT_ID
        self.base_url = f"https://api.telegram.org/bot{self.bot_token}"

        if not self.bot_token or not self.chat_id:
            logger.warning("Telegram credentials not configured. Notifications will be skipped.")

    def send_message(self, text: str) -> bool:
        """
        Sends a text message to the configured Telegram chat.

        Args:
            text: The message content to send.

        Returns:
            True if the message was sent successfully, False otherwise.
        """
        if not self.bot_token or not self.chat_id:
            logger.warning("Cannot send Telegram message: credentials missing.")
            return False

        url = f"{self.base_url}/sendMessage"
        payload = {"chat_id": self.chat_id, "text": text}

        try:
            response = requests.post(url, data=payload, timeout=5)
            response.raise_for_status()
            logger.info("Telegram message sent successfully.")
            return True
        except requests.RequestException as e:
            logger.error(f"Failed to send Telegram message: {e}")
            return False

    def send_trade_alert(self, symbol: str, direction: str, quantity: int,
                          price: float, reason: str = "") -> bool:
        """
        Sends a formatted trade alert (BUY/SELL execution).

        Args:
            symbol: The stock symbol traded.
            direction: "BUY" or "SELL".
            quantity: Number of shares traded.
            price: The execution price.
            reason: Optional reason (e.g. "TARGET", "STOP_LOSS") for exits.
        """
        emoji = "🟢" if direction == "BUY" else "🔴"
        message = (
            f"{emoji} TRADE ALERT: {direction}\n"
            f"Symbol: {symbol}\n"
            f"Quantity: {quantity}\n"
            f"Price: ₹{price}"
        )
        if reason:
            message += f"\nReason: {reason}"

        return self.send_message(message)

    def send_error_alert(self, error_message: str) -> bool:
        """
        Sends a formatted error alert.

        Args:
            error_message: Description of the error that occurred.
        """
        message = f"⚠️ ERROR ALERT\n{error_message}"
        return self.send_message(message)

    def send_daily_report(self, total_trades: int, total_pnl: float, win_rate: float) -> bool:
        """
        Sends a formatted end-of-day summary report.

        Args:
            total_trades: Number of trades executed today.
            total_pnl: Total profit/loss for the day.
            win_rate: Percentage of winning trades.
        """
        emoji = "📈" if total_pnl >= 0 else "📉"
        message = (
            f"{emoji} DAILY REPORT\n"
            f"Total Trades: {total_trades}\n"
            f"Win Rate: {win_rate}%\n"
            f"Total P&L: ₹{total_pnl}"
        )
        return self.send_message(message) 

        
           