#this is file to create the environment
# for the game
# it will create the deck and the columns
# and the talia

from Card import Card
from column import Column, Final_Column
from deck import Deck 

import random 
list_of_cards = []

suits = ['♠', '♥', '♦', '♣']

ranks = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']

def crate_deck():
    for suit in suits:
        for rank in ranks:
                list_of_cards.append(Card(suit, rank, False))

    deck = Deck(list_of_cards)
    return deck
deck = crate_deck()

def print_deck(deck):
    for card in deck:
        print(card)

def create_columns():
    columns = [Column() for _ in range(7)]
    return columns

columns = create_columns()      

def print_columns(columns):
    for i, column in enumerate(columns):
        print(f"Column {i+1}: {column}")

'''
print(deck.get_card())

temp = deck.get_card()
temp.flip()
print(temp)

print(temp.suit)'''

def set_card_in_column(deck, columns):
    for i in range(random.randint(1, 7)):
        deck.shuffle()
    for i in range(7):
        for j in range(i):
            temp = deck.get_card()
            columns[i].add_card(temp)
        temp = deck.get_card()
        temp.flip()
        columns[i].add_card(temp)


def setup_final_coliumns():

    final_columns = [Final_Column(suit) for suit in suits]
    return final_columns

final_colums = setup_final_coliumns()

def print_final_columns(final_columns):
    for i, column in enumerate(final_columns):
        print(f"Final Column {column.suit}: {column.show_cards()}")
        #print(f"Final Column {column.suit}{i+1}: {column.show_cards()}")

def main_columns(columns):
    create_columns()
    set_card_in_column(deck, columns)
    
    #print_final_columns(final_columns)
    #print_final_columns(final_columns)
    #print_columns(columns)
main_columns(columns)
print_columns(columns)
print_final_columns(final_colums)


