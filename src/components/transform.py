class TransformComponent(Component):
    def __init__(self, x, y) -> None:
        super().__init__()
        self.postition = pygame.math.Vector2(x, y)
        self.velocity = pygame.math.Vector2()
        
    def update(self, dt) -> None:
        self.postition += self.velocity * dt
