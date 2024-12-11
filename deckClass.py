from cardClass import Card
import random

class Deck:
    def __init__(self):
        self.array = []
        for i in range(13):
            num = i
            if (num==0):
                num = 'King'
            elif (num==1):
                num = 'Ace'
            elif (num==10):
                num = 'Ten'
            elif (num==11):
                num = 'Jack'
            elif (num==12):
                num = 'Queen'
            elif (num > 1 and num < 10):
                num = str(num)
            self.array.append(Card(num, "Club"))
            self.array.append(Card(num, "Spade"))
            self.array.append(Card(num, "Heart"))
            self.array.append(Card(num, "Diamond"))
    

    def shuffle(self):
        random.shuffle(self.array)

    def deal_card(self):
        card = self.array.pop(0)
        return card
    

