import pyray as pr
import numpy as np

from spacerescue.tools.math import ndarray_to_vector3, normalize
from spacerescue.render import resource_manager
from spacerescue.render.camera import Camera
from spacerescue.physic.universe import Universe
from spacerescue.physic.entity import Entity
from spacerescue.physic.entities.galaxy.star import Star


class HyperspacePortal(Entity):

    RESOURCE_MANAGER = resource_manager.get_instance()
    
    VELOCITY = 1e-6 # r⋅s−1
    PORTALS_MASS = 0.0001 # kg
    RADIUS = 9e6 # m
    
    def __init__(
        self,
        universe: Universe,
        position: np.ndarray,
        star: Star,
    ):
        super().__init__(
            universe=universe,
            mass=HyperspacePortal.PORTALS_MASS,
            radius=HyperspacePortal.RADIUS,
            position=position,
            spin_axis=star.spin_axis,
            parent=star,
        )
        self.angle = np.random.random() * np.pi
        self.angular_velocity = HyperspacePortal.VELOCITY
        self.heading = normalize(self.parent.position - self.position) if self.parent is not None else np.zeros(3)
        self.model = HyperspacePortal.RESOURCE_MANAGER.load_model("wormhole")

    def update(self, dt):
        self.angle += self.angular_velocity * dt
        super().update(dt)

    def draw(self, camera: Camera):
        if self.get_lod(camera.position) > 0:
            self.model.transform = pr.matrix_multiply(
                pr.matrix_rotate_z(self.angle),
                pr.matrix_invert(
                    pr.matrix_look_at(
                        pr.vector3_zero(),
                        ndarray_to_vector3(self.heading),
                        ndarray_to_vector3(self.spin_axis),
                    )
                ),
            )
            pr.draw_model(self.model, self.to_grid_position(), self.to_grid_size(camera.position), pr.WHITE)  # type: ignore
