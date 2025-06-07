import random

def determine_winner(player_choice, computer_choice):
    if player_choice == computer_choice:
        return "IT'S A TIE!!!"
    elif player_choice == "rock":
        return "You WIN!!!"
    elif player_choice == "scissors":
        return "You WIN!!!" if computer_choice == "rock" else "Computer WINS!!! You LOSE!!!"
    elif player_choice == "paper":
        return "You LOSE!!!"
    else:
        return "Invalid choice. Please choose rock, paper or scissors"

choices = ["rock", "paper", "scissors"]
print("Welcome to the MIND-blowing game of Rock-Paper-Scissors!")
while True:
    player_choice = input("Enter your choice (rock/paper/scissors) or 'quit' to exit:").lower()
    if player_choice == "quit":
        print("Thanks for playing!")
        break
    if player_choice in choices:
        computer_choice = random.choice(choices)
        print("Computer chooses:", computer_choice)
        result = determine_winner(player_choice, computer_choice)
        print(result)
    else:
        print("Invalid choice. Please choose rock, paper or scissors")
        