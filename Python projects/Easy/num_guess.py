import random
def num_guess():
    while True:
        print("I just thought of a number between 1 to 10.\n Can you guess it?")
        num_in = int(input("Enter your guess: "))
        num_act = random.randint(1, 10)
        if num_in == num_act:
            print("Correct! You did great!")
        else:
            print("Oh no, try again.")
        print("Do you want to know what the number is? (y/n)")
        choice = input()
        if choice == 'y':
            print(f"Ok. The actual number is {num_act}")
        else: 
            print("OK suit yourself.")
        print("Do you want to guess again? (y/n)")
        choice1 = input()
        if choice1 != 'y':
            print("Thanks for playing")
            break
        
        
        
if __name__ == "__main__":
    num_guess()