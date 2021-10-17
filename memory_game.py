import os
import random

#alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
MAX_LETTERS = 26
FIRST_ASCII_LETTER_INDEX = 65
LAST_ASCII_LETTER_INDEX = 90
MAX_BOARD_SIZE = 52
ALPHABET = "ABCDEFGHIJKLMNOPQRSTUWVYXZ"
column_list = []
row_list = []


# clears the screen
def console_clear():
    command = 'clear'
    if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
        command = 'cls'
    os.system(command)

def main():
    width = 2
    height = 9
    board = generate_board(height, width)
    for i in range(height):
        print(board[i])
    print(get_user_move(height))
    

def generate_board(height, width):
    global column_list
    global row_list

    if (height * width) > MAX_BOARD_SIZE:
        raise ValueError("Board is too large")
    elif (height * width) % 2 != 0:
        raise ValueError("Board size is odd number")
    
    for i in range(height):
        row_list.append(i+1)

    for i in range(width):
        column_list.append(chr(i+FIRST_ASCII_LETTER_INDEX))


    board = [['']*width for _ in range(height)] #list comprehension
    picked_letter_list = []
    ammount_of_unique_letter = (height * width) // 2


    for i in range(ammount_of_unique_letter):
        picked_letter_list.append(ALPHABET[i])

    picked_letter_list = picked_letter_list * 2
    random.shuffle(picked_letter_list)

    letter_index = 0

    for row in range(height):
        for col in range(width):
            board[row][col] = picked_letter_list[letter_index]
            letter_index += 1

    return board

#def print_board

def get_user_input(height):
    while True:
        #console_clear()
        #print_board(board)
        user_inp = input("What is your move?\n(example: A1)\n\n")
        
        if user_inp == "quit":
            exit()
        elif len(user_inp) == 2 or len(user_inp) == 3:
            if len(user_inp) == 3 and height < 10:
                print("Invalid input")
            else:
                return user_inp

def get_user_move(height):
    while True:
        user_input = get_user_input(height)
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
        print("Invalid input")
            



if __name__ == "__main__":
    main()