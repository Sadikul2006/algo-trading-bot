def calculate_risk_reward_ratio(entry_price: float, stop_loss_price: float,
                                 target_price: float) -> float:
    """
    Calculates the Risk/Reward ratio for a potential trade.

    Args:
        entry_price: The price at which the trade will be entered.
        stop_loss_price: The price at which the trade will be exited if
                          it goes wrong.
        target_price: The price at which profit will be booked.

    Returns:
        The risk/reward ratio (e.g. 3.0 means potential reward is 3x
        the potential risk). Higher is generally better.
    """
    if entry_price <= 0 or stop_loss_price <= 0 or target_price <= 0:
        raise ValueError("All prices must be positive.")

    risk = abs(entry_price - stop_loss_price)
    reward = abs(target_price - entry_price)

    if risk == 0:
        raise ValueError("Risk cannot be zero (entry price equals stop loss price).")

    return round(reward / risk, 2)


def is_favorable_trade(entry_price: float, stop_loss_price: float,
                        target_price: float, min_ratio: float = 1.5) -> bool:
    """
    Determines whether a trade meets a minimum acceptable risk/reward ratio.
    This can be used as a filter before entering any trade.

    Args:
        entry_price: The price at which the trade will be entered.
        stop_loss_price: The price at which the trade will be exited if wrong.
        target_price: The price at which profit will be booked.
        min_ratio: The minimum acceptable risk/reward ratio. Defaults to 1.5.

    Returns:
        True if the trade's risk/reward ratio meets or exceeds min_ratio.
    """
    ratio = calculate_risk_reward_ratio(entry_price, stop_loss_price, target_price)
    return ratio >= min_ratio