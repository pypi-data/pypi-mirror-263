from multiprocessing import Process, Queue

import subprocess
import time

from spacerescue.gameplay.challenge import Challenge
from spacerescue.tools.util import load_module, reload_module


class Code:

    def __init__(self):
        self.brain_module = load_module("src/brain.py", "brain")
        self.queue = Queue()

    def validate_code(self) -> Process:
        p = Process(target=_validate_code_proc, args=(self.queue,))
        p.start()
        return p

    def get_validate_code_status(self) -> subprocess.CompletedProcess:
        return self.queue.get()

    def execute_code(self, challenge: Challenge) -> bool:
        try:
            return challenge.check_answer(
                reload_module(self.brain_module).think(challenge.id)
            )
        except:
            return False


def _validate_code_proc(queue: Queue):
    result = subprocess.run(["coverage", "run", "--module", "pytest"])
    if result.returncode != 0:
        queue.put(result)
        time.sleep(1)
        return

    result = subprocess.run(["coverage", "report", "--show-missing", "--skip-covered", "--fail-under=80"])
    if result.returncode != 0:
        queue.put(result)
        time.sleep(1)
        return
    
    queue.put(result)
    time.sleep(1)