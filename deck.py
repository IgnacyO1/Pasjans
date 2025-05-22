class Deck:
    """
    Represents a deck of cards in a card game.
    
    This class provides functionality for managing a collection of cards,
    including shuffling, drawing cards, and viewing the top card.
    """
    def __init__(self, cards):
        """
        Initialize a deck with a list of cards.
        
        Args:
            cards: A list of Card objects to form the deck.
        """
        self.cards = cards
        

    def shuffle(self):
        """
        Randomly shuffle all cards in the deck.
        
        This method uses Python's random.shuffle to randomize card order.
        """
        import random
        random.shuffle(self.cards)

    def get_card(self):
        """
        Remove and return the top card from the deck.
        
        Returns:
            Card: The top card of the deck if available, None otherwise.
        """
        if self.cards != []:
            card = self.cards[-1]
            self.cards.pop()
            return card
        else:
            print("Brak kart w talii.")
            return None
            
    def show_card(self):
        """
        Show the top card of the deck without removing it.
        
        If the card is not visible (face down), it will be flipped face up.
        
        Returns:
            Card: The top card of the deck.
        """
        temp = self.cards[-1]
        if temp.is_visible() == False:
            temp.flip()
        return temp
    
    def get_length(self):
        """
        Return the number of cards in the deck.
        
        Returns:
            int: The number of cards currently in the deck.
        """
        return len(self.cards)


