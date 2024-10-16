import pygame

class Entity(pygame.sprite.Sprite):
    def __init__(self, groups, image: pygame.Surface, position: tuple = (0, 0), name: str = "default") -> None:

        super().__init__(groups)
        self.groups = groups
        self.image = image
        self.name = name
        self.rect = self.image.get_rect(topleft = position)

    def update(self) -> None:
        pass
