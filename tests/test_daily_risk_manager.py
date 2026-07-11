from risk.daily_risk_manager import DailyRiskManager

if __name__ == "__main__":
    risk_manager = DailyRiskManager(max_daily_loss=1000, max_trades_per_day=4)

    # Simulate a series of trades throughout the day
    trade_results = [500, -300, -800, 200, -700, -600]  # profit/loss per trade

    for i, pnl in enumerate(trade_results, start=1):
        if not risk_manager.can_trade():
            print(f"Trade {i}: BLOCKED — daily limit reached. Skipping.")
            continue

        risk_manager.record_trade(pnl)
        print(f"Trade {i}: PnL = {pnl} | Total P&L today: {risk_manager.total_pnl_today} | "
              f"Trades today: {risk_manager.trades_today} | Can trade next: {risk_manager.can_trade()}")