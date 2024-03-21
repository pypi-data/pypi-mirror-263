import logging
import pyray as pr

from spacerescue.constants import (
    FRAMES_PER_SECOND,
    SCREEN_HEIGHT,
    SCREEN_WIDTH,
)
from spacerescue.gameplay import context_manager
from spacerescue.sketch import Sketch
from spacerescue.tools.util import window_should_close

CONTEXT = context_manager.get_instance()

def main():
    logging.basicConfig(format='%(message)s', level=logging.DEBUG)
    
    CONTEXT.clean_all()
    
    pr.set_config_flags(pr.ConfigFlags.FLAG_MSAA_4X_HINT)
    pr.init_window(SCREEN_WIDTH, SCREEN_HEIGHT, "Space Rescue - A Escape Coding Adventure")
    pr.set_target_fps(FRAMES_PER_SECOND)  
    pr.init_audio_device()
    
    sketch = Sketch()
    while not window_should_close():
        sketch.update()
        sketch.draw()
    sketch.destroy()
    
    pr.close_audio_device()
    pr.close_window()
    
if __name__ == "__main__":
    main()
