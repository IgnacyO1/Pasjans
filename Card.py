
class Card:
    def __init__(self, suit, rank,visible=False):
        self.suit = suit
        self.rank = rank
        self.visible = visible
        

        self._suit = suit
        self._rank = rank

        self.value = self.set_value()
        self._value = self.value
    def color(self):
        if self.suit in ['♠', '♣']:
            return 'black'
        else:
            return 'red'
        #return self._color
    def flip(self):
        self.visible = not self.visible
    
    def is_visible(self):
        return self.visible
    
    def __str__(self):
        return f"{self.rank}{self.suit}" if self.visible else "[X]"
    
    def value_of_card(self):
        return self.value 
    

    def set_value(self):
        dict = {
            'A': 1,
            '2': 2,
            '3': 3,
            '4': 4,
            '5': 5,
            '6': 6,
            '7': 7,
            '8': 8,
            '9': 9,
            '10': 10,
            'J': 11,
            'Q': 12,
            'K': 13
        }

        for card in dict:
            if self.rank == card:
                self.value = dict[card]
                break
        return self.value


    
    