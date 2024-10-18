import pygame

from utils.state import State
from config.constants import SCREEN_WIDTH, SCREEN_HEIGHT

class OptionsMenu(State):
    def __init__(self, state_machine) -> None:
        super().__init__(state_machine)
        self.font = pygame.font.SysFont("Arial", 48)
        self.small_font = pygame.font.SysFont("Arial", 36)
        self.options = ["Toggle Fullscreen", "Back"]
        self.selected = 0
        self.fullscreen = False

    def enter(self) -> None:
        """Called when entering the options menu state."""
        print("Entering Options Menu")

    def exit(self) -> None:
        """Called when exiting the options menu state."""
        print("Exiting Options Menu")

    def handle_events(self, events) -> None:
        """Handle input events for the options menu."""
        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    self.selected = (self.selected - 1) % len(self.options)
                elif event.key == pygame.K_DOWN:
                    self.selected = (self.selected + 1) % len(self.options)
                elif event.key == pygame.K_RETURN:
                    selected_option = self.options[self.selected]
                    if selected_option == "Toggle Fullscreen":
                        self.toggle_fullscreen()
                    elif selected_option == "Back":
                        self.state_machine.pop()

    def toggle_fullscreen(self) -> None:
        """Toggle the fullscreen mode."""
        self.fullscreen = not self.fullscreen
        if self.fullscreen:
            self.state_machine.screen = pygame.display.set_mode(
                (SCREEN_WIDTH, SCREEN_HEIGHT),
                pygame.FULLSCREEN
            )
        else:
            self.state_machine.screen = pygame.display.set_mode(
                (SCREEN_WIDTH, SCREEN_HEIGHT)
            )
        print(f"Fullscreen set to {self.fullscreen}")

    def update(self) -> None:
        """Update logic for the options menu."""
        pass

    def draw(self, screen) -> None:
        """Render the options menu."""
        screen.fill((50, 50, 50))  # Dark gray background
        title_text = self.font.render("Options", True, (255, 255, 255))
        title_rect = title_text.get_rect(center=(SCREEN_WIDTH // 2, 100))
        screen.blit(title_text, title_rect)

        for idx, option in enumerate(self.options):
            color = (255, 255, 255) if idx == self.selected else (200, 200, 200)
            text = self.small_font.render(option, True, color)
            rect = text.get_rect(center=(SCREEN_WIDTH // 2, 200 + idx * 50))
            screen.blit(text, rect)

        # Display current fullscreen status
        status_text = self.small_font.render(
            f"Fullscreen: {'On' if self.fullscreen else 'Off'}",
            True,
            (255, 255, 255)
        )
        status_rect = status_text.get_rect(center=(SCREEN_WIDTH // 2, 350))
        screen.blit(status_text, status_rect)
