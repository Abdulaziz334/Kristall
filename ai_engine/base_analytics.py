def analyze_base(base_id, inventory, delivery_speed):
    score = (len(inventory) * 2) + (100 - delivery_speed)
    return {
        "base_id": base_id,
        "ai_score": score
    }