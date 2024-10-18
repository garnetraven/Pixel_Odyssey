import pygame

from entity import Entity

class Mob(Entity):
    def __init__(self, groups, image: pygame.Surface, position = (0, 0), parameters = {}) -> None:
        super().__init__(groups, image, position)
        
        if parameters:
            self.block_group = parameters['block_group']
            self.player = parameters['player']
            self.health = parameters['health']
            self.damage = parameters['damage']

        self.velocity = pygame.math.Vector2()
        self.mass = 5

    def move(self) -> None:
        pass

    def update(self) -> None:
        self.move()
