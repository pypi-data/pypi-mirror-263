import pyray as pr
import numpy as np

from spacerescue.constants import SCREEN_HEIGHT, SCREEN_WIDTH
from spacerescue.gameplay.root_scene import RootScene
from spacerescue.render.animators.open_vertical import OpenVertical
from spacerescue.render.widgets.console import Console
from spacerescue.render.animators.fade_inout import FadeInOut
from spacerescue.render.animators.fade_scr import FadeScr
from spacerescue.tools.util import is_skip_key


class GameOver(RootScene):

    def __init__(self):
        super().__init__()

    def enter_scene(self):
        super().enter_scene()
        self.menu = GameOver.RESOURCE_MANAGER.load_texture("menu")
        self.fade_in = FadeScr(0.5)
        self.fade_out = FadeInOut(255, 0, 1.0, pr.Color(*pr.BLACK))
        self.state = 0
        self._build_ui()
       
    def update(self):
        match self.state:
            case 0:
                if self.fade_in.is_playing():
                    self.fade_in.update()
                else:
                    self.state = 1

            case 1:
                if (
                    self.avatar_animator.is_playing()
                    or self.avatar_animator.is_playing()
                ):
                    self.avatar_animator.update()
                    self.console_animator.update()
                else:
                    self.state = 2

            case 2:
                if not is_skip_key():
                    self.avatar_animator.update()
                    self.console_animator.update()
                else:
                    self.state = 3

            case 3:
                if self.fade_out.is_playing():
                    self.fade_out.update()
                else:
                    self.leave_scene() # leave scene so that the challenge manager can leave the underlying game
                    self.state = 4

    def draw(self):
        pr.begin_drawing()

        pos_x = int((SCREEN_WIDTH - self.menu.width) / 2)
        pos_y = int((SCREEN_HEIGHT - self.menu.height) / 2)
        pr.draw_texture(self.menu, pos_x, pos_y, pr.WHITE)  # type: ignore

        if self.state in (1, 2):
            self.avatar_animator.draw()
            self.console_animator.draw()

        if self.state in (0, 3):
            self.fade_in.draw()
            self.fade_out.draw()

        pr.end_drawing()
        
    def _build_ui(self):
        self.avatar = Console(
            "widget",
            pr.Vector2(100, 100),
            pr.Vector2(276, 276),
            ["![avatar](resources/images/avatar.png)"],
        )
        self.avatar_animator = OpenVertical(self.avatar, 0.5, Console.BG_COLOR)

        self.console = Console(
            "widget",
            pr.Vector2(400, 100),
            pr.Vector2(SCREEN_WIDTH / 2, SCREEN_HEIGHT - 200),
            ["Congratulation!"],
        )
        self.console_animator = OpenVertical(self.console, 0.5, Console.BG_COLOR)
