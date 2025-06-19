import json
import os
from datetime import datetime

NOTIFY_FILE = "notification_module/notifications.json"

def create_notification(user_id, title, message):
    notification = {
        "user_id": user_id,
        "title": title,
        "message": message,
        "timestamp": datetime.now().isoformat()
    }

    save_notification(notification)
    return notification

def save_notification(notification):
    if not os.path.exists(NOTIFY_FILE):
        with open(NOTIFY_FILE, "w") as f:
            json.dump([], f)

    with open(NOTIFY_FILE, "r+") as f:
        data = json.load(f)
        data.append(notification)
        f.seek(0)
        json.dump(data, f, indent=4)

def get_user_notifications(user_id):
    if not os.path.exists(NOTIFY_FILE):
        return []

    with open(NOTIFY_FILE, "r") as f:
        data = json.load(f)
        return [n for n in data if n["user_id"] == user_id]