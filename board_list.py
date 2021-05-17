# from IPython.display import clear_output
lists=[" "]*10
lists[0]="#"
def board():
    # clear_output()
    print(lists[1]+"|"+lists[2]+"|"+lists[3])
    print("-----")
    print(lists[4]+"|"+lists[5]+"|"+lists[6])
    print("-----")
    print(lists[7]+"|"+lists[8]+"|"+lists[9])
def win(mark):
    return ((lists[1]==lists[2]==lists[3]==mark)or(lists[4]==lists[5]==lists[6]==mark)or(lists[7]==lists[8]==lists[9]==mark)or(lists[1]==lists[5]==lists[9]==mark)or(lists[3]==lists[5]==lists[7]==mark)or(lists[1]==lists[2]==lists[3]==mark))
def blank(position):
    return lists[position]==" "
def game():
    choose=input("choose 'X' or 'o'").upper()
    if choose=="X":
        first_player=choose
    elif choose=="O":
        second_player=choose
    turn="first"
    while 1:
        if (" "  not in lists):
            print("draw")
            break
        elif turn=="first":
            print("players 1 turn")
            position=int(input("enter your position: "))
            if (blank(position)):
                lists[position]="X"
                board()
            else:
                print("Give correct position")
            if win("X"):
                print("player 1 wins")
                break
            else:
                turn="second"
        elif turn=="second":
            print("players 2 turn")
            position=input("enter your position: ")
            if (blank(position)):
                lists[position]="o"
                board()
            else:
                print("Give correct position")
            if win("o"):
                print("player 2 wins")
                break
            else:
                turn="first"

while 1:
    game()
    replay=input("replay 'y' or 'n'").upper()
    if replay=="y":
        # game()
        continue
    else:
        print("thank you:)")
        break