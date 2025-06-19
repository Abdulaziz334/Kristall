from ai_feedback import submit_feedback, get_base_rating

# Foydalanuvchidan baho olish
feedback = submit_feedback("user123", "BASE_TASHKENT_01", 5, "Juda tez va sifatli yetkazildi!")
print(feedback)

# Bazaning o‘rtacha reytingi
rating = get_base_rating("BASE_TASHKENT_01")
print("Bazaning o‘rtacha reytingi:", rating)