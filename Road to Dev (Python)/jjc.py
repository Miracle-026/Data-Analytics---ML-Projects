#write a code that counts 1-20 and prints each on different lines , if the number is divisible by 3 print "fizz" , if its divisible by 5 print "buzz" if its divisible by 15 print "fizz"
for i in range(1, 21):
    if i % 3 == 0:
        print("fizz")
    elif i % 5 == 0:
        print("buzz")
    elif i % 15 == 0:
        print("fizzbuzz")
    else:
        print(i)