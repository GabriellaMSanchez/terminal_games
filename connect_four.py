class ConnectFour():

    board_length = 6
    board_width = 7

    def play_game(self): # When called, this plays the game.

        # First, Have Player One select a token (X's or O's):
        (player_one_token, player_two_token) = self.pick_token()
        # Since its a new game, start turn count at zero.
        turn_count = 0
        # Generate new board.
        board = self.generate_board(self.board_length, self.board_width)
        is_won = None
        # Player One always goes first.
        is_player_one = True

        while not is_won:
            # Print the board visually for the player to see
            print(self.print_board(board, self.board_width))
            # Increment turn count
            turn_count = self.turn_counter(turn_count)
            print(f"This is turn {turn_count}")
            # If turn count is over ten, that means it is a tie.
            if turn_count > 42:
                is_won = False
                break
            # Player One's turn
            if is_player_one:
                self.player_turn(is_player_one, board, player_one_token, self.board_length)
                # Validate if a player has won at the end of each turn.
                is_won = self.is_won(board)
                # If player has not one, it is next players turn.
                if not is_won:
                    is_player_one = False
            # Player Two's turn
            else:
                self.player_turn(is_player_one, board, player_two_token, self.board_length)
                # Validate if a player has won at the end of each turn.
                is_won = self.is_won(board)
                # If player has not one, it is next players turn.
                if not is_won:
                    is_player_one = True
            print(is_won)
                    

        # When someone has one,  print the winning board, and who has won.
        print(self.print_board(board, self.board_width))
        self.print_who_won(is_won, is_player_one)

    # Ask Player One to select X's or O's
    def pick_token(self):
        is_token_selected = None
        while is_token_selected == None:
            print("Let's Play Connect Four!\n")
            player_one_response = input("Player One are you X's or O's? X/O: ").lower()

            if player_one_response == "x":
                is_token_selected = True
                player_one_token, player_two_token = "X", "O"
                print("Player One is X's and Player Two is O's.")
            elif player_one_response == "o":
                is_token_selected = True
                player_one_token, player_two_token = "O", "X"
                print("Player One is O's and Player Two is X's.")
            else:
                print("That is not a valid input.")

        return (player_one_token, player_two_token)

    # Increments the turn count
    def turn_counter(self, turn_count):
        turn_count += 1
        return turn_count

    # Generates new board
    def generate_board(self, board_length, board_width):
        board = []

        for _ in range(board_length):
            stack = []
            for _ in range(board_width):
                stack.append(" ")
            board.append(stack)
        return board

    def column_headers(self, board_width):
        column_stack = []
        for i in range(board_width):
            column_stack.append(f"   {i + 1}   ")

        column_stack.append("\n")
        return "".join(column_stack)

    # Prints the board for the player to see
    def print_board(self, board, board_width):
        print_board = []

        print_board.append(self.column_headers(board_width))

        for i in range(len(board)):
            for j in range(len(board[i])):
                if j == len(board[i]) - 1:
                    print_board.append(f"|  {board[i][j]}   |")
                else:
                    print_board.append(f"|  {board[i][j]}   ")
            print_board.append("\n")
            horiz_line = self.generate_horizontal_line(board, self.board_width)
            print_board.append(horiz_line)
        return "".join(print_board)

    def generate_horizontal_line(self, board, board_width):
        for i in range(len(board)):
            if i <= len(board) - 1:
                horizontal_stack = []
                for i in range(board_width):
                    if i == 0:
                        horizontal_stack.append('+------+')
                    else:
                        horizontal_stack.append('------+')
                horizontal_stack.append("\n")
            return "".join(horizontal_stack)


    # Asks the player their input, validates choice, and saves choice in board.
    def player_turn(self, is_player_one, board, player_token, board_length):
        valid_input = None
        if is_player_one:
            player = 1
        else:
            player = 2

        while valid_input == None:
            player_input = input(f"Player {player}, please type the number that indicate the square you'd like to select: ").lower().strip()
            if player_input.isdigit():
                # token will always go to the "bottom" of the column, so the only invalid selection
                # would be if a column is full
                column = int(player_input) - 1
                for row in range(len(board)-1, -1, -1):
                    if board[row][column] == " ":
                        board[row][column] = player_token
                        valid_input = True
                        break
                    elif row == 0 and board[row][column] != " ":
                        print("This column is full, please make another selection.")
                        break
            else:
                print("That is not a valid input.")

        return board

    # Validates if a player has won.
    def is_won(self, board):
        player_won = None

        for i in range(len(board) - 1, -1, -1):
            for j in range(len(board) - 1):
                horiz_check = False
                vert_check = False
                if board[i][j] == " ":
                    continue
                # check horizontal win
                if (j + 3) <= len(board) - 1:
                    horiz_check = True
                    if board[i][j] == board[i][j + 1] == board[i][j + 2] == board[i][j + 3]:
                        print("horiz enter")
                        return True
                # check vertical win
                if (i - 3) >= 0:
                    vert_check = True
                    if board[i][j] == board[i - 1][j] == board[i - 2][j] == board[i - 3][j]:
                        print("vert enter")
                        return True
                # check diagonal win, a connect four diagonal can only occur
                # if both horizontal and vertical checks pass
                if horiz_check and vert_check:
                    if board[i][j] == board[i - 1][j + 1] == board[i - 2][j + 2] == board[i - 3][j + 3]:
                        print("diag enter")
                        return True
            return False

        # return player_won

    # Prints who has won or if there is a tie to the players.
    def print_who_won(self, is_won, is_player_one):
        if is_won:
            if is_player_one:
                print("Congrats! Player One has won!")
            else:
                print("Congrats! Player Two has won!")
            print("Good Game!")
        else:
            print("It's a tie! Nice Try.")

if __name__ == '__main__':
    game = ConnectFour()
    game.play_game()
