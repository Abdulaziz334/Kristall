bases = [
    {"id": "BASE_TASHKENT_01", "location": "Toshkent", "stock": 20},
    {"id": "BASE_SAMARKAND_01", "location": "Samarqand", "stock": 15},
]

def view_bases():
    print("\n🏬 Bazalar:")
    for b in bases:
        print(f"ID: {b['id']}, Joylashuv: {b['location']}, Mahsulotlar: {b['stock']}")