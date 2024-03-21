from multiprocessing import Process

from spacerescue.gameplay.challenge import Challenge, ChallengeAnswer, ChallengeBadAnswer
from spacerescue.gameplay.scene_manager import DestroyableScene
from spacerescue.tools.dynamic_code import DynamicCode


class RootScene(DestroyableScene):

    def __init__(self):
        super().__init__()
        self.challenge: Challenge | None = None
        self.code = DynamicCode()

    def has_challenge(self) -> bool:
        return self.challenge is not None

    def get_challenge(self) -> Challenge | None:
        return self.challenge
    
    def begin_first_challenge(self):
        from spacerescue.gameplay.challenges.challenge1 import Challenge1
        return self.begin_challenge(Challenge1(self))

    def begin_challenge(self, challenge: Challenge) -> bool:
        if challenge != self.challenge:
            self.challenge = challenge
            self.challenge.enter_state()
            return True
        else:
            return False

    def validate_challenge(self) -> Process:
        return self.code.validate_code()

    def submit_challenge(self) -> ChallengeAnswer:
        if self.challenge is not None and self.code.get_validate_code_status().returncode == 0:
            return self.code.execute_code(self.challenge)
        else:
            return ChallengeBadAnswer(Exception("Test Coverage failed to meet the criteria"))
        
    def get_last_answer(self):
        return self.code.get_last_result()

    def next_challenge(self):
        if self.challenge is not None:
            self.begin_challenge(self.challenge.leave_state())

    def abandon_challenge(self):
        if self.challenge is not None:
            self.challenge.leave_state()
