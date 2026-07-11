from data.historical_data import fetch_historical_data
from backtest.backtest_engine import BacktestEngine
from backtest.performance_metrics import generate_performance_report
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

    report = generate_performance_report(backtest.portfolio.trade_history, backtest.equity_curve)

    print("=== Backtest Performance Report ===")
    for key, value in report.items():
        print(f"{key}: {value}")