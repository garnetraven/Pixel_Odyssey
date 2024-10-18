class SpriteComponent(Component):
    def __init__(self, image: pygame.Surface) -> None:
        super().__init__()
        self.image = image
        self.rect = self.image.get_rect()

    def update(self, dt) -> None:
        transform = self.entity.get_component(TransformComponent)
        if transform:
            self.rect.topleft = transform.position

    def draw(self, screen) -> None:
        screen.blit(self.image, self.rect)