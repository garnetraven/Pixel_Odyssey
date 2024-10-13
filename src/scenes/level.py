import pygame
from utils.state import State
from scenes.pause_menu import PauseMenu
from entities.player import Player
from config.constants import *
from utils.texture_data import player_texture_data

class Tile(pygame.sprite.Sprite):
    def __init__(self, pos, size):
        super().__init__()
        self.image = pygame.Surface((size, size))
        self.image.fill((139, 69, 19))  # Brown color for dirt
        self.rect = self.image.get_rect(topleft = pos)

class Level(State):
    def __init__(self, state_machine):
        super().__init__(state_machine)
        self.all_sprites = pygame.sprite.Group()
        self.terrain_sprites = pygame.sprite.Group()

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
       
        # Load background image
        self.background = pygame.image.load('assets/background.png').convert()
        self.background = pygame.transform.scale(self.background, (SCREEN_WIDTH, SCREEN_HEIGHT))

        #self.generate_terrain()

    def generate_terrain(self):
        x_offset = 50
        y_offset = 200
        for row in range(20):
            for col in range(30):
                x = col * TILESIZE
                y = row * TILESIZE
                tile = Tile((x + x_offset, y + y_offset), TILESIZE)
                self.terrain_sprites.add(tile)
                self.all_sprites.add(tile)
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
                    self.state_machine.push(PauseMenu(self.state_machine)) 

    def update(self):
        self.player.update(self.terrain_sprites)

    def draw(self, screen):
        screen.blit(self.background, (0, 0))
        self.terrain_sprites.draw(screen)
        self.player.draw(screen)
