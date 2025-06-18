def show_products():
    print("🛒 Mahsulotlar ro‘yxati:")
    products = [
        {"id": "prod001", "name": "Grafik karta RTX", "price": 120000},
        {"id": "prod002", "name": "AI modul chipi", "price": 95000}
    ]
    for i, product in enumerate(products, start=1):
        print(f"{i}. {product['name']} - {product['price']} so‘m")

    tanlov = input("Buyurtma beriladigan mahsulot raqamini kiriting: ")
    if tanlov.isdigit() and 0 < int(tanlov) <= len(products):
        product = products[int(tanlov)-1]
        from order_module import create_order
        order = create_order("user123", product['id'], "Toshkent, Olmazor")
        print("✅ Buyurtma yaratildi:", order["order_id"])
    else:
        print("❌ Noto‘g‘ri tanlov.")

    input("Bosh menyuga qaytish uchun Enter bosing...")
    from .home_screen import show_home_screen
    show_home_screen()