"""
Pandas
Pandas is a Python library used for working with data sets. It has functions for analyzing, cleaning, exploring and manipulating data.
The name 'Pandas' has a reference to both 'Panel Data' and 'Python Data Analysis' and was created by Wes McKinney in 2008.
Pandas allows us to analyze big data and make conclusions based on statistical theories. It can also clean messy data sets and make them readable and relevant.
"""
import pandas as pd
mydataset = {
	'cars': ["BMW", "Volvo", "Ford"],
	'passings': [3,7,2]
}
myvar = pd.DataFrame(mydataset)
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