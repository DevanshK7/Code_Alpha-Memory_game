import random
import time
from colorama import Fore, Back, Style, init


init(autoreset=True) # Initialize colorama

class MemoryPuzzleGame:
    def __init__(self, size=4, time_limit=60):
        self.size = size
        self.time_limit = time_limit
        self.board = self.create_board()
        self.hidden_board = [['*' for _ in range(size)] for _ in range(size)]
        self.start_time = None

    def create_board(self):
        num_pairs = (self.size * self.size) // 2
        values = list(range(1, num_pairs + 1)) * 2
        random.shuffle(values)
        board = []
        for i in range(self.size):
            row = []
            for j in range(self.size):
                row.append(values.pop())
            board.append(row)
        return board

    def display_board(self, board):
        print("\nBoard:")
        for row in board:
            print(' '.join(f"{Fore.BLUE if cell == '*' else Fore.GREEN}{cell}{Style.RESET_ALL}" for cell in row))
        print()

    def get_input(self):
        while True:
            try:
                row = int(input("Enter row (0-indexed): "))
                col = int(input("Enter column (0-indexed): "))
                if 0 <= row < self.size and 0 <= col < self.size:
                    return row, col
                else:
                    print(f"{Fore.RED}Invalid input. Please try again.{Style.RESET_ALL}")
            except ValueError:
                print(f"{Fore.RED}Invalid input. Please enter numbers only.{Style.RESET_ALL}")

    def play(self):
        self.start_time = time.time()
        matched_pairs = 0
        total_pairs = (self.size * self.size) // 2

        while matched_pairs < total_pairs:
            if time.time() - self.start_time > self.time_limit:
                print(f"{Fore.RED}Time's up! You lose.{Style.RESET_ALL}")
                return

            self.display_board(self.hidden_board)

            print(f"{Fore.YELLOW}First card:{Style.RESET_ALL}")
            row1, col1 = self.get_input()
            self.hidden_board[row1][col1] = self.board[row1][col1]
            self.display_board(self.hidden_board)

            print(f"{Fore.YELLOW}Second card:{Style.RESET_ALL}")
            row2, col2 = self.get_input()
            self.hidden_board[row2][col2] = self.board[row2][col2]
            self.display_board(self.hidden_board)

            if self.board[row1][col1] == self.board[row2][col2]:
                print(f"{Fore.GREEN}Match found!{Style.RESET_ALL}")
                matched_pairs += 1
            else:
                print(f"{Fore.RED}No match. Try again.{Style.RESET_ALL}")
                time.sleep(1)
                self.hidden_board[row1][col1] = '*'
                self.hidden_board[row2][col2] = '*'

        print(f"{Fore.GREEN}Congratulations! You matched all pairs.{Style.RESET_ALL}")
        self.display_board(self.board)

if __name__ == "__main__":
    game = MemoryPuzzleGame(size=4, time_limit=60)
    game.play()
