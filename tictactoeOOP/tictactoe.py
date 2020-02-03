"""A tic tac toe game using OOP"""

import os
import time
import pyinputplus as p


class Board():
    """A simple attempt to represent a board"""
    def __init__(self):
        self.cells = [" "," "," "," "," "," "," "," "," "," "]

    def display_board(self):
        """displayes our main board"""
        print(" %s | %s | %s " %(self.cells[1], self.cells[2], self.cells[3]))
        print("-----------")
        print(" %s | %s | %s " %(self.cells[4], self.cells[5], self.cells[6]))
        print("-----------")
        print(" %s | %s | %s " %(self.cells[7], self.cells[8], self.cells[9]))

    def update(self, cell_number, player):
        """Displayes X or O on the board"""
        if self.cells[cell_number] == " ":
            self.cells[cell_number] = player
        else:
            print("You cannot overwrite!")
            time.sleep(1)

    def is_winner(self, player):
        """Finds winnig patterns"""
        for list_cells in[[1,2,3],[4,5,6],[7,8,9],[1,4,7],[2,5,8],[3,6,9],[1,5,9],[3,5,7]]:
            result = True
            for cell_number in list_cells:
                if self.cells[cell_number] != player:
                    result = False

            if result == True:
                return True
        
        return False

    def reset_screen(self):
        """Resets the screen"""
        self.cells = [" "," "," "," "," "," "," "," "," "," "]

    def is_tie(self):
        """Checks for a tie"""
        used_cells = 0
        for cell in self.cells:
            if cell != " ":
                used_cells += 1
        
        if used_cells == 9:
            return True
        else:
            return False
    
#creating an instance of a board
board = Board()

def header():
    """Displayes the header"""
    print("Welcome to TIC TAC TOE!\n")

def refresh_screen():
    """Refreshes the screen, call other functions as well"""
    #claer the screen after each portration
    os.system('clear')
    
    #display the header
    header()

    #display the board
    board.display_board()

#the main loop
while True:

    refresh_screen()

    #prompts for X's turn and accept only valid input
    x_input = p.inputInt("X's turn, enter number 1-9: ", min=1, max=9)
    
    #display X on the board according its number
    board.update(x_input, "X")

    #reshresh the screen
    refresh_screen()
    
    #check for an X win
    if board.is_winner("X"):
        print("X's won!")
        #ask again and validate the input
        ask_again = p.inputYesNo("Would you like to continue? (yes/no): ")
        if ask_again == 'yes':
            board.reset_screen()
            continue
        else:
            break
    
    #check for an tie
    if board.is_tie():
        print("It's a tie!")
        #ask again and validate the input
        ask_again = p.inputYesNo("Would you like to continue? (yes/no): ")
        if ask_again == 'yes':
            board.reset_screen()
            continue
        else:
            break


    #prompts for O's turn and accept only valid input
    o_input = p.inputInt("O's turn, enter number 1-9: ", min=1, max=9)

    #display O on the board acooridng its number
    board.update(o_input, "O")

    #refresh the screen
    refresh_screen()

    #check for an O win
    if board.is_winner("O"):
        print("O's won!")
        #ask again and validate the input
        ask_again = p.inputYesNo("Would you like to continue? (yes/no): ")
        if ask_again == 'yes':
            board.reset_screen()
            continue
        else:
            break

    #check for a tie
    if board.is_tie():
        print("It's a tie!")
        #ask again and validate the input
        ask_again = p.inputYesNo("Would you like to continue? (yes/no): ")
        if ask_again == 'yes':
            board.reset_screen()
            continue
        else:
            break

    refresh_screen()