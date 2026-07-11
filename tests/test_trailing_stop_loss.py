from risk.trailing_stop_loss import TrailingStopLoss

if __name__ == "__main__":
    tsl = TrailingStopLoss(entry_price=100, trail_percentage=5)
    print(f"Initial Stop Loss: {tsl.stop_loss_price}")

    # Simulate price movement over time
    price_sequence = [100, 105, 110, 108, 106, 104.5, 103, 104]

    for price in price_sequence:
        stop_loss = tsl.update(price)
        triggered = tsl.is_triggered(price)
        print(f"Price: {price} | Stop Loss: {stop_loss} | Triggered: {triggered}")