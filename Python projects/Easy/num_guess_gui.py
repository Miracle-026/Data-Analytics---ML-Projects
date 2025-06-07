import tkinter as tk
import random

class NumberGuessingGame:
    def __init__(self, master):
        self.master = master
        self.master.title("Number Guessing Game")
        self.secret_number = random.randint(1, 10)
        
        self.label = tk.Label(master, text="Guess a number between 1 and 10:")
        self.label.pack()
        
        self.entry = tk.Entry(master)
        self.entry.pack()
        
        self.guess_button = tk.Button(master, text="Guess", command=self.check_guess)
        self.guess_button.pack()
        
        self.result_label = tk.Label(master, text="")
        self.result_label.pack()
        
        self.play_again_button = tk.Button(master, text="Play Again", command=self.play_again)
        self.play_again_button.pack()
        self.play_again_button.config(state=tk.DISABLED)  # Disable initially

    def check_guess(self):
        try:
            guess = int(self.entry.get())
            if guess < 1 or guess > 10:
                self.result_label.config(text="Please guess a number between 1 and 10.")
                return
            
            if guess == self.secret_number:
                self.result_label.config(text="Correct! You did great!")
                self.play_again_button.config(state=tk.NORMAL)  # Enable play again button
            else:
                self.result_label.config(text="Oh no, try again.")
        except ValueError:
            self.result_label.config(text="Please enter a valid number.")

    def play_again(self):
        self.secret_number = random.randint(1, 10)  # Generate a new secret number
        self.result_label.config(text="")
        self.entry.delete(0, tk.END)  # Clear the entry field
        self.play_again_button.config(state=tk.DISABLED)  # Disable play again button

if __name__ == "__main__":
    root = tk.Tk()
    game = NumberGuessingGame(root)
    root.mainloop()  # Start the Tkinter event loop