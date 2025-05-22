import random
from Card import Card
from deck import Deck

class Column:
    """
    Represents a standard column of cards in a card game.
    Provides basic operations for managing a stack of cards.
    """
    def __init__(self):
        """Initialize an empty column of cards."""
        self.cards = []  # Lista kart w kolumnie
    
    def add_card(self, card):
        """
        Add a card to the top of the column.
        
        Args:
            card: The card to add to the column.
        """
        self.cards.append(card)
    
    def remove_top_card(self):
        """
        Remove and return the card from the top of the column.
        
        Returns:
            The top card if the column is not empty, None otherwise.
        """
        if self.get_length() > 0:
            return self.cards.pop()
        return None
    
    def get_top_card(self):
        """
        Return the top card without removing it from the column.
        
        Returns:
            The top card if the column is not empty, None otherwise.
        """
        if self.get_length() > 0:
            return self.cards[-1]
        return None
    
    def get_length(self):
        """
        Return the number of cards in the column.
        
        Returns:
            int: The number of cards in the column.
        """
        return len(self.cards)
    
    def is_empty(self):
        """
        Check if the column is empty.
        
        Returns:
            bool: True if the column is empty, False otherwise.
        """
        return len(self.cards) == 0
    
    def get_cards(self):
        """
        Return all cards in the column.
        
        Returns:
            list: All cards in the column.
        """
        return self.cards
    
    def __str__(self):
        """
        Return a string representation of the column.
        
        Returns:
            str: A string showing all cards in the column.
        """
        return ' '.join(str(card) for card in self.cards)
    
    def get_random_card(self):
        """
        Return a random card from the column without removing it.
        
        Returns:
            A random card if the column is not empty, None otherwise.
        """
        if self.get_length() > 0:
            return random.choice(self.cards)
        return None
    

class Final_Column:
    """
    Represents a final column for a specific suit in card games like solitaire.
    Cards are typically stacked in order from Ace to King of the same suit.
    """
    def __init__(self, suit):
        """
        Initialize a final column for a specific suit.
        
        Args:
            suit: The suit of cards for this column.
        """
        self.cards = []
        self.suit = suit
        self._suit = suit

    def add_card(self, card):
        """
        Add a card to the top of the final column.
        
        Args:
            card: The card to add to the column.
        """
        self.cards.append(card)
        
    def show_cards(self):
        """
        Show the top card of the final column or a placeholder if empty.
        
        Returns:
            str: The top card or "[X]" if the column is empty.
        """
        if self.cards != []:
            return self.cards[-1]
        else:
            return str("[X]")
        
    def top_card(self):
        """
        Get the top card of the final column without removing it.
        
        Returns:
            The top card if the column is not empty, None otherwise.
        """
        if len(self.cards) == 0:
            return None
        return self.cards[-1]
                  

class Draw_Column:
    """
    Represents the draw/stock pile in solitaire-like card games.
    Manages cards that can be drawn and recycled during gameplay.
    """
    def __init__(self, cards: list):
        """
        Initialize the draw column with a list of cards.
        
        Args:
            cards (list): List of cards remaining after dealing to columns.
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
        Draw the next card from the deck.
        Does NOT automatically reshuffle discarded cards when deck is empty.
        
        Returns:
            Card: The newly drawn card or None if no cards are available.
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
        Return the currently visible card without drawing a new one.
        
        Returns:
            Card: The current card or None if there isn't one.
        """
        return self.current_card
    
    def remove_card(self):
        """
        Remove and return the current card (e.g., when the player uses it).
        
        Returns:
            Card: The removed card or None if there is no current card.
        """
        if self.current_card is None:
            return None
        
        card = self.current_card
        self.current_card = None
        return card
    
    def skip_card(self):
        """
        Move the current card to the discard pile and draw a new one.
        
        Returns:
            Card: The newly drawn card or None if no cards are available.
        """
        if self.current_card is not None:
            self.drawn_cards.append(self.current_card)
            self.current_card = None
        
        return self.next_card()
    
    def reshuffle(self):
        """
        Shuffle the discarded cards and move them back to the draw pile.
        """
        import random
        if len(self.drawn_cards) > 0:
            random.shuffle(self.drawn_cards)
            self.cards = self.drawn_cards
            self.drawn_cards = []
    
    def is_empty(self):
        """
        Check if both the draw pile and discard pile are empty.
        
        Returns:
            bool: True if there are no cards left, False otherwise.
        """
        return len(self.cards) == 0 and len(self.drawn_cards) == 0 and self.current_card is None
    
    def get_count(self):
        """
        Return the total number of cards in the draw pile and discard pile.
        
        Returns:
            int: The total number of cards.
        """
        count = len(self.cards) + len(self.drawn_cards)
        if self.current_card is not None:
            count += 1
        return count
    
    def remove_first_card(self):
        """
        Remove and return the first card from the draw pile.
        
        Returns:
            Card: The first card from the draw pile or None if it's empty.
        """
        if len(self.cards) > 0:
            return self.cards.pop(0)
        return None
    
    def __str__(self):
        """
        Return a string representation of the current state of the draw pile.
        
        Returns:
            str: A description of the draw pile.
        """
        if self.current_card is not None:
            current = str(self.current_card)
        else:
            current = "[brak]"
            
        return f"Karta: {current} | Pozostało: {len(self.cards)} | Odrzucone: {len(self.drawn_cards)}"



