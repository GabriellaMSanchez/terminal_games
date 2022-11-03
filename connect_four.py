class ConnectFour():

    board_length = 7
    board_width = 8

    def play_game(self):
        self.generate_board()

    def generate_horizontal(self):
        horizontal_stack = []
        for i in range(self.board_length):
            if i == 0:
                horizontal_stack.append('+---+')
            else:
                horizontal_stack.append('---+')
        return "".join(horizontal_stack)

    def generate_vertical(self):
        vertical_stack = []
        for i in range(self.board_width):
            if i == 7:
                vertical_stack.append('|')
            else:
                vertical_stack.append('|   ')
        return "".join(vertical_stack)

    def column_headers(self):
        column_stack = []
        for i in range(1, self.board_width):
            column_stack.append(f"  {i} ")
        return "".join(column_stack)

    def generate_board(self):
        # these can probably be passed in as parameters
        horizontal_line = self.generate_horizontal()
        vertical_line = self.generate_vertical()
        header = self.column_headers()

        print(header)
        for _ in range(self.board_length):
            print(horizontal_line)
            for _ in range(3):
                print(vertical_line)
        print(horizontal_line)


        # to use this during gameplay, have a check to see if there are winners?
        # or to see if the game is occurring?
        # If its a new game, create blank board
        # Else place tokens in their selected spot?


if __name__ == '__main__':
    game = ConnectFour()
    game.play_game()


