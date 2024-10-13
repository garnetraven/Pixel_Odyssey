import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.x = x
        self.y = y
        self.width = 50
        self.height = 50
        self.color = (0, 255, 0)  # Green color
        self.velocity_x = 0
        self.velocity_y = 0
        self.speed = 200  # Pixels per second

    def handle_input(self, keys):
        """Handle keyboard input for player movement."""
        self.velocity_x = 0
        self.velocity_y = 0
        if keys[pygame.K_LEFT]:
            self.velocity_x = -self.speed
        if keys[pygame.K_RIGHT]:
            self.velocity_x = self.speed
        if keys[pygame.K_UP]:
            self.velocity_y = -self.speed
        if keys[pygame.K_DOWN]:
            self.velocity_y = self.speed

    def update(self, dt):
        """Update the player's position."""
        self.x += self.velocity_x * dt
        self.y += self.velocity_y * dt

    def draw(self, screen):
        """Draw the player on the screen."""
        pygame.draw.rect(screen, self.color, (self.x, self.y, self.width, self.height))
