import time

def send_drone(base_id, user_location, product_id):
    print(f"\n🚁 Dron {base_id} bazasidan jo'natildi...")
    time.sleep(1)

    route = calculate_route(base_id, user_location)
    print(f"📍 Marshrut: {route}")

    print(f"📦 Mahsulot ({product_id}) {user_location} manziliga yetkazilmoqda...")
    time.sleep(2)

    print("✅ Yetkazildi!")
    return {
        "status": "delivered",
        "base_id": base_id,
        "destination": user_location,
        "product_id": product_id
    }

def calculate_route(base_id, user_location):
    # Hozircha oddiy statik marshrut
    return f"{base_id} ➡ {user_location}"