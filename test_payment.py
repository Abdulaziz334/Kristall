from payment_module import process_payment

result = process_payment(
    order_id="123e4567-e89b-12d3-a456-426614174000",
    amount=120000,
    method="QR-PAYME",
    payer_id="user123"
)
print(result)