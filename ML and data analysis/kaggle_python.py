#Python

"""
#Lesson 1: Syntax, Variables and Numbers
alice_candies = 121
bob_candies = 77
carol_candies = 109
#Share 91 candies among Bob, Alice and Carol so that just 1 is left
total = alice_candies + bob_candies + carol_candies
print(total)
amount_left = total % 3
print(amount_left)
#We can also rewrite this code as:
def amount_left(total, nfriends=3):
    return total % nfriends
amount_left(total, 3)
"""

"""
#Lesson 2: Functions and Getting Help
#Try this:
def greet(who='Colin'):
    print('Hello', who)
greet()
greet(who='Kaggle')
greet('world')
#Next, try this functions applied to functions:
def mult_by_5(x):
    return 5*x
def call(fn, arg):
    return fn(arg)
def squared_call(fn, arg):
    return fn(fn(arg))
print(
    call(mult_by_5, 2),
    squared_call(mult_by_5, 2),
    sep="\n"
)
#And this:
def mod_5(x):
    return x % 5
print(
    max(100, 51, 14),
    max(100, 51, 14, key=mod_5),
    sep='\n'
)
"""

#Lesson 3: Booleans and Conditions
#This code returns true or false for a person who wants to run as president depending on their age
def can_run_for_president(age):
    return age >= 35
print("Can a 19-year-old run for president?", can_run_for_president(19))
#Another way to do this:
def president_validator(age):
    if age >= 35:
        return True
    else:
        return False
print("Can a 19-year-old run for president?", president_validator(19))