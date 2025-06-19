import json
import os

TRACKING_FILE = "ai_engine/user_behavior.json"

def log_user_action(user_id, action_type, details):
    log_entry = {
        "user_id": user_id,
        "action": action_type,
        "details": details
    }

    if not os.path.exists(TRACKING_FILE):
        with open(TRACKING_FILE, "w") as f:
            json.dump([], f)

    with open(TRACKING_FILE, "r+") as f:
        data = json.load(f)
        data.append(log_entry)
        f.seek(0)
        json.dump(data, f, indent=4)