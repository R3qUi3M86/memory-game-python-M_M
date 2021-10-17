import os
import random

MAX_LETTERS = 26
FIRST_ASCII_LETTER_INDEX = 65
LAST_ASCII_LETTER_INDEX = 90
MAX_BOARD_SIZE = 52
ALPHABET = "ABCDEFGHIJKLMNOPQRSTUWVYXZ"
column_list = []
row_list = []
discovered_letters = []
found_letters = []
previous_move = -1, -1
current_move = -1, -1

#OUTPUT LAYER
#Clears the screen
def console_clear():
    command = 'clear'
    if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
        command = 'cls'
    os.system(command)

#Prints current game board
def print_board(board):
    #Prints column letter indices
    column_display = "  "
    for col in column_list:
        column_display += col+" "
    print(column_display)

    #Prints rows and their numeric indices
    for row in range(len(board)):
        row_display = str(row+1) #Creates numeric index as initial row character

        for col in range(len(board[row])):
            cell_char = board[row][col]
            if cell_char in found_letters:
                row_display += " " + cell_char
            elif (row == current_move[1] and col == current_move[0]) or (row == previous_move[1] and col == previous_move[0]):
                row_display += " " + cell_char
            elif cell_char not in found_letters:
                row_display += " #"
        print(row_display)

#Displays endgame screen
def endgame(board, moves):
    console_clear()
    print_board(board)
    print(f"\nYou won! It took you {moves} moves to find all letters!")
    playagain_prompt()  

#INPUT LAYER
#Option for user to play again
def playagain_prompt():
    while True:
        user_input = input("Would you like to play again?(y/n): ")
        
        if user_input.lower() == "y":
            play_game()
        elif user_input.lower() == "n" or user_input.lower() == "quit":
            exit()

#Gets 2 or 3 character input from user
def get_user_input(height, board):
    while True:
        console_clear()
        print_board(board)
        user_inp = input("What is your move?\n(example: A1)\n\n")
        
        if user_inp == "quit":
            exit()
        elif len(user_inp) == 2 or len(user_inp) == 3:
            if len(user_inp) == 3 and height < 10:
                continue
            else:
                return user_inp

#Checks if move is not for already discovered or found letter
def check_valid_move(board, user_move):
    if board[user_move[1]][user_move[0]] in found_letters or user_move == previous_move:
        return False
    else:
        return True

#Returns integer tuple as board indices
def get_user_move(height, board):
    while True:
        user_input = get_user_input(height, board)
        input_char_list = list(user_input)
        
        if input_char_list[0].upper() in column_list:
            input_width = column_list.index(input_char_list[0].upper())

            if len(input_char_list) == 3 and input_char_list[1].isdigit() and input_char_list[2].isdigit():
                input_height = int(input_char_list[1] + input_char_list[2])

                if input_height in row_list:
                    return input_width, input_height-1

            elif input_char_list[1].isdigit() and int(input_char_list[1]) in row_list:
                input_height = int(input_char_list[1])
                return input_width, input_height-1

#LOGIC LAYER
#Main game loop
def play_game():
    global current_move
    global discovered_letters
    global previous_move
    global current_move

    width = 2
    height = 2
    board = generate_board(height, width)
    moves = 0
    
    reset_game_parameters()

    while len(found_letters) < ((height * width) // 2):
        console_clear()
        print_board(board)

        previous_move = current_move
        user_move = 0,0
        
        if len(discovered_letters) < 2:
            moves += 1
            while True:
                user_move = get_user_move(height, board)
                if check_valid_move(board, user_move) == False:
                    continue
                else:
                    discover_letter(board, user_move)
                    current_move = user_move
                    break
            
        else:
            input("Press Enter to continue...")
            discovered_letters = []
            current_move = -1, -1
            previous_move = -1, -1

    endgame(board, moves)

#Global parameters reset
def reset_game_parameters():
    global discovered_letters
    global found_letters
    global previous_move
    global current_move

    discovered_letters = []
    found_letters = []
    previous_move = -1, -1
    current_move = -1, -1

#Adds currently discovered letter to the global array
def discover_letter(board, user_move):
    global discovered_letters
    global found_letters

    discovered_letters.append(board[user_move[1]][user_move[0]])

    if len(discovered_letters) == 2 and discovered_letters[1] == discovered_letters[0]:
        found_letters.append(board[user_move[1]][user_move[0]])

#Checks for value error regarding board dimensions
def check_for_value_error(height, width):
    if (height * width) > MAX_BOARD_SIZE:
        raise ValueError("Board is too large")
    elif (height * width) % 2 != 0:
        raise ValueError("Board size is odd number")

#Generates lists of rows as letters and columns (starts with number 1 instead of 0)
def generate_row_col_lists(height, width):
    global column_list
    global row_list

    column_list = []
    for i in range(height):
        row_list.append(i+1)

    for i in range(width):
        column_list.append(chr(i+FIRST_ASCII_LETTER_INDEX))

#Generates picked letter list which will be used to populate the board
def generate_picked_letter_list(height, width):
    picked_letter_list = []
    ammount_of_unique_letter = (height * width) // 2

    for i in range(ammount_of_unique_letter):
        picked_letter_list.append(ALPHABET[i])

    picked_letter_list = picked_letter_list * 2
    random.shuffle(picked_letter_list)
    return picked_letter_list

#Generates board populated with letters
def generate_board(height, width):
    check_for_value_error(height, width)
    generate_row_col_lists(height, width)

    board = [['']*width for _ in range(height)] #list comprehension
    
    picked_letter_list = generate_picked_letter_list(height, width)

    letter_index = 0
    for row in range(height):
        for col in range(width):
            board[row][col] = picked_letter_list[letter_index]
            letter_index += 1

    return board

if __name__ == "__main__":
    play_game()