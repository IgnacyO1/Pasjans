import random
from Card import Card

class Column:
    def __init__(self):
        self.cards = []  # Lista kart w kolumnie
    
    def add_card(self, card):
        """Dodaje kartę na szczyt kolumny."""
        self.cards.append(card)
    
    def remove_top_card(self):
        """Usuwa i zwraca kartę ze szczytu kolumny."""
        if self.get_length() > 0:
            return self.cards.pop()
        return None
    
    def get_top_card(self):
        """Zwraca kartę na szczycie kolumny bez jej usuwania."""
        if self.get_length() > 0:
            return self.cards[-1]
        return None
    
    def get_length(self):
        """Zwraca liczbę kart w kolumnie."""
        return len(self.cards)
    
    def is_empty(self):
        """Sprawdza, czy kolumna jest pusta."""
        return len(self.cards) == 0
    
    def get_cards(self):
        """Zwraca wszystkie karty w kolumnie."""
        return self.cards
    
    def __str__(self):
        """Zwraca reprezentację tekstową kolumny."""
        return ' '.join(str(card) for card in self.cards)\
    
    def get_random_card(self):
        """Zwraca losową kartę z kolumny."""
        if self.get_length() > 0:
            return random.choice(self.cards)
        return None
    



class Final_Column:
    def __init__(self,suit):
        self.cards = []
        self.suit = suit
        self._suit = suit

    def add_card(self, card):
        """Dodaje kartę na szczyt kolumny."""
        self.cards.append(card)
    def show_cards(self):
        if self.cards != []:
            return self.cards[-1]
        else:
            return str("[X]")
                  
 