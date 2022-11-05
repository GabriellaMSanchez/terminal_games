class TicTacToe():  

    def play_game(self): # When called, this plays the game.

        # First, ask X's or O's:
        (player_one_token, player_two_token) = self.pick_token()
        # Since its a new game, start turn count at zero.
        turn_count = 0
        # Generate new board.
        board = self.generate_board()
        is_won = None
        # Player One always goes first.
        is_player_one = True
        while not is_won:
            # Print the board visually for the player to see
            print(self.print_board(board))
            # Increment turn count
            turn_count = self.turn_counter(turn_count)
            print(f"This is turn {turn_count}")
            # If turn count is over ten, that means it is a tie.
            if turn_count >= 10:
                is_won = False
                break
            # Player One's turn
            if is_player_one:
                self.player_turn(is_player_one, board, player_one_token)
                # Validate if a player has won at the end of each turn.
                is_won = self.is_won(board)
                # If player has not one, it is next players turn.
                if not is_won:
                    is_player_one = False
            # Player Two's turn
            else:
                self.player_turn(is_player_one, board, player_two_token)
                # Validate if a player has won at the end of each turn.
                is_won = self.is_won(board)
                # If player has not one, it is next players turn.
                if not is_won:
                    is_player_one = True
                    

        # When someone has one,  print the winning board, and who has won.
        print(self.print_board(board))
        self.print_who_won(is_won, is_player_one)

    # Ask Player One to select X's or O's
    def pick_token(self):
        is_token_selected = None
        while is_token_selected == None:
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

    # Generates new board
    def generate_board(self):
        board = []
        count = 1

        for _ in range(3):
            stack = [f"{count}", f"{count + 1}", f"{count + 2}"]
            count += 3
            board.append(stack)
        return board

    # Prints the board for the player to see
    def print_board(self, board):
        print_board = []

        for i in range(len(board)):
            for j in range(len(board[i])):
                if j == len(board[i]) - 1:
                    print_board.append(f"   {board[i][j]}   ")
                else:
                    print_board.append(f"   {board[i][j]}   |")
            print_board.append("\n")

            if i < len(board) - 1:
                print_board.append("-------|-------|-------\n")
        return "".join(print_board)

    # Increments the turn count
    def turn_counter(self, turn_count):
        turn_count += 1
        return turn_count

    # Asks the player their input, validates choice, and saves choice in board.
    def player_turn(self, is_player_one, board, player_token):
        valid_input = None
        if is_player_one:
            player = 1
        else:
            player = 2

        x = None
        y = None
        
        while valid_input == None:
            player_input = input(f"Player {player}, please type the number that indicate the square you'd like to select: ").lower().strip()
            if player_input.isdigit():
                int_input = int(player_input) - 1
                x = int_input // 3
                y = int_input % 3
                board[x][y] = player_token
                valid_input = True
            else:
                print("That is not a valid input.")
        
        board[x][y] = player_token

        return board

    # Validates if a player has won.
    def is_won(self, board):
        player_won = None

        for i in range(len(board)):
            for j in range(len(board)):
                if board[i][j].isdigit():
                    continue
                # check horizontal
                # - only check horizontal if at [0][0], [1][0], [2][0] indices
                elif board[i][0] == board[i][1] == board[i][2]:
                    return True
                # check vertical
                # - only check vertical if at [0][0], [0][1], [0][2]
                elif board[0][j] == board[1][j] == board[2][j]:
                    return True
                # check diagonal
                # only check diagonal if at [0][0], [0][2]
                elif board[0][0] == board[1][1] == board[2][2]:
                        return True
                elif board[0][2] == board[1][1] == board[2][0]:
                        return True

            return False
        
        return player_won

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
    game = TicTacToe()
    game.play_game()
