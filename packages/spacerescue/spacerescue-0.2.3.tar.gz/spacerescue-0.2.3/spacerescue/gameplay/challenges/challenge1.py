from __future__ import annotations

import numpy as np

from spacerescue.gameplay.challenges.challenge2 import Challenge2
from spacerescue.gameplay.challenge import (
    Challenge,
    ChallengeError,
    ChallengeTransition,
)
from spacerescue.gameplay.scenes.computer_console import ComputerConsole
from spacerescue.gameplay.scenes.travel_to_portal import TravelToPortal
from spacerescue.physic.entities.galaxy.galaxy import (
    ALL_STAR_SYSTEM_HABITABLE_PLANETS,
    ALL_STAR_SYSTEM_PORTALS,
)
from spacerescue.physic.entities.galaxy.hyperspace_portal import HyperspacePortal
from spacerescue.physic.entities.galaxy.planet import Planet
from spacerescue.physic.entities.galaxy.star import Star
from spacerescue.resources import HELP


class Challenge1(Challenge):

    TITLE = "Challenge 1 - Find the memo"

    MISSION = f"""# {TITLE}

    Find the coordinates of the planet to rescue the crew. The Earth Command sent you a message with the name of the
    planet.

    Be creative and fast, the life support won't last forever!.
    """

    def __init__(self, root_scene):
        super().__init__(
            Challenge1.TITLE, ComputerConsole(root_scene, HELP, Challenge1.MISSION)
        )
        self.root_scene = root_scene

    def check_answer(self, some_position):
        if (
            some_position is None
            or not isinstance(some_position, np.ndarray)
            or not some_position.shape[0] == 3
        ):
            raise ChallengeError("Answer do not match a space coordinate (x, y, z)")

        planet = Challenge1.CONTEXT.galaxy.find_closest_stellar_object(
            some_position, ALL_STAR_SYSTEM_HABITABLE_PLANETS
        )
        if (
            planet is None
            or not isinstance(planet, Planet)
            or not Challenge1.CONTEXT.rescue_planet.name == planet.name
        ):
            raise ChallengeError("Answer do not match an valid planet for the mission")

        star = planet.parent
        if (
            star is None
            or not isinstance(star, Star)
            or not Challenge1.CONTEXT.rescue_planet.parent.name == star.name
        ):
            raise ChallengeError(
                "Answer do not match a valid star system for the mission"
            )

        portal = next(
            Challenge1.CONTEXT.galaxy.filter_stellar_objects(
                ALL_STAR_SYSTEM_PORTALS(star)
            ),
            None,
        )
        if portal is None or not isinstance(portal, HyperspacePortal):
            raise ChallengeError("Answer do not match a valid portal for the mission")

        self.context["rescue_portal"] = portal
        return some_position

    def leave_state(self) -> Challenge:
        super().leave_state()
        return ChallengeTransition(
            Challenge2(self.root_scene), TravelToPortal(self.root_scene)
        )
