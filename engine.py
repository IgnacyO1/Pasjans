from Card import Card
from column import Column, Final_Column


def column_to_column(first_column: Column, second_column: Column) -> bool:
    """
    Check if the top card from the first column can be moved to the second column according to game rules.

    Args:
        first_column (Column): The source column.
        second_column (Column): The target column.

    Returns:
        bool: True if the move is valid, False otherwise.
    """
    
    if first_column.is_empty():
        return False
    
    source_card = first_column.get_top_card()

    if source_card is None or not source_card.is_visible():
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
    if target_card.value == source_card.value + 1:  # Changed condition
           return True 
    else:
        return False
        

def sequence_column_to_column(source_column: Column, target_column: Column, number_card: int):
    """
    Check if a sequence of cards from the source column can be moved to the target column.

    Args:
        source_column (Column): The column from which cards are moved.
        target_column (Column): The column to which cards are moved.
        number_card (int): Number of cards to move.

    Returns:
        bool: True if the move is valid, False otherwise.
    """
    
    source_cards :list = source_column.get_cards()
    target_cards :list = target_column.get_cards()

    if number_card > len(source_cards):
        return False

    #sprawdzić czy kolumny są puste
    if source_column.is_empty():
        return False
    

    #ustalić zakres przenoszenia 
    # sprawdzić czy każda karta jest widoczna 
    # sprawdzić popeawnosc ostatniej kart (liczyć od brzegu stossu)
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
    if target_card.value == last_card.value + 1 :
        return True 
    else:
        return False
    
    return True 

    
        
    
def column_to_final(first_column: Column, final_columns: list) -> bool:
    """
    Check if the top card from the given column can be moved to its corresponding final (foundation) column.

    Args:
        first_column (Column): The source column.
        final_columns (list): List of Final_Column objects.

    Returns:
        bool: True if the move is valid, False otherwise.
    """
    card = first_column.get_top_card()
    card_suit = card.suit
    where_column = None
    for column in final_columns:
        if column.suit == card_suit:
            where_column = column
            break
    if where_column is None:
        return False
    
    card_fc = where_column.top_card()
    if card_fc == None:
        if card.rank == 'A':
            return True
        else:
            return False
    
    if card_fc.value + 1 != card.value:
        return False
    
    if card_suit != card_fc.suit:
        return False
    return True

    '''if target_card is None:
        if source_card.rank == 'A':
            # Usuń kartę z kolumny dobierania
            card = draw_pile.remove_card()
            # Dodaj kartę do kolumny finalnej
            target_column.add_card(card)
            return True
        else:
            return False'''
        



def draw_to_column(draw_pile, target_column: Column) -> bool:
    """
    Check if the current card from the draw pile can be moved to the target column.

    Args:
        draw_pile: Draw_Column object representing the draw pile.
        target_column (Column): The target column.

    Returns:
        bool: True if the move is valid, False otherwise.
    """
    # Sprawdź czy w kolumnie dobierania jest aktualna karta
    source_card = draw_pile.get_current_card()
    
    if source_card is None:
        return False
    
    # Sprawdź czy karta może być przeniesiona na docelową kolumnę
    if target_column.is_empty():
        # Na pustą kolumnę można położyć tylko króla
        if source_card.rank == 'K':
            return True
        else:
            return False
    
    # Pobierz kartę na wierzchu docelowej kolumny
    target_card = target_column.get_top_card()
    #print(f"{str(target_card)} - Value: {target_card.value}, Color: {target_card.color()}, Rank: {target_card.rank}")
    #print(f"{str(source_card)} - Value: {source_card.value}, Color: {source_card.color()}, Rank: {source_card.rank}")
    if target_card is None:
        return False
    
    # Sprawdź kolor (musi być przeciwny)
    if source_card.color() == target_card.color():
        return False
    
    # Sprawdź wartość (karta z draw pile musi być o jeden mniejsza)
    if target_card.value == source_card.value + 1:
        return True
    
    return False

def draw_to_final(draw_pile, final_columns: list) -> bool:
    """
    Check if the current card from the draw pile can be moved to its corresponding final (foundation) column.

    Args:
        draw_pile: Draw_Column object representing the draw pile.
        final_columns (list): List of Final_Column objects.

    Returns:
        bool: True if the move is valid, False otherwise.
    """
    # Sprawdź czy w kolumnie dobierania jest aktualna karta

    source_card = draw_pile.get_current_card()
    
    if source_card is None:
        return False
    
    # Znajdź odpowiednią kolumnę finalną dla koloru karty
    target_column = None
    for column in final_columns:
        if column.suit == source_card.suit:
            target_column = column
            break
    
    if target_column is None:
        return False
    
    # Pobierz wierzchnią kartę kolumny finalnej
    target_card = target_column.top_card()
    #print(f"{str(target_card)} - Value: {target_card.value}, Color: {target_card.color()}, Rank: {target_card.rank}")
    #print(f"{str(source_card)} - Value: {source_card.value}, Color: {source_card.color()}, Rank: {source_card.rank}")
    # Jeśli kolumna finalna jest pusta, można położyć tylko asa
    if target_card is None:
        if source_card.rank == 'A':
            return True
        else:
            return False
    
    # Sprawdź czy wartość karty jest o jeden większa od wierzchniej karty kolumny finalnej
    if source_card.value != target_card.value + 1:
        return False
    
    return True 


def card_to_final(card: Card, final_columns: list) -> bool:
    """
    Check if the given card can be moved to its corresponding final (foundation) column.

    Args:
        card (Card): The card to move.
        final_columns (list): List of Final_Column objects.

    Returns:
        bool: True if the move is valid, False otherwise.
    """
    # Znajdź odpowiednią kolumnę finalną dla koloru karty
    target_column = None
    for column in final_columns:
        if column.suit == card.suit:
            target_column = column
            break
    
    if target_column is None:
        return False
    
    # Pobierz wierzchnią kartę kolumny finalnej
    target_card = target_column.top_card()
    
    # Jeśli kolumna finalna jest pusta, można położyć tylko asa
    if target_card is None:
        if card.rank == 'A':
            return True
        else:
            return False
    
    # Sprawdź czy wartość karty jest o jeden większa od wierzchniej karty kolumny finalnej
    if card.value != target_card.value + 1:
        return False
    
    return True

def card_to_column(card: Card, target_column: Column) -> bool:
    """
    Check if the given card can be moved to the target column.

    Args:
        card (Card): The card to move.
        target_column (Column): The target column.

    Returns:
        bool: True if the move is valid, False otherwise.
    """
    # Sprawdź czy kolumna jest pusta
    if target_column.is_empty():
        # Na pustą kolumnę można położyć tylko króla
        if card.rank == 'K':
            return True
        else:
            return False
    
    # Pobierz wierzchnią kartę docelowej kolumny
    target_card = target_column.get_top_card()
    
    if target_card is None:
        return False
    
    # Sprawdź kolor (musi być przeciwny)
    if card.color() == target_card.color():
        return False
    
    # Sprawdź wartość (karta z draw pile musi być o jeden mniejsza)
    if target_card.value == card.value + 1:
        return True
    
    return False