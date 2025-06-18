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