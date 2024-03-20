import pyray as pr

from spacerescue.constants import SCREEN_HEIGHT, SCREEN_WIDTH
from spacerescue.gameplay.root_scene import RootScene
from spacerescue.gameplay.scenes.title import Title
from spacerescue.render.animators.fade_inout import FadeInOut

class Logo(RootScene):

    def __init__(self):
        super().__init__()
        
    def enter_scene(self):
        super().enter_scene()
        self.timer = 0
        self.fade_in = FadeInOut(0, 255, 1.0, pr.Color(*pr.WHITE))
        self.fade_out = FadeInOut(255, 0, 1.0, pr.Color(*pr.WHITE))
        self.logo = Logo.RESOURCE_MANAGER.load_texture("logo")
        self.state = 0
       
    def update(self):
        match self.state:
            case 0:
                if 0.0 <= self.timer < 1.5:
                    self.fade_in.update()
                else:
                    self.state = 1
                    
            case 1:
                if 1.5 <= self.timer < 3.0:
                    pass # wait on the logo
                else:
                    self.state = 2
                    
            case 2:
                if 3.0 <= self.timer < 4.5:
                    self.fade_out.update()
                else:
                    self.fade_in.reset()
                    self.fade_out.reset()
                    self.state = 3
                    
            case 3:
                if 4.5 <= self.timer < 6.0:
                    self.fade_in.update()
                else:
                    self.state = 4
                    
            case 4:
                if 6.0 <= self.timer < 7.5:
                    pass # wait on the present
                else:
                    self.state = 5
                    
            case 5:
                if 7.5 <= self.timer < 9.0:
                    self.fade_out.update()
                else:
                    self.state = 6
                    
            case 6:
                self.leave_scene()
                Title().enter_scene()
                
        self.timer += max(pr.get_frame_time(), 1/60)
            
    def draw(self):
        pr.begin_drawing()
        pr.clear_background(pr.WHITE) # type: ignore
        
        if 0 <= self.state < 3:
            pos_x = int(SCREEN_WIDTH / 2 - self.logo.width / 2)
            pos_y = int(SCREEN_HEIGHT / 2 - self.logo.height / 2)
            pr.draw_texture(self.logo, pos_x, pos_y, pr.WHITE) # type: ignore
            
        if 3 <= self.state < 6:
            hw = pr.measure_text("present", 20) / 2
            pos_x = int(SCREEN_WIDTH / 2 - hw)
            pos_y = int(SCREEN_HEIGHT / 2 - hw)
            pr.draw_text("present", pos_x, pos_y, 20, pr.BLACK) # type: ignore
        
        self.fade_in.draw()
        self.fade_out.draw()
        
        pr.end_drawing()
