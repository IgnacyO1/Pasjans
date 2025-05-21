import random
from Card import Card
from deck import Deck
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
        

    def top_card(self):
        if len(self.cards) == 0:
            return None
        return self.cards[-1]
                  


class Draw_Column:
    def __init__(self, cards: list):
        """
        Inicjalizuje kolumnę kart do dobierania w grze pasjans.
        
        Args:
            cards (list): Lista kart pozostałych po rozdaniu do kolumn.
        """
        self.cards = cards.copy()  # lista kart wolnych do dobierania
        self.drawn_cards = []  # lista kart skipniętych/odrzuconych
        self.current_card = None  # aktualnie widoczna karta
        
        # Ustaw pierwszą kartę przy inicjalizacji
        if self.cards and len(self.cards) > 0:
            temp = self.cards.pop(0)
            if not temp.visible:
                temp.flip()
            self.current_card = temp
        

    def next_card(self):
        """
        Dobiera następną kartę z talii.
        Jeśli talia jest pusta, NIE tasuje odrzuconych kart automatycznie.
        
        Returns:
            Card: Aktualnie dobrana karta lub None, jeśli nie ma kart.
        """
        # Move current card to drawn cards if it exists
        if self.current_card is not None:
            self.drawn_cards.append(self.current_card)
        
        # Check if there are any cards left in the deck
        if len(self.cards) == 0:
            self.current_card = None
            return None
        
        # Pobierz kartę z wierzchu talii
        self.current_card = self.cards.pop(0)
        
        # Odwróć kartę (face up)
        if not self.current_card.visible:
            self.current_card.flip()
            
        return self.current_card
    
    def get_current_card(self):
        """
        Zwraca aktualnie widoczną kartę bez dobierania nowej.
        
        Returns:
            Card: Aktualna karta lub None, jeśli nie ma żadnej.
        """
        return self.current_card
    
    def remove_card(self):
        """
        Usuwa i zwraca aktualną kartę (np. gdy gracz użyje karty).
        
        Returns:
            Card: Usunięta karta lub None, jeśli nie ma aktualnej karty.
        """
        if self.current_card is None:
            return None
        
        card = self.current_card
        self.current_card = None
        return card
    
    def skip_card(self):
        """
        Przenosi aktualną kartę do odrzuconych i dobiera nową.
        
        Returns:
            Card: Nowo dobrana karta lub None, jeśli nie ma kart.
        """
        if self.current_card is not None:
            self.drawn_cards.append(self.current_card)
            self.current_card = None
        
        return self.next_card()
    
    def reshuffle(self):
        """
        Tasuje odrzucone karty i przenosi je z powrotem do talii.
        """
        import random
        if len(self.drawn_cards) > 0:
            random.shuffle(self.drawn_cards)
            self.cards = self.drawn_cards
            self.drawn_cards = []
    
    def is_empty(self):
        """
        Sprawdza, czy talia i odrzucone karty są puste.
        
        Returns:
            bool: True, jeśli nie ma żadnych kart, False w przeciwnym razie.
        """
        return len(self.cards) == 0 and len(self.drawn_cards) == 0 and self.current_card is None
    
    def get_count(self):
        """
        Zwraca łączną liczbę kart w talii i odrzuconych.
        
        Returns:
            int: Liczba kart.
        """
        count = len(self.cards) + len(self.drawn_cards)
        if self.current_card is not None:
            count += 1
        return count
    
    def remove_first_card(self):
        """
        Usuwa i zwraca pierwszą kartę z talii.
        
        Returns:
            Card: Pierwsza karta z talii lub None, jeśli talia jest pusta.
        """
        if len(self.cards) > 0:
            return self.cards.pop(0)
        return None
    
    def __str__(self):
        """
        Zwraca reprezentację tekstową aktualnego stanu talii.
        
        Returns:
            str: Opis talii.
        """
        if self.current_card is not None:
            current = str(self.current_card)
        else:
            current = "[brak]"
            
        return f"Karta: {current} | Pozostało: {len(self.cards)} | Odrzucone: {len(self.drawn_cards)}"



