import pyray as pr

from spacerescue.constants import SCREEN_HEIGHT, SCREEN_WIDTH
from spacerescue.gameplay.scenes.game import Game
from spacerescue.gameplay.root_scene import RootScene
from spacerescue.render.animators.fade_inout import FadeInOut
from spacerescue.render import resource_manager
from spacerescue.gameplay import context_manager
from spacerescue.tools.util import is_skip_key

class Title(RootScene):

    CONTEXT = context_manager.get_instance()
    
    def __init__(self):
        super().__init__()
        Title.CONTEXT.build_all()
       
    def enter_scene(self):
        super().enter_scene()
        self.title = Title.RESOURCE_MANAGER.load_texture("title")
        self.fade_in = FadeInOut(0, 255, 1.0, pr.Color(*pr.WHITE))
        self.fade_out = FadeInOut(255, 0, 1.0, pr.Color(*pr.BLACK))
        self.timer = 0
        self.state = 0
        self._start_play_music()
       
    def update(self):
        match self.state:
            case 0:
                if self.fade_in.is_playing():
                    self.fade_in.update()
                else:
                    self.timer = 0
                    self.state = 1
                    
            case 1:
                if 0.0 <= self.timer < 30.0 and not is_skip_key():
                    pass # wait on the logo
                else:
                    self.state = 2
                    
            case 2:
                if self.fade_out.is_playing():
                    self.fade_out.update()
                else:
                    self.state = 3
                    
            case 3:
                self.leave_scene()
                Game().enter_scene()
                self.state = 4
                
        self.timer += pr.get_frame_time()

    def draw(self):
        pr.begin_drawing()
        
        pos_x = int((SCREEN_WIDTH - self.title.width) / 2)
        pos_y = int((SCREEN_HEIGHT - self.title.height) / 2)
        pr.draw_texture(self.title, pos_x, pos_y, pr.WHITE) # type: ignore
        
        if self.state in (0, 2, 3):
            self.fade_in.draw()
            self.fade_out.draw()
        
        pr.end_drawing()
        
    def _start_play_music(self):
        music = resource_manager.get_instance().load_music("music")
        pr.set_music_volume(music, 0.5)
        pr.play_music_stream(music)
