from __future__ import annotations
from functools import cache

from spacerescue.render import resource_manager

class Scene:

    RESOURCE_MANAGER = resource_manager.get_instance("scene")

    def __init__(self):
        pass

    def enter_scene(self):
        get_instance().enter_scene(self)

    def leave_scene(self):
        get_instance().leave_scene()

    def update(self):
        pass

    def draw(self):
        pass


class DestroyableScene(Scene):

    def __init__(self):
        super().__init__()

    def leave_scene(self):
        Scene.RESOURCE_MANAGER.unload_all()
        super().leave_scene()

class SceneManager:

    def __init__(self):
        self.state: list[Scene] = []

    def has_current_scene(self):
        return len(self.state) > 0

    def get_current_scene(self):
        return self.state[-1]

    def enter_scene(self, scene: Scene):
        self.state.append(scene)

    def leave_scene(self):
        self.state.pop()


@cache
def get_instance(name: str = "singleton") -> SceneManager:
    return SceneManager()
