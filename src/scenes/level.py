# level.py
import pygame
from utils.state import State
from entities.player import Player
from config.constants import *

class Level(State):
    def __init__(self, state_machine):
        super().__init__(state_machine)
        self.all_sprites = pygame.sprite.Group()
        self.player = Player(self.all_sprites, pygame.Surface((TILESIZE * 2, TILESIZE * 3)), (100, 100))  
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

    def update(self):
        self.player.update()

    def draw(self, screen):
        screen.fill(self.background_color)
        self.player.draw(screen)
