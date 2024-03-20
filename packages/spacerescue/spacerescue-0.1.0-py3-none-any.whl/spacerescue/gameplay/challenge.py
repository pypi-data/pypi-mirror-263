from __future__ import annotations

import logging
import secrets

from spacerescue.gameplay.scene_manager import Scene


class Challenge:

    def __init__(self, description: str, scene: Scene):
        self.id = "47eb909a" # TODO: secrets.token_hex(nbytes=4)
        self.description = description
        self.scene = scene

    def enter_state(self):
        logging.info(f"INFO: CHALLENGE: [{self.description}] started with [{self.id}]")
        self.scene.enter_scene()

    def check_answer(self, answer) -> bool:
        logging.info(
            f"INFO: CHALLENGE: player answer [{answer}] to challenge [{self.id}]"
        )
        if answer:
            logging.info("INFO: CHALLENGE: player answered correctly")
            return True
        else:
            logging.warn("INFO: CHALLENGE: player answered wrongly")
            return False

    def leave_state(self) -> Challenge:
        self.scene.leave_scene()
        logging.info(f"INFO: CHALLENGE: [{self.description}] ended")
        return self


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
