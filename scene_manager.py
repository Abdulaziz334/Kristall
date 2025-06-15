# scene_manager.py

class Scene:
    def __init__(self, name):
        self.name = name
        self.objects = []

    def add_object(self, obj):
        self.objects.append(obj)

    def remove_object(self, obj):
        self.objects.remove(obj)

class SceneManager:
    def __init__(self):
        self.scenes = {}
        self.current_scene = None

    def create_scene(self, name):
        scene = Scene(name)
        self.scenes[name] = scene
        return scene

    def switch_scene(self, name):
        if name in self.scenes:
            self.current_scene = self.scenes[name]
        return self.current_scene
class Scene:
    def __init__(self, name):
        self.name = name
        self.objects = []

    def add_object(self, obj):
        self.objects.append(obj)

class SceneManager:
    def __init__(self):
        self.current_scene = None

    def create_scene(self, name):
        self.current_scene = Scene(name)
        return self.current_scene