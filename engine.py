from Card import Card
from column import Column, Final_Column


def column_to_column(first_column: Column, second_column: Column) ->bool:
    
    if first_column.is_empty():
        return False
    
    source_card = first_column.get_top_card()

    if source_card is not None or not source_card.is_visible():
        return False
    
    if second_column.is_empty(): #na pusta kolumnę można dac tylko króla 
        if source_card.rank == 'K':
            return True
        else:
            return False
    target_card = second_column.get_top_card()

    # Nie może być none karta na któtą nakłada się mysi być o jeden wieksza przeciwne kolory 

    #Sprawdzenie czy karta to nie None nie ma takiej szansy bo by były logiczne błedy ale dla pewnośći

    if target_card is None:
        return False 
    
    if target_card.is_visible() == False:
        return False 
    
    #Sprawdzenie kolorów 
    if source_card.color() == target_card.color():
        return False
    
    #Sprawdzenie wartości 

    if source_card.value +1 == target_card.value:
           return True 
    else:
        return False
        

def sequence_column_to_column(source_column: Column, target_column: Column, number_card: int):
    
    source_cards :list = source_column.get_cards()
    target_cards :list = target_column.get_cards()

    if number_card > len(source_cards):
        return False

    #sprawdzić czy kolumny są puste
    if source_column.is_empty():
        return False
    

    #ustalić zakres przenoszenia 
    # sprawdzić czy każda karta jest widoczna 
    # sprawdzić popeawnosc ostatniej kart (liczać od brzegu stossu)
    #kolor 
    #wartość
    #przelecieć po kartach dla pewności 
    try:
        card_to_move :list = source_cards[-number_card:]
    except IndexError:
        return False
    
    for card in card_to_move:
        if card.visible or card is not None:
            continue
        else:
            return False 
        
    for i in range(1, len(card_to_move)):
        if card_to_move[i].color() == card_to_move[i-1].color():
            return False
        

    last_card = source_cards[-number_card] 

    if target_column.is_empty():
        if last_card.rank == 'K':
            return True
        else:
            return False
    target_card = target_column.get_top_card()


     

    if target_card is None:
        return False 
    
    #Sprawdzenie kolorów
    if last_card.color() == target_card.color():
        return False
    
    #Sprawdzenie wartości
    if last_card.value + 1 == target_card.value:
        return True 
    else:
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
        






















'''
def cowlumn_to_column(first_column, second_column):
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
'''