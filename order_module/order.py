# order_module/order.py

import uuid
import json
import os

ORDERS_FILE = "order_module/orders.json"

def create_order(user_id, product_id, user_location):
    base = find_nearest_base(user_location, product_id)
    if not base:
        return {"error": "Mahsulot hech qaysi bazada topilmadi."}

    order = {
        "order_id": str(uuid.uuid4()),
        "user_id": user_id,
        "product_id": product_id,
        "user_location": user_location,
        "selected_base": base["id"],
        "status": "pending_payment"
    }

    save_order(order)
    return order

def find_nearest_base(user_location, product_id):
    # AI orqali eng yaqin baza va mavjud mahsulotni aniqlash
    # Hozircha statik
    return {
        "id": "BASE_TASHKENT_01",
        "distance_km": 3.4,
        "has_product": True
    }

def save_order(order):
    if not os.path.exists(ORDERS_FILE):
        with open(ORDERS_FILE, "w") as f:
            json.dump([], f)
    
    with open(ORDERS_FILE, "r+") as f:
        data = json.load(f)
        data.append(order)
        f.seek(0)
        json.dump(data, f, indent=4)