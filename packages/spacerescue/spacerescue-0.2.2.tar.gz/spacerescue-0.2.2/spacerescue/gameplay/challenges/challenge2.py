from __future__ import annotations

from spacerescue.resources import HELP
from spacerescue.gameplay.challenges.challenge3 import Challenge3
from spacerescue.gameplay.challenge import Challenge, ChallengeTransition
from spacerescue.gameplay.scenes.computer_console import ComputerConsole
from spacerescue.gameplay.scenes.travel_to_hyperspace import TravelToHyperspace

MISSION = """# Nearest Exit from Entrance in Maze (Graph)

You are given an m x n matrix maze (0-indexed) with empty cells (represented as '.') and walls (represented as '+'). You
are also given the entrance of the maze, where entrance = [entrancerow, entrancecol] denotes the row and column of the
cell you are initially standing at.

In one step, you can move one cell up, down, left, or right. You cannot step into a cell with a wall, and you cannot
step outside the maze. Your goal is to find the nearest exit from the entrance. An exit is defined as an empty cell that
is at the border of the maze. The entrance does not count as an exit.

Return the number of steps in the shortest path from the entrance to the nearest exit, or -1 if no such path exists.

## Example:

![toto](resources/images/challenge1.png)

Input: maze = [["+","+",".","+"],[".",".",".","+"],["+","+","+","."]], entrance = [1,2]

Output: 1

## Explanation: There are 3 exits in this maze at [1,0], [0,2], and [2,3].

Initially, you are at the entrance cell [1,2].

* You can reach [1,0] by moving 2 steps left.
* You can reach [0,2] by moving 1 step up.

It is impossible to reach [2,3] from the entrance.

Thus, the nearest exit is [0,2], which is 1 step away.
"""


class Challenge2(Challenge):

    def __init__(self, root_scene):
        super().__init__("Find the path", ComputerConsole(root_scene, HELP, MISSION))
        self.root_scene = root_scene
        
    def check_answer(self, answer) -> bool:
        return super().check_answer(answer == (1000, 1000, 1000))
        
    def leave_state(self) -> Challenge:
        super().leave_state()
        return ChallengeTransition(Challenge3(self.root_scene), TravelToHyperspace(self.root_scene))
