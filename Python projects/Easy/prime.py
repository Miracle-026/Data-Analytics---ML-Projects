# import math
# def prime_num(num):
#     if num <= 1:
#        return False
#     for i in range(2, int(math.sqrt(num)) + 1):
#         if num % i != 0:
#            return False
#         return True
    
# n = int(input("Enter number:"))
# if prime_num(n):
#     print(f"{n} is a prime number")
# else:
#     print(f"{n} is not a prime")

import math
n = int(input("Enter a number: "))
if n <= 1:
    print(f"{n} is not a prime number")
for i in range(2, int(math.sqrt(n)) + 1):
    if n % i == 0:
        print(f"{n} is a prime number")
    else:
        print(f"{n} is not a prime number")