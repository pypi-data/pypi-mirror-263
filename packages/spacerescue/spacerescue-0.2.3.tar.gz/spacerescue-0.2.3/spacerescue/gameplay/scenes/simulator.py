import numpy as np
import pyray as pr

from spacerescue.constants import SCREEN_HEIGHT, SCREEN_WIDTH
from spacerescue.gameplay.scenes.game import Game
from spacerescue.gameplay.scene_manager import DestroyableScene
from spacerescue.physic.entities.simulation.drone import Drone
from spacerescue.physic.entities.simulation.world import World
from spacerescue.render.animators.fade_scr import FadeScr
from spacerescue.render.widgets.button import Button
from spacerescue.render.widgets.screen import Screen
from spacerescue.tools.util import is_skip_key


class Simulator(DestroyableScene):

    SIMULATION_SPEED = 10
    BORDER_SIZE = 55
    
    def __init__(self, root_scene: Game):
        super().__init__()
        self.root_scene = root_scene
        self.brain = self.root_scene.get_last_answer()
   
    def enter_scene(self):
        super().enter_scene()
        self._spawn_entities()
        self._build_ui()
        self.state = 0
        self.collided = False

    def update_simulation(self, dt: float):
        for i in range(Simulator.SIMULATION_SPEED):
            self.world.update(dt)
            for drone in self.drones:
                if self.world.check_collision(drone):
                    self.destroyed_drones.append(drone)
                    self.drones.remove(drone)
                drone.update(dt)
                    
    def update(self):
        match self.state:
            case 0:
                if self.fade_in.is_playing():
                    self.fade_in.update()
                else:
                    self.state = 1

            case 1:
                dt = pr.get_frame_time()
                self.update_simulation(dt)
                for button in self.buttons:
                    button.update()
                if len(self.drones) == 0:
                    self.state = 2
                
            case 2:
                assert self.brain is not None
                self.brain.fit(self.destroyed_drones)
                self._spawn_entities()
                self.state = 1
            
            case 3:
                self.root_scene.abandon_challenge()
                from spacerescue.gameplay.challenges.challenge3 import Challenge3
                self.root_scene.begin_challenge(Challenge3(self.root_scene))
                
            case 4:
                self.root_scene.next_challenge()

    def draw(self):
        pr.begin_drawing()
        pr.clear_background(pr.Color(64, 191, 182, 255))
        
        # Draw Console
        
        pr.begin_scissor_mode(
            int(self.world.bound.x),
            int(self.world.bound.y),
            int(self.world.bound.width),
            int(self.world.bound.height),
        )
        self.world.draw()
        for drone in self.drones:
            drone.draw()
        pr.end_scissor_mode()
        bound = pr.Rectangle(
            int(self.world.bound.x - Simulator.BORDER_SIZE),
            int(self.world.bound.y - Simulator.BORDER_SIZE),
            int(self.world.bound.width + Simulator.BORDER_SIZE * 2),
            int(self.world.bound.height + Simulator.BORDER_SIZE * 2),
        )
        pr.draw_texture_pro(
            self.scanline,
            pr.Rectangle(0, 0, bound.width, bound.height),
            bound,
            pr.vector2_zero(),
            0.0,
            pr.WHITE,  # type: ignore
        )
        
        # Draw the UI
        
        self.screen.draw()
        for button in self.buttons:
            button.draw()
        if self.state == 0:
            self.fade_in.draw()
        pr.end_drawing()

    def _button_is_clicked(self, button: Button):
        if button.id == "button_submit":
            self.state = 4
        if button.id == "button_abandon":
            self.state = 3

    def _spawn_entities(self):
        self.world = World(
            205,
            135,
            SCREEN_WIDTH - 405,
            SCREEN_HEIGHT - 250,
        )
        assert self.brain is not None
        self.drones = self.brain.get_drones(self.world, np.array([-200.0, 200.0, 0.0]))
        self.destroyed_drones = []

    def _build_ui(self):
        self.scanline = Simulator.RESOURCE_MANAGER.load_texture("scanline")
        self.fade_in = FadeScr(0.5)
        self.screen = Screen("widget", "computer_console")
        self.buttons = [
            Button(
                "button_submit",
                pr.Vector2(SCREEN_WIDTH - 220, SCREEN_HEIGHT - 94),
                pr.Vector2(200, 38),
                "SUBMIT",
                pr.Color(254, 201, 123, 192),
                self._button_is_clicked,
            ),
            Button(
                "button_abandon",
                pr.Vector2(SCREEN_WIDTH - 220, SCREEN_HEIGHT - 45),
                pr.Vector2(200, 38),
                "ABANDON",
                pr.Color(252, 127, 104, 192),
                self._button_is_clicked,
            ),
        ]
