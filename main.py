import enviroment
import ui_moves
import column
import engine
deck, columns, final_columns = enviroment.setup_game()


#prining 
enviroment.print_game_state(columns, final_columns,deck)


print("-" * 40)

move = ui_moves.ask_for_move()
procesed_move = ui_moves.proces_move(move)
a = columns[0]
b = columns[1]



def ui_column_to_column(first_column, second_column):
    #przenosi wisualnie karty z jednej kolumny do drugiej
    #first column to jest skąd bierzemy karty, second column to jest dokąd je przenosimy
    card_first_column = first_column.get_top_card()
    card_second_column = second_column.get_top_card()

    card_second_column.add_card(card_first_column)
    first_column.remove_top_card()     
    




print(engine.column_to_column(a, b))    
#print(move.startswith("test"))

#test = move.split()
#print(test)

