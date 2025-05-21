import engine 

def ask_for_move() -> str:

    move = str(input("Enter your move:  "))
    if not move:
        print("Invalid move. Please try again.")
        return ask_for_move()
    return move

#drawn column :) 
def proces_move(move, columns: list, final_columns: list, draw_column):
    ''' on tylko określa co to jest za ruch, nie wykonuje go nie sprawdza czy jest poprawny'''
    #przy braku znalezienia poprawnego call do engine lub innych fucnji (quit help new game) callowac na nowo wprowadzenie ruchy
    move = move.lower().split()
    
    # Handle single-word commands
    if len(move) == 1:
        if move[0] == "quit":
            return "quit"
        elif move[0] == "help":
            return "help"
        elif move[0] == "next":
            return "next"
        elif move[0] == "reshuffle":
            return "reshuffle"
        elif move[0] == "restart" or move[0] == "new":
            return "restart"
    
    #print(move, len(move))
    if len(move) == 3:
        source = move[1]
        target = move[2]

        if move[0] != "move":
            return False 
        #print(source[1], target[1])
        #print(int(source[1]) in [1,2,3,4,5,6,7], int(target[1]) not in [1,2,3,4,5,6,7], source[0] != 'c' or target[0] != 'c')


        
        if int(source[1]) not in [1,2,3,4,5,6,7]:
            return False
        
        if int(target[1]) not in [1,2,3,4,5,6,7]:
            return False
        if source[0] != 'c' or target[0] != 'c':
            return False
        source_column = int(source[1])
        target_column = int(target[1])

        #print(source_column, target_column)

        source_column = columns[source_column - 1]
        target_column = columns[target_column - 1]

        #print(source_column, target_column)

        return engine.column_to_column(source_column, target_column)
    
    if len(move) == 2:
        source = move[0]
        target = move[1]

        if str(target) == "final":
            if source == "draw":
                #return engine.card_to_final(draw_column.get_current_card(), final_columns)
                return engine.draw_to_final(draw_column, final_columns)

            if source[0] == 'c' and int(source[1]) in [1,2,3,4,5,6,7]:

                source_column  = columns[int(source[1])-1]
                #print("janek mus jest czarny")

                return engine.column_to_final(source_column,final_columns)




        if str(source) == "draw":
            if target[0] == 'c' and int(target[1]) in [1,2,3,4,5,6,7]:
                target_column = columns[int(target[1])-1]
                #return engine.card_to_column(draw_column.get_current_card(), target_column)
                return engine.draw_to_column(draw_column , target_column)
            
             
            
        
    if len(move) == 4:
        source = move[1]
        target = move[2]
        number_card = int(move[3])

        if int(source[1]) not in [1,2,3,4,5,6,7]:
            return False
        
        if int(target[1]) not in [1,2,3,4,5,6,7]:
            return False
        if source[0] != 'c' or target[0] != 'c':
            return False
        source_column = int(source[1])
        target_column = int(target[1])

        #print(source_column, target_column)

        source_column = columns[source_column - 1]
        target_column = columns[target_column - 1]

        return engine.sequence_column_to_column(source_column, target_column, number_card)
    
    return "skibidi"

def execute_move(move_result, move, columns, final_columns, draw_column):
    """
    Execute the actual card movement after validation.
    
    Args:
        move_result: Result from proces_move (True if move is valid)
        move: Original move command split into words
        columns: Game columns
        final_columns: Foundation piles
        draw_column: Draw pile
    
    Returns:
        str: Message describing what happened
    """
    if move_result == "quit":
        return "quit"
    elif move_result == "help":
        return display_help()
    elif move_result == "next":
        card = draw_column.next_card()
        if card:
            return f"Drew next card: {card}"
        else:
            if len(draw_column.drawn_cards) > 0:
                return "No more cards in deck. Type 'reshuffle' to mix drawn cards and start drawing again."
            else:
                return "No cards available in the draw pile."
    elif move_result == "reshuffle":
        if len(draw_column.drawn_cards) > 0:
            draw_column.reshuffle()
            card = draw_column.next_card()
            if card:
                return f"Reshuffled drawn cards and drew: {card}"
            else:
                return "Reshuffled but no cards available"
        else:
            return "No drawn cards to reshuffle"
    elif move_result == "restart":
        return "restart"
        
    # Rest of the function remains the same...
    elif move_result is True:
        # Column to column move
        if len(move) == 3 and move[0] == "move":
            source_idx = int(move[1][1]) 
            target_idx = int(move[2][1])
            source_column = columns[source_idx - 1]
            target_column = columns[target_idx - 1]
            
            card = source_column.remove_top_card()
            target_column.add_card(card)
            
            # Reveal the new top card if needed
            if not source_column.is_empty():
                new_top = source_column.get_top_card()
                if not new_top.visible:
                    new_top.flip()
            
            return f"Moved {card} from column {source_idx} to column {target_idx}"
            
        # Column to final foundation move
        elif len(move) == 2 and move[1] == "final" and move[0][0] == "c":
            source_idx = int(move[0][1])
            source_column = columns[source_idx - 1]
            
            card = source_column.remove_top_card()
            # Find the matching foundation pile
            for fc in final_columns:
                if fc.suit == card.suit:
                    fc.add_card(card)
                    break
            
            # Reveal the new top card if needed
            if not source_column.is_empty():
                new_top = source_column.get_top_card()
                if not new_top.visible:
                    new_top.flip()
                    
            return f"Moved {card} from column {source_idx} to final {card.suit}"
            
        # Draw to final foundation move
        elif len(move) == 2 and move[0] == "draw" and move[1] == "final":
            card = draw_column.remove_card()
            # Find the matching foundation pile
            for fc in final_columns:
                if fc.suit == card.suit:
                    fc.add_card(card)
                    break
                    
            # Draw next card if available
            if draw_column.is_empty():
                draw_column.next_card()
                
            return f"Moved {card} from draw pile to final {card.suit}"
            
        # Draw to column move
        elif len(move) == 2 and move[0] == "draw" and move[1][0] == "c":
            target_idx = int(move[1][1])
            target_column = columns[target_idx - 1]
            
            card = draw_column.remove_card()
            target_column.add_card(card)
            
            # Draw next card if available
            if draw_column.is_empty():
                draw_column.next_card()
                
            return f"Moved {card} from draw pile to column {target_idx}"
            
        # Sequence of cards from one column to another
        elif len(move) == 4 and move[0] == "move":
            source_idx = int(move[1][1])
            target_idx = int(move[2][1])
            num_cards = int(move[3])
            source_column = columns[source_idx - 1]
            target_column = columns[target_idx - 1]
            
            # Get the cards to move
            cards_to_move = []
            for _ in range(num_cards):
                cards_to_move.insert(0, source_column.remove_top_card())
                
            # Add them to target
            for card in cards_to_move:
                target_column.add_card(card)
                
            # Reveal the new top card if needed
            if not source_column.is_empty():
                new_top = source_column.get_top_card()
                if not new_top.visible:
                    new_top.flip()
                    
            return f"Moved {num_cards} cards from column {source_idx} to column {target_idx}"
    
    elif move_result == "quit":
        return "quit"
    elif isinstance(move_result, str):
        return move_result
    else:
        return "Invalid move"

def display_help():
    """Display help information about available moves"""
    help_text = """
    Available moves:
    1. move c1 c2 - Move the top card from column 1 to column 2
    2. c1 final - Move the top card from column 1 to its foundation pile
    3. draw c1 - Move the current draw card to column 1
    4. draw final - Move the current draw card to its foundation pile
    5. move c1 c2 3 - Move 3 cards from column 1 to column 2
    6. next - Draw the next card from the draw pile
    7. reshuffle - Reshuffle the drawn cards back into the deck
    8. quit - Exit the game
    9. help - Show this help message
    10. restart - Start a new game
    """
    return help_text












