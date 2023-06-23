import random

board = [" " for _ in range(9)]
turn = 'x'
gamerunning = True

def print_board(board):
    print(board[0],'|',board[1],'|',board[2])
    print("---------")
    print(board[3],'|',board[4],'|',board[5])
    print("---------")
    print(board[6],'|',board[7],'|',board[8])

def user_input(board):
    global turn
    while True:
        inp = int(input("Select a spot from 1 to 9:"))
        if inp >= 1 and inp <= 9 and board[inp-1] == " ":
            board[inp-1] = turn
            break
        else:
            print("That spot is already occupied or You have entered an invalid number.")
            continue

def computer_input(board):
    global turn
    while True:
        move = random.randint(0,8)
        if board[move] == " ":
            board[move] = turn
            break
        else:
            continue

def switch_user():
    global turn
    if turn == 'x':
        turn = 'o'
    else:
        turn = 'x'

def check_tie(board):
    if " " not in board:
        print("it's a tie")
        gamerunning = False

def game():
    global board
    while gamerunning:
        print_board(board)
        user_input(board)

        if board[0] == board[1] == board[2] == 'x' or board[3] == board[4] == board[5] == 'x' or board[6] == board[7] == board[8] == 'x' or board[0] == board[3] == board[6]== 'x' or board[1] == board[4] == board[7] == 'x' or board[2] == board[5] == board[8] == 'x' or board[0] == board[4] == board[8] == 'x' or board[2] == board[4] == board[6] == 'x':
            print_board(board)
            print("x won!")
            break       

        if board[0] == board[1] == board[2] == 'o' or board[3] == board[4] == board[5] == 'o' or board[6] == board[7] == board[8] == 'o' or board[0] == board[3] == board[6]== 'o' or board[1] == board[4] == board[7] == 'o' or board[2] == board[5] == board[8] == 'o' or board[0] == board[4] == board[8] == 'o' or board[2] == board[4] == board[6] == 'o':
            print_board(board)
            print("o won!")
            break    
        
        check_tie(board)
        switch_user()
        computer_input(board)
        
        if board[0] == board[1] == board[2] == 'x' or board[3] == board[4] == board[5] == 'x' or board[6] == board[7] == board[8] == 'x' or board[0] == board[3] == board[6]== 'x' or board[1] == board[4] == board[7] == 'x' or board[2] == board[5] == board[8] == 'x' or board[0] == board[4] == board[8] == 'x' or board[2] == board[4] == board[6] == 'x':
            print_board(board)
            print("x won!")
            break       

        if board[0] == board[1] == board[2] == 'o' or board[3] == board[4] == board[5] == 'o' or board[6] == board[7] == board[8] == 'o' or board[0] == board[3] == board[6]== 'o' or board[1] == board[4] == board[7] == 'o' or board[2] == board[5] == board[8] == 'o' or board[0] == board[4] == board[8] == 'o' or board[2] == board[4] == board[6] == 'o':
            print_board(board)
            print("o won!")
            break

        check_tie(board)
        switch_user()

    reset = input("wanna play again(y/n)?")
    if reset == 'y' or reset == 'Y':
        board = [" " for _ in range(9)]
        game()

game()

    