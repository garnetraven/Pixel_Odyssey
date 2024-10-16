class StateMachine:
    def __init__(self) -> None:
        self.states = []

    def push(self, state) -> None:
        if self.states:
            self.states[-1].exit() # Exit current state
        self.states.append(state)
        state.enter() # Enter new current state

    def pop(self) -> None:
        if self.states:
            self.states[-1].exit() # Exit current state
            self.states.pop()

        if self.states:
            self.states[-1].enter() # Enter new current state

    def change_state(self, state) -> None:
        """Replace current state with new one"""
        self.pop()
        self.push(state)

    def handle_events(self, events) -> None:
        if self.states:
            self.states[-1].handle_events(events)

    def update(self) -> None:
        if self.states:
            self.states[-1].update()

    def draw(self, screen) -> None:
        if self.states:
            self.states[-1].draw(screen)
