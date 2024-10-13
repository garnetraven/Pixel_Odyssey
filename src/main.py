import pygame
from config.constants import SCREEN_WIDTH, SCREEN_HEIGHT, FPS 
from utils.state_machine import StateMachine
from scenes.main_menu import MainMenu

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("Pixel Odyssey")
        self.clock = pygame.time.Clock()
        self.running = True

        self.state_machine = StateMachine()
        self.state_machine.push(MainMenu(self.state_machine))

    def run(self):
        while self.running:
            dt = self.clock.tick(FPS) / 1000
            events = pygame.event.get()
            
            for event in events:
                if event.type == pygame.QUIT:
                    self.running = False
            
            self.state_machine.handle_events(events)
            self.state_machine.update(dt)
            self.state_machine.draw(self.screen)

            pygame.display.flip()
            self.clock.tick(FPS)

        pygame.quit()

if __name__ == "__main__":
    game = Game()
    game.run()
