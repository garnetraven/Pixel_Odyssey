import pygame
from config.constants import *

class Player(pygame.sprite.Sprite):
    def __init__(self, groups, image: pygame.Surface, position: tuple) -> None:
        super().__init__(groups)
        self.image = image
        self.rect = self.image.get_rect(topleft = position)
        self.color = (0, 255, 0)  # Green color
        self.velocity = pygame.math.Vector2()

        # Player stats
        self.base_speed = PLAYER_SPEED
        self.sprint_speed= PLAYER_SPEED * 1.5
        self.mass = 5
        self.terminal_velocity = self.mass * TERMINAL_VELOCITY
        self.jump_strength = PLAYER_JUMP_POWER

        # Player states
        self.is_jumping = False
        self.is_grounded = False
        self.is_sprinting = False

    def handle_input(self, keys):
        """Handle keyboard input for player movement."""
        self.velocity.x = 0  # Reset horizontal velocity
        
        # Check for sprint
        if keys[pygame.K_LSHIFT] or keys[pygame.K_RSHIFT]:
            self.current_speed = self.sprint_speed
            self.is_sprinting = True
        else:
            self.current_speed = self.base_speed
            self.is_sprinting = False

        if keys[pygame.K_a]:
            self.velocity.x = -self.current_speed
        if keys[pygame.K_d]:
            self.velocity.x = self.current_speed
        if keys[pygame.K_SPACE] and self.is_grounded:
            self.jump()

    def jump(self):
        if self.is_grounded:
            self.velocity.y = -self.jump_strength
            self.is_jumping = True
            self.is_grounded = False

    def update(self):
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

    def draw(self, screen):
        # Draw the player's image
        screen.blit(self.image, self.rect)
        
        # Optionally, draw a rectangle around the player for debugging
        pygame.draw.rect(screen, self.color, self.rect, 2)
        
        # Optionally, draw a dot at the player's center for reference
        center = self.rect.center
        pygame.draw.circle(screen, (255, 0, 0), center, 3)
