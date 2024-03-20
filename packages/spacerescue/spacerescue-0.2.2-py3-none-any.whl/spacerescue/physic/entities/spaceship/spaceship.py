import pyray as pr
import numpy as np

from spacerescue.constants import AU, SCREEN_HEIGHT, SCREEN_WIDTH
from spacerescue.physic.entities.galaxy.galaxy import ALL_STAR_SYSTEM_OBJECTS
from spacerescue.render import resource_manager
from spacerescue.physic.universe import Universe
from spacerescue.physic.entity import Entity
from spacerescue.render.camera import Camera
from spacerescue.render.cameras.camera_entity import CameraEntity
from spacerescue.tools.math import lerp, ndarray_to_vector3, normalize


class Spaceship(Entity):

    RESOURCE_MANAGER = resource_manager.get_instance()

    PULSE_SPEED = 1e5
    PULSE_FORCE = 1e5
    ARRIVED_RADIUS = 0.001 * AU
    SLOW_RADIUS = 0.5 * AU
    HEADING_SPEED = 2e-6

    def __init__(self, universe: Universe, position: np.ndarray, heading: np.ndarray):
        super().__init__(
            universe=universe,
            mass=1.0,
            radius=144,
            position=position,
            velocity=np.zeros(3),
        )
        self.model = Spaceship.RESOURCE_MANAGER.load_model("ncc-1701")
        self.model.materials[0].shader = Spaceship.RESOURCE_MANAGER.load_shader(
            "shader_lighting"
        )
        self.heading = heading
        self.target = None
        
    def is_arrived(self) -> bool:
        assert self.target is not None
        dist = float(np.linalg.norm(self.position - self.target.position))
        return dist < self.target_dist + Spaceship.ARRIVED_RADIUS

    def arrive(self, target: Entity | None, dist: float = 0.0):
        self.target = target
        self.target_dist = dist

    def update(self, dt: float):
        self.parent = self.universe.find_closest_stellar_object(
            self.position, ALL_STAR_SYSTEM_OBJECTS
        )
        if self.parent is not None:
            force = self.universe.laws.attraction(self.parent, self)
            self.add_force(force)
            self.parent.add_force(-force)

        if self.target is not None:
            self.add_force(
                self.universe.laws.arrive(
                    self,
                    self.target,
                    Spaceship.PULSE_SPEED,
                    Spaceship.PULSE_FORCE,
                    Spaceship.SLOW_RADIUS,
                    self.target_dist,
                )
            )

        super().update(dt)

        if self.target is not None:
            desired_heading = normalize(self.target.position - self.position)
            self.heading = lerp(self.heading, desired_heading, Spaceship.HEADING_SPEED * dt)

    def draw(self, camera: Camera):
        self.model.transform = pr.matrix_invert(
            pr.matrix_look_at(
                pr.vector3_zero(),
                ndarray_to_vector3(self.heading),
                ndarray_to_vector3(self.spin_axis),
            )
        )
        pr.draw_model(self.model, self.to_grid_position(), self.to_grid_size(camera.position), pr.WHITE)  # type: ignore
        
    def collect_photons(
        self, direction: np.ndarray | None = None
    ) -> pr.RenderTexture:
        direction = direction if direction is not None else self.heading
        camera = CameraEntity(self)
        surface = pr.load_render_texture(SCREEN_WIDTH // 4, SCREEN_HEIGHT // 4)
        pr.begin_texture_mode(surface)
        pr.clear_background(pr.BLACK)  # type: ignore
        pr.begin_mode_3d(camera.camera)
        self.universe.draw(camera)
        pr.end_mode_3d()
        pr.end_texture_mode()
        return surface
