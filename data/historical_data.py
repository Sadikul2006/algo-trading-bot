import logging
import pandas as pd
import yfinance as yf

logger = logging.getLogger(__name__)


def fetch_historical_data(symbol: str, period: str = "1y", interval: str = "1d") -> pd.DataFrame:
    """
    Fetches historical price data for an NSE-listed stock using yfinance.

    Args:
        symbol: The stock symbol without exchange suffix (e.g. "RELIANCE").
        period: How far back to fetch data (e.g. "1y", "6mo", "5y", "max").
        interval: Candle interval (e.g. "1d" for daily, "1h" for hourly).

    Returns:
        A pandas DataFrame with columns: open, high, low, close, volume,
        indexed by date, ordered oldest to newest.

    Raises:
        ValueError: If no data could be fetched for the given symbol.
    """
    yahoo_symbol = f"{symbol}.NS"

    logger.info(f"Fetching historical data for {yahoo_symbol} (period={period}, interval={interval})")

    raw_data = yf.download(yahoo_symbol, period=period, interval=interval, progress=False)

    if raw_data.empty:
        raise ValueError(f"No historical data found for symbol: {symbol}")

    if isinstance(raw_data.columns, pd.MultiIndex):
        raw_data.columns = raw_data.columns.get_level_values(0)

    raw_data = raw_data.rename(columns={
        "Open": "open",
        "High": "high",
        "Low": "low",
        "Close": "close",
        "Volume": "volume",
    })

    return raw_data[["open", "high", "low", "close", "volume"]]