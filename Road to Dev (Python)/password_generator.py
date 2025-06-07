import random
import string

def generate_random_string(length=16):
    characters = string.ascii_letters + string.digits
    random_string = ''.join(random.choice(characters) for _ in range(length))
    return random_string

# Call the function each time you need a new random string
print("Random string:", generate_random_string())
print("Random string:", generate_random_string())
print("Random string:", generate_random_string())
