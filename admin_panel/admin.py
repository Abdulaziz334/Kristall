import json
import os

USERS_FILE = "user_module/users.json"
ORDERS_FILE = "order_module/orders.json"
BASES_FILE = "ai_router/bases.json"

def list_users():
    if not os.path.exists(USERS_FILE):
        return []
    with open(USERS_FILE, "r") as f:
        return json.load(f)

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

def add_base(base_id, location, stock=None):
    if stock is None:
        stock = []

    base = {
        "id": base_id,
        "location": location,
        "stock": stock
    }

    bases = list_bases()
    bases.append(base)

    with open(BASES_FILE, "w") as f:
        json.dump(bases, f, indent=4)

    return base

def update_base_stock(base_id, new_stock):
    bases = list_bases()
    for base in bases:
        if base["id"] == base_id:
            base["stock"] = new_stock
            break

    with open(BASES_FILE, "w") as f:
        json.dump(bases, f, indent=4)
    return True