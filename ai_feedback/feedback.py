import json
import os

FEEDBACK_FILE = "ai_feedback/feedbacks.json"

def submit_feedback(user_id, base_id, rating, comment=""):
    if rating < 1 or rating > 5:
        return {"error": "Reyting 1 dan 5 gacha bo‘lishi kerak."}
    
    feedback = {
        "user_id": user_id,
        "base_id": base_id,
        "rating": rating,
        "comment": comment
    }

    all_feedbacks = load_feedbacks()
    all_feedbacks.append(feedback)
    
    with open(FEEDBACK_FILE, "w") as f:
        json.dump(all_feedbacks, f, indent=4)
    
    return {"success": True, "feedback": feedback}

def load_feedbacks():
    if not os.path.exists(FEEDBACK_FILE):
        return []
    with open(FEEDBACK_FILE, "r") as f:
        return json.load(f)

def get_base_rating(base_id):
    feedbacks = load_feedbacks()
    ratings = [f["rating"] for f in feedbacks if f["base_id"] == base_id]
    
    if not ratings:
        return 0
    return round(sum(ratings) / len(ratings), 2)