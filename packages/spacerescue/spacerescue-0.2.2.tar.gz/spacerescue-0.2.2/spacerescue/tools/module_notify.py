import os
import logging
import traceback
import importlib

from spacerescue.tools.util import load_module


class ModuleNotify:
    
    def __init__(self, path: str, module_name: str, func):
        self.path = path
        self.func = func
        self.module = load_module(path, module_name)
        self.timestamp = os.path.getmtime(path)
        
    def update(self):
        timestamp = os.path.getmtime(self.path)
        if timestamp > self.timestamp:
            self.timestamp = timestamp
            logging.info(f"INFO: FILEIO: [{self.path}] changed, reload code")
            try:
                importlib.reload(self.module)
                self.func()
            except Exception as e:
                logging.error(traceback.format_exc())