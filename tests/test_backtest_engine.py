from data.historical_data import fetch_historical_data
from backtest.backtest_engine import BacktestEngine
from strategy.mean_reversion_strategy import MeanReversionStrategy

if __name__ == "__main__":
    data = fetch_historical_data("RELIANCE", period="1y", interval="1d")

    strategy = MeanReversionStrategy(period=20, std_dev=2.0)

    backtest = BacktestEngine(
        strategy=strategy,
        historical_data=data,
        symbol="RELIANCE",
        starting_balance=100000,
        min_amount=5000,
        max_amount=6000,
        target_percentage=10,
        stop_loss_percentage=5,
        warmup_period=30,
    )

    backtest.run()

    print(f"Starting Balance: 100000")
    print(f"Final Cash Balance: {backtest.portfolio.cash_balance}")
    print(f"Total P&L: {backtest.portfolio.get_total_pnl()}")
    print(f"Total Trades: {len(backtest.portfolio.trade_history)}")
    print(f"Equity Curve Length: {len(backtest.equity_curve)}")