---

### 🧠 2. `KristallEngine/engine.py`
```python
import ai_core
import physics
import renderer

def start_engine():
    print("🔷 KristallEngine ishga tushdi...")
    ai_core.initialize()
    physics.load_physics()
    renderer.start_render_loop()

if __name__ == "__main__":
    start_engine()