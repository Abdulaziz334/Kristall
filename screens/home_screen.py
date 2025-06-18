def show_home_screen():
    print("📦 KristallEngine: Bosh menyu")
    print("1. Mahsulotlar")
    print("2. Buyurtmalarim")
    print("3. To‘lov")
    print("0. Chiqish")

    tanlov = input("Tanlovni kiriting: ")

    if tanlov == "1":
        from .product_screen import show_products
        show_products()
    elif tanlov == "2":
        from .order_status_screen import show_order_status
        show_order_status()
    elif tanlov == "3":
        from .payment_screen import show_payment
        show_payment()
    else:
        print("Dastur yakunlandi.")