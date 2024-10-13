import pygame
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from state import State

class MainMenu(State):
    def __init__(self, state_machine):
        super().__init__(state_machine)
        self.font = pygame.font.SysFont("Arial", 48)
        self.options = ["Start Game", "Options", "Quit"]
        self.selected = 0

    def enter(self):
        """Called when entering the main menu state."""
        print("Entering Main Menu")

    def exit(self):
        """Called when exiting the main menu state."""
        print("Exiting Main Menu")

    def handle_events(self, events):
        """Handle input events for the main menu."""
        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    self.selected = (self.selected - 1) % len(self.options)
                elif event.key == pygame.K_DOWN:
                    self.selected = (self.selected + 1) % len(self.options)
                elif event.key == pygame.K_RETURN:
                    if self.options[self.selected] == "Start Game":
                        self.state_machine.change_state()
                    elif self.options[self.selected] == "Quit":
                        self.state_machine.pop()
                        pygame.quit()
    
    def update(self, dt):
        """Update logic for the main menu."""
        pass

    def draw(self, screen):
        """Render the main menu."""
        screen.fill((0, 0, 0))  # Clear screen with black
        for idx, option in enumerate(self.options):
            color = (255, 255, 255) if idx == self.selected else (100, 100, 100)
            text = self.font.render(option, True, color)
            rect = text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + idx * 60))
            screen.blit(text, rect)
