def calculate_quantity(position_amount: float, entry_price: float) -> int:
    """
    Calculates how many shares to buy based on a fixed capital amount.
    """
    if position_amount <= 0:
        raise ValueError("Position amount must be positive.")
    if entry_price <= 0:
        raise ValueError("Entry price must be positive.")

    quantity = position_amount / entry_price
    return int(quantity)


def calculate_quantity_in_range(min_amount: float, max_amount: float, entry_price: float) -> int:
    """
    Calculates the quantity to buy such that the total capital deployed
    (quantity * entry_price) falls within [min_amount, max_amount].

    Args:
        min_amount: Minimum acceptable capital to deploy (e.g. 5000).
        max_amount: Maximum acceptable capital to deploy (e.g. 6000).
        entry_price: The price at which the trade will be entered.

    Returns:
        The quantity of shares to buy such that capital deployed falls
        within [min_amount, max_amount]. Returns 0 if no valid quantity
        exists within the range (stock is too expensive, or the price
        makes it impossible to land inside the range).
    """
    if min_amount <= 0 or max_amount <= 0:
        raise ValueError("Amounts must be positive.")
    if min_amount > max_amount:
        raise ValueError("min_amount cannot be greater than max_amount.")
    if entry_price <= 0:
        raise ValueError("Entry price must be positive.")

    # Find the largest quantity whose total cost doesn't exceed max_amount
    quantity = int(max_amount / entry_price)

    capital_deployed = quantity * entry_price

    # Valid only if it also meets the min_amount requirement
    if capital_deployed < min_amount:
        return 0

    return quantity

def calculate_target_price(entry_price: float, target_percentage: float) -> float:
    """
    Calculates the target (take-profit) price.
    """
    if entry_price <= 0:
        raise ValueError("Entry price must be positive.")
    if target_percentage <= 0:
        raise ValueError("Target percentage must be positive.")

    target_price = entry_price * (1 + target_percentage / 100)
    return round(target_price, 2)


def calculate_stop_loss_price(entry_price: float, stop_loss_percentage: float) -> float:
    """
    Calculates the stop loss price.
    """
    if entry_price <= 0:
        raise ValueError("Entry price must be positive.")
    if stop_loss_percentage <= 0:
        raise ValueError("Stop loss percentage must be positive.")

    stop_loss_price = entry_price * (1 - stop_loss_percentage / 100)
    return round(stop_loss_price, 2)