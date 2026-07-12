from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from data.historical_data import fetch_historical_data
from backtest.backtest_engine import BacktestEngine
from backtest.performance_metrics import generate_performance_report
from strategy.mean_reversion_strategy import MeanReversionStrategy

app = FastAPI(title="Algo Trading Bot Dashboard")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/health")
def health_check() -> dict:
    """Simple endpoint to verify the server is running."""
    return {"status": "ok", "message": "Algo Trading Bot API is running"}


@app.get("/backtest/{symbol}")
def run_backtest(symbol: str, period: str = "1y") -> dict:
    """
    Runs a backtest for the given stock symbol using the Mean Reversion
    strategy, and returns the performance report along with trade details.
    """
    try:
        data = fetch_historical_data(symbol, period=period, interval="1d")
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))

    strategy = MeanReversionStrategy(period=20, std_dev=2.0)

    backtest = BacktestEngine(
        strategy=strategy,
        historical_data=data,
        symbol=symbol,
        starting_balance=100000,
        min_amount=5000,
        max_amount=6000,
        target_percentage=10,
        stop_loss_percentage=5,
        warmup_period=30,
    )
    backtest.run()

    report = generate_performance_report(backtest.portfolio.trade_history, backtest.equity_curve)

    trades = [
        {
            "symbol": t.symbol,
            "entry_price": t.entry_price,
            "exit_price": t.exit_price,
            "quantity": t.quantity,
            "exit_reason": t.exit_reason,
            "pnl": t.calculate_pnl(),
        }
        for t in backtest.portfolio.trade_history
    ]

    return {
        "symbol": symbol,
        "performance": report,
        "trades": trades,
        "equity_curve": backtest.equity_curve,
    }