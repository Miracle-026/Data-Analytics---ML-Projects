import keyboard
def add(x, y):
    output = x + y
    return output
def sub(x, y):
    output = x - y
    return output
def prod(x, y):
    output = x * y
    return output
def div(x, y):
    output = x / y
    return output

def calculator():
    print("==========CASIO==========")
    print("1. Addition")
    print("2. Multiplication")
    print("3. Multiplication")
    print("4. Division")
    while True:
        user_choice = input("Enter choice (1/2/3/4) or press ESC to quit")
        if keyboard.is_pressed('esc'):
            print("Quitting the program")
            break
        num1 = int(input("Enter a number: "))
        num2 = int(input("Enter a number: "))
        if user_choice == '1':
            print(f"{num1} + {num2} = {add(num1, num2)}")
        elif user_choice == '2':
            print(f"{num1} - {num2} = {sub(num1, num2)}")
        elif user_choice == '3':
            print(f"{num1} * {num2} = {prod(num1, num2)}")
        elif user_choice == '4':
            print(f"{num1} / {num2} = {div(num1, num2)}")
        else:
            print("Invalid input")
        break
            
if __name__ == "__main__":
    calculator()