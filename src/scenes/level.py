import pygame
from utils.state import State
from entities.player import Player

class Level(State):
    def __init__(self, state_machine):
        super().__init__(state_machine)
        self.player = Player(100, 100)  
        self.background_color = (50, 50, 150) 

    def enter(self):
        """Called when entering the level state."""
        print("Entering Level")

    def exit(self):
        """Called when exiting the level state."""
        print("Exiting Level")

    def handle_events(self, events):
        """Handle input events for the level."""
        keys = pygame.key.get_pressed()
        self.player.handle_input(keys)

        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.state_machine.pop()  # Return to previous state

    def update(self, dt):
        """Update the level logic."""
        self.player.update(dt)
        # Add any additional level-specific updates here

    def draw(self, screen):
        """Render the level."""
        screen.fill(self.background_color)
        self.player.draw(screen)
        # Add any additional drawing code here
