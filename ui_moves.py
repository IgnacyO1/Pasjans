
def ask_for_move():

    move = input("Enter your move:  ").strip()
    if not move:
        print("Invalid move. Please try again.")
        return ask_for_move()
    return move


