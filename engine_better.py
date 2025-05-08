from Card import Card
from column import Column, Final_Column



def column_to_column(source_column, target_column):
    """
    Przenosi karty z jednej kolumny do drugiej.
    
    Args:
        source_column: Kolumna źródłowa (obiekt Column)
        target_column: Kolumna docelowa (obiekt Column)
        
    Returns:
        bool: True jeśli przeniesienie się udało, False w przeciwnym wypadku
    """
    # Sprawdzenie czy kolumna źródłowa ma karty
    if source_column.is_empty():
        return False
    
    # Pobierz karty ze szczytów obu kolumn
    source_card = source_column.get_top_card()
    
    # Sprawdzenie czy karta źródłowa jest widoczna
    if source_card is None or not source_card.is_visible():
        return False
    
    # Obsługa przypadku pustej kolumny docelowej
    if target_column.is_empty():
        # Na pustą kolumnę można położyć tylko Króla
        if source_card.rank == 'K':
            # Wykonaj ruch
            target_column.add_card(source_column.remove_top_card())
            
            # Odkryj nową kartę na szczycie kolumny źródłowej, jeśli istnieje
            new_top_card = source_column.get_top_card()
            if new_top_card and not new_top_card.is_visible():
                new_top_card.flip()
            return True
        return False
    
    # Kolumna docelowa nie jest pusta
    target_card = target_column.get_top_card()
    
    # Sprawdzenie zasad pasjansa
    if (target_card is not None and
        source_card.color() != target_card.color() and
        source_card.value() + 1 == target_card.value()):
        # Wykonaj ruch
        target_column.add_card(source_column.remove_top_card())
        
        # Odkryj nową kartę na szczycie kolumny źródłowej, jeśli istnieje
        new_top_card = source_column.get_top_card()
        if new_top_card and not new_top_card.is_visible():
            new_top_card.flip()
        return True
    
    return False

def column_to_final(source_column, final_columns_list):
    """
    Próbuje przenieść kartę ze szczytu kolumny źródłowej do 
    odpowiedniej kolumny finalnej.
    
    Args:
        source_column: Kolumna źródłowa (obiekt Column)
        final_columns_list: Lista kolumn finalnych
        
    Returns:
        bool: True jeśli przeniesienie się udało, False w przeciwnym wypadku
    """
    if source_column.is_empty():
        return False
    
    card = source_column.get_top_card()
    
    # Karta musi być widoczna
    if card is None or not card.is_visible():
        return False                    
    
    # Znajdź docelową kolumnę finalną na podstawie koloru karty
    target_column = None
    for column in final_columns_list:
        # Zakładam, że suit jest atrybutem, nie metodą
        if column.suit == card.suit:
            target_column = column
            break
            
    if target_column is None:
        return False
    
    # Pobierz górną kartę z kolumny finalnej
    top_final_card = target_column.top_card()
    
    # Przypadek 1: Kolumna finalna jest pusta - tylko As może być położony
    if top_final_card is None:
        if card.value() == 1:  # wartość Asa to 1
            # Wykonaj ruch
            target_column.add_card(source_column.remove_top_card())
            
            # Odkryj nową górną kartę w kolumnie źródłowej, jeśli istnieje
            new_top_card = source_column.get_top_card()
            if new_top_card and not new_top_card.is_visible():
                new_top_card.flip()
            return True
        return False
    
    # Przypadek 2: Kolumna finalna ma już karty
    # Sprawdź, czy kolory się zgadzają i czy wartość karty jest o 1 większa
    if (card.suit == top_final_card.suit and 
        card.value() == top_final_card.value() + 1):
        # Wykonaj ruch
        target_column.add_card(source_column.remove_top_card())
        
        # Odkryj nową górną kartę w kolumnie źródłowej, jeśli istnieje
        new_top_card = source_column.get_top_card()
        if new_top_card and not new_top_card.is_visible():
            new_top_card.flip()
        return True
    
    return False
