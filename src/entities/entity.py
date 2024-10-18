import pygame

from typing import Dict, Any

class Entity(pygame.sprite.Sprite):
    def __init__(self, groups, image: pygame.Surface, position: tuple = (0, 0), name: str = "default", parameters: Dict[str, Any] = None) -> None:

        super().__init__(groups)
        self.groups = groups
        self.image = image
        self.name = name
        self.rect = self.image.get_rect(topleft = position)
        self.velocity = pygame.math.Vector2()
        self.parameters = parameters or {}

    def update(self) -> None:
        pass

    def move(self) -> None:
        pass

    def handle_collision(self, other: 'Entity') -> None:
        pass
