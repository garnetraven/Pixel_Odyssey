import pygame

from utils.state import State
from scenes.pause_menu import PauseMenu
from entities.player import Player
from config.constants import *
from utils.camera import Camera
from utils.texture_data import player_texture_data

class Level(State):
    def __init__(self, state_machine) -> None:
        super().__init__(state_machine)
        self.sprites = Camera()
        self.terrain_sprites = pygame.sprite.Group()

        self.blocks = pygame.sprite.Group()
        self.enemy_group = pygame.sprite.Group()
        self.group_list: dict[str, pygame.sprite.Group] = {
            'block_group':self.blocks,
            'enemy_group':self.enemy_group
        }

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
            self.sprites,
            player_spritesheets,
            (100, 100),
            parameters= {
                'group_list': self.group_list,
            }
        )
       
        # Load background image
        self.background = pygame.image.load('assets/background.png').convert()
        self.background = pygame.transform.scale(self.background, (SCREEN_WIDTH, SCREEN_HEIGHT))

        #self.generate_terrain()

    def generate_terrain(self) -> None:
        pass

    def enter(self) -> None:
        print("Entering Level")

    def exit(self) -> None:
        print("Exiting Level")

    def handle_events(self, events) -> None:
        keys = pygame.key.get_pressed()
        self.player.handle_input(keys)

        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.state_machine.push(PauseMenu(self.state_machine)) 

    def update(self) -> None:
        self.player.update()

    def draw(self, screen) -> None:
        screen.blit(self.background, (0, 0))
        self.player.draw(screen)
