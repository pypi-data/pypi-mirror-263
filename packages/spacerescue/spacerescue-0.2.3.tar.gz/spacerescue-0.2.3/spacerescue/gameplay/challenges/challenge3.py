from __future__ import annotations

from spacerescue.gameplay.scenes.simulator import Simulator
from spacerescue.resources import HELP
from spacerescue.gameplay.challenges.challenge4 import Challenge4
from spacerescue.gameplay.challenge import Challenge, ChallengeTransition
from spacerescue.gameplay.scenes.computer_console import ComputerConsole

MISSION = """# Find your way out

You control a drone that must find his way through walls ...
"""


class Challenge3(Challenge):

    def __init__(self, root_scene):
        super().__init__("Avoid asteroid", ComputerConsole(root_scene, HELP, MISSION))
        self.root_scene = root_scene
        
    def check_answer(self, answer) -> bool:
        return super().check_answer(answer is not None and answer.get_drones is not None and answer.fit is not None)
        
    def leave_state(self) -> Challenge:
        super().leave_state()
        return ChallengeTransition(Challenge4(self.root_scene), Simulator(self.root_scene))
