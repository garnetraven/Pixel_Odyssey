import pygame

from config.constants import PLAYER_SPEED, PLAYER_SPRINT_SPEED, PLAYER_JUMP_POWER

class PlayerControllerComponent(Component):
    def __init__(self):
        super().__init__()
        self.is_jumping = False
        self.is_grounded = False
        self.is_sprinting = False

    def update(self, dt):
        transform = self.entity.get_component(TransformComponent)
        if not transform:
            return

        keys = pygame.key.get_pressed()
        
        # Reset horizontal velocity
        transform.velocity.x = 0

        # Check for sprint
        if keys[pygame.K_LSHIFT] or keys[pygame.K_RSHIFT]:
            current_speed = PLAYER_SPRINT_SPEED
            self.is_sprinting = True
        else:
            current_speed = PLAYER_SPEED
            self.is_sprinting = False

        # Horizontal movement
        if keys[pygame.K_a]:
            transform.velocity.x = -current_speed
        elif keys[pygame.K_d]:
            transform.velocity.x = current_speed

        # Jumping
        if keys[pygame.K_SPACE] and self.is_grounded:
            transform.velocity.y = -PLAYER_JUMP_POWER
            self.is_jumping = True
            self.is_grounded = False

        # Apply gravity (this should be handled by a separate physics component in a more complex system)
        transform.velocity.y += GRAVITY * dt