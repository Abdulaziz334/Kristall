from .behavior_tracker import log_user_action
from .dynamic_pricing import get_dynamic_price
from .base_analytics import analyze_base

def ai_recommendation(user_id, product_id, base_list):
    return sorted(
        base_list,
        key=lambda b: analyze_base(b["id"], b["inventory"], b["delivery_time"])["ai_score"],
        reverse=True
    )[0]["id"]