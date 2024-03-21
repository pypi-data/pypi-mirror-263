import pyray as pr
import pyperclip as pc

from spacerescue.constants import SCREEN_HEIGHT, SCREEN_WIDTH
from spacerescue.render import resource_manager
from spacerescue.gameplay.scenes.game import Game
from spacerescue.gameplay.scene_manager import DestroyableScene
from spacerescue.render.animators.open_horizontal import OpenHorizontal
from spacerescue.render.widgets.console import Console
from spacerescue.render.widgets.button import Button
from spacerescue.render.animators.fade_scr import FadeScr
from spacerescue.render.widgets.message_box import MessageBox
from spacerescue.render.widgets.progress_box import ProgressBox
from spacerescue.render.widgets.screen import Screen


class ComputerConsole(DestroyableScene):

    CAPTION = "     [F1: HELP] [F2: MISSION]             [ID: {}]"

    def __init__(self, root_scene: Game, help: str, mission: str):
        super().__init__()
        self.root_scene = root_scene
        self.buffers = [help, mission]

    def enter_scene(self):
        super().enter_scene()
        self._build_ui()
        self.state = 0

    def update(self):
        match self.state:
            case 0:
                if self.fade_in.is_playing():
                    self.fade_in.update()
                else:
                    self.state = 1

            case 1:
                if self.message_box is None:
                    self.console.update()
                    for button in self.buttons:
                        button.update()
                else:
                    self.state = 2

            case 2:
                if self.message_box is not None:
                    self.message_box.update()
                else:
                    self.state = 1

    def draw(self):
        pr.begin_drawing()
        pr.clear_background(pr.Color(64, 191, 182, 255))
        self.console.draw()
        self.screen.draw()
        for button in self.buttons:
            button.draw()
        if self.state == 2 and self.message_box is not None:
            self.message_box.draw()
        if self.state == 0:
            self.fade_in.draw()
        pr.end_drawing()

    def _build_ui(self):
        challenge = self.root_scene.get_challenge()
        assert challenge is not None

        self.fade_in = FadeScr(0.5)
        self.screen = Screen("widget", "computer_console")
        self.message_box = None
        self.console = Console(
            "widget",
            pr.Vector2(150, 80),
            pr.Vector2(SCREEN_WIDTH - 300, SCREEN_HEIGHT - 120),
            self.buffers,
            caption=ComputerConsole.CAPTION.format(challenge.id),
            first_buffer=1,
            border_size=55,
        )
        self.buttons = [
            Button(
                "button_submit",
                pr.Vector2(SCREEN_WIDTH - 220, SCREEN_HEIGHT - 94),
                pr.Vector2(200, 38),
                "SUBMIT",
                pr.Color(254, 201, 123, 192),
                self._button_is_clicked,
            ),
            Button(
                "button_abandon",
                pr.Vector2(SCREEN_WIDTH - 220, SCREEN_HEIGHT - 45),
                pr.Vector2(200, 38),
                "ABANDON",
                pr.Color(252, 127, 104, 192),
                self._button_is_clicked,
            ),
            Button(
                "button_music_onoff",
                pr.Vector2(20, SCREEN_HEIGHT - 94),
                pr.Vector2(200, 38),
                "MUSIC ON/OFF",
                pr.Color(64, 191, 182, 192),
                self._button_is_clicked,
            ),
            Button(
                "button_copy_id",
                pr.Vector2(20, SCREEN_HEIGHT - 45),
                pr.Vector2(200, 38),
                "COPY ID",
                pr.Color(64, 191, 182, 192),
                self._button_is_clicked,
            ),
        ]

    def _button_is_clicked(self, button: Button):
        match button.id:
            case "button_submit":
                mb = ProgressBox(
                    "mb_progress",
                    pr.Vector2(500, 300),
                    "Code under validation, wait a minute ...",
                    self.root_scene.validate_challenge(),
                    self._message_box_is_closed,
                )
                self.message_box = OpenHorizontal(mb, 0.3, MessageBox.BG_COLOR)

            case "button_abandon":
                self.root_scene.abandon_challenge()

            case "button_music_onoff":
                self._stop_music()

            case "button_copy_id":
                self._copy_challenge_id()

    def _message_box_is_closed(self, message_box: MessageBox):
        self.message_box = None
        match message_box.id:
            case "mb_progress":
                self._submit_code()

            case "mb_sucess":
                self.root_scene.next_challenge()

    def _submit_code(self):
        mb = (
            self.root_scene.submit_challenge()
            .map(
                lambda _: MessageBox(
                    "mb_sucess",
                    pr.Vector2(500, 300),
                    "Your answer is correct!\n\nYour crew needs you.\n\nReady for the next challenge?",
                    self._message_box_is_closed,
                )
            )
            .orElse(
                lambda x: MessageBox(
                    "mb_failure",
                    pr.Vector2(max(pr.measure_text(str(x), 20) + 40, 500), 300),
                    f"Your answer is incorrect!\n\n{x}\n\nYour crew really needs you.\nPlease try again and good luck.",
                    self._message_box_is_closed,
                )
            )
        )
        self.message_box = OpenHorizontal(mb, 0.3, MessageBox.BG_COLOR)

    def _stop_music(self):
        music = resource_manager.get_instance().load_music("music")
        if pr.is_music_stream_playing(music):
            pr.stop_music_stream(music)
        else:
            pr.play_music_stream(music)

    def _copy_challenge_id(self):
        challenge = self.root_scene.get_challenge()
        assert challenge is not None
        pc.copy(challenge.id)
