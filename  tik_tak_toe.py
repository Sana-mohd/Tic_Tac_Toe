import random
def display_board(board):
    print(board[1]+"|"+board[2]+"|"+board[3])
    print("-----")
    print(board[4]+"|"+board[5]+"|"+board[6])
    print("-----")
    print(board[7]+"|"+board[8]+"|"+board[9])
    print()
def player_input():
    marker=" "
    while not(marker=="X" or marker=="O"):
        marker=input("player 1: Do you want to be x or o: ").upper()
        if marker=="X":
            return ("x","o")
        else:
            return ("o","x")

def place_marker(board,marker,position):
    board[position]=marker

def win_check(board,mark):
    return ((board[1]==board[2]==board[3]==mark)or(board[4]==board[5]==board[6]==mark)or(board[7]==board[8]==board[9]==mark)or(board[1]==board[4]==board[6]==mark)or(board[2]==board[5]==board[8]==mark)or(board[3]==board[6]==board[9]==mark)or(board[1]==board[5]==board[9]==mark)or(board[3]==board[5]==board[7]==mark))

def choose_first():
    if random.randint(0,1)==0:
        return "computer"
    else:
        return "player 1"
def space_check(board,position):
    return board[position]==" "
def full_board_check(board):
    for i in range(1,10):
        if space_check(board,i):
            return False
    return True

def player_choice(board):
    if turn=="computer":
        position=random.randint(1,9)
        while not space_check(board,position):
            positon=random.randint(1,9)
    else:
        position=" "
        while position not in "1 2 3 4 5 6 7 8 9".split() or not space_check(board,int(position)):
            position=input("choose your next position(1-9): ")
    return int(position)

def replay():
    return input("do you want to play again? enter yes or no: ").lower().startswith("y")
print("welcome to Tic Tac Toe")

while True:
    theBoard=[" "]*10
    player1_marker,player2_marker=player_input()
    turn=choose_first()
    print(turn+"will go first")
    game_on=True
    while game_on:
        if turn=="player 1":
            display_board(theBoard)
            position=player_choice(theBoard)
            place_marker(theBoard, player1_marker, position)
            if win_check(theBoard,player1_marker):
                display_board(theBoard)
                print("congratulations  won the game!")
                game_on=False
            else:
                if full_board_check(theBoard):
                    display_board((theBoard))
                    print("the game is draw")
                    break
                else:
                    turn="computer"
        else:
            turn=="player 2"
            display_board(theBoard)
            position=player_choice(theBoard)
            place_marker(theBoard, player2_marker, position)
            if win_check(theBoard,player2_marker):
                display_board(theBoard)
                print("congratulations computer has won the game!")
                game_on=False
            else:
                if full_board_check(theBoard):
                    display_board((theBoard))
                    print("the game is tie")
                    break
                else:
                    turn="player 1"
    if not replay():
        break