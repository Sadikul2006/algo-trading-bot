from paper_trading.portfolio import Portfolio
from database.db import init_db

if __name__ == "__main__":
    init_db()  # Ensure tables exist

    portfolio = Portfolio(starting_balance=100000, use_database=True)

    print(f"Starting Balance: {portfolio.cash_balance}")

    portfolio.open_position(
        symbol="TCS", quantity=2, entry_price=3500,
        stop_loss_price=3325, target_price=3850, direction="BUY"
    )
    print(f"Cash after opening position: {portfolio.cash_balance}")

    pnl = portfolio.close_position(symbol="TCS", exit_price=3850, exit_reason="TARGET")
    print(f"Cash after closing position: {portfolio.cash_balance}")
    print(f"Trade P&L: {pnl}")
    print("Trade should now be saved in trading_bot.db")