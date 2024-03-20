import pyray as pr

from spacerescue.constants import AU
from spacerescue.gameplay.scenes.travel_in_space import TravelInSpace
from spacerescue.gameplay.scenes.game import Game
from spacerescue.physic.entities.galaxy.galaxy import ALL_PORTALS
from spacerescue.render.effects.star_field import StarField


class TravelToHyperspace(TravelInSpace):
    
    def __init__(self, root_scene: Game):
        super().__init__(root_scene)
        
    def enter_scene(self):
        super().enter_scene()
        self.star_field = StarField()
        self.spaceship.arrive(self.galaxy.find_closest_stellar_object(self.spaceship.position, ALL_PORTALS), 2.54 * AU)
        self.state = 0
        self.timer = 0
        
    def update_simulation(self, dt: float):
        super().update_simulation(dt)
          
        match self.state:
            case 0:
                if self.spaceship.is_arrived():
                    self.spaceship.arrive(self.galaxy.find_closest_stellar_object(self.spaceship.position, ALL_PORTALS), 2.53 * AU)
                    self.state = 1
            
            case 1:
                self.star_field.update(dt)
                if self.spaceship.is_arrived():
                    self.spaceship.add_force(self.spaceship.heading * 1e9)
                    self.state = 2
                    
            case 2:
                self.timer += dt
                if self.timer <= 0.5:
                    self.star_field.update(dt)
                else:
                    self.root_scene.next_challenge()
                    self.state = 3

    def draw_effect(self):
        if self.state >= 1:
            self.star_field.draw()
        