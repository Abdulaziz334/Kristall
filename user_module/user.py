# user_module/user.py

import uuid
import json
import os

USERS_FILE = "user_module/users.json"

def register_user(username, phone_number):
    user = {
        "user_id": str(uuid.uuid4()),
        "username": username,
        "phone_number": phone_number,
        "registered": True
    }

    save_user(user)
    return user

def get_all_users():
    if not os.path.exists(USERS_FILE):
        return []
    
    with open(USERS_FILE, "r") as f:
        return json.load(f)

def save_user(user):
    if not os.path.exists(USERS_FILE):
        with open(USERS_FILE, "w") as f:
            json.dump([], f)

    with open(USERS_FILE, "r+") as f:
        users = json.load(f)
        users.append(user)
        f.seek(0)
        json.dump(users, f, indent=4)

def get_user_by_phone(phone_number):
    users = get_all_users()
    for user in users:
        if user["phone_number"] == phone_number:
            return user
    return None
import json
import uuid
import os

USERS_FILE = "user_module/users.json"
HISTORY_FILE = "user_module/history.json"

def register_user(name, location):
    user = {
        "user_id": str(uuid.uuid4()),
        "name": name,
        "location": location
    }
    save_user(user)
    return user

def save_user(user):
    if not os.path.exists(USERS_FILE):
        with open(USERS_FILE, "w") as f:
            json.dump([], f)

    with open(USERS_FILE, "r+") as f:
        data = json.load(f)
        data.append(user)
        f.seek(0)
        json.dump(data, f, indent=4)

def add_order_history(user_id, order_id):
    record = {
        "user_id": user_id,
        "order_id": order_id
    }

    if not os.path.exists(HISTORY_FILE):
        with open(HISTORY_FILE, "w") as f:
            json.dump([], f)

    with open(HISTORY_FILE, "r+") as f:
        data = json.load(f)
        data.append(record)
        f.seek(0)
        json.dump(data, f, indent=4)

def get_user_history(user_id):
    if not os.path.exists(HISTORY_FILE):
        return []

    with open(HISTORY_FILE, "r") as f:
        data = json.load(f)
        return [h for h in data if h["user_id"] == user_id]