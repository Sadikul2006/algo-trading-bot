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