import pygame

from typing import Dict, List, Any

from config.constants import *
from entities.entity import Entity

class Player(Entity):
    def __init__(self, groups: List[pygame.sprite.Group], image: pygame.Surface, spritesheets: dict, position: tuple, parameters: Dict[str, Any]) -> None:
        super().__init__(groups, image, position, "player", parameters) 
        self.spritesheets = spritesheets
        self.animations = self.load_animations()
        self.current_frame = 0
        self.animation_speed = 0.2
        self.current_animation = 'idle'
        self.image = self.animations['idle'][self.current_frame]

        # Player-specific parameters
        self.health = parameters.get['health', 100]

        # Player stats
        self.base_speed = PLAYER_SPEED
        self.sprint_speed= PLAYER_SPRINT_SPEED
        self.mass = 5
        self.terminal_velocity = self.mass * TERMINAL_VELOCITY
        self.jump_strength = PLAYER_JUMP_POWER

        # Player states
        self.is_jumping = False
        self.is_grounded = False
        self.is_sprinting = False
        self.facing_right = True 

    def load_animations(self) -> dict:
        animations = {}
        for key, data in self.spritesheets.items():
            animations[key] = []
            spritesheet = data['spritesheet']
            frame_size = data['frame_size']
            frames = data['frames']
            scale = data['scale']
            scaled_size = (int(frame_size[0] * scale), int(frame_size[1] * scale))
            
            for i in range(frames):
                frame = pygame.Surface(frame_size, pygame.SRCALPHA)
                frame.blit(spritesheet, (0, 0), (i * frame_size[0], 0, frame_size[0], frame_size[1]))
                scaled_frame = pygame.transform.scale(frame, scaled_size)
                animations[key].append(scaled_frame)
        return animations

    def animate(self) -> None:
        self.current_frame += self.animation_speed
        if self.current_frame >= len(self.animations[self.current_animation]):
            self.current_frame = 0
        self.image = self.animations[self.current_animation][int(self.current_frame)]
        if not self.facing_right:
            self.image = pygame.transform.flip(self.image, True, False)

    def check_collisions(self, terrain_sprites) -> None:
        self.is_grounded = False
        for tile in terrain_sprites:
            if self.rect.colliderect(tile.rect):
                # Collision from above
                if self.velocity.y > 0: 
                    self.rect.bottom = tile.rect.top
                    self.velocity.y = 0
                    self.is_grounded = True
                    self.is_jumping = False
                # Collision from below
                elif self.velocity.y < 0:
                    self.rect.top = tile.rect.bottom
                    self.velocity.y = 0
                # Collision from the left
                elif self.velocity.x > 0:
                    self.rect.right = tile.rect.left
                # Collision from the right
                elif self.velocity.x < 0:
                    self.rect.left = tile.rect.right

    def handle_input(self, keys) -> None:
        self.velocity.x = 0  
        new_animation = 'idle'
        
        # Check for sprint
        if keys[pygame.K_LSHIFT] or keys[pygame.K_RSHIFT]:
            self.current_speed = self.sprint_speed
            self.is_sprinting = True
        else:
            self.current_speed = self.base_speed
            self.is_sprinting = False

        if keys[pygame.K_a]:
            self.velocity.x = -self.current_speed
            new_animation = 'run' if self.is_sprinting else 'walk'
            self.facing_right = False
        elif keys[pygame.K_d]:
            self.velocity.x = self.current_speed
            new_animation = 'run' if self.is_sprinting else 'walk'
            self.facing_right = True

        if keys[pygame.K_SPACE] and self.is_grounded:
            self.jump()
            new_animation = 'jump'

        if self.current_animation != new_animation:
            self.current_animation = new_animation
            self.current_frame = 0 

    def jump(self) -> None:
        if self.is_grounded:
            self.velocity.y = -self.jump_strength
            self.is_jumping = True
            self.is_grounded = False

    def move(self) -> None:
        # Apply gravity
        self.velocity.y += GRAVITY

        # Limit vertical velocity to terminal velocity
        if self.velocity.y > self.terminal_velocity:
            self.velocity.y = self.terminal_velocity
        
        # Update position
        self.rect.x += int(self.velocity.x)
        self.rect.y += int(self.velocity.y)
       
        # Keep the player within the screen bounds
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > SCREEN_WIDTH:
            self.rect.right = SCREEN_WIDTH
        if self.rect.top < 0:
            self.rect.top = 0
        if self.rect.bottom > SCREEN_HEIGHT:
            self.rect.bottom = SCREEN_HEIGHT
            self.velocity.y = 0
            self.is_grounded = True
            self.is_jumping = False
        else:
            self.is_grounded = False

    def handle_death(self):
        if self.health <= 0:
            self.kill()

    def update(self) -> None:
        self.move() 
        self.animate()

    def draw(self, screen) -> None:
        # Draw the player's image
        screen.blit(self.image, self.rect)
        
