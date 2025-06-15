# game_engine.py

class GameEngine:
    def __init__(self):
        self.running = False

    def start_game(self):
        self.running = True
        print("\n🚀 O'yin yuklanmoqda...")
        print("🧩 Sahna: 'Kristall Dala'")
        print("👤 Qahramon: Default AI")
        print("🎮 Boshqaruv: W/A/S/D bilan harakat, 'Q' chiqish")

        while self.running:
            command = input("➡️ Harakatni tanlang (W/A/S/D yoki Q): ").lower()
            if command in ["w", "a", "s", "d"]:
                print(f"🕹 Harakat: {command.upper()} yo'nalish")
            elif command == "q":
                print("📤 O'yindan chiqish...")
                self.running = False
            else:
                print("❗️ Noma'lum buyruq.")