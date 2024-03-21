from __future__ import annotations

from spacerescue.resources import HELP
from spacerescue.gameplay.challenges.challenge3 import Challenge3
from spacerescue.gameplay.challenge import Challenge, ChallengeError, ChallengeTransition
from spacerescue.gameplay.scenes.computer_console import ComputerConsole
from spacerescue.gameplay.scenes.travel_to_hyperspace import TravelToHyperspace

class Challenge2(Challenge):
    
    TITLE = "Challenge 2 - Find the way home"

    MISSION = f"""# {TITLE}

Using the different databases, find the fatest and safe way home. We remind you that the hyperspace tunnels are a
graph. You have the starting portal in the challenge_context["start_portal"] and the end portal in the  challenge_context["rescue_portal"].
    
Write a code that will return the list of space coordinates of each portal. A space coordinate is a numpy array of shape 3.

Be creative and fast, but be safe. Your crew depends on it.
    """

    def __init__(self, root_scene):
        super().__init__(Challenge2.TITLE, ComputerConsole(root_scene, HELP, Challenge2.MISSION))
        self.root_scene = root_scene
        
    def check_answer(self, answer):
        if answer is None:
            raise ChallengeError("Answer do not match a list of space coordinate (x, y, z)")
        return answer
        
    def leave_state(self) -> Challenge:
        super().leave_state()
        return ChallengeTransition(Challenge3(self.root_scene), TravelToHyperspace(self.root_scene))
