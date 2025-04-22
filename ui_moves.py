
def ask_for_move():

    move = input("Enter your move:  ").strip()
    if not move:
        print("Invalid move. Please try again.")
        return ask_for_move()
    return move


def proces_move(move):
    ''' on tylko określa co to jest za ruch, nie wykonuje go nie sprawdza czy jest poprawny'''

    move = move.lower()
    if move == "next":
        return "next" #Draw cards next card i tyle nic wiecej 
    
    if move.startswith("move"):
        move_parts = move.split()

        if len(move_parts) == 3:
            source = move_parts[1]
            destination = move_parts[2]


            if source in ["c1", "c2", "c3", "c4", "c5", "c6", "c7"] and destination in ["f1", "f2", "f3", "f4"]:
                #call a engine function with source and destination
                return f"Move from {source} to {destination}"
            
            if source in ["c1", "c2", "c3", "c4", "c5", "c6", "c7"] and destination == "final":
                #call a engine function with source and destination
                return f"Move from {source} to final"
                
            if source in ["draw"] and destination in ["c1", "c2", "c3", "c4", "c5", "c6", "c7"]:
                #call a engine function with source and destination
                return f"Move from {source} to {destination}"
    