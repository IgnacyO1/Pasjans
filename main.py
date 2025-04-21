import enviroment
import ui_moves
import column
deck, columns, final_columns = enviroment.setup_game()


#prining 
enviroment.print_game_state(columns, final_columns,deck)


print("-" * 40)

move = ui_moves.ask_for_move()

#print(move.startswith("test"))

test = move.split()
print(test)