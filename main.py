import enviroment
import ui_moves
import column
import engine
deck, columns, final_columns, draw_column = enviroment.setup_game()

#enviroment.print_deck(deck)
#prining 
enviroment.print_game_state(columns, final_columns,deck, draw_column)


print("-" * 40)
draw_column = column.Draw_Column(deck.cards)
move = ""
while str(move) != "quit": 
    move = ui_moves.ask_for_move()
    procesed_move = ui_moves.proces_move(move, columns,final_columns, draw_column)
    print(procesed_move)  
#print(move.startswith("test"))

#test = move.split()
#print(test)

