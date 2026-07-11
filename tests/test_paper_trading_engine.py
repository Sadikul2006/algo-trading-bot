import pandas as pd
from paper_trading.engine import PaperTradingEngine
from paper_trading.portfolio import Portfolio
from strategy.mean_reversion_strategy import MeanReversionStrategy

if __name__ == "__main__":
    portfolio = Portfolio(starting_balance=100000)
    strategy = MeanReversionStrategy(period=15, std_dev=2.0)

    engine = PaperTradingEngine(
        strategy=strategy,
        portfolio=portfolio,
        symbol="TESTSTOCK",
        min_amount=5000,
        max_amount=6000,
        target_percentage=10,
        stop_loss_percentage=5,
    )

    # Simulate a sequence of closing prices arriving one by one
    close_prices = [100, 101, 99, 100, 102, 98, 101, 100, 99, 100,
                     101, 99, 100, 102, 98, 101, 100, 99, 100, 85,
                     88, 92, 95, 99, 105, 110, 115]

    for i in range(15, len(close_prices) + 1):
        # Feed the engine data "up to today", simulating candles arriving over time
        window = pd.DataFrame({"close": close_prices[:i]})
        engine.process_candle(window)

    print(f"Final Cash Balance: {portfolio.cash_balance}")
    print(f"Total P&L: {portfolio.get_total_pnl()}")
    print(f"Trades completed: {len(portfolio.trade_history)}")

    for trade in portfolio.trade_history:
        print(f"  {trade.symbol} | Entry: {trade.entry_price} | Exit: {trade.exit_price} | "
              f"Reason: {trade.exit_reason} | P&L: {trade.calculate_pnl()}")