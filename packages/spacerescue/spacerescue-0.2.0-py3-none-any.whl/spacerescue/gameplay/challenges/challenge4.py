from __future__ import annotations

from spacerescue.gameplay.scenes.travel_in_space import TravelInSpace
from spacerescue.resources import HELP
from spacerescue.gameplay.challenge import Challenge, ChallengeEnd, ChallengeTransition
from spacerescue.gameplay.scenes.computer_console import ComputerConsole
from spacerescue.gameplay.scenes.game_over import GameOver

MISSION = """# Challenge 4
"""


class Challenge4(Challenge):

    def __init__(self, root_scene):
        super().__init__("Find the path", ComputerConsole(root_scene, HELP, MISSION))
        self.root_scene = root_scene
        
    def check_answer(self, answer) -> bool:
        return super().check_answer(answer == (1000, 1000, 1000))
        
    def leave_state(self) -> Challenge:
        super().leave_state()
        return ChallengeTransition(ChallengeEnd(GameOver()), TravelInSpace(self.root_scene))
