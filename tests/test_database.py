from database.db import init_db, get_session
from database.models import TradeRecord

if __name__ == "__main__":
    print("Initializing database...")
    init_db()
    print("Database initialized! Check for 'trading_bot.db' file in the project root.")

    # Insert a sample trade record to verify everything works
    session = get_session()
    try:
        sample_trade = TradeRecord(
            symbol="RELIANCE",
            direction="BUY",
            quantity=4,
            entry_price=1450.0,
            stop_loss_price=1377.5,
            target_price=1595.0,
        )
        session.add(sample_trade)
        session.commit()
        print(f"Sample trade inserted with id: {sample_trade.id}")

        # Read it back
        all_trades = session.query(TradeRecord).all()
        print(f"\nTotal trades in database: {len(all_trades)}")
        for t in all_trades:
            print(f"  ID: {t.id}, Symbol: {t.symbol}, Entry: {t.entry_price}")
    finally:
        session.close()