import pygame
from globals import *
from utils.state import State
from utils.events import EventHandler

class StartMenu(State):
    def __init__(self, app) -> None:
        print(SCREENWIDTH, SCREENHEIGHT)
        StartMenu.font = pygame.font.Font(None, 45)

        self.app = app
        self.screen = self.app.screen

        # text
        self.title = "Pixel Odyssey"
        self.title_text = StartMenu.font.render(self.title, True, "black", None)
        self.title_rect = self.title_text.get_rect(center = (app.SCREENWIDTH//2, app.SCREENHEIGHT//2 - TILESIZE*2))
        self.buttons = [
            StateButton(self.screen, 'Play', 'world_select', (app.SCREENWIDTH//2, app.SCREENHEIGHT//2)),
            QuitButton(self.screen, 'Quit', (app.SCREENWIDTH//2, app.SCREENHEIGHT//2 + TILESIZE*2)),
        ]

    def update(self):
        for button in self.buttons:
            if button.clicked():
                button.use(self.app)

    def draw(self):
        self.screen.fill('lightblue')
        for button in self.buttons:
            button.draw(self.screen)
        self.screen.blit(self.title_text, self.title_rect)

class WorldSelect(State):
    def __init__(self, app) -> None:
        WorldSelect.font = pygame.font.Font(None, 45)

        self.app = app
        self.screen = self.app.screen


        self.texts = []
        self.texts.append(Text(self.app, 'Select a Level', (app.SCREENWIDTH//2, TILESIZE*2)))


        # text
        self.buttons = [
            StateButton(self.screen, 'Play', 'overworld', (app.SCREENWIDTH//2, app.SCREENHEIGHT//2))
        ]

        with open('worlddata/worldnames.txt', 'r') as f:
            data = []
            for line in f:
                line = line.rstrip('\n')
                data.append(line)
            for index, line in enumerate(data):
                self.buttons.append(ValueButton(self.screen, line, line, (app.SCREENWIDTH//2, TILESIZE*3 + index * TILESIZE)))
            
    def update(self):
        for button in self.buttons:
            if button.clicked():
                if type(button) == ValueButton:
                    self.app.world_key = button.value
                    self.app.load_world()
                else:
                    button.use(self.app)

    def draw(self):
        self.screen.fill('lightblue')
        for button in self.buttons:
            button.draw(self.screen)
        for text in self.texts:
            text.draw()

class Text:
    def __init__(self, app, text, position) -> None:
        self.app = app
        self.text = StartMenu.font.render(text, True, "black", None)
        self.rect = self.text.get_rect(center = position)

    def draw(self):
        self.app.screen.blit(self.text, self.rect)

class Button:
    def __init__(self, screen, text: str, position: tuple) -> None:
        self.screen = screen
        self.text = StartMenu.font.render(text, True, "black")
        self.rect = self.text.get_rect(center = position)

    def clicked(self) -> bool:
        if EventHandler.clicked():
            mouse_pos = pygame.mouse.get_pos()
            return self.rect.collidepoint(mouse_pos)

    def use(self, *args, **kwargs):
        pass

    def draw(self, display: pygame.Surface):
        display.blit(self.text, self.rect)

class StateButton(Button):
    def __init__(self, screen, text: str, state: str, position: tuple) -> None:
        super().__init__(screen, text, position)
        self.state = state

    def use(self, app):
        app.active_state = self.state

class QuitButton(Button):
    def __init__(self, screen, text: str, position: tuple) -> None:
        super().__init__(screen, text, position)

    def use(self, app):
        app.running = False

class ValueButton(Button):
    def __init__(self, screen, text: str, value: str, position: tuple) -> None:
        super().__init__(screen, text, position)
        self.value = value

class PauseMenu(State):
    def __init__(self, app) -> None:
        self.app = app
        self.screen = self.app.screen
        self.font = pygame.font.Font(None, 45)

        self.title = "Paused"
        self.title_text = self.font.render(self.title, True, "black", None)
        self.title_rect = self.title_text.get_rect(center=(app.SCREENWIDTH//2, app.SCREENHEIGHT//2 - TILESIZE*2))

        self.buttons = [
            StateButton(self.screen, 'Resume', 'overworld', (app.SCREENWIDTH//2, app.SCREENHEIGHT//2)),
            StateButton(self.screen, 'Options', 'options', (app.SCREENWIDTH//2, app.SCREENHEIGHT//2 + TILESIZE)),
            StateButton(self.screen, 'Save and Quit to Menu', 'start', (app.SCREENWIDTH//2, app.SCREENHEIGHT//2 + TILESIZE*2)),
        ]

    def update(self):
        for button in self.buttons:
            if button.clicked():
                if button.state == 'start':
                    self.quit_to_menu()
                else:
                    button.use(self.app)
                    if button.state == 'overworld':
                        self.app.unpause()

    def quit_to_menu(self):
        # Save and close the game scene
        self.app.quit_to_menu()

    def draw(self):
        self.app.states['overworld'].draw()  # Draw the game in the background
        s = pygame.Surface((self.app.SCREENWIDTH, self.app.SCREENHEIGHT))
        s.set_alpha(128)
        s.fill((100, 100, 100))
        self.screen.blit(s, (0, 0))

        self.screen.blit(self.title_text, self.title_rect)
        for button in self.buttons:
            button.draw(self.screen)

class OptionsMenu(State):
    def __init__(self, app) -> None:
        self.app = app
        self.screen = self.app.screen
        self.font = pygame.font.Font(None, 45)

        self.title = "Options"
        self.title_text = self.font.render(self.title, True, "black", None)
        self.title_rect = self.title_text.get_rect(center=(app.SCREENWIDTH//2, app.SCREENHEIGHT//2 - TILESIZE*3))

        self.buttons = [
            StateButton(self.screen, 'Back', 'pause', (app.SCREENWIDTH//2, app.SCREENHEIGHT//2 + TILESIZE*3)),
        ]

        self.music_volume = app.music_volume
        self.sfx_volume = app.sfx_volume

    def update(self):
        for button in self.buttons:
            if button.clicked():
                button.use(self.app)

        # Handle volume controls
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.music_volume = max(0, self.music_volume - 1)
        if keys[pygame.K_RIGHT]:
            self.music_volume = min(100, self.music_volume + 1)
        if keys[pygame.K_DOWN]:
            self.sfx_volume = max(0, self.sfx_volume - 1)
        if keys[pygame.K_UP]:
            self.sfx_volume = min(100, self.sfx_volume + 1)

        self.app.music_volume = self.music_volume
        self.app.sfx_volume = self.sfx_volume

    def draw(self):
        self.screen.fill('lightblue')
        self.screen.blit(self.title_text, self.title_rect)

        music_text = self.font.render(f"Music Volume: {self.music_volume}", True, "black")
        sfx_text = self.font.render(f"SFX Volume: {self.sfx_volume}", True, "black")

        self.screen.blit(music_text, (self.app.SCREENWIDTH//2 - 100, self.app.SCREENHEIGHT//2 - TILESIZE))
        self.screen.blit(sfx_text, (self.app.SCREENWIDTH//2 - 100, self.app.SCREENHEIGHT//2 + TILESIZE))

        for button in self.buttons:
            button.draw(self.screen)
