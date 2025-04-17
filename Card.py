
class Card:
    def __init__(self, suit, rank,visible=False):
        self.suit = suit
        self.rank = rank
        self.visible = visible
        self._color = 'black' if suit in ['♠', '♣'] else 'red'

        self._suit = suit
        self._rank = rank

        self.value = None 

    def flip(self):
        self.visible = not self.visible
    
    def is_visible(self):
        return self.visible
    
    def __str__(self):
        return f"{self.rank}{self.suit}" if self.visible else "[X]"
    
    def value_of_card(self):
        return self.value 
    

    
    