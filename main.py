import enviroment
import ui_moves
import column
import engine

deck, columns, final_columns, draw_column = enviroment.setup_game()

#enviroment.print_deck(deck)
#prining 
enviroment.print_game_state(columns, final_columns, deck, draw_column)

print("-" * 40)
# Remove this line to avoid reinitializing draw_column:
# draw_column = column.Draw_Column(deck.cards)
move = ""
while str(move) != "quit": 
    move = ui_moves.ask_for_move()
    
    # Process the move
    processed_move = ui_moves.proces_move(move, columns, final_columns, draw_column)
    
    # Execute the move if valid
    result = ui_moves.execute_move(processed_move, move.lower().split(), columns, final_columns, draw_column)
    
    if result == "quit":
        break
    elif result == "restart":
        print("Starting a new game...")
        deck, columns, final_columns, draw_column = enviroment.setup_game()
        enviroment.print_game_state(columns, final_columns, deck, draw_column)
        continue
    
    print(result)
    
    # Update the game state display
    if processed_move is True or processed_move == "next" or processed_move == "reshuffle":
        enviroment.print_game_state(columns, final_columns, deck, draw_column)