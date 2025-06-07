import tkinter as tk
import random

def play_rps(user_choice):
    choices = ["rock", "paper", "scissors"]
    computer_choice = random.choice(choices)

    result = ""

    if user_choice == computer_choice:
        result = "It's a tie!"
    elif (
        (user_choice == "rock" and computer_choice == "scissors") or
        (user_choice == "paper" and computer_choice == "rock") or
        (user_choice == "scissors" and computer_choice == "paper")
    ):
        result = "You win!"
    else:
        result = "You lose!"

    result_label.config(text=f"Computer chose {computer_choice}. {result}")

# GUI setup
root = tk.Tk()
root.title("Rock-Paper-Scissors Game")

# Labels
label = tk.Label(root, text="Choose your move:")
label.pack(pady=10)

# Radio buttons
selected_option = tk.StringVar(value="")

rock_button = tk.Radiobutton(root, text="Rock", variable=selected_option, value="rock")
rock_button.pack(pady=5)

paper_button = tk.Radiobutton(root, text="Paper", variable=selected_option, value="paper")
paper_button.pack(pady=5)

scissors_button = tk.Radiobutton(root, text="Scissors", variable=selected_option, value="scissors")
scissors_button.pack(pady=5)

# Result label
result_label = tk.Label(root, text="")
result_label.pack(pady=10)

#Play button
play_button = tk.Button(root, text="Play", command=lambda: play_rps(selected_option.get()))
play_button.pack(pady=10)

# Run the GUI
root.mainloop()
