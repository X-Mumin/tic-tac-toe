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
        
        # Connect button clicks to the game logic
        for i in range(3):
            for j in range(3):
                self.gui.buttons[i][j].config(command=lambda row=i, col=j: self.button_click(row, col))

    def button_click(self, row, col):
        """Handles button clicks on the game board."""

        if self.game_board[row][col] == "":
            if self.current_player == self.player:
                self.current_player.move(self.game_board, self.gui, row, col)  # Player move
                self.current_player = self.computer  # Switch to computer

                # Computer's turn immediately after player's move
                if self.current_player == self.computer: 
                    self.computer.move(self.game_board, self.gui)  # Computer move
                    self.current_player = self.player  # Switch back to player

if __name__ == "__main__":
    root = tk.Tk()
    game = TicTacToeGame(root)
    root.mainloop()