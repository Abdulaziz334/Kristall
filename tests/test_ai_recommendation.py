from ai_recommendation import recommend_product, recommend_base

# Foydalanuvchiga mahsulot tavsiyasi
suggested = recommend_product("user123", ["prod123", "prod555"])
print("Tavsiya qilingan mahsulot:", suggested)

# Baza tavsiyasi
bases = [
    {"id": "BASE_TASHKENT_01", "distance_km": 2.1},
    {"id": "BASE_TASHKENT_02", "distance_km": 3.7},
    {"id": "BASE_TASHKENT_03", "distance_km": 1.5}
]
recommended_base = recommend_base("Toshkent", "prod123", bases)
print("Tavsiya qilingan baza:", recommended_base)