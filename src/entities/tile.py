import pygame
from config.constants import *
from utils.events import EventHandler

class Tile(pygame.sprite.Sprite):
    def __init__(self, groups, image: pygame.Surface, position: tuple, name: str = "default", type="block", flipped=0, durability: int = 20, hardness: int = 1, special_flags = None) -> None:
        super().__init__(groups)
        self.name = name
        self.type = type
        self.in_groups = groups
        self.image = image.copy()
        self.rect = self.image.get_rect(bottomleft = (position[0], position[1]+TILESIZE))
        self.flipped = flipped
        match flipped:
            case 1:
                self.image = pygame.transform.flip(self.image, True, False)
            case 2:
                self.image = pygame.transform.flip(self.image, True, True)
            case 3:
                self.image = pygame.transform.flip(self.image, False, True)
        self.active = True
        self.durability = durability
        self.hardness = hardness
        self.special_flags = special_flags

    def break_block(self, strength) -> bool:
        if strength >= self.hardness:
            self.durability -= 1 * strength
            if self.durability < 1:
                self.active = False
                self.kill()
                return True
        return False
