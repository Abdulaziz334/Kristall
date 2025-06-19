import random
from ai_feedback.feedback import get_base_rating

# Statik misol: kelajakda bu ML modelga ulanadi

def recommend_product(user_id, past_orders):
    all_products = ["prod789", "prod123", "prod555", "prod999"]
    recommended = random.choice(all_products)
    return {"recommended_product": recommended}

def recommend_base(user_location, product_id, available_bases):
    best_score = -1
    best_base = None

    for base in available_bases:
        rating = get_base_rating(base["id"])
        distance = base["distance_km"]
        score = (rating * 2) - distance  # oddiy AI scoring
        if score > best_score:
            best_score = score
            best_base = base

    return best_base["id"] if best_base else None