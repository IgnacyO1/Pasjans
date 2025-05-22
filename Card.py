class Card:
    """
    Represents a playing card with a suit, rank, and visibility state.
    
    Attributes:
        suit (str): The card suit symbol ('♠', '♥', '♦', '♣')
        rank (str): The card rank ('A', '2'-'10', 'J', 'Q', 'K')
        visible (bool): Whether the card is face up (visible) or face down
        value (int): Numerical value of the card (1-13)
    """
    def __init__(self, suit, rank, visible=False):
        """
        Initialize a new Card.
        
        Args:
            suit (str): The card suit symbol ('♠', '♥', '♦', '♣')
            rank (str): The card rank ('A', '2'-'10', 'J', 'Q', 'K')
            visible (bool, optional): Initial visibility state. Defaults to False.
        """
        self.suit = suit
        self.rank = rank
        self.visible = visible
        self.value = self.set_value()

    def set_value(self):
        """
        Calculate and return the numerical value of the card based on its rank.
        
        Returns:
            int: The card's value (1-13)
        """
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
                temp_value = dict[card]
                break
        return temp_value

    def color(self):
        """
        Determine the card's color based on its suit.
        
        Returns:
            str: 'black' for spades and clubs, 'red' for hearts and diamonds
        """
        if self.suit in ['♠', '♣']:
            return 'black'
        else:
            return 'red'

    def flip(self):
        """Toggle the visibility state of the card."""
        self.visible = not self.visible
    
    def is_visible(self):
        """
        Check if the card is face up.
        
        Returns:
            bool: True if the card is visible, False otherwise
        """
        return self.visible
    
    def __str__(self):
        """
        Get string representation of the card.
        
        Returns:
            str: The rank and suit if visible, otherwise '[X]'
        """
        return f"{self.rank}{self.suit}" if self.visible else "[X]"



