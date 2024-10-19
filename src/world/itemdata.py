from entities.tile import *

class Item:
    def __init__(self, name: str = "default", quantity: int = 0) -> None:
        self.name = name
        self.quantity = quantity
        self.target_group = None

    def use(self, *args, **kwargs):
        pass

    def pick(self, amount = 1):
        self.quantity += amount

    def drop(self, amount = 1):
        amt = amount
        self.quantity -= amount

        if self.quantity < 0:
            amt -= abs(self.quantity)
            self.quantity = 0

        return amt

    def empty(self):
        self.name = "default"
        self.quantity = 0

    def __str__(self) -> str:
        return f"Name: {self.name}, Quantity: {self.quantity}"
