import random

# Single player Tic-Tac-Toe game vs computer

# Initialize display board with 10 empty characters, input will be from 1-9
# Input will correspond to the index, so we need 10, last index being the input 9
my_board = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']


# Create display board. Index 0 will not be used because it is an invalid input to play the game
def display_board(my_board):
    new_line = '\n'
    print(f'   |   | {new_line} {my_board[1]} | {my_board[2]} | {my_board[3]} {new_line}   |   | {new_line} ----------- {new_line}'
          f'   |   | {new_line} {my_board[4]} | {my_board[5]} | {my_board[6]} {new_line}   |   | {new_line} ----------- {new_line}'
          f'   |   | {new_line} {my_board[7]} | {my_board[8]} | {my_board[9]} {new_line}   |   | {new_line} ----------- {new_line}')


# Returns if the space on the display board is open or not
def valid_space(index):
    return my_board[index] == ' '


# Inputs the number to the display board
def input_to_board(num, index):
    my_board[index] = num


# Checks if the player's input is valid and inputs
def player_input():
    valid = True
    while valid:
        num_input = input("Enter a position(1-9) to place your marker: ")
        try:  # try/except for valid inputs, if not, print that input is invalid
            num_input = int(num_input)
            if num_input > 0 and num_input < 10:
                if valid_space(num_input):
                    valid = False
                    input_to_board('X', num_input)
                else:
                    print("This position is not free")
            else:
                print("Please input a number from 1-9")
        except:
            print("Please enter a number from 1-9")


# Generate random input for the computer's move
def random_input(ri):
    ri_len = len(ri)
    r = random.randrange(0, ri_len)
    return ri[r]


# Checks if the current move has won the game or not
def valid_winner(my_board, my_input):
    return ((my_board[1] == my_input and my_board[2] == my_input and my_board[3] == my_input) or  # across the bottom
            (my_board[4] == my_input and my_board[5] == my_input and my_board[6] == my_input) or  # across the middle
            (my_board[7] == my_input and my_board[8] == my_input and my_board[9] == my_input) or  # across the top
            (my_board[7] == my_input and my_board[5] == my_input and my_board[3] == my_input) or  # diagonal
            (my_board[9] == my_input and my_board[5] == my_input and my_board[1] == my_input) or  # diagonal
            (my_board[7] == my_input and my_board[4] == my_input and my_board[1] == my_input) or  # horizontally on the left
            (my_board[8] == my_input and my_board[5] == my_input and my_board[2] == my_input) or  # horizontally on the middle
            (my_board[9] == my_input and my_board[6] == my_input and my_board[3] == my_input))  # horizontally on the right


# Checks if the computer's input is valid and inputs
def computer_input():
    # make a list of valid moves
    valid_moves = [x for x, my_input in enumerate(my_board) if my_input == ' ' and x != 0]
    move = 0

    # Check for computer's winning move or block player's winning move
    for my_letter in ['O', 'X']:
        for i in valid_moves:
            copy_of_board = my_board[:]
            copy_of_board[i] = my_letter
            if valid_winner(copy_of_board, my_letter):
                move = i
                return move

    # Take the corners of the board
    open_corners = []
    for i in valid_moves:
        if i in [1, 3, 7, 9]:
            open_corners.append(i)
    if len(open_corners) > 0:
        move = random_input(open_corners)
        return move

    # Take the center of the board
    if 5 in valid_moves:
        move = 5
        return move

    # Take edge
    open_edges = []
    for i in valid_moves:
        if i in [2, 4, 6, 8]:
            open_edges.append(i)

    if len(open_edges) > 0:
        move = random_input(open_edges)

    return move


# Checks if the board is full
def full_board(board):
    if board.count(' ') > 1:
        return False
    else:
        return True


def main():
    print("A game of Tic Tac Toe!")
    display_board(my_board)

    while not(full_board(my_board)):
        if not(valid_winner(my_board, 'O')):
            player_input()
            display_board(my_board)
        else:
            print("O has won!")
            break

        if not(valid_winner(my_board, "X")):
            move = computer_input()
            if move == 0:
                print("Game is tied!")
            else:
                input_to_board('O', move)
                print(f'Computer placed an O in position {move}: ')
                display_board(my_board)
        else:
            print("X has won!")
            break

    if full_board(my_board):
        print("Tie game!")


if __name__ == "__main__":
    main()





























