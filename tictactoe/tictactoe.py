
game_still_going = True

winner = None

current_player = 'X'


board = ["-", "-", "-",
         "-", "-", "-",
         "-", "-", "-"]

def play_game():

    display_board()

    while game_still_going:

        handle_turn(current_player)

        #checks for winner and return X or O
        check_if_game_over()
        #Flips the player
        flip_player()


    if winner == "X":
        print("X won!")

    elif winner == "O":
        print("O won!")
    else:
        print("It's a tie!")

    


def display_board():
  print("\n")
  print(board[0] + " | " + board[1] + " | " + board[2] + "     1 | 2 | 3")
  print(board[3] + " | " + board[4] + " | " + board[5] + "     4 | 5 | 6")
  print(board[6] + " | " + board[7] + " | " + board[8] + "     7 | 8 | 9")
  print("\n")



# Handle a turn for an arbitrary player
def handle_turn(player):

  # Get position from player
  print(player + "'s turn.")
  position = input("Choose a position from 1-9: ")

  # Whatever the user inputs, make sure it is a valid input, and the spot is open
  while True:

    # Make sure the input is valid
    while position not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
      position = input("Choose a position from 1-9: ")
 
    # Get correct index in our board list
    position = int(position) - 1

    # Then also make sure the spot is available on the board
    if board[position] == "-":
        break

    else:
      print("You can't go there. Go again.")

  # Put the game piece on the board
  board[position] = player

  # Show the game board
  display_board()

def check_if_game_over():

    check_winner()

    check_tie()

def check_winner():
    # giving access to the global winner variable so we can assing X or O
    global winner
    #Those are going to return winners X or O
    row_winner = check_rows()
    column_winner = check_columns()
    diagonal_winner = check_diagonals()
    
    if row_winner:
        winner = row_winner
    elif column_winner:
        winner = column_winner
    elif diagonal_winner:
        winner = diagonal_winner
    else:
        return None



def check_tie():

    global game_still_going

    if "-" not in board:
        game_still_going = False
        return True
    else:
        return False


def check_rows():

    #giving access to a global variable
    global game_still_going

    #cheking the rows
    row_1 = board[0] == board[1] == board[2] != "-"
    row_2 = board[3] == board[4] == board[5] != "-"
    row_3 = board[6] == board[7] == board[8] != "-"

    #if any of those are True and set the global loop to false to stop the game
    if row_1 or row_2 or row_3:
        game_still_going = False
    #Return the winner X or O
    if row_1:
        return board[0]
    elif row_2:
        return board[3]
    elif row_3:
        return board[6]
    #Or return None if there is no winner
    else:
        return None
    


def check_columns():
    
    #access to a global variable
    global game_still_going

     #cheking the columns
    column_1 = board[0] == board[3] == board[6] != "-"
    column_2 = board[1] == board[4] == board[7] != "-"
    column_3 = board[2] == board[5] == board[8] != "-"

    #if any of those are True and set the global loop to false to stop the game
    if column_1 or column_2 or column_3:
        game_still_going = False
    #Return the winner X or O
    if column_1:
        return board[0]
    elif column_2:
        return board[1]
    elif column_3:
        return board[2]
    #Or return None if there is no winner
    else:
        return None
    




def check_diagonals():
        #access to a global variable
    global game_still_going

     #cheking the rows
    diagonal_1 = board[0] == board[4] == board[8] != "-"
    diagonal_2 = board[2] == board[4] == board[6] != "-"

    #if any of those are True and set the global loop to false to stop the game
    if diagonal_1 or diagonal_2:
        game_still_going = False
    #Return the winner X or O
    if diagonal_1:
        return board[0]
    elif diagonal_2:
        return board[2]
    #Or return None if there is no winner
    else:
        return None




def flip_player():
    
    #access to a global variable
    global current_player
    #Change the current player
    if current_player == "X":
        current_player = "O"
    elif current_player == "O":
        current_player = "X"






play_game()