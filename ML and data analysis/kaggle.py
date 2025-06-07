#Intro to Python

"""
#Lesson 1: Arithmetic and Variables
print("Hello World")
print(1+2)
print(9-5)
print(((1+3) * (9-2) / 2) ** 2)
test_var = 4+5
print(test_var)
#Calculate the total number of seconds in 4 years
num_years = 4; days_per_year = 365; hours_per_day = 24; minutes_per_hour = 60; seconds_per_minutes = 60
total_secs = num_years * days_per_year * hours_per_day * minutes_per_hour * seconds_per_minutes
print(total_secs)
#Exercise
#Calculate birth rate per minute
births_per_min = 250
births_per_day = births_per_min * hours_per_day * minutes_per_hour
print(births_per_day)
#From the dataset below, calculate the number of passengers that boarded the titanic, the number that survived and the number of minors aboard the ship
import pandas as pd
titanic_data = pd.read_csv("C:/Users/DEKATECH/Road to Dev (Python)/train.csv")
titanic_data.head()
total_passengers = len(titanic_data)
print(total_passengers)
survived_passengers = (titanic_data.Survived == 1).sum()
print(survived_passengers)
minor_passengers = (titanic_data.Age < 18).sum()
print(minor_passengers)
#Calculate the fraction that survived and the fraction that were minors
survived_fraction = survived_passengers / total_passengers
print(survived_fraction)
minor_fraction = minor_passengers / total_passengers
print(minor_fraction)
"""

"""
#Lesson 2: Functions
def add_three(input_var):
    output_var = input_var + 3
    return output_var
print(add_three(5))
#Calculate a weekly paycheck after taxes. 12% is for taxes and the hourly pay is $15/hour
def calculate_pay(hours_worked):
    pay_beforetax = hours_worked * 15
    pay_aftertax = pay_beforetax * (1 - 0.12)
    return pay_aftertax
print(calculate_pay(40))
#Perform the same function above but with more arguments
def calculate_pay1(hours_worked, hour_pay, tax_rate):
    pay_beforetax = hours_worked * hour_pay
    pay_aftertax = pay_beforetax * (1 - tax_rate)
    return pay_aftertax
print(calculate_pay1(40, 24, 0.22))
#Exercise
#Return the expected cost of a house with a number of bedrooms and bathrooms
def get_expected_cost(bedrooms, bathrooms):
    price = 80000 + 30000*bedrooms + 10000*bathrooms
    return price
print(get_expected_cost(2, 2))
#Using the code above, set options for different combinations of bedrooms and bathrooms and set the price for each of them
option_one = get_expected_cost(bedrooms=2, bathrooms=3)
option_two = get_expected_cost(bedrooms=3, bathrooms=2)
option_three = get_expected_cost(bedrooms=3, bathrooms=3)
option_four = get_expected_cost(bedrooms=3, bathrooms=4)
print(option_one, option_two, option_three, option_four)
#Write the function that gets the cost of painting a room based on the length of the walls and ceilings
def get_cost(sqft_walls, sqft_ceiling, sqft_per_gallon, cost_per_gallon):
    total_sqft = sqft_walls + sqft_ceiling
    gallons_needed = total_sqft / sqft_per_gallon
    cost = cost_per_gallon * gallons_needed
    return cost
#Apply the code above to 432 square feet of walls and 144 square feet of ceilings
print(get_cost(432, 144, 400, 15))
import math
cost = get_cost(432, 144, 400, 15)
actual_cost = math.ceil(cost)
print(actual_cost)
"""

"""
#Lesson 3: Data Types
#Redo the house problem but this time use a boolean as an argument
def get_expected_cost_again(beds, baths, has_basement):
    cost = 80000 + 30000*beds + 10000*baths + 40000*has_basement
    return cost
print(get_expected_cost_again(2, 2, True))
#Exercise
#Return the cost of a ring with custome engravings.
def get_cost_ring(engraving, solid_gold):
    cost = solid_gold * (100 + 10*len(engraving)) + (not solid_gold) * (50 + 7*len(engraving))
    return cost
print(get_cost_ring("Hello", True))
print(get_cost_ring("Charlie+Devner", True))
print(get_cost_ring("08/10/2000", True))
"""

"""
#Lesson 4: Conditions and Conditional Statements
#Evaluate the input temperature
def evaluate_temp(temp):
    message = "normal temperature"
    if temp > 37:
        message = "high temperature"
    return message
print(evaluate_temp(36))
#Update the code block above to have a minimum and maximum point
def evaluate_temp1(temp):
    if temp > 38:
        message = "High temperature: Fever"
    elif temp > 35:
        message = "Normal temperature"
    else:
        message = "Low temperature"
    return message
print(evaluate_temp1(40))
#Calculate tax. Less than $12000 pays 25% and more than $12000 pays 30%
def tax_calc(income):
    if income < 12000:
        tax = income * 0.25
    else:
        tax = income * 0.3
    return tax
print(tax_calc(10000))
#Return the dose for a mdeication based on input weight
def get_dose(weight):
    if weight < 5.2:
        dose = 1.25
    elif weight < 7.9:
        dose = 2.5
    elif weight < 10.4:
        dose = 3.75
    elif weight < 15.9:
        dose = 5.0
    elif weight < 21.2:
        dose = 7.5
    else:
        dose = 10.0
    return dose
print(get_dose(12))
#Exercise
#Write code to assign grade to an exam score.
def get_grade(score):
    if score >= 90:
        print("A")
    elif score >=  80:
        print("B")
    elif score >= 70:
        print("C")
    elif score >= 60:
        print("D")
    else:
        print("F")
get_grade(70)
#Perform the exercise in lesson 3 but use conditional formatting
def get_cost_ring1(engraving, solid_gold):
    if solid_gold == True:
        cost = 100 + 10*len(engraving)
    else:
        cost = 50 + 7*len(engraving)
    return cost
print(get_cost_ring1("Dekatech", True))
#Calculate the water bill given the tier and price per 1000 gallons
def get_water_bill(num_gallons):
    if num_gallons <= 8000:
        bill = (5 * num_gallons) / 1000
    elif num_gallons <= 22000:
        bill = (6 * num_gallons) / 1000
    elif num_gallons <= 30000:
        bill = (7 * num_gallons) / 1000
    else:
        bill = (10 * num_gallons) / 1000
    return bill
print(get_water_bill(20000))
#Calculate the data bill a customer uses in a month.
def get_phone_bill(gb):
    if gb <= 15:
        bill = 100
    else:
        bill = 100 + ((gb - 15) * 100)
    return bill
print(get_phone_bill(20))
"""

"""
import math
#Lesson 5: Intro to Lists
#Analyze the following:
hardcover_sales = [139, 128, 172, 139, 191, 168, 170]
#Smallest amount of hardcover sold:
print(min(hardcover_sales))
#Highest amount of hardcover sold:
print(max(hardcover_sales))
#Total sum of all hardcover sales:
print(sum(hardcover_sales))
#Average of all hardcover sales:
print(sum(hardcover_sales) / 7)
#Exercise
menu = ['Stewed meat with onions', 'Bean soup', 'Risotto with trout and shrimp', 'Fish soup with cream and onion', 'Gyro']
#Remove bean soup from the above menu and add roasted beef salad
menu.remove('Bean soup')
menu.append("Roasted beef salad")
print(menu)
num_customers = [137, 147, 135, 128, 170, 174, 165, 146, 126, 159, 141, 148, 132, 147, 168, 153, 170, 161, 148, 152, 141, 151, 131, 149, 164, 163, 143, 143, 166, 171]
#From the list above, find the following:
#Average number in the first 7 days:
avg_num_first = sum(num_customers[:7]) / 7
#Average number in the last 7 days:
avg_num_last = sum(num_customers[-7:]) / 7
#Most customers that visited:
max_month = max(num_customers)
#Least customers that visited:
min_month = min(num_customers)
print(avg_num_first, avg_num_last, max_month, min_month)
#Turn the strings below into lists:
alphabet = "A.B.C.D.E.F.G.H.I.J.K.L.M.N.O.P.Q.R.S.T.U.V.W.X.Y.Z"
letters = alphabet.split(".")
print(letters)
address = "Mr. H. Potter,The cupboard under the Stairs,4 Privet Drive,Little Whinging,Surrey"
addresses = address.split(",")
print(addresses)
#People rate movies. Write a code to return the percentage of people who like the movie (4 and 5)
def percent_liked(ratings):
    list_liked = [i>=4 for i in ratings]
    percent_liked = (sum(list_liked) / len(list_liked)) * 100
    return percent_liked
print(f"{percent_liked([1, 2, 3, 4, 5, 4, 5, 1])}%")
#Write a function that returns the % growth in the total number of users relative to a specified number of years
def percentage_growth(num_users, yrs_ago):
    growth = (num_users[len(num_users)-1]-num_users[len(num_users)-yrs_ago-1])/num_users[len(num_users)-yrs_ago-1] *100
    return math.ceil(growth)
num_users_test = [920344, 1043553, 1204334, 1458996, 1503323, 1593432, 1623463, 1843064, 1930992, 2001078]
print(f"{percentage_growth(num_users_test, 7)}%")
"""