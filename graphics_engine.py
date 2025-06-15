class GraphicsEngine:
    def __init__(self):
        self.objects = []

    def render(self):
        for obj in self.objects:
            print(f"Chizilmoqda: {obj}")

    def add_object(self, obj):
        self.objects.append(obj)