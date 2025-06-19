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
from admin_panel.manage_orders import view_orders
from admin_panel.manage_bases import view_bases

def admin_menu():
    while True:
        print("\n🛠 ADMIN PANEL")
        print("1. Buyurtmalar")
        print("2. Bazalar")
        print("0. Chiqish")

        tanlov = input("Tanlang: ")

        if tanlov == "1":
            view_orders()
        elif tanlov == "2":
            view_bases()
        elif tanlov == "0":
            break
        else:
            print("❌ Noto‘g‘ri tanlov.")

# Dastur ishga tushganda chaqirilsin
if __name__ == "__main__":
    admin_menu()