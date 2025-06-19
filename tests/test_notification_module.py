from notification_module import create_notification, get_user_notifications

notif = create_notification(
    user_id="user123",
    title="Buyurtma tasdiqlandi",
    message="Sizning buyurtmangiz qabul qilindi va tayyorlanmoqda."
)
print("Yangi xabar:", notif)

xabarlar = get_user_notifications("user123")
print("Foydalanuvchining xabarlari:", xabarlar)