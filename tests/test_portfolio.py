from paper_trading.portfolio import Portfolio

if __name__ == "__main__":
    portfolio = Portfolio(starting_balance=100000)

    print(f"Starting Balance: {portfolio.cash_balance}")

    # Open a position
    portfolio.open_position(
        symbol="RELIANCE", quantity=4, entry_price=1450,
        stop_loss_price=1377.5, target_price=1595, direction="BUY"
    )
    print(f"Cash after opening position: {portfolio.cash_balance}")

    # Close it at a profit
    pnl = portfolio.close_position(symbol="RELIANCE", exit_price=1595, exit_reason="TARGET")
    print(f"Cash after closing position: {portfolio.cash_balance}")
    print(f"Trade P&L: {pnl}")

    print(f"\nTotal P&L: {portfolio.get_total_pnl()}")
    print(f"Portfolio Value: {portfolio.get_portfolio_value()}")
    print(f"Trade History Count: {len(portfolio.trade_history)}")