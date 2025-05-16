
import engine 

def ask_for_move() -> str:

    move = str(input("Enter your move:  "))
    if not move:
        print("Invalid move. Please try again.")
        return ask_for_move()
    return move


def proces_move(move, columns: list, final_columns: list):
    ''' on tylko określa co to jest za ruch, nie wykonuje go nie sprawdza czy jest poprawny'''
    #przy braku znalezienia poprawnego call do engine lub innych fucnji (quit help new game) callowac na nowo wprowadzenie ruchy
    move = move.lower().split()
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
                return "Work in progress"

            if source[0] == 'c' and int(source[1]) in [1,2,3,4,5,6,7]:

                source_column  = columns[int(source[1])-1]
                print("janek mus jest czarny")
                return engine.column_to_final(source_column,final_columns)
        
        
        
            
    




