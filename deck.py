class Deck:
    def __init__(self, cards):
        self.cards = cards
        self.current_card_index = 0

    def shuffle(self):
        import random
        random.shuffle(self.cards)

    def get_card(self):
        if self.cards != []:
            card = self.cards[-1]
            self.cards.pop()
            return card
        else:
            print("Brak kart w talii.")
            return None
    def show_card(self):
        temp = self.cards[-1]
        temp.flip()
        return temp
        #return self.cards[-1]