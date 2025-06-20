
# API So‘rovlar Namunalari

## Mahsulotga buyurtma berish

#POST /api/order/create?product_id=1&to_base_id=2&user_id=999

...
# 🔌 API So‘rovlar Namunalari

#Bu yerda KristallEngine tizimining asosiy API so‘rovlari namunalari keltirilgan.

#---

## 🛒 Mahsulot buyurtma qilish

#**So‘rov turi:** `POST`

#**URL:**
#**Izoh:**
#- `product_id`: Mahsulot ID
#- `to_base_id`: Qabul qiluvchi baza ID
#- `user_id`: Buyurtmachi foydalanuvchi ID

#**Javob namunasi:**
#```json
#{ "status": "success",  "order_id": 1024,  "message": "Buyurtma bazaga yuborildi"}