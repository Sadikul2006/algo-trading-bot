import threading
import time
import logging
from datetime import datetime
from paper_trading.portfolio import Portfolio
from paper_trading.engine import PaperTradingEngine
from strategy.mean_reversion_strategy import MeanReversionStrategy
from broker.groww_client import GrowwClient
from telegram.notifier import TelegramNotifier
from database.db import init_db

logger = logging.getLogger(__name__)


class BotState:
    """Singleton-style manager for the bot's running state and background loop."""

    def __init__(self):
        self.is_running = False
        self.symbol = "RELIANCE"
        self.portfolio = Portfolio(starting_balance=100000, use_database=True)
        self.strategy = MeanReversionStrategy(period=20, std_dev=2.0)
        self.engine = PaperTradingEngine(
            strategy=self.strategy,
            portfolio=self.portfolio,
            symbol=self.symbol,
            min_amount=5000,
            max_amount=6000,
            target_percentage=10,
            stop_loss_percentage=5,
        )
        self.notifier = TelegramNotifier()
        self._thread = None
        self.last_update = None

    def start(self) -> str:
        if self.is_running:
            return "Bot is already running."

        init_db()
        self.is_running = True
        self._thread = threading.Thread(target=self._run_loop, daemon=True)
        self._thread.start()
        self.notifier.send_message("🟢 Bot STARTED")
        logger.info("Bot started.")
        return "Bot started successfully."

    def stop(self) -> str:
        if not self.is_running:
            return "Bot is already stopped."

        self.is_running = False
        self.notifier.send_message("🔴 Bot STOPPED")
        logger.info("Bot stopped.")
        return "Bot stopped successfully."

    def _run_loop(self):
        """Background loop: fetches live price and processes it every interval."""
        from broker.groww_client import GrowwClient
        try:
            client = GrowwClient()
        except Exception as e:
            logger.error(f"Failed to connect to broker: {e}")
            self.is_running = False
            return

        import pandas as pd
        while self.is_running:
            try:
                ltp_data = client.get_ltp(self.symbol)
                # NOTE: requires a live data subscription to work
                price = list(ltp_data.values())[0] if ltp_data else None

                if price:
                    window = pd.DataFrame({"close": [price]})  # simplified single-row
                    self.engine.process_candle(window)
                    self.last_update = datetime.now()
            except Exception as e:
                logger.error(f"Error in bot loop: {e}")
                self.notifier.send_error_alert(str(e))

            time.sleep(60)  # check every 60 seconds

    def get_status(self) -> dict:
        return {
            "is_running": self.is_running,
            "symbol": self.symbol,
            "cash_balance": self.portfolio.cash_balance,
            "open_positions": {
                s: {"quantity": p.quantity, "entry_price": p.entry_price}
                for s, p in self.portfolio.open_positions.items()
            },
            "total_pnl": self.portfolio.get_total_pnl(),
            "total_trades": len(self.portfolio.trade_history),
            "last_update": str(self.last_update) if self.last_update else None,
        }


bot_state = BotState()