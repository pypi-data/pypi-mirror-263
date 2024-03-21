from __future__ import annotations

from spacerescue.gameplay.challenge import (
    Challenge,
    ChallengeEnd,
)
from spacerescue.gameplay.scenes.game_over import GameOver
from spacerescue.gameplay.scenes.quizz_console import QuizzConsole


class Challenge4(Challenge):

    TITLE = "Challenge 4 - Quizz 0"

    QUESTION = f"""# {TITLE}
    
Before to enter in the planet control, Hearth command needs to check your identity by asking few questions.

What is your name ?
    """
    
    CHOICES = {
        "Romuald": False,
        "Benoit": False,
        "Yannick": False,
        "Akira": True
    }

    def __init__(self, root_scene):
        super().__init__(
            Challenge4.TITLE, QuizzConsole(root_scene, Challenge4.QUESTION, Challenge4.CHOICES)
        )
        self.root_scene = root_scene

    def leave_state(self) -> Challenge:
        super().leave_state()
        return ChallengeEnd(GameOver())
