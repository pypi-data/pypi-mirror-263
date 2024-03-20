import pyray as pr

from spacerescue.render import resource_manager
from spacerescue.gameplay import scene_manager


class Sketch:

    def __init__(self):
        self.music = resource_manager.get_instance().load_music("music")

        from spacerescue.gameplay.scenes.logo import Logo
        Logo().enter_scene()
        # from spacerescue.gameplay.scenes.game import Game
        # Game().enter_scene()
        # from hackaton.gameplay.scenes.game import Game
        # from hackaton.gameplay.scenes.travel_to_portal import TravelToPortal
        # TravelToPortal(Game()).enter_scene()

    def destroy(self):
        resource_manager.get_instance().unload_all()

    def update(self):
        if pr.is_music_stream_playing(self.music):
            pr.update_music_stream(self.music)
        scene_manager.get_instance().get_current_scene().update()

    def draw(self):
        if scene_manager.get_instance().has_current_scene():
            scene_manager.get_instance().get_current_scene().draw()
