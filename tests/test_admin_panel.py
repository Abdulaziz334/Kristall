from admin_panel import list_users, list_orders, list_bases, add_base, update_base_stock

print("🧍‍♂️ Foydalanuvchilar:", list_users())
print("📦 Buyurtmalar:", list_orders())
print("📍 Bazalar:", list_bases())

# Yangi baza qo‘shish
new_base = add_base("BASE_SAMARQAND_01", "Samarqand, Registon", stock=["prod123", "prod456"])
print("➕ Qo‘shilgan baza:", new_base)

# Bazaga yangi mahsulotlar qo‘shish
update_base_stock("BASE_SAMARQAND_01", ["prod123", "prod789", "prod999"])