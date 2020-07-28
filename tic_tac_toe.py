board = [[' ',' ',' '],[' ',' ',' '],[' ',' ',' ']]
turn = 0
player_input = None
play = True
play_again = False
print("Welcome to Tic Tac Toe")


def print_board():
    print(f'  {board[2][0]} | {board[2][1]} | {board[2][2]}')
    print('------------')
    print(f'  {board[1][0]} | {board[1][1]} | {board[1][2]}')
    print('------------')
    print(f'  {board[0][0]} | {board[0][1]} | {board[0][2]}')

def check_play_again():
    global play_again, board, turn, play
    print('Do you want to play again? y/n')
    play_again_choice = input()
    if play_again_choice.lower() == 'y':
        play_again = True
        board = [[' ',' ',' '],[' ',' ',' '],[' ',' ',' ']]
        turn = 0
        print_board()
        play = True
    else:
        play = False



def get_input():
    global turn, board
    print('Please select a square 1-9: ')
    player_input = int(input())
    if turn % 2 == 0:
        if player_input < 4:
            if board[0][player_input-1] == ' ': 
                board[0][player_input-1] = 'X'
                turn+=1
            else:
                print('Spot is already taken. Please try another')
        elif player_input < 7:
            player_input -= 3
            if board[1][player_input-1] == ' ':
                board[1][player_input-1] = 'X'
                turn+=1
            else:
                print('Spot is already taken. Please try another')
        elif player_input <10:
            player_input -= 6
            if board[2][player_input-1] == ' ':
                board[2][player_input-1] = 'X'
                turn+=1
            else:
                print('Spot is already taken. Please try another')
    else:
        if player_input < 4:
            if board[0][player_input-1] == ' ': 
                board[0][player_input-1] = 'O'
                turn+=1
            else:
                print('Spot is already taken. Please try another')
        elif player_input < 7:
            player_input -= 3
            if board[1][player_input-1] == ' ':
                board[1][player_input-1] = 'O'
                turn+=1
            else:
                print('Spot is already taken. Please try another')
        elif player_input <10:
            player_input -= 6
            if board[2][player_input-1] == ' ':
                board[2][player_input-1] = 'O'
                turn+=1
            else:
                print('Spot is already taken. Please try another')
            
def check_if_winner():
    global board, play, play_again
    for row in board:
        if all(val=='X' for val in row):
            print('We have a horizontal winner')
            check_play_again()
        elif all(val=='O' for val in row):
            print('We have a horizontal winner')
            play = False
            check_play_again()
            
    if (board[0][0] == board[1][0] == board[2][0]) and board[0][0] != ' ':
        print('We have a vertical winner')
        play = False
        check_play_again()
    elif (board[0][1] == board[1][1] == board[2][1]) and board[0][1] != ' ':
        print('We have a vertical winner')
        play = False
        check_play_again()
    elif (board[0][2] == board[1][2] == board[2][2]) and board[0][2] != ' ':
        print('We have a vertical winner')
        play = False
        check_play_again()
    elif (board[2][0] == board[1][1] == board[0][2]) and board[0][2] != ' ':
        print('We have a diagonal winner')
        play = False
        check_play_again()
    elif (board[2][2] == board[1][1] == board[0][0]) and board[2][2] != ' ':
        print('We have a diagonal winner')
        play = False
        check_play_again()
       
    
            
    
def check_if_over():
    global turn
    global play
    if turn >=9:
        play = False
        
    

    


print_board()
while play:
    get_input()
    print_board()
    check_if_winner()
    check_if_over()

    



