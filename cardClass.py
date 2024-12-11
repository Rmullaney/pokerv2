class Card:
    def __init__(self, value, suit):
        self.value = value
        self.suit = suit

    def print_card(self):
        print(f"{self.value} of {self.suit}s")