from __future__ import annotations

from spacerescue.gameplay.challenges.challenge2 import Challenge2
from spacerescue.gameplay.challenge import Challenge, ChallengeTransition
from spacerescue.gameplay.scenes.computer_console import ComputerConsole
from spacerescue.gameplay.scenes.travel_to_portal import TravelToPortal
from spacerescue.resources import HELP


MISSION = """# Challenge 1 - 

Find the coordinates of the planet to rescue the crew. The Earth Command sent you a message with the name of the planet.

Be creative and fast, the life support won't last forever and so your crew members.
"""


class Challenge1(Challenge):

    def __init__(self, root_scene):
        super().__init__("Find the memo", ComputerConsole(root_scene, HELP, MISSION))
        self.root_scene = root_scene

    def check_answer(self, answer) -> bool:
        return super().check_answer(answer == (1000, 1000, 1000))

    def leave_state(self) -> Challenge:
        super().leave_state()
        return ChallengeTransition(Challenge2(self.root_scene), TravelToPortal(self.root_scene))
