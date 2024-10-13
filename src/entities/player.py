import pygame
from config.constants import *

class Player(pygame.sprite.Sprite):
    def __init__(self, groups, image: pygame.Surface((TILESIZE * 2, TILESIZE * 3)), position: tuple) -> None:
        super().__init__(groups)
        self.image = image
        self.rect = self.image.get_rect(topleft = position)
        self.width = 50
        self.height = 50
        self.color = (0, 255, 0)  # Green color
        self.velocity = pygame.math.Vector2()
        self.mass = 5
        self.terminal_velocity = self.mass * TERMINAL_VELOCITY

    def handle_input(self, keys):
        """Handle keyboard input for player movement."""
        self.velocity_x = 0
        if keys[pygame.K_LEFT]:
            self.velocity_x = -self.speed
        if keys[pygame.K_RIGHT]:
            self.velocity_x = self.speed

    def update(self, dt, screen_width, screen_height):
        """Update the player's position and apply gravity."""
        # Apply gravity to vertical velocity
        self.velocity_y += self.gravity * dt

        # Update position based on velocity and delta time
        self.x += self.velocity_x * dt
        self.y += self.velocity_y * dt

        # Clamp position to stay within screen bounds and simulate ground collision
        if self.x < 0:
            self.x = 0
        elif self.x > screen_width - self.width:
            self.x = screen_width - self.width

        if self.y < 0:
            self.y = 0
            self.velocity_y = 0  # Reset vertical velocity if hitting the ceiling
        elif self.y > screen_height - self.height:
            # Simulate ground collision by stopping vertical movement when hitting the ground
            self.y = screen_height - self.height
            self.velocity_y = 0

    def draw(self, screen):
        """Draw the player on the screen."""
        pygame.draw.rect(screen, self.color, (self.x, self.y, self.width, self.height))
