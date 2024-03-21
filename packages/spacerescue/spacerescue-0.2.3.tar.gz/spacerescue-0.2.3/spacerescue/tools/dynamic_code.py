from types import ModuleType
from multiprocessing import Process, Queue

import os
import time
import logging
import traceback
import subprocess
import importlib

from spacerescue.gameplay.challenge import (
    Challenge,
    ChallengeAnswer,
    ChallengeBadAnswer,
    ChallengeGoodAnswer,
)


class DynamicModule:

    def __init__(self, module: ModuleType, timestamp: float):
        self.module = module
        self.timestamp = timestamp


class DynamicCode:

    def __init__(self):
        self.dynamic_package = self._import_dynamic_package("brain")
        self.queue = Queue()
        self.last_result = None

    def validate_code(self) -> Process:
        p = Process(target=_validate_code_proc, args=(self.queue,))
        p.start()
        time.sleep(1)
        return p

    def get_validate_code_status(self) -> subprocess.CompletedProcess:
        return self.queue.get()

    def execute_code(self, challenge: Challenge) -> ChallengeAnswer:
        try:
            self.dynamic_package = self._reload_dynamic_package(
                "brain", self.dynamic_package
            )
            self.last_result = self.dynamic_package["brain.brain"].module.think(
                challenge.id, challenge.context
            )
            return ChallengeGoodAnswer(challenge.check_answer(self.last_result))
        except Exception as x:
            logging.error(traceback.format_exc())
            return ChallengeBadAnswer(x)

    def get_last_result(self):
        return self.last_result

    def _import_dynamic_package(self, package_name: str, dynamic_package: dict = {}):
        modules = [
            (os.path.join(package_name, file), file[:-3])
            for file in os.listdir(package_name)
            if self._is_valid_module_name(file)
        ]
        for file, module in modules:
            package = f"{package_name}.{module}"
            logging.debug(
                f"DEBUG: CODE: [{package}] Found a new module to load and monitor"
            )
            dynamic_package[package] = DynamicModule(
                importlib.import_module(package), os.path.getmtime(file)
            )
        return dynamic_package

    def _reload_dynamic_package(self, package_name: str, dynamic_package: dict):
        modules = [
            (os.path.join(package_name, file), file[:-3])
            for file in os.listdir(package_name)
            if self._is_valid_module_name(file)
        ]
        for file, module in modules:
            package = f"{package_name}.{module}"
            if package in dynamic_package.keys():
                timestamp = os.path.getmtime(file)
                if timestamp > dynamic_package[package].timestamp:
                    logging.debug(
                        f"DEBUG: CODE: [{package}] Found an existing module to reload"
                    )
                    importlib.reload(dynamic_package[package].module)
            else:
                logging.debug(
                    f"DEBUG: CODE: [{package}] Found a new module to load and monitor"
                )
                dynamic_package[package] = DynamicModule(
                    importlib.import_module(package), os.path.getmtime(file)
                )
        return dynamic_package

    def _is_valid_module_name(self, file: str):
        return file.endswith(".py")


def _validate_code_proc(queue: Queue):
    result = subprocess.run(
        [
            "coverage",
            "run",
            "--module",
            "pytest"
        ]
    )
    if result.returncode != 0:
        return queue.put(result)

    result = subprocess.run(
        [
            "coverage",
            "report",
            "--show-missing",
            "--skip-covered",
            "--fail-under=80",
            "--include=brain/*.py",
            "--omit=brain/__init__.py",
        ]
    )
    if result.returncode != 0:
        return queue.put(result)

    return queue.put(result)
