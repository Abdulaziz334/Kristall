class UIManager:
    def __init__(self):
        self.elements = []

    def add_button(self, name):
        self.elements.append(f"Button: {name}")
        print(f"Tugma qo‘shildi: {name}")