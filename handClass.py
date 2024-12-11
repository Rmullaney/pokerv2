from cardClass import Card
from deckClass import Deck
from playerClass import Player

class Hand:
    def __init__(self):
        self.deck = Deck()
        self.deck.shuffle()

    ## initial version only with two non-betting, non-folding computers

    def playGame(self):
        self.player1 = Player()
        self.player2 = Player()

        self.player1.add_card(self.deck.deal_card())
        self.player2.add_card(self.deck.deal_card())
        self.player1.add_card(self.deck.deal_card())
        self.player2.add_card(self.deck.deal_card())

        print("Player 1:\n")
        self.player1.print_hand()
        print()
        print("Player 2:\n")
        self.player2.print_hand()

def main():
    hand = Hand()
    hand.playGame()

main()






