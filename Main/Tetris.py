import os

class Block:

    def create_block(row, col, board):
        
        if board[row][col] == 0:
            board[row][col] = 1
        else:
            raise Exception("Block already exists at this location")
        
        return board
    
    def delete_row(row, board):

        for col in range(len(board[row])):  #Remove all blocks in the row for when the player gets a teris
            board[row][col] = 0

        return board #Return the board with the row deleted
    
    def move_block(row, col, board, direction):
            
            if direction == "left":
                if col == 0:
                    pass

                else:

                    board[row][col] = 0
                    board[row][col - 1] = 1

            elif direction == "right":

                if col == len(board[row]) - 1:
                    pass
                    
                else:
                    board[row][col] = 0
                    board[row][col + 1] = 1

            elif direction == "down":
                if row == len(board) - 1:
                    pass

                else:
                    board[row][col] = 0
                    board[row + 1][col] = 1
            else:
                raise Exception("Invalid direction")
    
            return board
    
    def block_is_static(row, col, board):
        if row == len(board) - 1:
            return True
        elif board[row + 1][col] != 0:
            return True
        else:
            return False
        
    def all_blocks_static(board):
        for row in range(len(board)):
            for col in range(len(board[row])):

                if board[row][col] != 0:
                    if Block.block_is_static(row, col, board):
                        pass
                    else:
                        return False
        return True
    
    def static_blocks(board):
        static_blocks = []

        for row in range(len(board)):
            for col in range(len(board[row])):

                if board[row][col] != 0:
                    if Block.block_is_static(row, col, board):
                        static_blocks.append([row, col])
        return static_blocks

class gui:

    def print_board(board):
        for row in board:
            for col in row:
                if col == 0:
                    print("   ", end = "")
                else:
                    print("[ ]", end = "")
            print()

    def clear_screen():
        if os.name == "nt":
            os.system("cls")

        else:
            os.system("clear")

class game:

    def tick(board):

        for row in range(len(board) - 1, -1, -1): #Start at the bottom of the board and work up
            for col in range(len(board[row])): #Start at the left of the board and work right
                if board[row][col] != 0: #If there is a block in the current location
                    if Block.block_is_static(row, col, board): #If the block is static
                        board[row][col] = 2 #Set the block to static
                    else: #If the block is not static
                        board[row][col] = 0 #remove the block and place it one row down
                        board[row + 1][col] = 1

        return board
    
    def check_for_teris(board):
        
        for row in range(len(board)):

            if 0 not in board[row]:
                board = Block.delete_row(row, board)

    def update_board(board):

        gui.clear_screen()
        gui.print_board(board)

def main():
    
    board = [


#col 0  1  2  3  4  5  6  7  8
    [0, 0, 0, 0, 0, 0, 0, 0, 0], #Row 0
    [0, 0, 0, 0, 0, 0, 0, 0, 0], #Row 1
    [0, 0, 0, 0, 0, 0, 0, 0, 0], #Row 2
    [0, 0, 0, 0, 0, 0, 0, 0, 0], #Row 3
    [0, 0, 0, 0, 0, 0, 0, 0, 0], #Row 4
    [0, 0, 0, 0, 0, 0, 0, 0, 0], #Row 5
    [0, 0, 0, 0, 0, 0, 0, 0, 0], #Row 6
    [0, 0, 0, 0, 0, 0, 0, 0, 0], #Row 7
    [0, 0, 0, 0, 0, 0, 0, 0, 0]  #Row 8
]
    
    while True:

        game.update_board(board)

        usr_input = input("Enter a command: ")

        if usr_input == "create block":
            row = int(input("Enter a row: "))
            col = int(input("Enter a col: "))

            board = Block.create_block(row, col, board)

        elif usr_input == "move block":
            row = int(input("Enter a row: "))
            col = int(input("Enter a col: "))
            direction = input("Enter a direction: ")
            try:
                board = Block.move_block(row, col, board, direction)
            except:
                print("Invalid direction or smth")

        elif usr_input == "tick":
            board = game.tick(board)
            game.check_for_teris(board)
            game.update_board(board)
            
        elif usr_input == "exit":
            break
        else:
            print("Invalid command")

while True:
    try:
        main()
    except:
        print("An error occured")
    
    print("Would you like to restart or exit?")
    usr_input = input("Enter 'restart' or 'exit': ")

    while True:

        print("Would you like to restart or exit?")
        usr_input = input("Enter 'restart' or 'exit': ")

        if usr_input == "restart":
            break
        elif usr_input == "exit":
            exit()
        else:
            print("Invalid command")

