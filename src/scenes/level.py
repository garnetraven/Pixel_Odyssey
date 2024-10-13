# level.py
import pygame
from utils.state import State
from entities.player import Player
from config.constants import *

class Level(State):
    def __init__(self, state_machine):
        super().__init__(state_machine)
        self.player = Player((100, 100))  
        self.background_color = (50, 50, 150) 

    def enter(self):
        print("Entering Level")

    def exit(self):
        print("Exiting Level")

    def handle_events(self, events):
        keys = pygame.key.get_pressed()
        self.player.handle_input(keys)

        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.state_machine.pop() 

    def update(self, dt):
        # Pass screen dimensions to ensure player stays within bounds and applies gravity correctly
        screen_width = SCREEN_WIDTH
        screen_height = SCREEN_HEIGHT
        self.player.update(dt, screen_width, screen_height)

    def draw(self, screen):
        screen.fill(self.background_color)
        self.player.draw(screen)
