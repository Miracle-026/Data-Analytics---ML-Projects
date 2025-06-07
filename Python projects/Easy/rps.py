import random

print("==========Welcome to this game of rock paper scissors==========")
print("To play, please select rock/paper/scissors")
user_choice = input("Select rock/paper/scissors: ")
computer_choice = random.choice(['rock', 'paper', 'scissors'])
if user_choice == computer_choice:
    print("It's a tie!")
elif user_choice == 'rock' and computer_choice == 'scissors':
    print("You win")
elif user_choice == 'scissors' and computer_choice == 'paper':
    print("You win")
elif user_choice == 'paper' and computer_choice == 'rock':
    print("You win")
elif user_choice == 'scissors' and computer_choice == 'rock':
    print("You lose")
elif user_choice == 'paper' and computer_choice == 'scissors':
    print("You lose")
elif user_choice == 'rock' and computer_choice == 'paper':
    print("You lose")    
else:
    print("Invalid input")
        
print("Do you want to continue?")
inp = ("Y/N: ")

    