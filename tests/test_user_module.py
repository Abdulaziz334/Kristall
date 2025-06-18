from user_module import register_user, get_user_by_phone

# Ro‘yxatdan o‘tkazish
user = register_user("Ali", "+998901234567")
print("Yangi foydalanuvchi:", user)

# Foydalanuvchini telefon orqali qidirish
found_user = get_user_by_phone("+998901234567")
print("Topilgan foydalanuvchi:", found_user)