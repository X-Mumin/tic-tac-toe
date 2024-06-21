import tkinter as tk
from tic_tac_toe_gui import TicTacToeGUI
from Player import Player
from Computer import Computer

class TicTacToeGame:
    def __init__(self, master):
        """Initializes the Tic-Tac-Toe game."""

        self.master = master
        self.gui = TicTacToeGUI(master)
        self.game_board = [
            ["", "", ""],
            ["", "", ""],
            ["", "", ""]
        ]
        self.player = Player("X")
        self.computer = Computer("O")
        self.current_player = self.player  # Start with the player
        self.game_over = False  # Flag to indicate if the game is over

        # Connect button clicks to the game logic
        for i in range(3):
            for j in range(3):
                self.gui.buttons[i][j].config(command=lambda row=i, col=j: self.button_click(row, col))

    def button_click(self, row, col):
        """Handles button clicks on the game board."""

        if self.game_board[row][col] == "" and not self.game_over:
            if self.current_player == self.player:
                self.current_player.move(self.game_board, self.gui, row, col)  # Player move
                self.current_player = self.computer  # Switch to computer

                # Computer's turn immediately after player's move
                if self.current_player == self.computer and not self.game_over:
                    self.computer.move(self.game_board, self.gui)  # Computer move
                    self.current_player = self.player  # Switch back to player

            self.check_for_winner()  # Check for a winner after each move

    def check_for_winner(self):
        """Checks for a winner or a draw."""

        # Check rows
        for row in self.game_board:
            if row[0] == row[1] == row[2] and row[0] != "":
                self.declare_winner(row[0])
                return

        # Check columns
        for col in range(3):
            if self.game_board[0][col] == self.game_board[1][col] == self.game_board[2][col] and self.game_board[0][col] != "":
                self.declare_winner(self.game_board[0][col])
                return

        # Check diagonals
        if (self.game_board[0][0] == self.game_board[1][1] == self.game_board[2][2] or
            self.game_board[0][2] == self.game_board[1][1] == self.game_board[2][0]) and self.game_board[1][1] != "":
            self.declare_winner(self.game_board[1][1])
            return

        # Check for a draw
        if all(cell != "" for row in self.game_board for cell in row):
            self.declare_winner("Tie")

    def declare_winner(self, winner):
        """Declares the winner and updates the game state."""

        self.game_over = True
        if winner == "Tie":
            self.gui.game_message.set("It's a tie!")
        else:
            self.gui.game_message.set(f"{winner} wins!")

if __name__ == "__main__":
    root = tk.Tk()
    game = TicTacToeGame(root)
    root.mainloop()