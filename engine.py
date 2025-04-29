def column_to_column(first_column, second_column):
    """Przenosi karty z jednej kolumny do drugiej."""
    #first column to jest skąd bierzemy karty, second column to jest dokąd je przenosimy
    card_first_column = first_column.get_top_card()
    card_second_column = second_column.get_top_card()

    card1 = card_first_column
    card2 = card_second_column

    if card1 == None or card2 == None:
        return False
    if card1.color() == card2.color():
        return False
    
    if card1.value() != card2.value() + 1:
        return False
    return True

