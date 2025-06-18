import random

def choose_best_base(user_location, product_id, bases):
    """
    Foydalanuvchiga eng mos bazani tanlaydi.
    """
    # Simulyatsiya qilingan AI modeli:
    # masofa, mavjudlik, va yuk holatiga qarab tanlov

    scored_bases = []
    for base in bases:
        if product_id not in base["products"]:
            continue

        distance_score = 100 - base["distance_km"]  # yaqinlik
        load_score = 100 - base.get("current_load", 0)  # yuklama
        total_score = distance_score * 0.6 + load_score * 0.4

        scored_bases.append((base["id"], total_score))

    if not scored_bases:
        return None

    # Eng yuqori ball olgan bazani tanlash
    scored_bases.sort(key=lambda x: x[1], reverse=True)
    return scored_bases[0][0]  # faqat baza ID ni qaytaradi


def get_available_bases():
    """
    Bazalarning holatini olish (hozircha statik)
    """
    return [
        {
            "id": "BASE_TASHKENT_01",
            "distance_km": 2.5,
            "products": ["prod789", "prod123"],
            "current_load": 30
        },
        {
            "id": "BASE_SAMARKAND_02",
            "distance_km": 10.0,
            "products": ["prod789"],
            "current_load": 60
        }
    ]