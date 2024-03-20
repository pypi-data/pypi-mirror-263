from __future__ import annotations

from spacerescue.gameplay.scenes.travel_in_space import TravelInSpace
from spacerescue.resources import HELP
from spacerescue.gameplay.challenges.challenge4 import Challenge4
from spacerescue.gameplay.challenge import Challenge, ChallengeTransition
from spacerescue.gameplay.scenes.computer_console import ComputerConsole

MISSION = """# Asteroid Collision (Recursivity) 

We are given an array asteroid of integers representing asteroids in a row. 

For each asteroid, the absolute value represents its size, and the sign represents its direction (positive meaning right,
negative meaning left). Each asteroid moves at the same speed. 

Find out the state of the asteroids after all collisions. If two asteroids meet, the smaller one will explode. If both
are the same size, both will explode. Two asteroids moving in the same direction will never meet. 

## Example: 

Input: asteroids = [5, 10, -5] 

Output: [5, 10] 

## Explanation: The 10 and -5 collide resulting in 10. The 5 and 10 never collide. 
"""


class Challenge3(Challenge):

    def __init__(self, root_scene):
        super().__init__("Avoid asteroid", ComputerConsole(root_scene, HELP, MISSION))
        self.root_scene = root_scene
        
    def check_answer(self, answer) -> bool:
        return super().check_answer(answer == (1000, 1000, 1000))
        
    def leave_state(self) -> Challenge:
        super().leave_state()
        return ChallengeTransition(Challenge4(self.root_scene), TravelInSpace(self.root_scene))
