import time
import logging
import requests
from config.settings import settings
from dashboard.bot_state import bot_state

logger = logging.getLogger(__name__)


def listen_for_commands():
    """Polls Telegram for new messages and handles /start and /stop commands."""
    base_url = f"https://api.telegram.org/bot{settings.TELEGRAM_BOT_TOKEN}"
    last_update_id = None

    while True:
        try:
            params = {"timeout": 30}
            if last_update_id:
                params["offset"] = last_update_id + 1

            response = requests.get(f"{base_url}/getUpdates", params=params, timeout=35)
            data = response.json()

            for update in data.get("result", []):
                last_update_id = update["update_id"]
                message = update.get("message", {}).get("text", "")
                print(f"DEBUG: Received message: '{message}'")

                if message == "/start":
                    result = bot_state.start()
                    bot_state.notifier.send_message(result)
                elif message == "/stop":
                    result = bot_state.stop()
                    bot_state.notifier.send_message(result)
                elif message == "/status":
                    status = bot_state.get_status()
                    status_text = (
                        f"📊 BOT STATUS\n"
                        f"Running: {status['is_running']}\n"
                        f"Symbol: {status['symbol']}\n"
                        f"Cash Balance: ₹{status['cash_balance']}\n"
                        f"Total P&L: ₹{status['total_pnl']}\n"
                        f"Total Trades: {status['total_trades']}\n"
                        f"Last Update: {status['last_update']}"
                    )
                    bot_state.notifier.send_message(status_text)

        except Exception as e:
            logger.error(f"Error in command listener: {e}")

        time.sleep(2)


if __name__ == "__main__":
    listen_for_commands()