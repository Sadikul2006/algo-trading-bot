import pandas as pd
from paper_trading.trade import Trade


def calculate_win_rate(trades: list[Trade]) -> float:
    """
    Calculates the percentage of trades that were profitable.

    Returns:
        Win rate as a percentage (0-100). Returns 0.0 if no trades exist.
    """
    if not trades:
        return 0.0

    winning_trades = [t for t in trades if t.calculate_pnl() > 0]
    return round((len(winning_trades) / len(trades)) * 100, 2)


def calculate_profit_factor(trades: list[Trade]) -> float:
    """
    Calculates the ratio of gross profit to gross loss.
    A value above 1.0 means the strategy is profitable overall;
    above 2.0 is generally considered strong.

    Returns:
        The profit factor. Returns float('inf') if there are no losing
        trades (undefined division), or 0.0 if there are no trades at all.
    """
    if not trades:
        return 0.0

    gross_profit = sum(t.calculate_pnl() for t in trades if t.calculate_pnl() > 0)
    gross_loss = abs(sum(t.calculate_pnl() for t in trades if t.calculate_pnl() < 0))

    if gross_loss == 0:
        return float("inf")

    return round(gross_profit / gross_loss, 2)


def calculate_max_drawdown(equity_curve: list[float]) -> float:
    """
    Calculates the maximum drawdown: the largest peak-to-trough decline
    in the equity curve, as a percentage.

    Returns:
        Max drawdown as a positive percentage (e.g. 15.5 means a 15.5% drop
        from the highest point). Returns 0.0 if equity_curve is empty.
    """
    if not equity_curve:
        return 0.0

    equity_series = pd.Series(equity_curve)
    running_max = equity_series.cummax()
    drawdown = (equity_series - running_max) / running_max * 100

    return round(abs(drawdown.min()), 2)


def calculate_sharpe_ratio(equity_curve: list[float], risk_free_rate: float = 0.0) -> float:
    """
    Calculates a simplified annualized Sharpe Ratio based on daily returns
    of the equity curve.

    Args:
        equity_curve: List of portfolio values over time.
        risk_free_rate: The risk-free rate to subtract (default 0 for simplicity).

    Returns:
        The annualized Sharpe Ratio. Returns 0.0 if insufficient data.
    """
    if len(equity_curve) < 2:
        return 0.0

    equity_series = pd.Series(equity_curve)
    daily_returns = equity_series.pct_change().dropna()

    if daily_returns.std() == 0:
        return 0.0

    sharpe = (daily_returns.mean() - risk_free_rate) / daily_returns.std()
    annualized_sharpe = sharpe * (252 ** 0.5)

    return round(annualized_sharpe, 2)


def generate_performance_report(trades: list[Trade], equity_curve: list[float]) -> dict:
    """
    Generates a complete performance report combining all metrics.

    Returns:
        A dictionary with all key performance metrics.
    """
    return {
        "total_trades": len(trades),
        "win_rate": calculate_win_rate(trades),
        "profit_factor": calculate_profit_factor(trades),
        "max_drawdown": calculate_max_drawdown(equity_curve),
        "sharpe_ratio": calculate_sharpe_ratio(equity_curve),
        "total_pnl": round(sum(t.calculate_pnl() for t in trades), 2),
    }