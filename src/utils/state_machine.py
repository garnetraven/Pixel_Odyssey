class StateMachine:
    def __init__(self):
        self.states = []

    def push(self, state):
        if self.states:
            self.states[-1].exit() # Exit current state
        self.states.append(state)
        state.enter() # Enter new current state

    def pop(self):
        if self.states:
            self.states[-1].exit() # Exit current state
            self.states.pop()

        if self.states:
            self.states[-1].enter() # Enter new current state

    def change_state(self, state):
        """Replace current state with new one"""
        self.pop()
        self.push(state)

    def handle_events(self, events):
        if self.states:
            self.states[-1].handle_events(events)

    def update(self, dt):
        if self.states:
            self.states[-1].update(dt)

    def draw(self, screen):
        if self.states:
            self.states[-1].draw(screen)
