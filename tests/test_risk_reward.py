from risk.risk_reward import calculate_risk_reward_ratio, is_favorable_trade

if __name__ == "__main__":
    # Good trade: high reward relative to risk
    ratio1 = calculate_risk_reward_ratio(entry_price=100, stop_loss_price=95, target_price=115)
    print(f"Trade 1 - Entry:100, SL:95, Target:115 -> Ratio: {ratio1}, Favorable: {is_favorable_trade(100, 95, 115)}")

    # Poor trade: low reward relative to risk
    ratio2 = calculate_risk_reward_ratio(entry_price=100, stop_loss_price=95, target_price=102)
    print(f"Trade 2 - Entry:100, SL:95, Target:102 -> Ratio: {ratio2}, Favorable: {is_favorable_trade(100, 95, 102)}")