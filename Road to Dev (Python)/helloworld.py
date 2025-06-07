#!/bin/python3
#Introduction
print("Hello, World!")
print("I am Onuchukwu Chukwuanugo Miracle")
#Variables and Indentation
if 5 > 2 :
     print("Five is greater than two!")
x = 5
y = "Hello, World!"
#Comments
#This is a comment.
print("Hello, World!")
print("Hello, World!")
#This is a comment.
#print("Hello, World!")
print("Cheers, Mate!")
#This is a comment
#written in
#more than just
#one line
print("Hello, World!")
"""
This is a comment
written in more than just
one line
"""
print("Hello, World!")
#Variables
x = 5
y = "John"
print (x)
print (y)
x = 4   # x is of type int
x = "Sally"   # x is now of type str
print(x)
x = str(3)   # x will be '3'
y = int('3')  # y will be 3
z = float(3)   # z will be 3.0
x = 5
y = "John"
print(type(x))
print(type(y))
x = "dC"
# is the same as 
x = 'dC'
a = 4
A = "Sally"
#A will not overwrite a
print(a)
print(A)
A = 4
A = "Sally"
#A will now overwrite a
print(A)
print(A)
myvar = "De Caprio"
my_var = "DC"
_my_var = "De CAPRIO"
myVar = "DE CAPRIO"
MYVAR = "DE Caprio"
myvar2 = "De CAprio"
print(myvar)
print(my_var)
print(_my_var)
print(myVar)
print(MYVAR)
print(myvar2)
print("Variables are case sensitive. They can be alpha-numeric (i.e contain letters and numbers) and can also contain underscores. For a legal variable, numbers must come after letters not before them.")        
myVariableName = "De Caprio (Camel case)"
MyVariableName = "DE CAPRIO (Pascal case)"
my_variable_name = "de caprio (Snake case)"
print(myVariableName)
print(MyVariableName)
print(my_variable_name)
x, y, z = "Orange", "Banana", "Pineapple"
print(x)
print(y)
print(z)
print("The above is assigning multiple values to multi-variables.")
x = y = z = "Orange"
print(x)
print(y)
print(z)
print("The above is assigning a value to multi-variables.")
fruits = ["apple", "cherry", "soursop"]
x, y, z = fruits
print(x)
print(y)
print(z)
print("The above is unpacking. I unpacked from the list (fruits) and assigned each of the values (apple, cherry and soursop) to the variables (x, y and z respectively.")
x = "awesome"
print("Python is " + x)
x = "Python is"
y = " awesome"
z = x + y
print(z)
print("Here, I am adding a variable to another variable.")
x = 10
y = 7
z = x + y
print(z)
print("You can't combine a string value and an integer. You can only combine strings with strings or integers with integers.")
x = "awesome"
def myfunc():
  print("Python is " + x)
myfunc() 
x = "awesome"

def myfunc():
  x = "fantastic"
  print("Python is " + x)

myfunc()

print("Python is " + x) 
x = "awesome"

def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x) 
carname = "Volvo"
print(carname)
x = {"name" : "John", "age" : 36}
print(type(x))
x = True
print(type(x))
x = "Hello world"
print(len(x))
txt = "Hello world"
x = txt[0]
txt = "Hello world"
x = txt[2:5]
txt = "Hello world"
x = txt.upper()
print(x)
txt = "Hello world"
x = txt.replace("H", "J")
print(x)
if 5 != 10:
   print("APPLES AND ORANGES")
txt = "APPLES AND ORANGES"
x = txt.lower()
print(x)
print("These are the data types in python. str for text, int, float and complex for numbers, list, tuple and range for sequence, dict for mapping, set and frozenset for sets, bool for boolean, bytes, bytearray and memoryview for binary.")
x = 5
print(type(x))
x = "Hello World!"
x = 20
x = 20.5
x = 1j
x = [ "apple", "banana", "cherry" ]
x = ( "apple", "banana", "cherry" )
x = range(6)
x = { "name" : "John", "age" : 36 }
x = { "apple", "banana", "cherry" }
x = frozenset ({ "apple", "banana", "cherry" })
x = True
x = b"Hello"
x = bytearray(5)
x = memoryview(bytes(5))
#Numbers
x = str("HELLO WORLD!")
x = int(20)
x = float(2.5)
x = complex(1j)
x = list(("apple", "banana", "cherry"))
x = tuple(("apple", "banana", "cherry"))
x = range(6)
x = dict(name="John", age=36)
x = set(("apple", "banana", "cherry"))
x = frozenset(("apple", "banana", "cherry"))
x = bool(5)
x = bytes(5)
x = bytearray(5)
x = memoryview(bytes(5))
a = 748849493839384494049404895738   #a is an int
print(a)
b = 838384748493928394948.9289384938938   #b is a float
print(b)
c = 893839348e93   #To add an exponential
print(c)
d = 93938E34   #To add an exponential
print(d)
e = 34+8j
print(e)
x = 24
a = float(24)
print(a) 
q = 26.0
b = int(q)
print(b)
r = 29
d = complex(r)
print(d)
u = 90.0
e = complex(u)
print(e)
print("Remember that you cannot convert from complex to another data type")
import random
print(random.randrange(1,10))
print("Use the above syntax to import random numbers")
x = str(20.0)
z = int("3")
c = float("24")
print(x)
print(z)
print(c)
a = """Lorem ipsum dolor sit amet,
consectetur adipiscing eli,
sed do eiusmod empor incicididun u labore e dolore mana aliqua."""
print(a)
b = "Good morning fam"
print(b[1])   #To get a character at a specified position
for x in "banana":
	print(x)
print("The above syntax is a loop syntax which prints the characters of a word line by line.")
p = "The best things in life are free!"
print("free" in p) 
print("The above syntax is a string-checker syntax which returns true if a particular phrase or character is found in a string.")
l = "The best things in life are free!"
if "free" in l:
   print(l)   
print("We can also use the if statement to perform the loop.")
p = "The best things in life are free!"
print("free" not in p) 
l = "The best things in life are free!"
if "free" in l:
   print(l)  
o = "The best things in life are free!"
if "expensive" not in o:
   print(o)   
print("We can use the not in statement to check if a phrase or character is absent in a string.")
m =  "Good morning fam"
print(m[2:5])
print("The above which is a slice syntax which returns a range of characters excluding the last position.")
m =  "Good morning fam"
print(m[:5])   #slice from the start
m =  "Good morning fam"
print(m[2:])   #slice to the end
m =  "Good morning fam"
print(m[-5:-2])
t = "Good morning fam"
print(t.upper())
t = "Good morning fam"
print(t.lower())
t = " Good morning fam "
print(t.strip())   #strip statement removes any space before or after the string
t = "Good morning fam"
print(t.replace("morning", "afternoon"))  
t = "Good morning,fam"
print(t.split(","))
a = "Good"
b = "Morning"
c = a + " " + b   #" " adds space between the two variables
print(c) 
age = 17
h = "My name is Miracle and I'm {}"
print(h.format(age))   #The format statement concatenates string and integers, as ordinary concatenation cannot
item_name = "NESCAFE"
item_no = 577
price = 50
myorder = "I want to pay {} dollars in purchase of {} with item number as {}"
print(myorder.format(price, item_name, item_no))
a = "We are \"Vikings\" that originate from the north."
print(a)
#\' 	Single Quote 	
#\\ 	Backslash 	
#\n 	New Line 	
#\r 	Carriage Return 	
#\t 	Tab 	
#\b 	Backspace 	
#\f 	Form Feed 	
#\ooo 	Octal value 	
#\xhh 	Hex value 	

#Method 	Description
#capitalize()	Converts the first character to upper case
#casefold()	Converts string into lower case
#center()	Returns a centered string
#count()	Returns the number of times a specified value occurs in a string
#encode()	Returns an encoded version of the string
#endswith()	Returns true if the string ends with the specified value
#expandtabs()	Sets the tab size of the string
#find()		Searches the string for a specified value and returns the position of where it was found
#format()	Formats specified values in a string
#format_map()	Formats specified values in a string
#index()	Searches the string for a specified value and returns the position of where it was found
#isalnum()	Returns True if all characters in the string are alphanumeric
#isalpha()	Returns True if all characters in the string are in the alphabet
#isdecimal()	Returns True if all characters in the string are decimals
#isdigit()	Returns True if all characters in the string are digits
#isidentifier()	Returns True if the string is an identifier
#isinstance	Determines if an object is of a certain data type
#islower()	Returns True if all characters in the string are lower case
#isnumeric()	Returns True if all characters in the string are numeric
#isprintable()	Returns True if all characters in the string are printable
#isspace()	Returns True if all characters in the string are whitespaces
#istitle() 	Returns True if the string follows the rules of a title
#isupper()	Returns True if all characters in the string are upper case
#join()		Joins the elements of an iterable to the end of the string
#ljust()	Returns a left justified version of the string
#lower()	Converts a string into lower case
#lstrip()	Returns a left trim version of the string
#maketrans()	Returns a translation table to be used in translations
#partition()	Returns a tuple where the string is parted into three parts
#replace()	Returns a string where a specified value is replaced with a specified value
#rfind()	Searches the string for a specified value and returns the last position of where it was found
#rindex()	Searches the string for a specified value and returns the last position of where it was found
#rjust()	Returns a right justified version of the string
#rpartition()	Returns a tuple where the string is parted into three parts
#rsplit()	Splits the string at the specified separator, and returns a list
#rstrip()	Returns a right trim version of the string
#split()	Splits the string at the specified separator, and returns a list
#splitlines()	Splits the string at line breaks and returns a list
#startswith()	Returns true if the string starts with the specified value
#strip()	Returns a trimmed version of the string
#swapcase()	Swaps cases, lower case becomes upper case and vice versa
#title()	Converts the first character of each word to upper case
#translate()	Returns a translated string
#upper()	Converts a string into upper case
#zfill()	Fills the string with a specified number of 0 values at the beginning

print(10 > 9)
print(10 == 9)
print(10 < 9)
a = 200
b = 33
if b > a:
  print("b is greater than a")
else:
  print("b is not greater than a") 
print(bool("Hello"))
print(bool(15))
x = "Hello"
y = 15
print(bool(x))
print(bool(y))
#Almost any value is evaluated to True if it has some sort of content.
#Any string is True, except empty strings.
#Any number is True, except 0.
#Any list, tuple, set, and dictionary are True, except empty ones.
bool(False)
bool(None)
bool(0)
bool("")
bool(())
bool([])
bool({}) 
class myclass():
  def __len__(self):
    return 0
myobj = myclass()
print(bool(myobj))    #This will return false
def myFunction() :
  return True

print(myFunction()) 
x = 200
print(isinstance(x, int)) 

#+ 	Addition 	x + y 	
#- 	Subtraction 	x - y 	
#* 	Multiplication 	x * y 	
#/ 	Division 	x / y 	
#% 	Modulus 	x % y 	
#** 	Exponentiation 	x ** y 	
#// 	Floor division 	x // y   #arithmetic operators

#= 	x = 5 	x = 5 	
#+= 	x += 3 	x = x + 3 	
#-= 	x -= 3 	x = x - 3 	
#*= 	x *= 3 	x = x * 3 	
#/= 	x /= 3 	x = x / 3 	
#%= 	x %= 3 	x = x % 3 	
#//= 	x //= 3 	x = x // 3 	
#**= 	x **= 3 	x = x ** 3 	
#&= 	x &= 3 		x = x & 3 	
#|= 	x |= 3 		x = x | 3 	
#^= 	x ^= 3 		x = x ^ 3 	
#>>= 	x >>= 3 	x = x >> 3 	
#<<= 	x <<= 3 	x = x << 3   #assignment operators

#== 	Equal 		x == y 	
#!= 	Not equal 	x != y 	
#> 	Greater than 	x > y 	
#< 	Less than 	x < y 	
#>= 	Greater than or equal to 	x >= y 	
#<= 	Less than or equal to 		x <= y   #comparison operators

#and  	Returns True if both statements are true 			x < 5 and  x < 10 	
#or 	Returns True if one of the statements is true 			x < 5 or x < 4 	
#not 	Reverse the result, returns False if the result is true 	not(x < 5 and x < 10)   #logical operators

#is  		Returns True if both variables are the same object 	x is y 	
#is not 	Returns True if both variables are not the same object 	x is not y   #identity operators

#in  		Returns True if a sequence with the specified value is present in the object 		x in y 	
#not in 	Returns True if a sequence with the specified value is not present in the object 	x not in y   #membership operators

#&  	AND 		Sets each bit to 1 if both bits are 1
#| 	OR 		Sets each bit to 1 if one of two bits is 1
# ^ 	XOR 		Sets each bit to 1 if only one of two bits is 1
#~  	NOT 		Inverts all the bits
#<< 	Zero fill left shift 	Shift left by pushing zeros in from the right and let the leftmost bits fall off
#>> 	Signed right shift 	Shift right by pushing copies of the leftmost bit in from the left, and let the rightmost bits fall off   #bitwise operators

mylist = ["money", "woman", "sleep", "food", "games"]
print(mylist)
mylist = ["money", "woman", "sleep", "food", "games", "money", "woman", "sleep", "food", "games"]
print(mylist)
mylist = ["woman", 23000000, "food", True]
print(mylist)
myvar = list(("money", "woman", "sleep", "food", "games"))   #the list constructor can be used to make lists (notice the double brackets)
print(myvar)
thislist = list(('apple', 'banana', 'cherry', 'garden egg'))
if 'banana' in thislist:
   print('Banana is a fruit')
else:
   print('Banana for life')
thislist[1] = 'moi moi'
print(thislist)
thislist[1:3] = ['moi moi', 'akamu']
print(thislist)
thislist[1:4] = ['moi moi', 'akamu', 'groundnut']
print(thislist)
thislist[1:4] = ['groundnut']
print(thislist)
thislist = list(('apple', 'banana', 'cherry', 'garden egg'))
thislist.insert(2, 'cucumber')
print(thislist)
thislist = list(('apple', 'banana', 'cherry', 'garden egg'))
thislist.append('cucumber')   #cucumber will appear at the end of the string
print(thislist)
thislist = list(('apple', 'banana', 'cherry', 'garden egg'))
myvar = list(("money", "woman", "sleep", "food", "games"))
thislist.extend(myvar)   #myvar will become part of thislist
print(thislist)
thislist = list(('apple', 'banana', 'cherry', 'garden egg'))
thistuple = ('kiwi', 'plum', 'lemon')
thislist.extend(thistuple)
print(thislist) 
thislist.remove('plum')   #plum will be removed from the list ['apple', 'banana', 'cherry', 'garden egg', 'kiwi', 'lemon']
print(thislist) 
thislist.pop(4)   #same goes here 
print(thislist)
thislist.pop()   #if no index is specified, the last item will be removed from the list 
print(thislist)
del thislist[0]
print(thislist)
del thislist
thislist = list(('apple', 'banana', 'cherry', 'garden egg'))
thislist.clear()
print(thislist)
#del totally deletes the list so that it ceases to exist while clear() deletes just the content of the list
thislist = list(('apple', 'banana', 'cherry', 'garden egg'))
for x in thislist:
   print(x) 
thislist = list(('apple', 'banana', 'cherry', 'garden egg'))
for i in range(len(thislist)):
   print(thislist[i])
thislist = list(('apple', 'banana', 'cherry', 'garden egg'))
i = 0
while i < len(thislist):
   print(thislist[i])
   i = i + 1
thislist = list(('apple', 'banana', 'cherry', 'garden egg'))
[print(x) for x in thislist] 
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []
for x in fruits:
	if "a" in x:
		newlist.append(x)   #this will create a new list that contains only the letter "a"
print(newlist)

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x for x in fruits if "a" in x]
print(newlist)

newlist = [x for x in fruits if x != "apple"]
print(newlist)

newlist = [x for x in fruits if x == "apple"]
print(newlist)

newlist = [x for x in fruits]
print(newlist)

newlist = [x for x in range(10)]
print(newlist)

newlist = [x for x in range(10) if x < 5]
print(newlist)

newlist = [x.upper() for x in fruits]
print(newlist)

newlist = ['hello' for x in fruits]
print(newlist)

newlist = [x if x != "banana" else "orange" for x in fruits]
print(newlist)

newlist = [x if x != "udala" else "orange" for x in fruits]
print(newlist)

thislist = list(('yam', 'apple', 'banana', "udala", 'cherry', 'garden egg'))
thislist.sort()
print(thislist)


thislist = list(('yam', 'apple', 'banana', "udala", 'cherry', 'garden egg'))
thislist.sort(reverse = True)
print(thislist)

def myfunc(n):
	return abs(n - 50)
thislist = [100, 50, 65, 82, 23]
thislist.sort(key = myfunc)
print(thislist)

thislist = list(('apple', 'Orange', 'banana', 'Mango', 'date'))
thislist.sort()
print(thislist)

thislist = list(('apple', 'Orange', 'banana', 'Mango', 'date'))
thislist.sort(key = str.lower)
print(thislist)

thislist = list(('yam', 'apple', 'banana', "udala", 'cherry', 'garden egg'))
thislist.reverse()
print(thislist)

thislist = list(('yam', 'apple', 'banana', "udala", 'cherry', 'garden egg'))
mylist = ['water', 'rice', 'beans', 'abacha']
thislist = mylist
print(mylist) 

thislist = list(('yam', 'apple', 'banana', "udala", 'cherry', 'garden egg'))
mylist = ['water', 'rice', 'beans', 'abacha']
thislist = mylist.copy()
print(mylist) 

thislist = list(('yam', 'apple', 'banana', "udala", 'cherry', 'garden egg'))
mylist = list(thislist)
print(mylist)

thislist = list(('yam', 'apple', 'banana', "udala", 'cherry', 'garden egg'))
mylist = ['water', 'rice', 'beans', 'abacha']
omnilist = thislist + mylist
print(omnilist)

thislist = list(('yam', 'apple', 'banana', "udala", 'cherry', 'garden egg'))
mylist = ['water', 'rice', 'beans', 'abacha']
for x in mylist:
	thislist.append(x)
print(thislist)

thislist = list(('yam', 'apple', 'banana', "udala", 'cherry', 'garden egg'))
mylist = ['water', 'rice', 'beans', 'abacha']
thislist.extend(mylist)
print(thislist)

#listmethods
#append()	adds an element at the end of the list
#clear()	removes all the elements from the list
#copy()		returns a copy of the list
#count() 	returns the number of elements with the specified value
#extend()	adds the elements of a list or iterable to the end of a current list
#index()	returns the index of the first element with the specified value
#insert		adds an element at the specified position
#pop()		removes the element at the specified position
#remove()	same as pop
#reverse() 	reverses the order of the list
#sort()		sorts the list 

thistuple = ("apple", "banana", "cherry", "apple", "cherry")
print(thistuple) 

#to create a tuple with only one item, add a comma or the tuple will be invalid
tuple1 = ("apple",)	#valid tuple
print(tuple1)
print(type(tuple1))
tuple2 = ("apple")	#invalid tuple
print(tuple2)
print(type(tuple2)) 

tuple3 = tuple(("anime", "manga", "porn", "comedy", "vskit"))
print(tuple3)
print(tuple3[1])
print(tuple3[-1])
print(tuple3[2:5])
print(tuple3[:4])
print(tuple3[2:])
print(tuple3[-4:-1])

tuple3 = tuple(("anime", "manga", "porn", "comedy", "vskit"))
if 'anime' in tuple3:
	print("I LOVE ANIME")
else:
	print("I HATE PEOPLE WHO HATE ANIME")  

#tuples are clearly unchangeable, but you can change them by changing the tuple to a list, make the necessary changes and convert it back to a tuple
tuple3 = tuple(("anime", "manga", "porn", "comedy", "vskit"))
list3 = list(tuple3)
list3.pop(2)
tuple3 = tuple(list3)
print(tuple3) 

tuple4 = ("football", "avatar", "golden morn")
(sport, movie, beverage) = tuple4
print(sport)
print(movie)
print(beverage)

tuple4 = ("football", "avatar", "golden morn", "cornflakes", "milo/milk")
(sport, movie, *beverage) = tuple4
print(sport)
print(movie)
print(beverage)

tuple4 = ("football", "avatar", "naruto", "jujutsu kaisen", "golden morn")
(sport, *movie, beverage) = tuple4
print(sport)
print(movie)
print(beverage)

fruituple = ("apple", "banana", "cherry", "garden egg")
for x in fruituple:
	print(x) 

fruituple = ("apple", "banana", "cherry", "garden egg")
for i in range(len(fruituple)):
	print(fruituple[i])

fruituple = ("apple", "banana", "cherry", "garden egg")
i = 0
while i < len(fruituple):
	print(fruituple[i])
	i = i + 1
print(fruituple * 2)

#tuple methods
#count	returns the number of times a specified value occurs in a tuple
#index	searches the tuple for a specified value and returns the position where it was found

#next = set
thisset = {"apple", "orange", "banana", "kiwi", "lemon", "lime", "mango", "tiger nut"}
print(thisset)
print(type(thisset))
print(len(thisset))
myset = set(("tiger nut", "orange", "lime", "banana", "lemon", "kiwi", "mango", "apple"))
for x in thisset:
    print(x)
myset = set(("tiger nut", "orange", "lime", "banana", "lemon", "kiwi", "mango", "apple"))
print("banana" in myset)
#or
if "banana" in myset:
	print("I LOVE BANANA")
else:
    print("False")
thisset.add("cucumber")
print(thisset)
myset.update(thisset)
print(myset)
mylist = list(("date", "coconut", "groundnut"))
myset.update(mylist)
print(myset)
myset.discard("kiwi")
print(myset)
myset.pop() 
print(myset)
thisset.clear()
print(thisset)
klass = set(("carbohydrates", "proteins", "vitamins", "minerals", "water", "fats and oil", "roughages"))
typo = set(("fruits", "vegetables", "nuts"))
fruitset = klass.union(typo)
print(fruitset)
thisset = {"cucumber", "orange", "banana", "kiwi", "lemon", "lime", "mango", "tiger nut"}
myset = set(("tiger nut", "orange", "lime", "banana", "lemon", "kiwi", "mango", "apple"))
myset.intersection_update(thisset)
print(myset)
myset.intersection(thisset)
print(myset)
myset.symmetric_difference_update(thisset)
print(myset)
thisset = {"cucumber", "orange", "banana", "kiwi", "lemon", "lime", "mango", "tiger nut"}
myset.symmetric_difference(thisset)
print(myset)
#add()				adds an element to the set
#clear()			removes all elements of a set
#copy()				returns the copy of a set
#difference()			returns a set containing the difference between two or more sets
#difference_update()		removes the items in a set that are also included in another specified set
#discard()			removes the specified item
#intersection()			returns a set that is the intersection of two other sets
#intersection_update		removes the items in a set that are not present in other specified sets
#issubset()			returns whether another set contains this set or not
#issuperset()			same as issubset
#pop()				removes an element from the set
#remove()			removes the specified element
#symmetric_difference		returns a set with the symmetric difference of two sets
#symmetric_difference_update()	inserts the symmetric differences from this set and another
#union()			returns a set containing the union of sets
#update()			updates the set with the union of this set and others 	

thisdict = {
	"brand" : "Ford",
	"model" : "Mustang",
	"year" : 1964
}
print(thisdict) 
print(thisdict["brand"])
print(len(thisdict))
cardict = {
     "brand" : "Toyota",
     "automatic" : False,
     "manual" : True,
     "model" : "Carinae",
     "year of production" : "2000",
     "colors" : ["electronic blue", "crimson"]
}
print(cardict)
x = cardict["model"]
print(x)
y = cardict.get("colors")
print(y)
z = cardict.keys()
print(z)
cardict["type"] = "Type C"
print(z)
a = cardict.values()
print(a)
cardict["net worth"] = "$200b"
print(a)
b = cardict.items()
print(b)
cardict["id no"] = 20007098
print(b)
if "type" in cardict:
     print("This Toyota Carinae is a type C")
else:
     print("Wrong Card")
cardict["year of production"] = 1991
print(cardict) 
cardict.update({"year of production" : 2000})
print(cardict)
cardict.pop("net worth")
print(cardict)
cardict.popitem()
print(cardict)
del cardict["automatic"]
print(cardict)
for x in cardict:
	print(x)
for x, y in cardict.items():
	print(x, y)
thisdict = cardict.copy()
print(thisdict)
mydict = dict(cardict)
print(mydict)
onuchukwu_family = {
	"parents" : {
     	"names" : ["Dr Chika", "Mrs Adaobi"]
     	},
     	"children" : {
     	"names" : ["Sarah", "Chukwuanugo", "Kristyna", "Praise"]
     	}
}
print(onuchukwu_family)

father = {
	"name" : "Dr Onuchukwu Chika",
	"DOB" : 1970
}
mother = {
	"name" : "Mrs Onuchukwu Adaobi",
	"DOB" : 1979
}
child_1 = {
	"name" : "Sarah",
	"DOB" : 2000
}
child_2 = {
	"name" : "Chukwuanugo",
	"DOB" : 2005
}
child_3 = {
	"name" : "Kristyna",
	"DOB" : 2009
}
child_4 = {
	"name" : "Praise",
	"DOB" : 2011
}
myfamily = {
	"father" : father,
	"mother" : mother,
	"1st child" : child_1,
	"2nd child" : child_2,
	"3rd child" : child_3,
	"4th child" : child_4
}
print(myfamily)

#dictionary methods
#clear()	removes all elements from the dictionary
#copy()		returns a copy of the dictionary
#fromkeys()	returns a dictionary with the specified keys and values
#get()		returns the value of the specified keys
#items()	returns a list containing a tuple for each key value pair
#keys		returns a list containing the dictionary's keys
#pop()		removes the element with the specified key
#popitem()	removes the last inserted key value pair
#setdefault()	returns the value of the specified key. If the key does not exist, insert the key with the specified value
#update()	updates the dictionary with the specified key-value pairs
#values()	returns a list of all values in the dictionary

a = 20
b = 40
if b > a:
	print("b is greater than a")
elif a == b:
	print("a is equal to b")
a = 20
b = 20
if b > a:
	print("b is greater than a")
elif a == b:
	print("a is equal to b")	
c = 200
d = 50
if d > c:
	print("d is greater than c")
elif c == d:
	print("c is equal to d")
else:
	print("c is greater than d")
if c > d: print("c is greater than d")
x = 2
y = 6
print("X") 
print("Y")
m = 330
n = 330
print("M") 
print("=") 
print("N")
a = 200
b = 33
c = 500
if a > b and b < c:
	print("Both conditions are true")
a = 200
b = 33
c = 500
if a < b or b < c:
	print("At least, one of the conditions are true")
x = 41
if x > 10:
	print("x is above 10")
	if x > 20:
		print("and also above 20")
	else:
		print("but below 20")
g = 17
h = 18
if h > g:
	pass
else: 
	fail

i = 1
while i < 6:
	print(i)
	i += 1
i = 1 
while i < 6:
	print(i)
	if i ==3:
		break	
	i += 1
i = 0
while i > 6:
	i += 1
	if i == 3:
		continue
	print(i)
i = 1
while i < 6:
	print(i)
	i += 1
else:
	print("i is no longer less than 6")

fruits = ["apple", "banana", "cherry"]
for x in fruits:
	print(x)
	if x == "banana":
		break
fruits = ["apple", "banana", "cherry"]
for x in fruits:
	print(x)
	if x == "banana":
		continue
adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]
for x in adj:
	for y in fruits:
		print(x, y)

def my_function():
	print("Hi there")
def my_function(fname):
	print(fname + "Refsnes")
my_function("Emily\t")
my_function("Tobias\t")
my_function("Linus\t")
def my_function(fname, lname):
	print(fname + " " + lname)
my_function("Chukwuanugo", "Onuchukwu")
def family_function(*kids):
	print("The youngest child is" + kids[2])
family_function("Emily", "Tobias", "Linus")
def alpha_function(child1, child2, child3, child4):
	print("The oldest child is " + child1)
	print("The youngest child is " + child4)
alpha_function(child1 = "Sarah", child2 = "Chukwuanugo", child3 = "Kristyna", child4 = "Praise")
def beta_function(**kid):
	print("His first name is " + kid["fname"], "and his last name is " + kid["lname"])
beta_function(fname = "Tobias", lname = "Refsnes")
def country_function(country = "Nigeria"):
	print("I am from " + country)
country_function("Sweden")
country_function("India")
country_function()
country_function("Brazil")
def food_function(food):
	for x in food:
		print(x)
fruits = ['apple', 'banana', 'cherry']
food_function(fruits)
def maths_function(x):
	return 5 * x
print(maths_function(3))
print(maths_function(5))
print(maths_function(9))

def tri_recursion(k):
	if(k > 0):
		result = k + tri_recursion(k - 1)
		print(result)
	else:
		result = 0
	return result
print("\nRecursion Example Results")
tri_recursion(6)

x = lambda a : a + 10
print(x(5))
x = lambda a, b : a * b
print(x(5, 6))
x = lambda a, b, c, d, e : a + b - c * d /e
print(x(5, 6, 7, 8, 9))
def myfunc(n):
	return lambda a : a * n
mydoubler = myfunc(2)
print(mydoubler(11)) 
print(mydoubler(20)) 
def maicfunc(n):
	return lambda a : a * n
tripler = maicfunc(3)
print(tripler(10))
def myfunc(n):
	return lambda a : a * n
mydoubler = myfunc(2)
tripler = myfunc(3)
print(mydoubler(20)) 
print(tripler(10))

mycars = ["Ford", "Toyota", "BMW", "Mercedes Benz", "Nissan", "Volvo", "Peugeot"]
x = mycars[0]
print(x)
mycars[6] = "Range Rover"
print(mycars)
for x in mycars:
	print(x)  
mycars.append("Honda")
mycars.pop(6)
mycars.remove("Volvo")
print(mycars)

class SS3:
	x = 5
print(SS3)
p1 = SS3()
print(p1.x)
class person:
	def __init__(self, name, age):
		self.name = name
		self.age = age
p1 = person("John", 36)
print(p1.name)
print(p1.age)
print(p1.name, p1.age)
class person:
	def __init__(self, name, age):
		self.name = name
		self.age = age
	def myfunc(self):
		print("Hello there. My name is " + self.name, "and I'm " + self.age)
p1 = person("Chukwuanugo", "17")
p1.myfunc()
class pupil:
	def __init__(mybestsubject, name, subject):
		mybestsubject.name = name
		mybestsubject.subject = subject
	def intro(mybestsubject):
		print("My name is " + mybestsubject.name, "and my best subject is " + mybestsubject.subject)
p2 = pupil("Kristyna", "Basic Science")
p2.intro()
p1.age = 40
del p1.age
class Person:
	def __init__(self, fname, lname):
		self.firstname = fname
		self.lastname = lname
	def printname(self):
		print(self.firstname, self.lastname)
x = Person("John", "Doe")
x.printname()
class Student(Person):
	pass 
x = Student("Jay", "Henderson")
x.printname() 
class Person:
	def __init__(self, fname, lname):
		self.firstname = fname
		self.lastname = lname
	def printname(self):
		print(self.firstname, self.lastname)
x = Person("John", "Doe")
x.printname()
class Student(Person):
	def __init__(self, fname, lname, year):
		super().__init__(fname, lname)
		self.firstname = fname
		self.lastname = lname
		self.graduationyear = year	
	def name(self):
		print(self.firstname, self.lastname, self.graduationyear)
	def welcome(self):
		print("Welcome", self.firstname, self.lastname, "to the class of", self.graduationyear)
x = Student("Mike", "Olsen", 2019)
x.name()
x.welcome()

tuple_1 = ("Apple", "Banana", "Cherry", "Date", "Garden egg")
it_1 = iter(tuple_1)
print(next(it_1))
print(next(it_1))
print(next(it_1))
str_1 = "Tiger nut"
it_2 = iter(str_1)
print(next(it_2))
print(next(it_2))
print(next(it_2))
print(next(it_2))
print(next(it_2))
print(next(it_2))
print(next(it_2))
print(next(it_2))
print(next(it_2))
class MyNumbers:
	def __iter__(self):
		self.a = 1
		return self
	def __next__(self):
		x = self.a
		self.a += 1
		return x
myclass = MyNumbers()
myiter = iter(myclass)
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
class MyNumbers:
	def __iter__(self):
		self.a = 1
		return self
	def __next__(self):
		if self.a <= 20:
			x = self.a
			self.a += 1
			return x
		else:
			raise StopIteration
myclass = MyNumbers()
myiter = iter(myclass)
for x in myiter:
	print(x)


def func():
	x = 300
	print(x)
func()
def func_1():
	x = 300
	def inner_func_1():
		print(x)
	inner_func_1()
func_1()
a = 400
def func_2():
	print(a)
func_2()
print(a)
b = 500
def func_3():
	b = 550
	print(b)
func_3()
print(b)
def func_4():
	global c
	c = 600
	print(c)
func_4()
print(c)
d = 700
def func_5():
	global d
	d = 750
	print(d)
func_5()
print(d)

#Modules
import module1
module1.greeting("Jonathan")
import module1
a = module1.person1["age"]
print(a)
import module1 as mx
b = mx.person1["age"]
print(b)
import platform
x = platform.system()
print(x)
import platform
y = dir(platform)
print(y)
import module1
z = dir(module1)
print(z)
from module1 import person1
print(person1)
print(person1["age"])
import datetime
x = datetime.datetime.now()
print(x)
print(x.year)
print(x.strftime("%A"))
import datetime
x = datetime.datetime(2020, 4, 1, 12, 16, 20)
print(x)
import datetime
n = datetime.datetime(2005, 3, 4)
print(n.strftime("%c"))
#%a	weekday(shortversion)
#%A	weekday(longversion)
#%b	month name(shortversion)
#%B	month name(longversion)
#%c	local version of date and time
#%C	century
#%d	day of the month(01-31)
#%f	microsecond(000000-999999)
#%G	ISO 8601 year
#%H	hour(00-23)
#%I	hour(00-12)
#%j	day number of the year(001-365)
#%m	month(01-12)
#%M 	minute(00-59)
#%p	AM/PM
#%S	second(00-59)
#%u 	ISO 8601 weeekday(1-7)
#%U	week number of the year(00-53, sunday as first day of the week)
#%V	ISO 8601 weeknumber(01-53)
#%w	weekday as numbers 0-6(sunday is 0)
#%W	week number of the year(00-53, monday as first day of the week)
#%x	local version of date and time
#%y	year(shortversion without century)
#%Y	year(fullversion)
#%z	UTC offset
#%Z	timezone
#%% 	a % character

x = min(5, 10, 15)
y = max(20, 40, 60)
print(x)
print(y)
z = abs(-7.25)
print(z)
a = pow(4, 3)
print(a)
import math
b = int(math.sqrt(64))
print(b)
c = math.ceil(1.4)
d = math.floor(1.4)
print(c)
print(d)
e = math.pi
print(e)


import json
e = '{ "name":"John", "age":30, "city":"New York"}'
f = json.loads(e)
print(f["age"])
print(f)
g = {
	"name" : "John",
	"age" : 30,
	"city" : "New York"
}
h = json.dumps(g)
print(h)
#we can convert dicts, lists, tuples, strings, int's, floats, True, False, None from python objects to json
print(json.dumps(["apple", "banana", "cherry", "date", "egg", "fish"]))
print(json.dumps(("football", "hockey", "rugby", "basketball", "tennis", "table tennis")))
print(json.dumps("Obi is a boy, Ada is a girl"))
print(json.dumps(21))
print(json.dumps(106.0))
print(json.dumps(True))
print(json.dumps(False))
print(json.dumps(None)) 
#python		json
"""
dict		object
list		array
tuple		array
str		string
int		number
float		number
True		true
False		false
None  		null
"""
x = {
	"Name" : "John",
	"Age" : 30,
	"Married" : True,
	"Divorced" : False, 
	"Children" : ("Ann", "Billy"),
	"Pets" : None,
	"Cars" : [
		{"Model": "BMW 230", "MPG": 27.5},
		{"Model": "Ford Edge", "MPG": 24.1}
	]
}
print(json.dumps(x))
print(json.dumps(x, indent=4))
x = {
	"Name" : "John",
	"Age" : 30,
	"Married" : True,
	"Divorced" : False, 
	"Children" : ("Ann", "Billy"),
	"Pets" : None,
	"Cars" : [
		{"Model": "BMW 230", "MPG": 27.5},
		{"Model": "Ford Edge", "MPG": 24.1}
	]
}
print(json.dumps(x, indent=4, separators=(". ", " = "), sort_keys=True))

import re
txt = "The rain in Spain"
a = re.search("^The.Spain$", txt)
if x:
	print("Yes! We have a match!")
else:
	print("Oops! No match today!")
#findall	returns a list containing all matches
#search		returns a Match object if there is a match anywhere in the string
#split		returns a list where the string as been split at each match
#sub		replaces one or many matches with a string
txt = "The rain in Spain"
a = re.findall("^The.Spain$", txt)
if a:
	print("Yes! We have a match!")
else:
	print("Oops! No match!")
#metacharacters
#[]	a set of characters
#\	signals a special sequence (can also be used to escape special characters)
#.	any character (except newline character)
#^	starts with 
#$	ends with
#*	zero or more occurrences
#+	one or more occurrences
#?	zero or one occurrence
#{}	exactly the specified number of occurrences
#|	either or
#()	capture and group
import re
b = "The old time road"
c = re.findall("[a-m]", b)
print(c)
d = "That will be 70 dollars"
e = re.findall("\d", d)
print(e)
f = "Hello Nigeria"
g = re.findall("Ni...ia", f)
print(g)
h = re.findall("^Hello", f)
if h:
	print("Hi")
else:
	print("Nanda?!") 
i = re.findall("Nig.*a", f)
print(i)
j = re.findall("He.{2}o", f)
print(j)
k = "The rain in Spain falls mainly in the plain!"
l = re.findall("falls|stays", k)
print(l)
if l:
	print("At least, we have a match")
else:
	print("No match")
#special sequences
"""
\A	returns a match if the specified characters are at the beginning of the string
\b	returns a match where the specified characters are at the beginning or at the end of a word*
\B	returns a match where the specified characters are present, but not at the beginning or end of a word*
\d	returns a match where the string contains digits
\D	returns a match where the string does not contain digits
\s	returns a match where the string contains a white space
\S	returns a match where the string does not contain a white space
\w	returns a match where the string contains any word characters**
\W	returns a match where the string does not contain any word characters
\Z	returns a match if the specified characters are at the end of the string
* - the added "r" in the beginning makes sure that the string is treated as a raw string
** - characters from A-Z, digits from 0-9 and the underscore(_) character
"""
#sets
"""
[arn]		returns a match where one of the specified characters are present
[a-n]		returns a match for any lower case character alphabetically between the specified characters
[^arn]		returns a match for any character except those specified
[0123]		returns a match where one of the specified digits are present
[0-9]		returns a match for any digit between those specified
[0-5][0-9]	returns a match for any two-digit numbers from 00-59
[a-zA-Z]	returns a match for any character alphabetically between a and z, lower or upper case
[+]		returns a match for any + character in the string
"""
m = "A raisin in the sun"
n = re.search("sun", m)
print(n)
o = re.search("\s", m)
print("The first white space character is located  in position:", o.start())
p = re.search("moon", m)
print(p)
q = "Purple Hibiscus"
r = re.split("\s", q)
print(r)
s = re.split("\s", q, 1)
print(s)
t = "I love to take tea and bread every morning"
u = re.sub("love", "hate", t)
print(u)
v = "I was in a plane, going to Spain, selling cocaine when the police man came"
w = re.search("Portugal", v)
print(w)
"""
Match Properties
.span()		returns a tuple containing tbe start and end positions of the match
.string		returns the string passed into the function
.group()	returns the part of the string where there was a match
"""
x = "Going to Spain"
y = re.search(r"\bS\w+", x)
print(y.span())
print(y.string)
print(y.group())

import camelcase
z = camelcase.CamelCase()
aa = "Hello Everyone"
print(z.hump(aa))

try:
	print(ab)
except:
	print("An exception occurred")
"""
try		tests a block of code for errors
except		handles the errors
else		executes code in the absence of errors
finally		executes code, regardless of the results of the try and except 
"""
try:
	print(ac)
except NameError:
	print("Variable ac not defined")
finally:
	print("The 'try except' is finished")
try:
	print("Hello")
except:
	print("Something else went wrong")
else:
	print("Nothing went wrong")
try:
	f = open("random.txt")
	try:
		f.write("Lorem Ipsum lorem lorem")
	except:
		print("Something went wrong while writing to the file")
	finally:
		f.close()
except:
	print("Something went wrong while opening the file")
else:
	print("random.txt")
finally:
	print("File is non-writable")
ad = -5
if ad < 0:
	raise Exception("Sorry, positive integers only")  
ae = 5.25
if not type(ae) is str:
	raise Exception("Strings Only!")

username = input("Enter username:")
print("Welcome " + username)

price2 = 24
af = "The price for a single doughnut is {} cents"
print(af.format(price2))
price1 = 24
ag = "The price for a single doughnut is {:.2f} cents"
print(ag.format(price1))
quantity = 3
item_no1 = 567
item_no2 = 568
item_no3 = 569
price = 100
my_order = "I want {} pieces of doughnut with item numbers {}, {}, {}, for {:.2f} naira"
print(my_order.format(quantity, item_no1, item_no2, item_no3, price))
ah = 17
ai = "Chukwuanugo"
aj = "Hi there, I'm {1} and I'm {0} years old."
print(aj.format(ah, ai))
my_order1 = "I want a {carname} {model} color {color}."
print(my_order1.format(carname = "Toyota", model = "Sienna", color = "white")) 

"""
File methods
"r"	read, opens a file for reading, returns an error if the file does not exist
"a"	append, opens a file for appending, creates the file if it does not exist
"w"	write, opens a file for writing, creates the file if it does not exist
"x"	create, creates the specified file, returns an error if the file exists
"t"	text mode
"b"	binary mode(e.g images)
"""

ak = open("DK.txt", "rt")
print(ak.read())
print(ak.read(5))
print(ak.readline())
ak.close()
al = open("DK.txt", "a")
al.write("Deka Tech Home of Engineering is a company founded by Engr. Chukwuanugo under the sponsorship of big-time investors")
al.close()
al = open("DK.txt", "r")
print(al.read())
al = open("DK.txt", "w")
al.write("Whoops! I've deleted it")
al.close()
al = open("DK.txt", "r")
print(al.read())
al.close()
import os
os.remove("DK.txt")
if os.path.exists("DK.txt"):
	os.remove("DK.txt")
else:
	print("This file does not exist")
os.rmdir("C:\\Users\Anugo\demo\demo1")	#you can only remove an empty folder

import matplotlib
print(matplotlib.__version__)
import matplotlib.pyplot as plt
import numpy as np
xpoints = np.array([0, 6])
ypoints = np.array([0, 250])
plt.plot(xpoints, ypoints)
plt.show()
xpoints = np.array([1, 8])
ypoints = np.array([3, 10])
plt.plot(xpoints, ypoints, 'o')
plt.show()
xpoints = np.array([1, 2, 6, 8])
ypoints = np.array([3,8, 1, 10])
plt.plot(xpoints, ypoints)
plt.show()
ypoints = np.array([3,8, 1, 10, 5, 7])
plt.plot(ypoints)
plt.show()
x = np.array([0, 1, 2, 3, 4])
y = np.array([0, 67, 73, 60, 67])
plt.plot(x, y, marker = 'o')
plt.show()
x = np.array([0, 1, 2, 3, 4])
y = np.array([0, 5, 10, 15, 25])
plt.plot(x, y, marker = '*')
plt.show()
"""
Marker methods
o	circle
*	star
.	point
,	pixel
x	X
X	X(filled)
+	plus
P	plus(filled)
s	square
D	diamond
d	diamond(thin)
p	pentagon
H, h	hexagon
v	triangle(down)
^	triangle(up)
<	triangle(left)
>	triangle(down)
1	tri(down)
2	tri(up)
3	tri(left)
4	tri(right)
|	Vline
_	Hline
"""
a = np.array([0, 2, 4, 6, 8])
b = np.array([0, 1, 2, 3, 4])
plt.plot(a, b, '*:r')
plt.show()
"""
Line methods
-	solid
:	dotted
--	dashed
-.	dashed/dotted
"""
"""
Color methods
r	red
g	green
b	blue
c	cyan
m	magenta
y	yellow
k	black
w	white
"""
c = np.array([0, 1, 2, 3, 4, 5])
d = np.array([51, 43, 22, 17, 13, 11])
plt.plot(c, d, '.--k', ms = 20)
plt.show()
e = np.array([0, 1, 2, 3, 4, 5])
f = np.array([15, 34, 22, 71, 31, 11])
plt.plot(e, f, 'D-.c', ms = 20, mec = 'y', mfc = 'g')
plt.show()
g = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
h = np.array([0, 2, 4, 6, 8, 10, 12, 14, 16, 18])
plt.plot(g, h, '+-m', ms = 10, mec = '#4CAF50', mfc = 'w')
plt.show()
i = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
j = np.array([0, 18, 12, 16, 8, 10, 14, 2, 6, 4])
plt.plot(i, j, ls = 'dotted', c = 'r', lw = 10)
plt.show()
k = np.array([0, 2, 4, 6, 8])
l = np.array([40, 30, 20, 10, 0])
plt.plot(k)
plt.plot(l)
plt.show()
m = np.array([0, 10, 20, 30, 40, 50])
n = np.array([0, 20, 40, 60, 80, 100])
o = np.array([0, 10, 20, 30, 40, 50])
p = np.array([0, 40, 80, 120, 160, 200])
plt.plot(m, n, o, p, '*:m', mfc = 'k')
plt.show()
q = np.array([80, 85, 90, 95, 100, 105, 110, 115, 120, 125])
r = np.array([240, 250, 260, 270, 280, 290, 300, 310, 320, 330])
font1 = {
	'family':'sans-serif',
	'color':'black',
	'size':20
}
font2 = {
	'family':'serif',
	'color':'darkred',
	'size':10
}
plt.title("Sports Watch Data", fontdict = font1, loc = 'center')
plt.xlabel("Average Pulse", fontdict = font2)
plt.ylabel("Calorie Burnage", fontdict = font2)
plt.plot(q, r, 'D:c')
plt.grid(color = 'green', ls = '--', lw = 0.5)
plt.show()
s = np.array([0, 2, 3, 4, 5, 6, 7, 8, 9, 10])
t = np.array([0, 4, 9, 16, 25, 36, 49, 64, 81, 100])
plt.xlabel("Whole Numbers")
plt.ylabel("Perfect Squares")
plt.subplot(1, 2, 1)
plt.plot(s, t, 'd--k')
plt.grid(color = 'cyan', ls = '-', lw = 1.0)
s = np.array([11, 12, 13, 14, 15, 16, 17, 18, 19, 20])
t = np.array([121, 144, 169, 196, 225, 256, 289, 324, 361, 400])
plt.title("Graph of Whole Numbers against Perfect Squares", loc = "left")
plt.xlabel("Whole Numbers")
plt.ylabel("Perfect Squares")
plt.subplot(1, 2, 2)
plt.plot(s, t, 'd--k')
plt.suptitle("Numbers")
plt.grid(color = 'cyan', ls = '-', lw = 1.0)
plt.show()
u = np.array([5, 7, 8, 7, 2, 17, 2, 9, 4, 11, 1, 2, 9, 6])
v = np.array([99, 86, 87, 88, 111, 86, 103, 87, 94, 78, 77, 85, 86, 90])
plt.scatter(u, v, color = 'hotpink')
u = np.array([2, 2, 8, 1, 15, 8, 12, 9, 7, 3, 1, 1, 4, 7, 14, 12])
v = np.array([100, 105, 84, 105, 90, 99, 90, 95, 94, 100, 79, 112, 91, 80, 85, 108])
plt.scatter(u, v, color = '#88c999')
plt.title("Observation of 13 cars and 15 cars differently and their respective speeds", loc = "center")
plt.show()
w = np.array([5, 7, 8, 7, 2, 17, 2, 9, 4, 11, 1, 2, 9, 6])
x = np.array([99, 86, 87, 88, 111, 86, 103, 87, 94, 78, 77, 85, 86, 120])
colors = np.array(["red", "green", "blue", "yellow", "pink", "black", "orange", "purple", "beige", "brown", "gray", "cyan", "magenta", "tomato"])
sizes = np.array([20, 50, 100, 40, 15, 90, 60, 75, 30, 25, 55, 95, 70, 10])
plt.scatter(w, x, c=colors, cmap='viridis', s=sizes, alpha=0.5)
plt.colorbar()
plt.show()
"""
Available ColorMaps: Accent, Blues, BrBG, BuGn, BuPu, CMRmap, Dark2, GnBu, Greens, Gryes, OrRd, Oranges, PRGn, Paired, Pastel1, Pastel2, PiYG, PuBu, PuBuGn, Purples, RdBu, RdGy, RdPu, RdYIBu, RdYIGn, Reds, Set1, Set2, Set3, Spectral, Wistia, YIGn, YIGnBu, YIOrBr, YIOrRd, afmhot, autumn, binary, bone, brg, bwr, cividis, cool, coolwarm, copper, cubehelix, flag, gist_earth, gist_gray, gist_heat, gist_ncar, gist_rainbow, gist_stern, gist_yarg, gnuplot, gnuplot2, gray, hot, hsv, inferno, jet, magma, nipy_spectral, ocean, pink, plasma, prism, rainbow, seismic, spring, summer, tab10, tab20, tab20b, tab20c, terrain, twilight, twilight_shifted, viridis, winter
always add (_r) for reverse
"""
y = np.random.randint(100, size=(100))
z = np.random.randint(100, size=(100))
colors = np.random.randint(100, size=(100))
sizes = 10 * np.random.randint(100, size=(100))
plt.scatter(y, z, c=colors, s=sizes, alpha=0.5, cmap='Pastel1')
plt.colorbar()
plt.show()
#Bar Chart
aa = np.array(["A", "B", "C", "D"])
ab = np.array([3, 8, 1, 10])
plt.bar(aa, ab, color = "magenta", width = 0.5)
plt.show()
ac = np.array(["A", "B", "C", "D", "E", "F"])
ad = np.array([52, 43, 22, 17, 13, 11])
plt.barh(ac,ad, color = "#4CAF50", height = 0.5)
plt.show()
#The default height and weight values are 0.8
#Histogram
ae = np.random.normal(170, 10, 250)
plt.hist(ae)
plt.show()
#Pie Chart
af = np.array([35, 25, 25, 15, 80, 95, 40, 60])
mylabels = ["Apples", "Bananas", "Cherries", "Dates", "Eggs", "Fishes", "Groundnuts", "Hot cakes"] 
myexplode = [0, 0.2, 0, 0.2, 0.2, 0, 0, 0]
plt.pie(af, labels = mylabels, startangle = 90, explode = myexplode, shadow = True)
plt.legend(title = "Fruits and the Amount Available:")
plt.show()
#The value of each wedge is determined by comparing with other vakues using the formula x/sum(x)

#NumPy
ag = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 0])
print(ag)
print(type(ag))
#To check version of NumPy
print(np.__version__)
#The array object in NumPy is called ndarray. An ndarray can be created by passing a list, tuple or any array-like object into the array method.
ag = np.array((1, 2, 3, 4, 5, 6, 7, 8, 9, 0))
print(ag)
#Dimensions in arrays are same as nested arrays.
#0-D (scalars)
ah = np.array(42)
print(ah)
#1-D array
ag = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 0])
print(ag)
#2-D array (they're often used to represent matrices and 2nd order tensors)
ai = np.array([[1,2,3], [4,5,6]])
print(ai)
#3-D array (they're often used to represent 3rd order tensors)
aj = np.array([[[1,2,3], [4,5,6]], [[7,8,9], [10,11,12]]])
print(aj)
#Check number of dimensions
print(ah.ndim)
print(ag.ndim)
print(ai.ndim)
print(aj.ndim)
#Higher dimensional arrays
#The number of dimensions of an array can be defined using the ndmin argument.
ak = np.array([10,20,30,40,50,60,70,80,90,100], ndmin=5)
print(ak)
print('Number of dimensions: ', ak.ndim)
#Indexes in arrays start with 0
print(ag[0])
print('2nd element on 1st row: ', ai[0,1])
print(aj[0,1,2]) #0 represents the first dimension (i.e [[1,2,3], [4,5,6]]), 1 represents the second array (i.e [4,5,6]) while 2 represents the 3rd dimension which is the third value of the second array.
print(ai[1,-1])
#Slicing arrays means taking elements from one given index to another. It usually takes the format [start:end] or [start:end:step]. If we omit start, it's considered as 0. if we omit end, any length is sliced. If we omit end, its considered as 1.
print(ag[1:5:2])
print(ag[-3:-1])
print(ag[::2])
print(ai[1, 1:3]) #from the second array, return the second and third values
print(ai[0:2, 2]) #from both elements, return the second index
print(ai[0:2, 1:3]) #from both elements, return the second and third values
print(aj[1:2, 1:4]) #from the 2nd array of the 2nd dimension, print the 1st to last values
#Data types in Python includes strings(for text), integers(for numbers), float(for real numbers), boolean(for true or false comparism) and complex(for complex numbers)
"""
In addition to the data types listed above, NumPy has a few extra and they are referred to with one character(i or u). They include:
i - integer
b - boolean
u - unsigned integer
f - float
c - complex float
m - timedelta
M - datetime
O - object
S - string
U - unicode string
V - fixed chunk of memory for other types (void)
"""
# The argument dtype returns the data type of the array
print(ag.dtype)
al = np.array(['apple', 'banana', 'cherry'])
print(al)
print(al.dtype)
#Creating an array with a defined type can be done by including the argument dtype in the array() function
am = np.array([1, 2, 3, 4], dtype='S')
print(am)
print(am.dtype)
#For i, u, f, S and U, we can define size as well.
an = np.array([5, 10, 15, 20], dtype='i4')
print(an, an.dtype)
#If non-integers are included in an array of integers, they cannot be converted thus a ValueError will occur
#The astype() method creates a copy of an existing array and allows us to specify the data type to which we want to convert as a parameter.
ao = np.array([1.1, 1.2, 1.3, 1.4, 1.5, 1.6])
ap = ao.astype('i')
print(ap, ap.dtype)
aq = ap.astype(bool)
print(aq, aq.dtype)
#The argument copy() also makes a copy of an array
ar = ao.copy()
ao[0] = 1.0
print(ao, ar)
#The view() argument makes a view of the array, and changes made to the original would affect the view
at = ap.view()
ap[4] = 5
print(ap, at)
#Any change made to the view will also affect the original
at[2] = 3
print(ap, at)
#The base attribute returns None if an array owns the data it contains. Otherwise, it refers to the original object.
print(ar.base, at.base)
"""
The shape of an array is the number of elements in each dimension
The shape attribute returns a tuple with each index having the number of corresponding elements
"""
au = np.array([[1,2,3,4,5], [6,7,8,9,10]])
print(au.shape)
#The above example returns (2, 5) which means that the array has 2 dimensions and each dimension has 5 elements
av = np.array([5,10,15,20,25,30,35,40,45,50,55,60,65,70,75,80,85,90,95,100], ndmin=5)
print(av)
print("Shape of the array: ", av.shape)
#The reshape() method changes the shape of the array.
ao = np.array([1.1, 1.2, 1.3, 1.4, 1.5, 1.6, 1.7, 1.8])
aw = ao.reshape(2, 4)
print(aw)
ax = ao.reshape(2, 2, -1)
print(ax)
print(ax.base)
ao = np.array([1.1, 1.2, 1.3, 1.4, 1.5, 1.6, 1.7, 1.8])
ay = ao.reshape(2,2,-1)
print(ay)
#From the example above, passing -1 into the reshape() helps determine the number of elements or dimensions for the array.
#Passing reshape(-1) only converts a multidimensional array into a 1-D array (i.e flattens the array)
print(au.reshape(-1))
"""
We can use the for loop to iterate an array.

"""
#Iterating 1-D arrays means it'll loop through all elements.
for x in ao:
	print(x)
#Iterating 2-D arrays means it'll loop through all rows.
for x in au:
	print(x)
#To actually loop through all elements in a 2-D array
for x in au:
	for y in x:
		print(y)
#Iterating 3-D arrays means it'll loop through all 2-D arrays.
az = np.array([[[1,2,3], [4,5,6]], [[7,8,9], [10,11,12]]])
for x in az:
	print(x)
#To actually loop through all elements in
for x in az:
	for y in x:
		for z in y:
			print(z)
#The nditer() function also helps in very basic to very advanced iterations especially for arrays with very high dimensionality.
for x in np.nditer(az):
	print(x)
"""
The op_dtypes argument changes the datatype of the elements we want to iterate while iterating.
NumPy does not change the datatype of the element in-place (where the element is in the array), so it needs some other space (buffer) to perform this action.
To enable it in nditer(), we pass flags=['buffered].
"""
for x in np.nditer(ao, flags=['buffered'], op_dtypes=['S']):
	print(x)
#While iterating, we can also define the step size:
for x in np.nditer(au[:, ::2]):
	print(x)
#The ndenumerate() method enumerates the iteration
for idx, x in np.ndenumerate(ao):
	print(idx, x)
for idx, x in np.ndenumerate(au):
	print(idx, x)
for idx, x in np.ndenumerate(az):
	print(idx, x)
#The concatenate() function joins two or more arrays together
ba = np.array([2,4,6,8])
bb = np.array([10,12,14,16])
bc = np.concatenate((ba, bb))
print(bc)
bd = np.array([[1,2,3], [4,5,6]])
be = np.array([[7,8,9], [10,11,12]])
bf = np.concatenate((bd, be), axis=0)
print(bf)
#The only difference between stacking and concatenation is that stacking is done along a new axis. Staking is done by putting one 1-D array over another using the stack() function.
bg = np.array([100,200,300])
bh = np.array([400,500,600])
bi = np.stack((bg, bh), axis=1)
print(bi)
#hstack() stacks along rows
bj = np.hstack((bg, bh)) #1-D
print(bj)
#vstack() stacks along columns
bk = np.vstack((bg, bh)) #2-D
print(bk)
#dstack() stacks along height(depth)
bl = np.dstack((bg, bh)) #3-D
print(bl)
#array_split() splits an array. We can pass in the array we want to split and how many times we want to split it.\
bm = np.array_split(bj, 3)
print(bm)
bn = np.array_split(bj, 4)
print(bn)
print(bn[0])
print(bn[1])
print(bn[2])
print(bn[3])
#Splitting 2-D arrays
bo = np.array_split(bk, 3, axis=1)
print(bo)
bp = np.hsplit(bk, 3)
print(bp)
#In splitting, use hsplit for 2-D and vsplit for 3-D arrays
#where() searches an array for a certain value and returns the indexes that get a match
bq = np.array([1,2,3,4,5,4,4])
br = np.where(bq == 4)
print(br)
bs = np.array([1,2,3,4,5,6,7,8,9,0])
bt = np.where(bs%2 == 0)
print(bt)
bu = np.where(bs%2 == 1)
print(bu)
#searchsorted() performs a binary search in the array and returns the index where the specified value would be inserted to maintain the search order
bv = np.searchsorted(bs, 8)
print(bv)
#Pass side='right' to begin the search from right
bw = np.searchsorted(bs, 8, side='right')
print(bw)
#Multiple values can be searched by grouping them in an array
bx = np.searchsorted(bs, [2,4,6])
print(bx)
#sort() sorts a specified array in an ordered sequence. The sorted result is just a copy as the original remains unchanged.
by = np.array([52,43,22,17,13,11])
print(np.sort(by))
bz = np.array(['date', 'tiger nut', 'cucumber'])
print(np.sort(bz))
ca = np.array([True, False, True])
print(np.sort(ca))
cb = np.array([[3,6,1], [4,5,2]])
print(np.sort(cb))
"""
A boolean index is a list of booleans corresponding to indexes in an array.
Filtering is done using the boolean index. If the value at an index is True, that element is contained in the filter array. But if it is false, the element is excluded from the filtered array.
"""
boolidx = [True, False, False, True, True, True]
cc = by[boolidx]
print(cc)
#Create a filter array that will only return values higher than 42
cd = np.array([40,41,42,43,44,45,46,47,48,49])
boolidx1 = []
for element in cd:
	if element > 42:
		boolidx1.append(True)
	else:
		boolidx1.append(False)
ce = cd[boolidx1]
print(boolidx1)
print(ce)
#Create a filter array that'll only return even numbers
boolidx2 = []
for element in cd:
	if element % 2 == 0:
		boolidx2.append(True)
	else:
		boolidx2.append(False)
cf = cd[boolidx2]
print(boolidx2)
print(cf)
#The two examples above can also be performed by creating a filter directly from the array
boolidx1 = cd > 42
ce = cd[boolidx1]
print(boolidx1)
print(ce)
boolidx2 = cd % 2 == 0
cf = cd[boolidx2]
print(boolidx2)
print(cf)
#NumPy random numbers
"""
Random means something that cannot be predicted logically and not just a different occurence.
Pseudo random are random occurences generated through a generation algorithm. If there is a program to generate numbers, it can be predicted and thus not truly random.
In order to generate true random numbers, we need an outside source for the random data. This source is generally our keystrokes, mouse movement, data on network.
We don't truly need random numbers unless its related to security(encryption keys) or the basis of application is randomness(digital roulette wheels) 
"""
#The random module generates random numbers
from numpy import random
print(random.randint(100))
#The rand() method returns a float between 0 and 1
print(random.rand())
#The randint() method takes a size parameter where you can specify the shape of the array
print(random.randint(100, size=(5)))
print(random.randint(100, size=(3,5))) #2-D array with 3 rows each with 5 random integers
#The rand() method also allows to specify the shape of the array
print(random.rand(5))
print(random.rand(3,5))
"""
The choice() method allows a random value to be generated based on an array of values.
It takes an array as the parameter and randomly returns one of its values.
"""
print(random.choice([3,5,7,9]))
#Adding a size parameter to the choice() method allows an array of values to be returned.
print(random.choice([3,5,7,9], size=(3,5)))
"""
Data distribution is a list of all possible values and how often each value works which is very important in statistics and data science
A random distribution is a set of random numbers that follow a certain probability density function.
A probability density function is a function that describes a continous probability(probability of all values in an array)
Random numbers can be generated based on defined probabilities using the choice() method.
"""
print(random.choice([3,5,7,9], p=[0.1,0.3,0.6,0.0], size=(100)))
print(random.choice([3,5,7,9], p=[0.1,0.3,0.6,0.0], size=(3,5)))
#A permutation refers to an arrangement of elements.
#The shuffle() method ranomly shuffles an array. It makes changes to the original array.
cg = np.array([52,43,22,17,13,11])
random.shuffle(cg)
print(cg)
#The permutation() method generates a permutation of elements of an array. It returns a new array and leaves the original unchanged.
print(random.permutation(cg))
#Seaborn is a library that uses Matplotlib underneath to plot graphs. It is also used to visualize random distributions.
#Distplot stands for distribution plot. It takes an array as input and plots a curve corresponding to the distribution of points in the array.
import matplotlib.pyplot as plt
import seaborn as sns
sns.distplot([0,1,2,3,4,5,6,7,8,9])
plt.show()
sns.distplot([0,1,2,3,4,5,6,7,8,9], hist=False) #Removes the histogram
plt.show()
"""
The normal (Gaussian) distribution was named after the German mathematician Carl Friedrich Gauss.
It fits the probability distribution of many events(IQ scores, heartbeat etc).
It has 3 parameters:
loc(Mean) - where the peak of the bell exists
scale(Standard Deviation) - how flat the graph distribution should be
size - the shape of the returned array
"""
from numpy import random
print(random.normal(size=(2,3)))
print(random.normal(loc=1, scale=2, size=(2,3)))
sns.distplot(random.normal(size=1000), hist=False)
plt.show()
#A normal distribution curve is also known as a "Bell Curve" because of it's bell shape
"""
A binomial distribution is a discrete distribution. It describes the outcome of binary scenarios. It has 3 parameters:
n - number of trials
p - probability of occurence of each trial
size - the shape of the returned array
A discrete distribution is defined as separate set of events e.g a coin toss.
"""
print(random.binomial(n=10, p=0.5, size=10))
sns.distplot(random.binomial(n=10, p=0.5, size=1000), hist=True, kde=False)
plt.show()
"""
The main difference between normal and binomial distribution is that normal is continous whle binomial is discrete.
But if there are enough data points, it will be quite similar normal ditribution with certain loc and scale.  
"""
sns.distplot(random.normal(loc=50, scale=5, size=1000), hist=False, label='normal')
sns.distplot(random.binomial(n=100, p=0.5, size=1000), hist=False, label='binomial')
plt.show()
"""
A poisson distribution is also a discrete distribution which estimates how many times an event can happen in a specified time. It has 2 parameters:
lam - rate/known number of occurences
size - shape of the returned array
"""
print(random.poisson(lam=2, size=10))
sns.distplot(random.poisson(lam=2, size=1000), kde=False, label="Poisson")
plt.show()
"""
The difference between a normal and poisson distribution is that the former is continous while the latter is discrete.
But for a large enough poisson distribution, it will become similar to normal distribution with certain standard deviation and mean.
"""
sns.distplot(random.normal(loc=50, scale=7, size=1000), hist=False, label='normal')
sns.distplot(random.poisson(lam=50, size=1000), hist=False, label='poisson')
plt.show()
"""
The difference between poisson and binomial distributions is that binomial is for discrete trials, while poisson is for continous trials.
But for very large n and near-zero p, binomial distribution is near identical to poisson such that n * p is almost equal to lam.
"""
sns.distplot(random.binomial(n=1000, p=0.01, size=1000), hist=False, label='binomial')
sns.distplot(random.poisson(lam=10, size=1000), hist=False, label='poisson')
plt.show()
"""
Uniform distribution is used to describe probability where every event has equal chances of occuring e.g generation of random numbers. It has 3 parameters:
a - lower bound(default-0.0)
b - upper bound(default-1.0)
size - shape of the returned array
"""
print(random.uniform(size=(2,3)))
sns.distplot(random.uniform(size=1000), hist=False)
plt.show()
"""
Logistic distribution is used to describe growth. It is used extensively in machine learning in logistic regression, neural networks etc. It has 3 parameters:
loc - mean(peak value, default-0)
scale - standard deviation(flatness of the distribution, default-1)
size - the shape of the returned array
"""
print(random.logistic(loc=1, scale=2, size=(2,3)))
sns.distplot(random.logistic(size=1000), hist=False)
plt.show()
"""
The difference between logistic and normal is that logistic distribution has more area under the tails, meaning it represents more possibility of occurence of an event further away from the mean.
For higher value of scale(S.D), the normal and logistic distributions are near identical apart from the peak.
"""
sns.distplot(random.normal(scale=2, size=1000), hist=False, label='normal')
sns.distplot(random.logistic(size=1000), hist=False, label='logistic')
plt.show()
"""
Multinomial distribution is a generalization of binomial distribution. It describes outcomes of multi-nomial scenarios unlike binomial where scenarios must only be one or two (e.g blood type of a population, dice roll outcome). It has 3 parameters:
n - number of possible outcomes(e.g 6 for a dice roll)
pvals - list of probabilities of outcomes (e.g [1/6, 1/6, 1/6, 1/6, 1/6, 1/6] for a dice roll)
size - shape of the returned array
"""
print(random.multinomial(n=6, pvals=[1/6, 1/6, 1/6, 1/6, 1/6, 1/6]))
sns.distplot(random.multinomial(n=6, pvals=[1/6, 1/6, 1/6, 1/6, 1/6, 1/6], size=1000), hist=False)
plt.show()
"""
Note: Multi nominal samples won't produce a single value, rather they'll produce one value for one pval. As they are generalization of binomial representations, their visual representation and similarity of normal distributions is same as that of multiple binomial distributions.
"""
"""
Exponential distribution is used for describing time till next event(e.g failure or success). It has 2 parameters:
scale - inverse of rate (default value is 1.0)
size - shape of the returned array
"""
print(random.exponential(scale=2, size=(2,3)))
sns.distplot(random.exponential(scale=2, size=1000), hist=False)
plt.show()
"""
The relation between poisson and exponential distribution is that poisson deals with a number of ocurrences of an event in a time period while exponential deals with the time between these events.
"""
"""
Chi Square distribution is used as a basis to verify the hypothesis. It has 2 parameters:
df - degree of freedom
size - shape of the returned array
"""
print(random.chisquare(df=2, size=(2, 3)))
sns.distplot(random.chisquare(df=1, size=1000), hist=False)
plt.show()
"""
Rayleigh distribution is used in signal processing. It has 2 parameters:
scale - (standard deviation) determines how flat the distribution will be. Default=1.0
size - shape of the returned array
"""
print(random.rayleigh(scale=2, size=(2, 3)))
sns.distplot(random.rayleigh(scale=2, size=1000), hist=False)
plt.show()
"""
The similarity between Rayleigh and Chi Square distribution is that at unit S.D and 2 df, both represent the same distributions.
"""
"""
Pareto distribution is a distribution following the Pareto's law (i.e 80-20 distribution: 20% factors cause 80% outcome). It has 2 parameters:
a - shape parameter
size - shape of the returned array
"""
print(random.pareto(a=2, size=(2,3)))
sns.distplot(random.pareto(a=2, size=1000), kde=False)
plt.show()
"""
Zipf distributions are used to sample data based on Zipf's law.
Zipf's law states that in a collection, the nth common term is 1/n times of the most common term. E.g the 5th common word in English occurs nearly 1/5 times as of the most used word. It has 2 parameters:
a - distribution parameter
size - shape of the returned array
"""
print(random.zipf(a=2, size=(2,3)))
sns.distplot(random.zipf(a=2, size=1000), kde=False)
plt.show()
zd = random.zipf(a=2, size=1000)
sns.distplot(zd[zd<10], kde=False)
plt.show()
"""
ufunc stands for Universal Function. They are numpy functions that operates on the ndarray object.
They are used to implement vectorization in numpy which is more faster than iterating over elements. They also provide broacasting and additional methods like reduce, accumulate etc. that are very helpful for computation. They also take additional arguments like:
where - boolean array or condition defining where the operations should take place.
dtype - defining the return type of elements.
out - output array where the return value should be copied.
Vectorization involves converting iterative statements into a vector-based operation. It is faster as modern CPUs are optimized for such operations.
"""
#For example, adding elements of 2 lists without ufunc would be like this:
ch = [1,2,3,4]
ci = [5,6,7,8]
cj = []
for i, j in zip(ch, ci):
	cj.append(i + j)
print(cj)
#By introducing ufunc, we use the add() function:
ch = [1,2,3,4]
ci = [5,6,7,8]
ck = np.add(ch, ci)
print(ck)
"""
In order to create a custom ufunc, a function will have to be defined, then added to the numpy ufunc library with the frompyfunc() method. This method takes the following arguments:
function - the name of the function.
inputs - the number of input arguments (arrays).
outputs - the number of output arrays.
"""
def myadd(x, y):
	return x * y
myadd = np.frompyfunc(myadd, 2, 1)
print(myadd([1,2,3,4], [5,6,7,8]))
"""
The type() method returns the type of a function to check if its a ufunc or not.
Ufuncs always return: <class 'numpy.ufunc'>.
"""
print(type(np.add))
#If its not a ufunc, it will return: <class 'function'>.
print(type(np.concatenate))
#If the function is not recognized, it will produce an error.
print(type(np.ojitske))
#To test if the function is a ufunc in an if statement, use the numpy.ufunc value (or np.ufunc)
if type(np.add) == np.ufunc:
	print('add() is a ufunc')
else:
	print('add() is not a ufunc')
"""
Simple arithmetic operators can be used directly between numpy arrays.
Performing arithmetic conditionally means that conditions can be defined where the arithmetic operation should happen. It takes the where parameter in which the condition can be specified.
"""
#As we have seen earlier, the add() function sums the content of 2 arrays and returns the output as a new array.
cl = np.array([1,2,3,4,5,6])
cm = np.array([52,43,22,17,13,11])
print(np.add(cl, cm))
#The subtract() function subtracts the values of one array from the other and returns the output as a new array.
print(np.subtract(cm, cl))
#The multiply() function multiplies the values of one array with the other and returns the output as a new array.
print(np.multiply(cl, cm))
#The divide() function divides the values of one array with the other and returns the output as a new array.
print(np.divide(cm, cl))
#The power() function raises the values of one array to the power of the values of the other and returns the output as a new array.
print(np.power(cl, cm))
#Both the mod() and remainder() functions return the remainder of the values in the first array corresponding to the values in the second, and returns the output as a new array.
print(np.mod(cl, cm))
print(np.remainder(cm, cl))
#The divmod() function return both the quotient and the mod. The output is two arrays, the first containing the quotient and the second containing the mod.
print(np.divmod(cm, cl))
#Both the absolute() and abs() functions will return absolute values contained in an array. It would be best to use absolute(), to avoid confusion with math.abs().
cn = np.array([-1,-2,-3,-4,-5,-6,-7,-8,-9])
print(np.absolute(cn))
"""
There are primarily 5 ways of rounding off decimals in numpy which includes truncation, fix, rounding, floor and ceil.
"""
#The trunc() and fix() functions remove the decimals and return the float number closest to 0.
co = np.array([-3.1428792235, 3.666667])
print(np.trunc(co))
print(np.fix(co))
#The around() function increments preceeding digits or decimals by 1 if>= else do nothing
print(np.around(co))
#The floor() function rounds off decimals to the nearest lower integer.
print(np.floor(co))
#The ceil() function rounds off decimals to the nearest upper integer.
print(np.ceil(co))
"""
NumPy also provides functions to perform logarithm at base 2, e and 10.
"""
cp = np.arange(1, 10)
print(np.log2(cp))
print(np.log(cp)) #Natural log
print(np.log10(cp))
#To take a log at any base, a custom function will be defined, using the frompyfunc() along with the math.log() functions with 2 input parameters and 1 output parameter.
from math import log
cq = np.frompyfunc(log, 2, 1)
print(cq(100, 15))
#Summation is quite different from addition because addition is done over two arguments, while summation is done over n elements.
print(np.sum([cl, cm]))
#If axis=1 is specified, each number in an array will be summed.
print(np.sum([cl, cm], axis=1))
"""
Cumulative sum means partially adding elements in an array.
For instance, the partial sum of [1,2,3,4] = [1, 1+2, 1+2+3, 1+2+3+4] = [1,3,6,10]
This partial sum can be performed using the cumsum() function.
"""
print(np.cumsum(cl))
#The prod() function returns the product of elements in an array.
print(np.prod(cm))
print(np.prod([cl, cm], axis=1))
#Cumulative product means partially multiplying elements in an array. It occurs based on the same principle as partial sum and can be performed using the cumprod() function.
print(np.cumprod([5,6,7,8]))
"""
A discrete difference means subtracting 2 successive elements.
E.g the discrete difference for [1,2,3,4] = [2-1, 3-2, 4-3] = [1,1,1]
The diff() function returns the discrete difference.
"""
print(np.diff([cm]))
#To perform the operation a number of times (with input and output), a parameter n would be given
print(np.diff([cm], n=2))
#The LCM (Least Common Multiple) is the least number that is a common multiple of 2 numbers. This operation can be performed using the lcm() function.
print(np.lcm(4,6))
#The reduce() method returns the LCM of all values in an array, using the ufunc (lcm()) on each element and reduce the array by 1 dimension.
print(np.lcm.reduce([3,6,9]))
cr = np.arange(1,11)
print(np.lcm.reduce(cr))
#The GCD (Greatest Common Denominator), also HCF (Highest Common Factor) is the biggest number that is a common factor of both of the numbers. This can be performed using the gcd() function.
print(np.gcd(6,9))
#To find HCF in arrays, we will use the reduce() method in line with the ufunc (gcd()).
print(np.gcd.reduce([20,8,32,36,16]))
#NumPy also provides ufuncs (sin(), cos(), tan()) for trigonometric operations.
print(np.sin(np.pi/2))
print(np.sin([np.pi/2, np.pi/3, np.pi/4, np.pi/5]))
#By default, all trigonometric functions take radians as parameters, but the rad2deg() function allows us to convert from radians to degrees and vice versa.
print(np.deg2rad([0,90,180,270,360])) 
#Note: radian values are given as pi/180*degree_values
print(np.rad2deg([np.pi/2,np.pi,1.5*np.pi,2*np.pi]))
#To find angles from values of sine, cos and tan, we inverse the functions (i.e arcsin(), arccos() and arctan()).
print(np.arcsin(1.0))
print(np.arcsin([1,-1,0.1]))
#NumPy finds hypotenuses using the Pythagoras theorem and can be performed using the hypot() function.
print(np.hypot(4,3))
#NumPy also provides hyperbolic functions (sinh(), cosh(), tanh()), all taking radian as a parameter.
print(np.sinh(np.pi/2))
print(np.cosh([np.pi/2, np.pi/3, np.pi/4, np.pi/5]))
#To find angles from values of hyperbolic sine, cos and tan, we inverse the functions (i.e arcsinh(), arccosh() and arctanh()).
print(np.arctanh(0.4))
print(np.arctanh([0.1,0.2,0.3,0.4]))
"""
A set is a collection of unique elements. It is used for operations involving frequent intersection, union and difference operations.
Sets are created using the unique() method by finding unique elements from any array.
"""
print(np.unique([1,1,1,2,3,4,5,5,6,7]))
#The union1d() method finds the unique values for 2 arrays.
cs = np.array([1,2,3,4])
ct = np.array([3,4,5,6])
print(np.union1d(cs, ct))
#The intersect1d finds values that are present in both arrays.
print(np.intersect1d(cs, ct, assume_unique=True))
#The setdiff1d() method finds only values that are absent in the 2nd set.
print(np.setdiff1d(cs, ct, assume_unique=True))
#The setxor1d() method finds values absent in both sets.
print(np.setxor1d(cs, ct, assume_unique=True))


"""
Pandas
Pandas is a Python library used for working with data sets. It has functions for analyzing, cleaning, exploring and manipulating data.
The name 'Pandas' has a reference to both 'Panel Data' and 'Python Data Analysis' and was created by Wes McKinney in 2008.
Pandas allows us to analyze big data and make conclusions based on statistical theories. It can also clean messy data sets and make them readable and relevant.
"""
import pandas
mydataset = {
	'cars': ["BMW", "Volvo", "Ford"],
	'passings': [3,7,2]
}
myvar = pandas.DataFrame(mydataset)
print(myvar)
#A Pandas series is like a column in a table. It is a one-dimensional array holding data of any type.
myvar1 = [1,3,7,8,9]
print(pd.Series(myvar1))
print(myvar1[4])
#Custom labels can be create using the index argument:
myvar2 = [2,4,6,8,0]
print(pd.Series(myvar2, index=["a","b","c","d","e"]))
myvar3 = {"day1": 420, "day2": 380, "day3": 390}
print(pd.Series(myvar3))
#The specified indexes will only be included in the displayed output:
myvar3s1 = {"day1": 420, "day2": 380, "day3": 390}
print(pd.Series(myvar3s1, index=["day1", "day2"]))
data = {"calories": [420,380,390], "duration": [50,40,45]}
print(pd.DataFrame(data))
#The loc attribute is used to access 1 or more specified rows in DataFrame:
df = pd.DataFrame(data, index=["day1","day2","day3"])
print(df)
print(df.loc[1])
print(df.loc["day2"])
daf = pd.DataFrame(data)
print(daf.loc[[0,1]])
data1 = pd.read_csv('C:\\Users\Anugo\data.csv')
print(data1.to_string)
data2 = {
	"Duration":{"0":60,"1":60,"2":60,"3":45,"4":45,"5":60},
	"Pulse":{"0":110,"1":117,"2":103,"3":109,"4":117,"5":102},
	"Maxpulse":{"0":130,"1":145,"2":135,"3":175,"4":148,"5":127},
	"Calories":{"0":409,"1":479,"2":340,"3":282,"4":406,"5":300}
}
print(pd.DataFrame(data2))
#The head() method returns the headers and a specified number of rows, starting from the top.
print(data1.head(10))
#The default value is 5 (i.e if you don't specify any number of rows in the head() method)
print(data1.head())
#The tail() method does the same function as the head() but instead starts from the last.
print(data1.tail())
#The info() method gives more information about the data set.
print(data1.info())
"""
Data cleaning means fixing bad data in your data set.
Bad data may include empty cells, data in wrong format, wrong data, duplicates etc.
"""
data3 = pd.read_csv('C:\\Users\Anugo\dirtydata.csv')
dafe = data3.dropna()
print(dafe.to_string())
"""
The dropna() method returns a new DataFrame and does not affect the original.
To change the original, add the inplace=True argument.
"""
data3.dropna(inplace=True)
print(data3.to_string())
"""
The dropna(inplace=True) will not only return a new DataFrame, but will also remove rows containing null values in the original.
The fillna() method replaces empty cells with a value.
"""
data4 = pd.read_csv('C:\\Users\Anugo\dirtydata.csv')
data4.fillna(130, inplace=True)
print(data4.to_string())
data5 = pd.read_csv('C:\\Users\Anugo\dirtydata.csv')
data5["Calories"].fillna(130, inplace=True)
data5["Date"].fillna('2020/12/22', inplace=True)
print(data5.to_string())
data6 = pd.read_csv('C:\\Users\Anugo\dirtydata.csv')
dafe1 = data6["Calories"].mean()
dafe2 = data6["Calories"].median()
dafe3 = data6["Calories"].mode()[0]
data6["Calories"].fillna(dafe1, inplace=True)
data6["Calories"].fillna(dafe2, inplace=True)
data6["Calories"].fillna(dafe3, inplace=True)
print(data6.to_string())
data7 = pd.read_csv('C:\\Users\Anugo\dirtydata.csv')
data7["Date"] = pd.to_datetime(data7["Date"])
print(data7.to_string())
data7.dropna(subset=["Date"], inplace=True)
print(data7.to_string())
data8 = pd.read_csv('C:\\Users\Anugo\dirtydata.csv')
data8.loc[7, "Duration"] = 45
print(data8.to_string())
data9 = pd.read_csv('C:\\Users\Anugo\dirtydata.csv')
for x in data9.index:
	if data9.loc[x, "Duration"] > 60:
		data9.loc[x, "Duration"] = 60
print(data9.to_string())
data0 = pd.read_csv('C:\\Users\Anugo\dirtydata.csv')
for x in data0.index:
	if data0.loc[x, "Duration"] > 60:
		data0.drop(x, inplace=True)
print(data0.to_string())
#The duplicated() method returns a Boolean value for each row of data, which can be used to identify duplicates in the dataset.
data10 = pd.read_csv('C:\\Users\Anugo\dirtydata.csv')
print(data10.duplicated())
#The drop_duplicates() method removes duplicates from the dataset:
data10.drop_duplicates(inplace=True)
print(data10.to_string())
#The corr() method calculates the relationship between each column in your dataset:
data11 = pd.read_csv('C:\\Users\Anugo\data.csv')
print(data11.corr())
"""
The example above is explained as follows:
The result of the corr() method is a table with a lot of numbers (varying from -1 to 1) representing how well the relationship is between the columns. 
0.6 to 1 (perfect correlation) are good correlations (their negative forms can be included but increasing one of the columns will decrease the other). Anything less can be considered as poor correlation.
"""
#Remember that the corr() method ignores "non-numeric" columns.
#The plot() method is used inline with Pyplot to create diagrams.
import matplotlib.pyplot as plt
data12 = pd.read_csv('C:\\Users\Anugo\data.csv')
data12.plot()
plt.show()
#The kind argument specifies the kind of graph you want. Here, scatter is specified and it needs both x and y axes included.
data12.plot(kind='scatter', x='Duration', y='Calories')
plt.show()
data12.plot(kind='scatter', x='Duration', y='Maxpulse')
plt.show()
data12["Duration"].plot(kind='hist')
plt.show()

"""
SciPy
Scipy is a scientific computation that uses NumPy underneath.
It stands for Scientific Python and provides more utility for optimization, stats and signal processing. It is also an open source library.
SciPy was created by NumPy's creator Travis Olliphant.
"""
import scipy
from scipy import constants
#As SciPy is more focused on scientific computations, it provides many in-built constants which can be helpful when working with data science.
print(constants.liter) #How many cubic meters are there in one liter?
print(constants.pi)
print(dir(constants)) #returns a list of units under the constants module
#These units are placed under these categories: metric, binary, mass, angle, time, length, pressure, volume, speed, temperature, energy, power and force.
#Metric (SI) prefixes (metres):
print(constants.yotta)
print(constants.zetta)
print(constants.exa)
print(constants.peta)
print(constants.tera)
print(constants.giga)
print(constants.mega)
print(constants.kilo)
print(constants.hecto)
print(constants.deka)
print(constants.deci)
print(constants.centi)
print(constants.milli)
print(constants.micro)
print(constants.nano)
print(constants.pico)
print(constants.femto)
print(constants.atto)
print(constants.zepto)
#Binary prefixes (bytes):
print(constants.kibi)
print(constants.mebi)
print(constants.gibi)
print(constants.tebi)
print(constants.pebi)
print(constants.exbi)
print(constants.zebi)
print(constants.yobi)
#Mass prefixes (kg):
print(constants.gram)
print(constants.metric_ton)
print(constants.grain)
print(constants.lb) #pound also applies
print(constants.oz) #ounce also applies
print(constants.stone)
print(constants.long_ton)
print(constants.short_ton)
print(constants.troy_ounce)
print(constants.troy_pound)
print(constants.carat)
print(constants.atomic_mass) #m_u/u also applies
#Angle (radians):
print(constants.degree)
print(constants.arcmin) #arcminute also applies
print(constants.arcsec) #arcsecond also applies
#Time (seconds):
print(constants.miute)
print(constants.hour)
print(constants.day)
print(constants.week)
print(constants.year)
print(constants.Julian_year)
#Length (meters):
print(constants.inch)
print(constants.foot)
print(constants.yard)
print(constants.mile)
print(constants.mil)
print(constants.pt) #point also applies
print(constants.survey_foot)
print(constants.survey_mile)
print(constants.nautical_mile)
print(constants.fermi)
print(constants.angstorm)
print(constants.micron)
print(constants.astronomical_unit) #au also applies
print(constants.light_year)
print(constants.parsec)
#Pressure (pascals):
print(constants.atm) #atmosphere also applies
print(constants.bar)
print(constants.torr)
print(constants.mmHg)
print(constants.psi)
#Area (square meter)
print(constants.hectare)
print(constants.acre)
#Volume (cubic meter):
print(constants.litre) #liter also applies
print(constants.gallon) #gallon_US also applies
print(constants.gallon_imp)
print(constants.fluid_ounce) #fluid_ounce_US also applies
print(constants.fluid_ounce_imp)
print(constants.barrel) #bbl also applies
#Speed (meters per second):
print(constants.kmh)
print(constants.mph)
print(constants.mach) #speed_of_sound also applies
print(constants.knot)
#Temperature (Kelvin):
print(constants.zero_Celsius)
print(constants.degree_Fahrenheit)
#Energy (joules):
print(constants.eV) #electron_volt also applies
print(constants.calorie) #calorie_th also applies
print(calorie_IT)
print(constants.erg)
print(constants.Btu) #Btu_IT also applies
print(constants.Btu_th)
print(constants.ton_TNT)
#Power (watts):
print(constants.hp) #horsepower also applies
#Force (newton):
print(constants.dyn) #dyne also applies
print(constants.lbf) #pound_force also applies
print(constants.kgf) #kilogram_force also applies
"""
Optimizers in SciPy
Optimizers are a set of procedures defined in SciPy that either find the minimum value of a function or the root of an equation.
NumPy is capable of finding roots for polynomials and linear equations, but can not for non-linear equations (e.g x + cos(x)).
To be able to do so, use SciPy's optimize.root function. This function takes 2 required arguments:
fun - a function representing the equation
x0 - an initial guess for the root
The function returns an object with information regarding the solution. The actual answer is given under the attribute x of the returned object.
"""
#Find the root of the equation x + cos(x):
from scipy.optimize import root
from math import cos
def eqn(x):
	return x + cos(x)
myroot = root(eqn, 0)
print(myroot.x)
print(myroot)
"""
Minimizing a function
A function here represents a curve. Curves have high (maxima) and low points (minima). The highest point in the whole curve is called the global maxima, whereas the rest of them are called local maxima. Same goes for the lowest point. 
We can use scipy.optimize.minimize() to minimize the function. The minimize() function takes the following arguments:
fun - a function representing an equation
x0 - an initial guess for the root
method - name of method to use. Legal values include: 'CG', 'BFGS', 'Newton-CG', 'L-BFGS-B', 'TNC', 'COBYLA', 'SLSQP'
callback - function called after each iteration of optimization
options - a dictionary defining extra parameters:
{
	"disp": boolean - print detailed description
	"gtol": number - the tolerance of the error
}
"""
#Minimize the function x^2 + x + 2 with BFGS:
from scipy.optimize import minimize
def eqn1(x):
	return x**2 + x + 2
mymin = minimize(eqn, 0, method='BFGS')
print(mymin)
print(mymin.x)
"""
Sparse data is data that has mostly unused elements (elements that don't carry any information i.e most of the element values are 0).
Dense array is an array where most of the values are  not 0.
The scipy.sparse module provides functions to deal with sparse data.
There are 2 types of sparse matrices:
CSC - Compressed Sparse Column for efficient arithmetic and fast column slicing.
CSR - Compressed Sparse Row for fast row slicing and faster matrix vector products. This matrix can be created by passing an array into the function scipy.sparse.csr_matrix()
"""
import numpy as np
from scipy.sparse import csr_matrix
arr = np.array([0,0,0,0,0,1,1,0,2])
print(csr_matrix(arr))
arr1 = np.array([[0,0,0], [0,0,1], [1,0,2]])
print(csr_matrix(arr1).data) #returns only non-zero data
print(csr_matrix(arr1).count_nonzero()) #returns the number of non-zero data
mat = csr_matrix(arr1)
mat.eliminate_zeros() #removes zero-entries from the matrix
print(mat)
mat.sum_duplicates() #eliminates duplicates by adding them
print(mat)
newarr = csr_matrix(arr1).tocsc()
print(newarr)
"""
Graphs is an essential data structure. The scipy.sparse.csgraph module is used for working with graphs.
Adjacency matrix is a nxn matrix where n is the number of elements in a graph. The values represents the connection between the elements.
"""
import numpy as np
from scipy.sparse.csgraph import connected_components
from scipy.sparse import csr_matrix
arr2 = np.array([[0,1,2], [1,0,0], [2,0,0]])
newarr1 = csr_matrix(arr2)
print(connected_components(newarr1))
"""
The dijkstra method is used to find the shortest path in a graph from one element to another. It takes the following arguments:
return_predecessors - boolean(true to return the whole path of the traversal otherwise false).
indices - index of the element to return all paths from that element only.
limit - max weight of path.
"""
#Find the shortest path from element 1 to 2:
import numpy as np
from scipy.sparse.csgraph import dijkstra
from scipy.sparse import csr_matrix
print(dijkstra(newarr1, return_predecessors=True, indices=0))
#The floyd_warshall() method is used to find the shortest path between all pairs of elements
from scipy.sparse.csgraph import floyd_warshall
print(floyd_warshall(newarr1, return_predecessors=True))
#The bellman_ford() method is used to find the shortest path between all pairs of elements, as well as handle negative weights.
from scipy.sparse.csgraph import bellman_ford
print(bellman_ford(newarr1, return_predecessors=True, indices=0))
#The depth_first_order() method returns a depth first traversal from a node. It takes the following arguments: the graph and the starting element to traverse graph from.
#Traverse the graph depth first for given adjacency matrix:
from scipy.sparse.csgraph import depth_first_order
print(depth_first_order(newarr1, 1))
#The breadth_first_order() method returns a breadth first traversal from a node. It takes the following arguments: the graph and the starting element to traverse graph from.
#Traverse the graph breadth first for given adjacency matrix:
from scipy.sparse.csgraph import breadth_first_order
print(breadth_first_order(newarr1, 1))
"""
Spatial data refers to data that is represented in a geometric space e.g points on a coordinated system.
The scipy.spatial module has functions for working with spatial data.
"""
"""
Triangulation of a polygon is to divide the polygon into multiple triangles with which we can compute the area of the polygon.
A triangulation with points means creating surface composed triangles in which all of the given points are on at least one vertex of any triangle in the surface.
One method to generate these triangulations through points is the Delaunay() triangulation
"""
#Create a triangulation from the points:
from scipy.spatial import Delaunay
import matplotlib.pyplot as plt
points = np.array([[2,4], [3,4], [3,0], [2,2], [4,1], [1,2], [5,0], [3,1], [1,2], [0,2]])
simplices = Delaunay(points).simplices
plt.triplot(points[:,0], points[:,1], simplices)
plt.scatter(points[:,0], points[:,1], color='r')
plt.show()
#A convex hull is the smallest polygon that covers all given points. The ConvexHull() method can be used to create a convex hull.
from scipy.spatial import ConvexHull
hull = ConvexHull(points)
hull_points = hull.simplices
plt.scatter(points[:,0], points[:,1], color='r')
for simplex in hull_points:
	plt.plot(points[simplex,0], points[simplex,1], 'k-')
plt.show()
"""
KDTrees are a data structure optimized for nearest neighbour queries e.g in a set of points using KDTrees, we can efficiently ask which points are nearest to a certain point.
The KDtree() method returns a KDTree object. The query() method returns the distance to the nearest neighbour and the location of the neighbours.
"""
#Find the nearest neighbour to point (1,1):
from scipy.spatial import KDTree
points1 = [(1,-1), (2,3), (-2,3), (2,-3)]
kdt = KDTree(points1)
print(kdt.query((1,1)))
"""
Distance Matrix
There are many distance metrics used to find various types of distances between two points in data science, Euclidean distance, cosine distance etc.
The distance between 2 vectors may not only be the length of straight line between them, it can also be the angle between them from the origin, or number of unit steps required.
Many of the machine learning algorithm's performance depends greatly on distance metrics.
"""
#Find the euclidean distance between given points:
from scipy.spatial.distance import euclidean
p1 = (1,0)
p2 = (10,2)
print(euclidean(p1, p2))
#Cityblock Distance (Manhattan Distance) is the distance computed using 4 degrees of movement e.g up an down movement or left and right, diagonal movement is invalid.
#Find the cityblock distance between given points:
from scipy.spatial.distance import cityblock
print(cityblock(p1, p2))
#Cosine Distance is the value of cosine angle between two points A and B
from scipy.spatial.distance import cosine
print(cosine(p1, p2))
#Hamming Distance is the proportion of bits where two bits are different. It's a way to measure distance for binary sequences.
#Find the hamming distance between given points:
from scipy.spatial.distance import hamming
p3 = (True, False, True)
p4 = (False, True, True)
print(hamming(p1, p2))
"""
SciPy Matlab Arrays
NumPy provides methods to persist the data in readable formats, but SciPy provides us with interoperability with Matlab as well.
The scipy.io module has functions for working with Matlab arrays.
The savemat() function allow data to be exported in Matlab format. The method takes the following parameters:
filename - the file name for saving the data
mdict - a dictionary containing the data
do_compression - a boolean value that specifies whether to compress the result or not (default-False)
"""
#Export the array as variable name "vec" to a .mat file:
from scipy import io
import numpy as np
arr3 = np.arange(10)
io.savemat('arr3.mat', {"vec":arr3})
"""
The loadmat() function allows data to be imported from a Matlab file. It takes only one parameter which is filename
It will return a structured array whose keys are the variable names and the corresponding values are the variable values
"""
mydata = io.loadmat('arr3.mat')
print(mydata)
print(mydata['vec'])
"""
Notice that the array was originally one dimensional and upon extraction, it has increased by one dimension.
To resolve this issue, an additional argument will be passed squeeze_me=True
"""
mydata = io.loadmat('arr3.mat', squeeze_me=True)
print(mydata)
print(mydata['vec'])
"""
Interpolation is a method for generating points between given points. This has a lot of usage.
Where we usually deal with missing data in a dataset, interpolation can be used to substitute those missing values. This method is called imputation.
Apart from imputation, interpolation is often used where we need to smooth the discrete points in a dataset.
The scipy.interpolate module has many functions that deal with interpolation.
"""
"""
The interp1d() function is used to interpolate a distribution with 1 variable.
It takes x and y points and returns a callable function that can be calle with new x and returns a corresponding y.
"""
#For given xs and ys interpolate values from 2.1 to 2.9:
from scipy.interpolate import interp1d
import numpy as np
xs = np.arange(10)
ys = 2*xs + 1
interp_func = interp1d(xs, ys)
newarr2 = interp_func(np.arange(2.1,3,0.1))
print(newarr2)
"""
Spline Interpolation
In 1D interpolation, the points are fitted for a single curve whereas in spline interpolation, the points are fitted against a piecewise function defined with polynomials called splines.
The UnivariateSpline() function takes xs and ys and produce a callable function that can be called with new xs.
A piecewise function is a function that has different definition for different ranges.
"""
#Find univariate spline interpolation for 2.1 to 2.9 for the following non-linear points:
from scipy.interpolate import UnivariateSpline
xs1 = np.arange(10)
ys1 = xs**2 + np.sin(xs1) + 1
interp_func1 = UnivariateSpline(xs1, ys1)
newarr3 = interp_func1(np.arange(2.1, 3, 0.1))
print(newarr3)
"""
Radial basis function is a function that is defined corresponding to a fixed reference point.
The Rbf() function also takes xs and ys as arguments and produce a callable function that can be called with new xs.
"""
#Interpolate using the following xs and ys using rbf and find values for 2.1 to 2.9:
from scipy.interpolate import Rbf
xs2 = np.arange(10)
ys2 = xs**2 + np.sin(xs2) + 1
interp_func2 = Rbf(xs2, ys2)
newarr4 = interp_func2(np.arange(2.1, 3, 0.1))
print(newarr4)
"""
SciPy Statistical Significance Tests
Statistical significance means that the result that was produced has a reason behind it and wasn't produced randomly or by chance.
The scipy.stats module has functions for performing statistical significance tests.
Below are some techniques and keywords that are important when performing such tasks:
Hypothesis - An assumption about a parameter in population.
Null hypothesis - Assuming that the observation is not statistically significant
Alternate hypothesis - Assuming that the observation is due to some reason
One tailed test - Testing a hypothesis for one side of the value
Two tailed test - Testing a hypothesis for both sides of the value
Alpha value - Level of significance
P value - Tells how close to extreme the data actually is.
T-test - Determines if there is significant defernce between means of two variables and tell if they belong to the same distribution.
The ttest_ind() function takes two samples of same size and produces a tuple of t-statistic and p-value.
"""
#Find if the given values v1 and v2 are from the same distribution:
import numpy as np
from scipy.stats import ttest_ind
v1 = np.random.normal(size=100)
v2 = np.random.normal(size=100)
tt = ttest_ind(v1, v2)
print(tt)
tt1 = ttest_ind(v1, v2).pvalue
print(tt1)
"""z
The KS-test is used to check if given values follow a distributtion. The function takes 2 parameters: the value to be tested and the CDF
A CDF can be either a string or a callable function that returns the probability. 
By default, this test is a two tailed test, but it can also be a one tailed test.
"""
#Find if the given value follows the normal distribution:
from scipy.stats import kstest
v = np.random.normal(size=100)
print(kstest(v, 'norm'))
#The describe() function returns a summary of values in an array. It returns the following description: number of observations(nobs), minimum and maximum values, mean, variance, skewness, kurtosis etc
#Show statistical description of the values in an array:
from scipy.stats import describe
print(describe(v))
"""
Normality tests are based on skewness and kurtosis. The normaltest() function returns p value for the null hypothesis.
Skewness is a measure of symmetry in data. For normal distributions, it is 0. If negative, the data is skewed left and vice versa.
Kurtosis is a measure of whether the data is heavy or lightly tailed to a normal distribution. Positve kurtosis means heavily tailed and vice versa.
"""
from scipy.stats import skew, kurtosis
print(skew(v))
print(kurtosis(v))
from scipy.stats import normaltest
print(normaltest(v))