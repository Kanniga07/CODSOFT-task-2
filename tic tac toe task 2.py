import math

class TicTacToe:
    def __init__(self):
        self.board = ['-'] * 9
        self.AI = 'x'
        self.YOU = 'o'

    def print_board(self):
        for i in range(0, 9, 3):
            print(self.board[i] + ' | ' + self.board[i+1] + ' | ' + self.board[i+2])
        print()

    def check_winner(self, player):
        winning_combinations = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8],
            [0, 3, 6], [1, 4, 7], [2, 5, 8],
            [0, 4, 8], [2, 4, 6]
        ]
        for combo in winning_combinations:
            if all(self.board[i] == player for i in combo):
                return True
        return False

    def is_board_full(self):
        return all(cell != '-' for cell in self.board)

    def minimax_alpha_beta(self, depth, alpha, beta, maximizing_player):
        if self.check_winner(self.AI):
            return 1  
        if self.check_winner(self.YOU):
            return -1  
        if self.is_board_full():
            return 0  

        if maximizing_player:
            max_eval = -math.inf
            for i in range(9):
                if self.board[i] == '-':
                    self.board[i] = self.AI
                    eval = self.minimax_alpha_beta(depth + 1, alpha, beta, False)
                    self.board[i] = '-'
                    max_eval = max(max_eval, eval)
                    alpha = max(alpha, eval)
                    if beta <= alpha:
                        break
            return max_eval
        else:
            min_eval = math.inf
            for i in range(9):
                if self.board[i] == '-':
                    self.board[i] = self.YOU
                    eval = self.minimax_alpha_beta(depth + 1, alpha, beta, True)
                    self.board[i] = '-'
                    min_eval = min(min_eval, eval)
                    beta = min(beta, eval)
                    if beta <= alpha:
                        break
            return min_eval

    def find_best_move(self):
        best_move = -1
        best_eval = -math.inf
        for i in range(9):
            if self.board[i] == '-':
                self.board[i] = self.AI
                eval = self.minimax_alpha_beta(0, -math.inf, math.inf, False)
                self.board[i] = '-'
                if eval > best_eval:
                    best_eval = eval
                    best_move = i
        return best_move

    def play_game(self):
        while True:
            self.print_board()
            move = int(input("Pick your option (0-8): "))
            if self.board[move] == '-':
                self.board[move] = self.YOU
                if self.check_winner(self.YOU):
                    self.print_board()
                    print("You're the winner!")
                    break
                elif self.is_board_full():
                    self.print_board()
                    print("It's a tie!")
                    break
                ai_move = self.find_best_move()
                self.board[ai_move] = self.AI
                if self.check_winner(self.AI):
                    self.print_board()
                    print("AI triumphs!")
                    break
                elif self.is_board_full():
                    self.print_board()
                    print("It's a stalemate!")
                    break
            else:
                print("The cell is already full. Give it another go.")

# Main game loop
if __name__ == "__main__":
    game = TicTacToe()
    game.play_game()
