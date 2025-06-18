import json
import os

ORDERS_FILE = "order_module/orders.json"

def route_order(order_id):
    order = get_order_by_id(order_id)
    if not order:
        return {"error": "Buyurtma topilmadi"}

    base_chain = calculate_route(order["selected_base"], order["user_location"])
    
    order_route = {
        "order_id": order_id,
        "route": base_chain,
        "status": "in_transit"
    }

    save_route(order_route)
    return order_route

def calculate_route(base_id, user_location):
    return [base_id, "MID_BASE_02", "USER_DESTINATION"]

def get_order_by_id(order_id):
    if not os.path.exists(ORDERS_FILE):
        return None
    
    with open(ORDERS_FILE, "r") as f:
        orders = json.load(f)
        for order in orders:
            if order["order_id"] == order_id:
                return order
    return None

def save_route(route):
    os.makedirs("base_router", exist_ok=True)
    with open("base_router/routes.json", "a") as f:
        f.write(json.dumps(route) + "\n")