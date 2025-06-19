def get_dynamic_price(base_price, demand_level, stock_left):
    if demand_level > 7:
        return base_price * 1.2
    elif stock_left < 10:
        return base_price * 1.1
    else:
        return base_price