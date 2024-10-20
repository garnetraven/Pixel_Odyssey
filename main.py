import pygame
import sys
from globals import *
from world.scene import Scene
from utils.events import EventHandler
from ui.menus import StartMenu, WorldSelect, PauseMenu, OptionsMenu

class Game:
    def __init__(self) -> None:
        pygame.init()
        self.screen = pygame.display.set_mode((1280, 720))
        Game.SCREENWIDTH = self.screen.get_width()
        Game.SCREENHEIGHT = self.screen.get_height()

        self.clock = pygame.time.Clock()

        self.running = True
        self.paused = False

        # world key
        self.world_key = ''

        # Audio settings
        self.music_volume = 50
        self.sfx_volume = 50

        self.scene = Scene(self)
        self.states = {
            'overworld': None,
            'start': StartMenu(self),
            'world_select': WorldSelect(self),
            'pause': PauseMenu(self),
            'options': OptionsMenu(self),
        }
        self.active_state = 'start'

    def start(self) -> None:
        self.loop()
        self.close()

    def loop(self) -> None:
        while self.running:
            self.update()
            self.draw()

    def update(self) -> None:
        if self.active_state == "quit":
            self.running = False
        EventHandler.poll_events()
        if EventHandler.is_closed_requested():
            self.running = False
        if EventHandler.keydown(pygame.K_q):
            self.running = False
        if EventHandler.keydown(pygame.K_p): # screenshot
            with open('screenshots/screenshot.txt', 'r') as f:
                num = int(f.readline())
                print(num)
                
            pygame.image.save(self.screen, f'screenshots/save_{num}.png')
            with open('screenshots/screenshot.txt', 'w') as f:
                f.write(str(num + 1))

        if self.active_state == 'overworld' and EventHandler.keydown(pygame.K_ESCAPE):
            self.toggle_pause()

        self.states[self.active_state].update()

        # Check if we need to update the overworld state after a transition
        if self.active_state == 'overworld' and self.states['overworld'] != self.scene:
            self.states['overworld'] = self.scene

    def draw(self) -> None:
        self.states[self.active_state].draw()
        pygame.display.update()
        self.clock.tick(FPS)

    def close(self) -> None:
        if self.scene:
            self.scene.close()
        pygame.quit()
        sys.exit()

    def toggle_pause(self):
        if self.active_state == 'overworld':
            self.active_state = 'pause'
            self.paused = True
        elif self.active_state == 'pause':
            self.active_state = 'overworld'
            self.paused = False

    def unpause(self):
        self.active_state = 'overworld'
        self.paused = False

    def load_world(self):
        self.scene.on_load()
        self.states['overworld'] = self.scene
        self.active_state = 'overworld'

    def quit_to_menu(self):
        if self.scene:
            self.scene.close()
        self.states['overworld'] = None
        self.active_state = 'start'

if __name__ == "__main__":
    game = Game()
    game.start()
