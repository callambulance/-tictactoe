import sys
import random

#colors for outputs
class bcolors:
    Blue = "\033[34m"
    LightMagenta = "\033[95m"
    LightYellow  = "\033[93m"
    green='\033[32m'
    LightGreen   = "\033[92m"
    Cyan  = "\033[36m"
    LightCyan = "\033[96m"
    ENDC = '\033[0m'

#combinations for check won    
win_combinations = (('A1', "A2", "A3"), ("B1", "B2", "B3"), ("C1", "C2", "C3"), ("A1", "B1", "C1"), ("A2","B2","C2"), ("A3","B3","C3"), ("A1","B2","C3"), ("C1","B2","A3"))
#to quit game
quit_mode = 'Q'
player="X"
#count moves to check if board is full
count=0

#main def
def tictactoe_game():
    board = {'A1': '.' , 'A2': '.' , 'A3': '.',
            'B1': '.' , 'B2': '.' , 'B3': '.' ,
            'C1': '.' , 'C2': '.' , 'C3': '.' }
    main_menu(board, player, count)  

#def for menu
def main_menu(board, player, count):
    print ("\n")
    print (f"{bcolors.Cyan} Hello, let's play!\n".center(143)) #143 for center
    print(f"You can leave the game any time, just print 'Q'\n".center(143))
    print(f"{bcolors.LightGreen}Write '1' for player vs computer game mode or '2' for 2 players game mode:{bcolors.ENDC}".center(150)) #150 for center
    print("\n")
    player_mode = input("".center(69)) #69 for center
    print("\n")

    while player_mode != '1' and player_mode != '2' and player_mode != quit_mode:
        print(f"{bcolors.LightGreen}Write '1' for player vs computer game mode or '2' for 2 players game mode: {bcolors.ENDC}".center(150))
        print("\n")
        player_mode = input("".center(69))

    if player_mode=='2':
        print_board(board)
        get_move(player_mode, player, board, count)

    elif player_mode=='1':
        print_board(board)
        ai_mode(player, player_mode, board, count)
    
    elif player_mode == quit_mode:
        quit()

def ai_mode(player, player_mode, board, count):
    if player == "X":
        get_ai_move(player_mode, board, count)
        has_won(player_mode, board, player, count) 

    elif player=="O":
        get_move(player_mode, player, board, count)
        has_won(player_mode, board, player, count)
    
#def for move input
def get_move(player_mode, player, board, count):
    if count<9:
        print("\n")
        print(f"{bcolors.LightGreen}Choose a position(A1-C3): {bcolors.ENDC}".center(150))
        print("\n")
        position = input("".center(69)).capitalize()

        if position == quit_mode:
            quit()
        else: 
            mark(player_mode, player, position, board, count)

    else:
        has_won(player_mode, board, player, count)

#def for ai move
def get_ai_move(player_mode, board, count):
    #center spot = B2
    if count<9:
        if board["B2"] == ".":
            board["B2"] = player

        else:
            position = random.choice(list(board.keys()))
            while board[position] != ".":
                position = random.choice(list(board.keys()))
            board[position] = player
            
    else:
        has_won(player_mode, board, player, count)
            
#def to change the cell
def mark(player_mode, player, position, board, count):
    if position in board:
        if board[position] == ".":
            board[position] = player
            has_won(player_mode, board, player, count)
        
            #get_move(player_mode, player, board, count)    
        elif board[position] != ".":
            print("\n")
            print(f"{bcolors.LightYellow}Place is taken, pick another.{bcolors.ENDC}".center(150))
            print("\n")
            get_move(player_mode, player,board, count)

    else:
        print("\n")
        print(f"{bcolors.LightYellow}Select a valid position.{bcolors.ENDC}".center(150))
        print("\n")
        get_move(player_mode, player, board, count)
    
#print board
def print_board(board): 
    print(bcolors.LightCyan+"".center(138)) #138 for center
    print("    1:  2:  3:".center(138))
    print(f"A: {board['A1']} | {board['A2']} | {board['A3']}".center(138))
    print("   ---+---+---".center(138))
    print(f"B: {board['B1']} | {board['B2']} | {board['B3']}".center(138))
    print("   ---+---+---".center(138))
    print(f"C: {board['C1']} | {board['C2']} | {board['C3']}".center(138))
    print("".center(138)+bcolors.ENDC)

#check if someone won
def has_won(player_mode, board, player, count):  
    for i in win_combinations:
        if board[i[0]] == board[i[1]] == board[i[2]] != ".":
            print_board(board)
            print_result(player)
            break          

    if count>=9:
            print_board(board)
            is_full()

    else:
        print_board(board)
        count+=1
        if player=='X':
            player='O'
        elif player=='O':
            player='X'
        if player_mode == "1":
                ai_mode(player, player_mode, board, count)
        else:
            get_move(player_mode, player, board, count)

#desk is full and it's a tie
def is_full():
    print(f"{bcolors.LightYellow}It's a tie!{bcolors.ENDC}".center(150))
    one_more_game()

#print who is the winner
def print_result(player):
    print("\n")
    print(f"{bcolors.LightYellow}Game over, player {player} won!{bcolors.ENDC}".center(150))
    one_more_game()

#loop for game
def one_more_game():
    print("\n")
    print(f"{bcolors.LightGreen}Do you want to play one more game? (y/n) - {bcolors.ENDC}".center(150))
    print("\n") 
    more_game_answer = input("".center(69))

    while more_game_answer != 'y' and more_game_answer != 'n':
        print("\n")
        print(f"{bcolors.LightGreen}Your answer has to be y (yes) or n (no). Do you want to play one more game? (y/n) - {bcolors.ENDC}".center(153)) 
        print("\n")
        more_game_answer = input("".center(69))

    if more_game_answer == 'y':
        tictactoe_game()
    elif more_game_answer == 'n':
        quit()
                
#to quit game       
def quit():
    print("\n")
    print(f"{bcolors.Cyan}Thank you for playing! See you next time!{bcolors.ENDC}".center(140))
    sys.exit(0)        

tictactoe_game()