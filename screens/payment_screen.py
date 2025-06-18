from payment_module import process_payment

def show_payment():
    print("💳 To‘lov oynasi")
    order_id = input("Buyurtma ID sini kiriting: ")
    amount = input("To‘lov summasi (so‘m): ")
    method = input("To‘lov turi (QR-PAYME, QR-CLICK, UZC): ")

    result = process_payment(
        order_id=order_id,
        amount=int(amount),
        method=method,
        payer_id="user123"
    )
    print("✅ Natija:", result)

    input("Bosh menyuga qaytish uchun Enter bosing...")
    from .home_screen import show_home_screen
    show_home_screen()