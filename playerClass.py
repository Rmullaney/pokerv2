class Player:
    ##only handling cards functionality so far

    def __init__(self):
        self.cards = []

    def add_card(self, card):
        self.cards.append(card)

    def print_hand(self):
        if (len(self.cards) == 0):
            print("error in playerClass#print_hand")
        else:
            self.cards[0].print_card()
            self.cards[1].print_card()

    

    

