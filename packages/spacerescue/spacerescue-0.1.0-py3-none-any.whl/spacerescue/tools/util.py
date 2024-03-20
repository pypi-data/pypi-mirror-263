from functools import lru_cache, wraps

import sys
import numpy as np
import importlib as imp
import pyray as pr

request_for_exit = False


def wait_while_true(pred):
    while pred():
        pass


def window_request_close():
    global request_for_exit
    request_for_exit = True


def window_should_close():
    global request_for_exit
    return pr.window_should_close() or request_for_exit


def is_skip_key():
    return pr.is_key_pressed(pr.KeyboardKey.KEY_SPACE) or pr.is_mouse_button_pressed(
        pr.MouseButton.MOUSE_BUTTON_LEFT
    )


def first_not_none(a: list):
    return next((x for x in a if x is not None), None)


def np_cache(function):
    @lru_cache()
    def cached_wrapper(self, hashable_array):
        array = np.array(hashable_array)
        return function(self, array)

    @wraps(function)
    def wrapper(self, array):
        return cached_wrapper(self, tuple(array))

    # copy lru_cache attributes over too
    wrapper.cache_info = cached_wrapper.cache_info  # type: ignore
    wrapper.cache_clear = cached_wrapper.cache_clear  # type: ignore

    return wrapper


def load_module(source, module_name):
    spec = imp.util.spec_from_file_location(module_name, source)  # type: ignore
    module = imp.util.module_from_spec(spec)  # type: ignore
    sys.modules[module_name] = module
    spec.loader.exec_module(module)
    return module


def reload_module(module_name):
    return imp.reload(module_name)
