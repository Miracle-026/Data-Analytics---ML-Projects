#Pandas
"""
#Lesson 1: Creating, Writing and Reading
import pandas as pd
#Core objects in pandas: DataFrame and Series
#A dataframe is a table which contains an array of individual entries, each of which has a certain value.
df = pd.DataFrame({'Yes':[50,21], 'No':[131,2]})
print(df)
#Dataframes are not limited to integers
df1 = pd.DataFrame({'Bob':['I liked it.', 'It was awful'], 'Sue':['Pretty good', 'Bland']})
print(df1)
#We can change the labels for dataframes by using the index attribute
df2 = pd.DataFrame({'Bob':['I liked it.', 'It was awful'], 'Sue':['Pretty good', 'Bland']}, index=['Product A', 'Product B'])
print(df2)
#A series is a sequence of values but with labels.
series = pd.Series([1,2,3,4,5])
print(series)
#We can assign labels and even a name for the series.
series1 = pd.Series([30,35,40], index=['2015 sales', '2016 sales', '2017 sales'], name='Product A')
print(series1)
#Now let's read a csv file
wine_reviews = pd.read_csv("C:/Users/DEKATECH/ML and data analysis/winemag130kv2.csv")
print(wine_reviews.shape)
print(wine_reviews.head())
wine_reviews1 = pd.read_csv("C:/Users/DEKATECH/ML and data analysis/winemag130kv2.csv", index_col=0)
print(wine_reviews1.head())
"""

"""
#Lesson 2: Indexing, selecting and assigning
#It is important to select relevant data points for quick processing.
import pandas as pd
reviews = pd.read_csv("C:/Users/DEKATECH/ML and data analysis/winemag130kv2.csv", index_col=0)
pd.set_option('display.max_rows', 5)
#In Python, we can access the property of an object by accessing it as an attribute. E.g:
rs = reviews.country
#print(rs)
#For a dictionary, we can use the [] operator
rs1 = reviews['country']
#print(rs1)
#To select a specific series:
rs_spec = reviews['country'][0]
#print(rs_spec)
#Pandas has its own native accessors: loc and iloc. iloc is used for index-based selection and loc is used for label-based selection
riloc = reviews.iloc[0] #to select the first row of data in a df
#print(riloc)
riloc1 = reviews.iloc[:, 0] #to select the first column of data in a df
#print(riloc1)
riloc2 = reviews.iloc[:3, 0] #to select the country column from the first, second and third rows
#print(riloc2)
riloc3 = reviews.iloc[1:3, 0] # to select the country column from the second and third rows
#print(riloc3)
#You can also pass a list to the iloc attribute
riloc4 = reviews.iloc[[0,1,2], 0]
#print(riloc4)
riloc5 = reviews.iloc[-5:] #to select the last 5 elements from the dataset
#print(riloc5)
rloc = reviews.loc[0, 'country'] #to select the first entry
#print(rloc)
rloc1 = reviews.loc[:, ['taster_name', 'taster_twitter_handle', 'points']]
#print(rloc1)
rloc2 = reviews.set_index("title")
#print(rloc2.head)
#Conditional selection
rc = reviews.country == "Italy"
#print(rc)
rc1 = reviews.loc[reviews.country == "Italy"] #to select all rows where the country is Italy
#print(rc1)
rc2 = reviews.loc[(reviews.country == "Italy") & (reviews.points >= 90)] #to select all rows where the country is Italy and the points are greater than or equal to 90
print(rc2)
#isin operator selects data whose values is in a list of values
risin = reviews.loc[reviews.country.isin(['Italy', 'France'])]
#print(risin)
#isnull and notnull lets you highlight values which are/are not empty
rnotnull = reviews.loc[reviews.country.notnull()]
#print(rnotnull)
reviews['critic'] = 'everyone'
#print(reviews['critic'])
reviews['index_backwards'] = range(len(reviews), 0, -1)
print(reviews['index_backwards'])
"""

"""
#Lesson 3: Summary Functions and Maps
import numpy as np
import pandas as pd
pd.set_option('display.max_row', 5)
reviews = pd.read_csv("C:/Users/DEKATECH/ML and data analysis/winemag130kv2.csv", index_col=0)
#Pandas provides many simple summary functions which restructure the data in a useful way.
rsf = reviews.points.describe()
#print(rsf)
#describe() works for both numerical and string input
rsf1 = reviews.taster_name.describe()
#print(rsf1)
#For simple statistic summary about a column, we can use mean()
rsf2 = reviews.points.mean()
#print(rsf2)
#To see a list of unique values, use unique()
rsf3 = reviews.taster_name.unique()
#print(rsf3)
#To see a list of unique values and how often they occur in the dataset, use value_counts()
rsf4 = reviews.taster_name.value_counts()
#print(rsf4)
#A map is a term for a function that takes one set of values and maps them to another set of values.
#There are two methods for mapping: map() and apply()
rpm = reviews.points.mean()
#print(reviews.points.map(lambda p:p - rpm))
#Here's a faster way
rpm2 = reviews.points.mean()
#print(reviews.points - rpm2)
#apply() does same but transforms the whole df by calling a custom method on each row.
def rpm1(row):
    row.points = row.points - rpm
    return row
#print(reviews.apply(rpm1, axis='columns'))
#print(reviews.country + " - " + reviews.region_1)
"""

#Lesson 4: Grouping and sorting
import numpy as np
import pandas as pd
pd.set_option('display.max_row', 5)
reviews = pd.read_csv("C:/Users/DEKATECH/ML and data analysis/winemag130kv2.csv", index_col=0)
#We can use groupby() to group data, instead of value_counts()
#print(reviews.groupby('points').points.count())
#print(reviews.groupby('points').price.min())
#print(reviews.groupby('winery').apply(lambda df: df.title.iloc[0]))
#print(reviews.groupby(['country', 'province']).apply(lambda df: df.loc[df.points.idxmax()]))
#print(reviews.groupby(['country']).price.agg([len, min, max]))
countries_reviewed = reviews.groupby(['country', 'province']).description.agg([len])
#print(countries_reviewed)
#print(type(countries_reviewed.index))