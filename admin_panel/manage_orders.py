import json
import os

ORDERS_FILE = "order_module/orders.json"

def view_orders():
    if not os.path.exists(ORDERS_FILE):
        print("📂 Buyurtmalar mavjud emas.")
        return
    
    with open(ORDERS_FILE, "r") as f:
        orders = json.load(f)
        for o in orders:
            print(f"📦 Order ID: {o['order_id']}")
            print(f"👤 Foydalanuvchi: {o['user_id']}")
            print(f"📍 Joylashuv: {o['user_location']}")
            print(f"🏪 Baza: {o['selected_base']}")
            print(f"🧾 Status: {o['status']}\n")