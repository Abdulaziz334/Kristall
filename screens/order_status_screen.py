import json
import os

ORDERS_FILE = "order_module/orders.json"

def show_order_status():
    print("📦 Mening buyurtmalarim")

    if not os.path.exists(ORDERS_FILE):
        print("❌ Buyurtmalar topilmadi.")
    else:
        with open(ORDERS_FILE, "r") as f:
            orders = json.load(f)
            for order in orders:
                if order["user_id"] == "user123":
                    print(f"- {order['order_id']} | Mahsulot: {order['product_id']} | Holat: {order['status']} | Baza: {order['selected_base']}")

    input("Bosh menyuga qaytish uchun Enter bosing...")
    from .home_screen import show_home_screen
    show_home_screen()