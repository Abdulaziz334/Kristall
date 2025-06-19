from ai_engine import log_user_action, get_dynamic_price, ai_recommendation

log_user_action("user123", "view_product", {"product_id": "prod789"})

price = get_dynamic_price(10000, demand_level=8, stock_left=5)
print("AI narx:", price)

base_list = [
    {"id": "BASE01", "inventory": ["prod789", "prod456"], "delivery_time": 10},
    {"id": "BASE02", "inventory": ["prod789"], "delivery_time": 5}
]
best_base = ai_recommendation("user123", "prod789", base_list)
print("Eng yaxshi baza:", best_base)