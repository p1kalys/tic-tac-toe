class TicTacToe:
    def __init__(self, n):
        self.rows = [0]*n
        self.cols = [0]*n
        self.diagonal = 0
        self.anti_diagonal = 0
        self.size = n
        self.winner = None
        self.moves_left = n*n

    def move(self, row, col, player):
        self.moves_left -= 1
        player_value = 1 if player == 'X' else -1
        self.rows[row] += player_value
        self.cols[col] += player_value

        if row == col:
            self.diagonal += player_value

        if row + col == self.size - 1:
            self.anti_diagonal += player_value

        if (abs(self.rows[row]) == self.size or abs(self.cols[col]) == self.size or abs(self.diagonal) == self.size or abs(self.anti_diagonal) == self.size):
            self.winner = player
            return player
        return -1
    
    def is_game_over(self):
        return self.winner is not None or self.moves_left == 0

n = 3
game = TicTacToe(n)

players = ['X', 'O']
current_player = 0

visited = set()

while not game.is_game_over():
    while True:
        try:
            row = int(input(f"Player {players[current_player]}, enter row (0 to {n - 1}): "))
            col = int(input(f"Player {players[current_player]}, enter column (0 to {n - 1}): "))
            if 0 <= row < n and 0 <= col < n:
                if (row, col) not in visited:
                    visited.add((row, col))
                    break
                else:
                    print("This position is already chosen. Try again.")
            else:
                print(f"Invalid input! Row and column must be between 0 and {n - 1}. Try again.")
        except ValueError:
            print("Invalid input! Please enter numbers.")
    
    win = game.move(row, col, players[current_player])
    if win != -1:
        print(f"Player {win} wins!")
        break
    current_player = 1 - current_player
else:
    print("It's a draw!")
    