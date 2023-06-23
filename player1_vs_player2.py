# print the board
board = {1:' ', 2:' ', 3:' ',
         4:' ', 5:' ', 6:' ',
         7:' ', 8:' ', 9:' ',}

def printboard(board):
    print(board[1],'|',board[2],'|',board[3])
    print("---------")
    print(board[4],'|',board[5],'|',board[6])
    print("---------")
    print(board[7],'|',board[8],'|',board[9])

#game functionality
def game():
    #variables
    turn = "x"
    count = 0
    
    #loop
    for i in range(10):
        #print game board
        printboard(board)

        #take user input
        inp = int(input(f"It's your turn {turn}! Select a spot from 1 to 9: "))

        #check for validity
        if inp >= 1 and inp <= 9 and board[inp] == ' ':
            board[inp]=turn
            count += 1
        else:
            print("That sopt is already occupied or You have entered invalid number.")
            continue 

        #check for win
        if count >= 5:
            #top row
            if board[1] == board[2] == board[3] != ' ':
                printboard(board)
                print('Game over')
                print(f"***** {turn} won *****")
                break
            
            #middle row
            elif board[4] == board[5] == board[6] != ' ':
                printboard(board)
                print('Game over')
                print(f"***** {turn} won *****")
                break

            #bottom row
            elif board[7] == board[8] == board[9] != ' ':
                printboard(board)
                print('Game over')
                print(f"***** {turn} won *****")
                break

            #first column
            elif board[1] == board[4] == board[7] != ' ':
                printboard(board)
                print('Game over')
                print(f"***** {turn} won *****")
                break

            #second column
            elif board[2] == board[5] == board[8] != ' ':
                printboard(board)
                print('Game over')
                print(f"***** {turn} won *****")
                break

            #third column
            elif board[3] == board[6] == board[9] != ' ':
                printboard(board)
                print('Game over')
                print(f"***** {turn} won *****")
                break

            #first diagonal    
            elif board[1] == board[5] == board[9] != ' ':
                printboard(board)
                print('Game over')
                print(f"***** {turn} won *****")
                break

            #second diagonal
            elif board[3] == board[5] == board[7] != ' ':
                printboard(board)
                print('Game over')
                print(f"***** {turn} won *****")
                break
        
        #check for tie
        if count == 9:
            printboard(board)
            print("game over!")
            print("It's a tie")
            break

        #switch user
        if turn == 'x':
            turn = 'o'
        else:
            turn = 'x'
    #play again
    restart = input("wanna play again? (y/n)")
    if restart == 'y' or restart == 'Y':
        for key in board:
            board[key] = ' '
        game()
game()






