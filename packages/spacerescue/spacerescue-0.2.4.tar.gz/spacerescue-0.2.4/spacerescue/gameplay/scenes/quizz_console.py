import numpy as np
import pyray as pr

from spacerescue.constants import SCREEN_HEIGHT, SCREEN_WIDTH
from spacerescue.gameplay.challenge import ChallengeAnswer, ChallengeBadAnswer, ChallengeGoodAnswer
from spacerescue.gameplay.scenes.game import Game
from spacerescue.gameplay.scene_manager import DestroyableScene
from spacerescue.render.animators.fade_scr import FadeScr
from spacerescue.render.animators.open_horizontal import OpenHorizontal
from spacerescue.render.widgets.button import Button
from spacerescue.render.widgets.message_box import MessageBox
from spacerescue.render.widgets.quizz import Quizz
from spacerescue.render.widgets.screen import Screen


class QuizzConsole(DestroyableScene):

    BORDER_SIZE = 55

    def __init__(self, root_scene: Game, question: str, choices: dict[str, bool]):
        super().__init__()
        self.root_scene = root_scene
        self.question = question
        self.choices = choices

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
        self.fade_in = FadeScr(0.5)
        self.message_box = None
        self.console = Quizz(
            "console",
            pr.Vector2(205, 135),
            pr.Vector2(SCREEN_WIDTH - 405, SCREEN_HEIGHT - 250),
            self.question,
            self.choices,
            55,
        )
        self.screen = Screen("widget", "computer_console")
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
        ]

    def _button_is_clicked(self, button: Button):
        if button.id == "button_submit":
            self._submit_answer()
        elif button.id == "button_abandon":
            self.root_scene.abandon_challenge()

    def _message_box_is_closed(self, message_box: MessageBox):
        self.message_box = None
        match message_box.id:
            case "mb_progress":
                self._submit_code()

            case "mb_sucess":
                self.root_scene.next_challenge()
    
    def _submit_answer(self):
        mb = (
            self._submit_challenge()
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
                    pr.Vector2(500, 300),
                    f"Your answer is incorrect!\n\nYour crew really needs you.\nPlease try again and good luck.",
                    self._message_box_is_closed,
                )
            )
        )
        self.message_box = OpenHorizontal(mb, 0.3, MessageBox.BG_COLOR)
    
             
    def _submit_challenge(self) -> ChallengeAnswer:
        result = True
        for i, choice in enumerate(self.choices.keys()):
            checkbox = self.console.checkboxes[i]
            result = result and checkbox.clicked == self.choices[choice]
        return ChallengeGoodAnswer() if result else ChallengeBadAnswer()