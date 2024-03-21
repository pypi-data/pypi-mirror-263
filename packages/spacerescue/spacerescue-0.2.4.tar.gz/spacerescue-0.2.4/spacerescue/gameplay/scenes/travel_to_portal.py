from spacerescue.constants import (
    AU,
)
from spacerescue.gameplay.scenes.travel_in_space import TravelInSpace
from spacerescue.gameplay.scenes.game import Game
from spacerescue.physic.entities.galaxy.galaxy import ALL_PORTALS

class TravelToPortal(TravelInSpace):
    
    def __init__(self, root_scene: Game):
        super().__init__(root_scene)
        
    def enter_scene(self):
        super().enter_scene()
        self.spaceship.arrive(self.galaxy.find_closest_stellar_object(self.spaceship.position, ALL_PORTALS), 2.55 * AU)
 
    def update_simulation(self, dt: float):
        super().update_simulation(dt)
        
        if self.spaceship.is_arrived():
            self.root_scene.next_challenge()
           