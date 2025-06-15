# physics_core.py

class PhysicsEngine:
    def __init__(self, gravity=9.81):
        self.gravity = gravity

    def apply_gravity(self, mass, time):
        return mass * self.gravity * time

    def calculate_velocity(self, acceleration, time):
        return acceleration * time

    def calculate_force(self, mass, acceleration):
        return mass * acceleration