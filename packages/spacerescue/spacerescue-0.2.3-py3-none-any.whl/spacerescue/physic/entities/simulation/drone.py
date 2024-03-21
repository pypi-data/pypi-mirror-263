import numpy as np
import pyray as pr

from spacerescue.physic.entities.simulation.world import World
from spacerescue.physic.entity import Entity


class Drone(Entity):

    THRUST = 3000
    MASS = 10
    RADIUS = 10

    def __init__(self, world: World, position: np.ndarray):
        super().__init__(
            universe=world,
            mass=Drone.MASS,
            radius=Drone.RADIUS,
            position=position,
            velocity=np.zeros(3),
        )

    def predict(self):
        pass
    
    def thrust(self):
        self.add_force(np.array([0, Drone.THRUST, 0]))

    def update(self, dt: float):
        self.predict()
        self.add_force(self.universe.laws.gravity(self))
        super().update(dt)
        self.universe.mapper.enforce_boundary(self)

    def draw(self):
        eye = np.zeros(3)
        pos = self.to_grid_position()
        pr.draw_circle(int(pos.x), int(pos.y), self.to_grid_size(eye), pr.WHITE)  # type: ignore
