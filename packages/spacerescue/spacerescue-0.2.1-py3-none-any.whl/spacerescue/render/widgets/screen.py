import pyray as pr

from spacerescue.constants import SCREEN_HEIGHT, SCREEN_WIDTH
from spacerescue.render import resource_manager
from spacerescue.render.widget import Widget


class Screen(Widget):

    RESOURCE_MANAGER = resource_manager.get_instance("scene")

    def __init__(self, id: str, texture_name: str):
        super().__init__(
            id,
            pr.Rectangle(
                0,
                0,
                SCREEN_WIDTH,
                SCREEN_HEIGHT,
            ),
        )
        self.surface = Screen.RESOURCE_MANAGER.load_texture(texture_name)

    def draw(self):
        pr.draw_texture_pro(
            self.surface,
            pr.Rectangle(
                0,
                0,
                self.surface.width,
                self.surface.height,
            ),
            self.bound,
            pr.vector2_zero(),
            0.0,
            pr.WHITE,  # type: ignore
        )
