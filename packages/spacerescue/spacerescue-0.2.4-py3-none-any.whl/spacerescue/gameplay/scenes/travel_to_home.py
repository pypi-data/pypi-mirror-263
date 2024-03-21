from spacerescue.constants import (
    AU,
)
from spacerescue.gameplay.scenes.travel_in_space import TravelInSpace
from spacerescue.gameplay.scenes.game import Game
from spacerescue.physic.entities.galaxy.galaxy import ALL_STAR_SYSTEM_HABITABLE_PLANETS, ALL_STARS
from spacerescue.tools.util import is_skip_key

class TravelToHome(TravelInSpace):
    
    def __init__(self, root_scene: Game):
        super().__init__(root_scene)
        
    def enter_scene(self):
        super().enter_scene()
        star = self.galaxy.find_closest_stellar_object(self.spaceship.position, ALL_STARS)
        self.spaceship.arrive(self.galaxy.find_closest_stellar_object(self.spaceship.position, ALL_STAR_SYSTEM_HABITABLE_PLANETS(star)), 1 * AU)
 
    def update_simulation(self, dt: float):
        super().update_simulation(dt)
        
        if self.spaceship.is_arrived() or is_skip_key():
            self.root_scene.next_challenge()
           