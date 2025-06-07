#Day 1: Install Python and set up your coding environment ( IDLE, PyCharm, VSCode, etc.)
print("Done")

#Day 2: Learn basic syntax, data types, and operators in Python
print("Done")

#Day 3: Practice writing Python code using online platforms like LeetCode, HackerRank, or CodeWars

def check_weird(n):
    if n % 2 != 0:
        print("Weird")
    elif n % 2 == 0 and 2 <= n <= 5:  # Check if n is even and in the range of 2 to 5
        print("Not Weird")
    elif n % 2 == 0 and 6 <= n <= 20:  # Check if n is even and in the range of 6 to 20
        print("Weird")
    elif n % 2 == 0 and n > 20:  # Check if n is even and greater than 20
        print("Not Weird")
n = 4
check_weird(n)