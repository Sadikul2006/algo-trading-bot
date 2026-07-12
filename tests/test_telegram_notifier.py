from telegram.notifier import TelegramNotifier

if __name__ == "__main__":
    notifier = TelegramNotifier()

    print("Sending trade alert...")
    notifier.send_trade_alert(symbol="RELIANCE", direction="BUY", quantity=4, price=1450)

    print("Sending exit alert...")
    notifier.send_trade_alert(symbol="RELIANCE", direction="SELL", quantity=4, price=1595, reason="TARGET")

    print("Sending error alert...")
    notifier.send_error_alert("Failed to connect to broker API.")

    print("Sending daily report...")
    notifier.send_daily_report(total_trades=5, total_pnl=1250.50, win_rate=60.0)

    print("All test messages sent!")