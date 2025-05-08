from Card import Card
from column import Column, Final_Column



def column_to_column(first_column, second_column):
    """Przenosi karty z jednej kolumny do drugiej."""
    #first column to jest skąd bierzemy karty, second column to jest dokąd je przenosimy

    if first_column.is_empty():
        return False
    
    if first_column not in [1,2,3,4,5,6,7] or second_column not in [1,2,3,4,5,6,7]:
        return False
    card_first_column = first_column.get_top_card()
    card_second_column = second_column.get_top_card()

    if second_column.is_empty() and card_first_column.rank != 'K':
        return False

    card1 = card_first_column
    card2 = card_second_column

    if card1 == None or card2 == None:
        return False
    if card1.color() == card2.color():
        return False
    
    if card1.value() != card2.value() + 1:
        return False
    return True

def column_to_final(first_column: int, final_columns: list) -> bool:
    card_suit = first_column.get_top_card().suit
    card = first_column.get_top_card()
    where_column = None
    for column in final_columns:
        if column.suit() == card_suit:
            where_column = column
            break
    if where_column is None:
        return False
    
    card_fc = where_column.top_card()
    if card_fc == None:
        return False 
    
    if card_fc.value() + 1 != card.value():
        return False
    
    if card_suit != card_fc.suit:
        return False
    return True
        