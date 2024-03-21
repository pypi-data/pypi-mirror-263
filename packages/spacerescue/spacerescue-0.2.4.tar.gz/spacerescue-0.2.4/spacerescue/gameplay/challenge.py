from __future__ import annotations

import logging
import secrets

from spacerescue.gameplay.scene_manager import Scene
from spacerescue.gameplay import context_manager


class ChallengeError(ValueError):
    pass


class ChallengeAnswer:
    """Interface"""

    def map(self, func) -> ChallengeAnswer:
        raise Exception("Not implemented")

    def orElse(self, func):
        raise Exception("Not implemented")


class ChallengeGoodAnswer(ChallengeAnswer):

    def __init__(self, result = None):
        self.result = result

    def map(self, func) -> ChallengeAnswer:
        return ChallengeGoodAnswer(func(self.result))

    def orElse(self, func):
        return self.result


class ChallengeBadAnswer(ChallengeAnswer):

    def __init__(self, exception: Exception | None = None):
        self.exception = exception

    def map(self, func) -> ChallengeAnswer:
        return self

    def orElse(self, func):
        return func(self.exception)


class Challenge:

    CONTEXT = context_manager.get_instance()
    SECRET_IDS = {}

    def __init__(self, description: str, scene: Scene):
        self.id = self._generate_id()
        self.context = Challenge.CONTEXT.challenge_context
        self.description = description
        self.scene = scene

    def enter_state(self):
        logging.info(f"INFO: CHALLENGE: [{self.description}] started with [{self.id}]")
        self.scene.enter_scene()

    def leave_state(self) -> Challenge:
        self.scene.leave_scene()
        logging.info(f"INFO: CHALLENGE: [{self.description}] ended")
        return self

    def check_answer(self, answer):
        raise Exception("Not implemented")
    
    def _generate_id(self):
        class_name = type(self).__name__
        if not class_name in Challenge.SECRET_IDS.keys():
            Challenge.SECRET_IDS[class_name] = secrets.token_hex(nbytes=4)
        return Challenge.SECRET_IDS[class_name]


class ChallengeTransition(Challenge):

    def __init__(self, next_challenge: Challenge, scene: Scene):
        super().__init__("To be continued", scene)
        self.next_challenge = next_challenge

    def leave_state(self) -> Challenge:
        super().leave_state()
        return self.next_challenge


class ChallengeEnd(Challenge):

    def __init__(self, scene: Scene):
        super().__init__("The End", scene)

    def leave_state(self) -> Challenge:
        super().leave_state()
        return self
