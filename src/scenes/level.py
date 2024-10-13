# level.py
import pygame
from utils.state import State
from entities.player import Player
from config.constants import *
from utils.texture_data import player_texture_data

class Level(State):
    def __init__(self, state_machine):
        super().__init__(state_machine)
        self.all_sprites = pygame.sprite.Group()

        # Load player spritesheets
        player_spritesheets = {}
        for key, data in player_texture_data.items():
            spritesheet = pygame.image.load(data['file_path']).convert_alpha()
            player_spritesheets[key.split('_')[1]] = {
                'spritesheet': spritesheet,
                'frame_size': data['frame_size'],
                'frames': data['frames'],
                'scale': data['scale']
            }

        # Create the player with the loaded spritesheet
        self.player = Player(
            self.all_sprites,
            player_spritesheets,
            (100, 100)
        )
        
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
