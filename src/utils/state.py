class State:
    def __init__(self, state_machine) -> None:
        self.state_machine = state_machine

    def enter(self) -> None:
        """Called when entering this state."""
        pass

    def exit(self) -> None:
        """Called when exiting this state."""
        pass
    
    def handle_events(self, events) -> None:
        """Handle events for this state."""
        pass
    
    def update(self) -> None:
        """Update the state logic."""
        pass

    def draw(self, screen) -> None:
        """Draw the state on the screen."""
        pass
