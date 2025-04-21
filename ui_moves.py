
def ask_for_move():

    move = input("Enter your move:  ").strip()
    if not move:
        print("Invalid move. Please try again.")
        return ask_for_move()
    return move


def proces_move(move):
    ''' on tylko określa co to jest za ruch, nie wykonuje go nie sprawdza czy jest poprawny'''

    if move == "next":
        return "next" #Draw cards next card i tyle nic wiecej 
    
    if move.startswith("move"):
        return proces_move(move)
    