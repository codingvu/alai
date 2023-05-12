def play_tic_tac_toe():
    board = ['-'] * 9  # create a list to represent the game board
    
    def display_board():
        print(board[0] + '|' + board[1] + '|' + board[2])
        print(board[3] + '|' + board[4] + '|' + board[5])
        print(board[6] + '|' + board[7] + '|' + board[8])

    def check_win(mark):
        # check for horizontal wins
        for i in range(0, 9, 3):
            if board[i] == board[i+1] == board[i+2] == mark:
                return True
        # check for vertical wins
        for i in range(3):
            if board[i] == board[i+3] == board[i+6] == mark:
                return True
        # check for diagonal wins
        if board[0] == board[4] == board[8] == mark:
            return True
        if board[2] == board[4] == board[6] == mark:
            return True
        return False

    def check_tie():
        return '-' not in board

    display_board()
    while True:
        # player 1's turn
        while True:
            position = int(input("Player 1, choose a position (1-9): ")) - 1
            if board[position] == '-':
                board[position] = 'X'
                break
            else:
                print("That position is already taken. Please choose another position.")

        display_board()

        if check_win('X'):
            print("Player 1 wins!")
            break

        if check_tie():
            print("Tie game!")
            break

        # player 2's turn
        while True:
            position = int(input("Player 2, choose a position (1-9): ")) - 1
            if board[position] == '-':
                board[position] = 'O'
                break
            else:
                print("That position is already taken. Please choose another position.")

        display_board()

        if check_win('O'):
            print("Player 2 wins!")
            break

        if check_tie():
            print("Tie game!")
            break

if __name__ == "__main__":
    play_tic_tac_toe()
