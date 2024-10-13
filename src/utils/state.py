class State:
    def __init__(self, state_machine):
        self.state_machine = state_machine

    def enter(self):
        """Called when entering this state."""
        pass

    def exit(self):
        """Called when exiting this state."""
        pass
    
    def handle_events(self, events):
        """Handle events for this state."""
        pass
    
    def update(self):
        """Update the state logic."""
        pass

    def draw(self, screen):
        """Draw the state on the screen."""
        pass
