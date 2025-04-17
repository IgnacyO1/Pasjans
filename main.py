import enviroment
import ui_moves
deck, columns, final_columns = enviroment.setup_game()
enviroment.print_game_state(columns, final_columns,deck)

print("-" * 40)

move = ui_moves.ask_for_move()