from __future__ import annotations

from spacerescue.gameplay.scenes.simulator_console import SimulatorConsole
from spacerescue.gameplay.scenes.travel_to_home import TravelToHome
from spacerescue.resources import HELP
from spacerescue.gameplay.challenges.challenge4 import Challenge4
from spacerescue.gameplay.challenge import Challenge, ChallengeError, ChallengeTransition
from spacerescue.gameplay.scenes.computer_console import ComputerConsole

class Challenge3(Challenge):
    
    TITLE = "Challenge 3 - Plot a course to home"
    
    MISSION = f"""# {TITLE}

You control a drone that must find his way through walls ...

Write a class Drone that will have the intelligence to drive it through the obstacles.

You are almost home, good luck!
    """

    def __init__(self, root_scene):
        super().__init__(Challenge3.TITLE, ComputerConsole(root_scene, HELP, Challenge3.MISSION))
        self.root_scene = root_scene
        
    def check_answer(self, answer):
        if answer is None or answer.get_drones is None or answer.fit is None:
            raise ChallengeError("Answer do not match the specification of a Drone.")
        return answer
        
    def leave_state(self) -> Challenge:
        super().leave_state()
        return ChallengeTransition(ChallengeTransition(Challenge4(self.root_scene), TravelToHome(self.root_scene)), SimulatorConsole(self.root_scene))
