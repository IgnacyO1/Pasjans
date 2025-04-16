from Card import Card
from column import Column
from deck import Deck  
import random 
deck = []

suits = ['♠', '♥', '♦', '♣']

ranks = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']

for suit in suits:
    for rank in ranks:
            deck.append(Card(suit, rank, True))

talia = Deck(deck)
talia.shuffle()

def print_deck(deck):
    for card in deck:
        print(card)

def create_columns():
    columns = [Column() for _ in range(7)]
    return columns
         


columns = create_columns()

def add_cards_to_columns(deck, columns):
    random.shuffle(deck)
    for i in range(7):
        for j in range(i-1):
            temp  = talia.get_card()
            columns[i].a





