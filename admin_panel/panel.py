import json
import os

ORDERS_FILE = "order_module/orders.json"
BASES_FILE = "admin_panel/bases.json"
USERS_FILE = "admin_panel/users.json"

def list_orders():
    if not os.path.exists(ORDERS_FILE):
        return []
    with open(ORDERS_FILE, "r") as f:
        return json.load(f)

def list_bases():
    if not os.path.exists(BASES_FILE):
        return []
    with open(BASES_FILE, "r") as f:
        return json.load(f)

def add_base(base_id, location):
    base = {"id": base_id, "location": location}
    data = list_bases()
    data.append(base)
    with open(BASES_FILE, "w") as f:
        json.dump(data, f, indent=4)

def list_users():
    if not os.path.exists(USERS_FILE):
        return []
    with open(USERS_FILE, "r") as f:
        return json.load(f)

def add_user(user_id, name):
    user = {"id": user_id, "name": name}
    data = list_users()
    data.append(user)
    with open(USERS_FILE, "w") as f:
        json.dump(data, f, indent=4)