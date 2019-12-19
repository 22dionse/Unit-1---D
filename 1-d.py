#!/usr/bin/env/python3

# These print statements are going to act as visible indicators as if some-
# -one has taken a turn putting down their mark on the board.
def show():
    print("===============================")
    print("+---+---+---+")
    print("|",board[0],"|",board[1],"|",board[2],"|")
    print("+---+---+---+")
    print("|",board[3],"|",board[4],"|",board[5],"|")
    print("+---+---+---+")
    print("|",board[6],"|",board[7],"|",board[8],"|")
    print("+---+---+---+")
    
    # This will check if the space you chose is a valid space
def check(i):
    if move > 8:
        print("ERROR: Invalid space")
        if xnum == 1:
            del board[i]
            board.insert(i,"X")



# This is going to calculate all of the moves from x/o
def x_move(i):
    if board[i] == "X" or board[i] == "O":
        print("===============================")
        print("ERROR: Spot already taken!")
        print("===============================")
    else:
        del board[i]
        board.insert(i,"X")
def o_move(i):
    if board[i] == "X" or board[i] == "O":
        print("===============================")
        print("ERROR: Spot already taken!")
        print("===============================")
    else:
        del board[i]
        board.insert(i,"O")



# This is going to show the playble board
board = [0,1,2,
         3,4,5,
         6,7,8]
                
# This is going to show all possible winning combonations for Tic Tac Toe 
winning_comb = [[0,1,2],[3,4,5],[6,7,8],
                [0,3,6],[1,4,7],[2,5,8],
                [0,4,8],[2,4,6]]
                


# This will start the game
while True:
    turn_num = 1
    board = [0,1,2,3,4,5,6,7,8]
    print("===============================")
    print("Welcome to Tic-Tac-Toe")
    
    while True:
        for list in winning_comb:
            xnum = 0
            onum = 0
            for num in list:
                if board[num] == "X":
                    xnum += 1
                elif board[num] == "O":
                    onum += 1
                else:
                    pass
            if xnum == 3 or onum == 3:
                break
        if xnum == 3 or onum == 3:
            break

        #This will tell who's turn it is
        show()
        if turn_num % 2 == 1:
            print()
            print("X's turn")
            print()
        else:
            print()
            print("O's turn")
            print()
        
        # This will tell the possible spaces
        move = int(input("Choose a space. "))
        if move < 0 or move > 8:
            print("===============================")
            print("ERROR: Invalid space")
            continue
        else:
            if turn_num % 2 == 1:
                x_move(move)
            else:
                o_move(move)
            turn_num += 1
    if xnum == 3:
        show()
        print()
        print("X Wins!")
        print()
        print("Game over!")
        break
    elif onum == 3:
        show()
        print()
        print("O Wins!")
        print()
        print("Game over!")
        break
    else:
        show()
        print()
        print("Draw!")
        print()
        print("Game over!")
        break




                                                    