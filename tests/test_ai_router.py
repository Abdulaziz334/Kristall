from ai_router import choose_best_base, get_available_bases

user_location = "Toshkent"
product_id = "prod789"

bases = get_available_bases()
selected_base_id = choose_best_base(user_location, product_id, bases)

print("Tanlangan baza ID:", selected_base_id)