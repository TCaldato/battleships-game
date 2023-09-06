import random

# Constants
USER_SHIP = "U"
COMP_SHIP = "C"
HIT = "X"
GRID_SIZE_MIN = 5
GRID_SIZE_MAX = 9
NUM_SHIPS = 3
SHIP_SIZE = 3

# Class representing the game board
class Board:
    def __init__(self, size):
        self.size = size
        self.grid = [['*'] * size for _ in range(size)]

    def mark_hit(self, row, col):
        self.grid[row - 1][col - 1] = HIT

    def display_grid(self):
        """
        Display the grid with row and column numbering
        """
        print("    " + " ".join(str(i + 1) for i in range(self.size)))
        for i, row in enumerate(self.grid):
            print(str(i + 1) + " | " + " ".join(row))

# Class representing the user's board
class UserBoard(Board):
    def place_ships(self):
        for _ in range(NUM_SHIPS):
            while True:
                row = random.randint(1, self.size)
                col = random.randint(1, self.size)
                if self.grid[row - 1][col - 1] == '*':
                    self.grid[row - 1][col - 1] = COMP_SHIP
                    break

# Class representing the computer's board
class ComputerBoard(Board):
    def place_ships(self):
        for _ in range(NUM_SHIPS):
            while True:
                row = random.randint(1, self.size)
                col = random.randint(1, self.size)
                if self.grid[row - 1][col - 1] == '*':
                    self.grid[row - 1][col - 1] = USER_SHIP
                    break

# Class to manage the game
class BattleshipGame:
    def __init__(self, size):
        self.user_board = UserBoard(size)
        self.comp_board = ComputerBoard(size)
        self.user_board.place_ships()
        self.comp_board.place_ships()

    def play(self):
        while True:
            print("User's Board:")
            self.user_board.display_grid()
            print("\nComputer's Board:")
            self.comp_board.display_grid()
            user_row = int(input(f"Enter row (1 to {self.user_board.size - 1}): "))
            user_col = int(input(f"Enter col (1 to {self.user_board.size - 1}): "))

            if (
                0 <= user_row < self.user_board.size
                and 0 <= user_col < self.user_board.size
            ):
                if self.comp_board.grid[user_row - 1][user_col - 1] == COMP_SHIP:
                    print("User hit a computer ship!")
                    self.comp_board.mark_hit(user_row, user_col)
                else:
                    print("User missed.")
                    self.user_board.mark_hit(user_row, user_col)
                # Check for game over condition
                if all(
                    all(cell == HIT or cell == USER_SHIP for cell in row)
                    for row in self.comp_board.grid
                ):
                    print("User wins!")
                    break
                comp_row = random.randint(1, self.comp_board.size)
                comp_col = random.randint(1, self.comp_board.size)
                if self.user_board.grid[comp_row - 1][comp_col - 1] == USER_SHIP:
                    print("Computer hit a user ship!")
                    self.user_board.mark_hit(comp_row, comp_col)
                else:
                    print("Computer missed.")
                    self.comp_board.mark_hit(comp_row, comp_col)
                # Check for game over condition
                if all(
                    all(cell == HIT or cell == COMP_SHIP for cell in row)
                    for row in self.user_board.grid
                ):
                    print("Computer wins!")
                    break
            else:
                print("Invalid input. Row and column must be within range.")

# Main program
def main():
    print("\nWelcome to Battleship Game")
    print("In this game, you have 5 attempts to try to sink the computer's ship.")
    print("Do you think you can do it???")
    size = int(
        input(f"Enter the grid size ({GRID_SIZE_MIN}-{GRID_SIZE_MAX}): ")
    )
    if GRID_SIZE_MIN <= size <= GRID_SIZE_MAX:
        game = BattleshipGame(size)
        game.play()
    else:
        print(f"Invalid grid size. Please choose a size between {GRID_SIZE_MIN} and {GRID_SIZE_MAX}.")

    print("\nLet's play!!!")

if __name__ == "__main__":
    main()

