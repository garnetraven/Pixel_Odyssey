import pygame
import sys

from globals import * 
from utils.events import EventHandler

class Game:
    def __init__(self) -> None:
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("Pixel Odyssey")

        self.clock = pygame.time.Clock()

        self.running = True

        #self.scene = Scene(self)

        self.states = {}
        #    'overworld':self.scene,
        #    'home_base':HomeBase(self),
        #    'start':StartMenu(self),
        #    'world_select':WorldSelect(self),
        #}
        self.active_state = 'start'

    def start(self) -> None:
        self.loop()
        self.close()

    def loop(self) -> None:
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
            with open("screenshots/screenshot.txt", 'r') as f:
                num = int(f.readline())
                print(num)

        self.states[self.active_state].update()

    def draw(self) -> None:
        self.states[self.active_state].draw()
        pygame.display.update()
        self.clock.tick(FPS)

    def close(self) -> None:
        self.states[self.active_state].close()
        pygame.quit()
        sys.exit()

if __name__ == "__main__":
    game = Game()
    game.start()
