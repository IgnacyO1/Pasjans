from colorama import init, Fore, Style
init(autoreset=True)

#this is file to create the environment
# for the game
# it will create the deck and the columns
# and the talia

from Card import Card
from column import Column, Final_Column, Draw_Column    
from deck import Deck 

import random 

suits = ['♠', '♥', '♦', '♣']
ranks = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']

def create_deck():
    """
    Create a standard deck of 52 playing cards.

    Returns:
        Deck: A deck object containing all 52 cards.
    """
    list_of_cards = []
    for suit in suits:
        for rank in ranks:
                list_of_cards.append(Card(suit, rank, False))

    deck = Deck(list_of_cards)
    return deck

def print_deck(deck):
    """
    Print all cards in the deck with their value, color and rank.

    Args:
        deck (Deck): The deck to print.
    """
    for card in deck.cards:
        card.flip()  # Flip the card if needed
        print(f"{str(card)} - Value: {card.value}, Color: {card.color()}, Rank: {card.rank}")

def create_columns():
    """
    Create 7 empty columns for the game.

    Returns:
        list: A list containing 7 Column objects.
    """
    columns = [Column() for _ in range(7)]
    return columns

def print_columns(columns):
    """
    Print the contents of each column.

    Args:
        columns (list): List of Column objects to print.
    """
    for i, column in enumerate(columns):
        karty = [koloruj_karte(card) for card in column.cards]
        print(f"Column {i+1}: {' '.join(karty)}")

def set_card_in_column(deck, columns):
    """
    Distribute cards from the deck to the columns according to solitaire rules.
    Each column i gets i face-down cards and 1 face-up card on top.

    Args:
        deck (Deck): The deck to take cards from.
        columns (list): List of Column objects to distribute cards to.
    """
    for i in range(random.randint(1, 7)):
        deck.shuffle()
    for i in range(7):
        for j in range(i):
            temp = deck.get_card()
            columns[i].add_card(temp)
        temp = deck.get_card()
        temp.flip()
        columns[i].add_card(temp)

def setup_final_columns():
    """
    Create the four final columns for each suit.

    Returns:
        list: A list containing 4 Final_Column objects, one for each suit.
    """
    final_columns = [Final_Column(suit) for suit in suits]
    return final_columns

def koloruj_suit(suit):
    """
    Zwraca suit w odpowiednim kolorze.
    """
    if suit in ['♥', '♦']:
        return f"{Fore.RED}{suit}{Style.RESET_ALL}"
    else:
        return f"{Fore.BLACK}{suit}{Style.RESET_ALL}"

def print_final_columns(final_columns):
    """
    Print the contents of each final column.

    Args:
        final_columns (list): List of Final_Column objects to print.
    """
    for column in final_columns:
        karty = [koloruj_karte(card) for card in column.cards]
        colored_suit = koloruj_suit(column.suit)
        print(f"Final Column {colored_suit}: {' '.join(karty)}")

def setup_draw_column(deck):
    """
    Create a draw column from the deck.

    Args:
        deck (Deck): The deck to create the draw column from.

    Returns:
        Draw_Column: A Draw_Column object initialized with the deck's cards.
    """
    draw_column = Draw_Column(deck.cards)
    return draw_column

def setup_game():
    """
    Set up the game environment: deck, columns, and final columns.

    Returns:
        tuple: A tuple containing (deck, columns, final_columns, draw_column).
    """
    # Create and shuffle the deck
    deck = create_deck()
    deck.shuffle()

    # Create columns and distribute cards
    columns = create_columns()
    set_card_in_column(deck, columns)

    # Create final columns
    final_columns = setup_final_columns()

    draw_column = setup_draw_column(deck)

    return deck, columns, final_columns, draw_column

def print_game_state(columns, final_columns, deck, draw_column):
    """
    Print the current state of the game: columns, final columns, and drawn cards.

    Args:
        columns (list): List of Column objects.
        final_columns (list): List of Final_Column objects.
        deck (Deck): The current deck.
        draw_column (Draw_Column): The draw column.
    """
    print("Columns:")
    print_columns(columns)

    print("\nFinal Columns:")
    print_final_columns(final_columns)

    print("\nDrawn Cards:")
    current_card = draw_column.get_current_card()
    if current_card:
        print(koloruj_karte(current_card))
    elif len(draw_column.cards) > 0:
        print("No current card. Type 'next' to draw the next card.")
    elif len(draw_column.drawn_cards) > 0:
        print("No cards left in deck. Type 'reshuffle' to mix drawn cards and start drawing again.")
    else:
        print("Empty Column")

def koloruj_karte(card):
    """
    Zwraca string z kartą w odpowiednim kolorze.
    """
    if not hasattr(card, "suit") or not hasattr(card, "rank"):
        return str(card)
    if card.suit in ['♥', '♦']:
        color = Fore.RED
    else:
        color = Fore.BLACK
    return f"{color}{card.rank}{card.suit}{Style.RESET_ALL}"



