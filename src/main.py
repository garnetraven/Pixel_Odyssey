import pygame
import sys
from config.constants import SCREEN_WIDTH, SCREEN_HEIGHT, FPS 
from utils.state_machine import StateMachine
from scenes.main_menu import MainMenu

class Game:
    def __init__(self) -> None:
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("Pixel Odyssey")
        self.clock = pygame.time.Clock()
        self.running = True

        self.state_machine = StateMachine()
        self.state_machine.push(MainMenu(self.state_machine)) # Push initial state as Main Menu

    def run(self) -> None:
        while self.running:
            events = pygame.event.get()
            for event in events:
                if event.type == pygame.QUIT:
                    self.running = False
            
            # Handle events, update game state, and draw 
            self.state_machine.handle_events(events)
            self.state_machine.update()
            self.state_machine.draw(self.screen)

            pygame.display.flip()

            # Limit frame rate to FPS
            self.clock.tick(FPS)

        self.close() 

    def close(self) -> None:
        pygame.quit()
        sys.exit()

if __name__ == "__main__":
    game = Game()
    game.run()
