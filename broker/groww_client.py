import logging
from growwapi import GrowwAPI
from config.settings import settings

# Set up a logger specific to this module
logger = logging.getLogger(__name__)


class GrowwClient:
    """
    Wrapper around the Groww SDK.
    This is the ONLY class in the entire project that talks directly
    to the Groww API. Every other module (strategy, risk, data, etc.)
    goes through this class instead of calling growwapi directly.
    """

    def __init__(self) -> None:
        """
        Authenticates with Groww using the API key/secret from settings,
        and initializes the underlying SDK client.
        """
        settings.validate()  # fail fast if credentials are missing

        try:
            access_token = GrowwAPI.get_access_token(
                api_key=settings.GROWW_API_KEY,
                secret=settings.GROWW_API_SECRET,
            )
            self._client = GrowwAPI(access_token)
            logger.info("Successfully authenticated with Groww API.")
        except Exception as e:
            logger.error(f"Failed to authenticate with Groww API: {e}")
            raise

    def get_profile(self) -> dict:
        """Fetches the authenticated user's account profile."""
        return self._client.get_user_profile()

    def get_holdings(self) -> dict:
        """Fetches the user's current stock holdings (long-term delivery stocks)."""
        return self._client.get_holdings_for_user(timeout=5)

    def get_positions(self) -> dict:
        """Fetches the user's current positions (CASH, FNO, COMMODITY)."""
        return self._client.get_positions_for_user()

    def get_ltp(self, trading_symbol: str, exchange: str = "NSE") -> dict:
        """
        Fetches the Last Traded Price (LTP) for a given stock/index symbol.

        Args:
            trading_symbol: The stock symbol, e.g. "RELIANCE" or "NIFTY".
            exchange: The exchange the symbol belongs to. Defaults to "NSE".

        Returns:
            A dictionary containing the LTP data for the requested symbol.
        """
        exchange_trading_symbol = f"{exchange}_{trading_symbol}"
        return self._client.get_ltp(
            segment=self._client.SEGMENT_CASH,
            exchange_trading_symbols=exchange_trading_symbol,
        )