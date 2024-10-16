import pygame
from entities.player import Player

class Camera(pygame.sprite.Group):
    def __init__(self) -> None:
        super().__init__()

    def draw(self, target: Player, display: pygame.Surface) -> None:
        offset = pygame.math.Vector2()
        offset.x = display.get_width() / 2 - target.rect.centerx
        offset.y = display.get_height() / 1.6 - target.rect.centery
        
        for sprite in self.sprites():
            sprite_offset = pygame.math.Vector2()
            sprite_offset.x = offset.x + sprite.rect.x
            sprite_offset.y = offset.y + sprite.rect.y
            
            display.blit(sprite.image, sprite_offset)
