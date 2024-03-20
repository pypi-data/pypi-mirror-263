import pyray as pr
import numpy as np

from spacerescue.render import resource_manager
from spacerescue.render.camera import Camera
from spacerescue.physic.universe import Universe
from spacerescue.physic.entity import Entity


class Star(Entity):

    RESOURCE_MANAGER = resource_manager.get_instance()
    
    ANGULAR_VELOCITY = 2e-7 # r⋅s−1   # sun like
    MASS = 1.99e30 # kg               # sun like
    RADIUS = 6.96e8 # m               # sun like
    BLOOM_RATIO = 1e7
    
    def __init__(
        self,
        universe: Universe,
        spin_axis: np.ndarray,
        position: np.ndarray,
        color: pr.Color,
    ):
        super().__init__(
            universe=universe,
            mass=Star.MASS,
            radius=Star.RADIUS,
            position=position,
            spin_axis=spin_axis
        )
        self.color = color
        self.angle = np.random.random() * np.pi
        self.angular_velocity = Star.ANGULAR_VELOCITY
        self.model = Star.RESOURCE_MANAGER.load_model("sun")

    def update(self, dt):
        self.angle += self.angular_velocity * dt
        super().update(dt)

    def draw(self, camera: Camera):
        if self.get_lod(camera.position) > 0:
            self.model.transform = pr.matrix_rotate(pr.Vector3(*self.spin_axis), self.angle)
            pr.draw_model(self.model, self.to_grid_position(), self.to_grid_size(camera.position), pr.WHITE)  # type: ignore
        else:
            self.model.transform = pr.matrix_identity()
            pr.draw_sphere(self.to_grid_position(), self.to_grid_size(camera.position), pr.WHITE)  # type: ignore

    def to_grid_size(self, eye: np.ndarray) -> float:
        if self.get_lod(eye) > 0:
            return super().to_grid_size(eye)
        else:
            return super().to_grid_size(eye) * Star.BLOOM_RATIO