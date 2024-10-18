class AnimationComponent(Component):
    def __init__(self, animations):
        super().__init__()
        self.animations = animations
        self.current_animation = 'idle'
        self.current_frame = 0
        self.animation_speed = 0.2

    def update(self, dt):
        self.current_frame += self.animation_speed
        if self.current_frame >= len(self.animations[self.current_animation]):
            self.current_frame = 0

        sprite = self.entity.get_component(SpriteComponent)
        if sprite:
            sprite.image = self.animations[self.current_animation][int(self.current_frame)]

    def set_animation(self, animation_name):
        if animation_name != self.current_animation:
            self.current_animation = animation_name
            self.current_frame = 0
