from risk.position_sizing import (
    calculate_quantity_in_range,
    calculate_target_price,
    calculate_stop_loss_price,
)

if __name__ == "__main__":
    min_amount = 5000
    max_amount = 6000

    # Different realistic stock prices to test with
    sample_prices = [1450, 320, 89, 2100, 7500]

    for entry_price in sample_prices:
        quantity = calculate_quantity_in_range(min_amount, max_amount, entry_price)
        capital_deployed = quantity * entry_price

        print(f"\nEntry Price: ₹{entry_price}")
        print(f"  Quantity: {quantity} shares")
        print(f"  Capital Deployed: ₹{capital_deployed}")

        if quantity > 0:
            target = calculate_target_price(entry_price, 10)
            stop_loss = calculate_stop_loss_price(entry_price, 5)
            print(f"  Target: ₹{target}")
            print(f"  Stop Loss: ₹{stop_loss}")
        else:
            print("  Skipped: stock too expensive for this budget range")