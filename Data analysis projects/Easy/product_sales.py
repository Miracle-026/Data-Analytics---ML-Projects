#Load the libraries
import pandas as pd
import matplotlib.pyplot as plt
import calendar
import seaborn as sns

#Load the dataset
df = pd.read_csv("C:/Users/DEKATECH/Data analysis projects/Easy/statsfinal.csv")

#Rename the columns for better readability
df = df.rename(columns={
    "Q-P1": "Units of Product 1",
    "Q-P2": "Units of Product 2",
    "Q-P3": "Units of Product 3",
    "Q-P4": "Units of Product 4",
    "S-P1": "Sales of Product 1",
    "S-P2": "Sales of Product 2",
    "S-P3": "Sales of Product 3",
    "S-P4": "Sales of Product 4",
})

#Drop the unnecessary column
df.drop(columns=["Unnamed: 0"], axis=1, inplace=True)
#print(df.head(10))

#Check for missing values in the dataset
cols_with_msg_val = [col for col in df.columns if df[col].isnull().any()]
#print("Columns with missing values:", cols_with_msg_val)      #There are no missing values in the dataset

#Change the type of "Date" column to datetime
df["Date"] = pd.to_datetime(df["Date"], dayfirst=True, errors='coerce')
#print(df.head(30))

df["Month of Sale"] = df["Date"].dt.month_name()
#print(df.head(30))

"""
#Bar chart of total units sold and total sales by product
total_units = {
    "Product 1": df["Units of Product 1"].sum(),
    "Product 2": df["Units of Product 2"].sum(),
    "Product 3": df["Units of Product 3"].sum(),
    "Product 4": df["Units of Product 4"].sum()
}

total_sales = {
    "Product 1": df["Sales of Product 1"].sum(),
    "Product 2": df["Sales of Product 2"].sum(),
    "Product 3": df["Sales of Product 3"].sum(),
    "Product 4": df["Sales of Product 4"].sum()
}

summary_df = pd.DataFrame({
    "Total Units Sold": total_units,
    "Total Sales": total_sales
})

summary_df.plot(kind='bar', figsize=(10, 6))
plt.title('Total Units Sold and Total Sales by Product')
plt.xlabel('Products')
plt.ylabel('Total')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
"""

#Group the data units sold per month for each product
units_sold_monthly = df.groupby(["Month of Sale"])[["Units of Product 1", "Units of Product 2", "Units of Product 3", "Units of Product 4"]].sum().reset_index()
#print(units_sold_monthly)
month_num_p1 = units_sold_monthly["Units of Product 1"].idxmax()+1
month_name_p1 = calendar.month_name[month_num_p1]
#print(f"Product 1 sold the highest in {month_name_p1}, selling {max(units_sold_monthly["Units of Product 1"])} units.")
month_num_p2 = units_sold_monthly["Units of Product 2"].idxmax()+1
month_name_p2 = calendar.month_name[month_num_p2]
#print(f"Product 2 sold the highest in {month_name_p2}, selling {max(units_sold_monthly['Units of Product 2'])} units.")
month_num_p3 = units_sold_monthly["Units of Product 3"].idxmax()+1
month_name_p3 = calendar.month_name[month_num_p3]
#print(f"Product 3 sold the highest in {month_name_p3}, selling {max(units_sold_monthly['Units of Product 3'])} units.")
month_num_p4 = units_sold_monthly["Units of Product 4"].idxmax()+1
month_name_p4 = calendar.month_name[month_num_p4]
#print(f"Product 4 sold the highest in {month_name_p4}, selling {max(units_sold_monthly['Units of Product 4'])} units.")
#Group the data by sales per month for each product
revenue_per_month = df.groupby(["Month of Sale"])[["Sales of Product 1", "Sales of Product 2", "Sales of Product 3", "Sales of Product 4"]].sum().reset_index()
#print(revenue_per_month)
month_num_p1 = revenue_per_month["Sales of Product 1"].idxmax()+1
month_name_p1 = calendar.month_name[month_num_p1]
#print(f"Product 1 earned the highest revenue in {month_name_p1}, making {max(revenue_per_month["Sales of Product 1"])} dollars.")
month_num_p2 = revenue_per_month["Sales of Product 2"].idxmax()+1
month_name_p2 = calendar.month_name[month_num_p2]
#print(f"Product 2 earned the highest revenue in {month_name_p2}, making {max(revenue_per_month["Sales of Product 2"])} dollars.")
month_num_p3 = revenue_per_month["Sales of Product 3"].idxmax()+1
month_name_p3 = calendar.month_name[month_num_p3]
#print(f"Product 3 earned the highest revenue in {month_name_p3}, making {max(revenue_per_month["Sales of Product 3"])} dollars.")
month_num_p4 = revenue_per_month["Sales of Product 4"].idxmax()+1
month_name_p4 = calendar.month_name[month_num_p4]
#print(f"Product 4 earned the highest revenue in {month_name_p4}, making {max(revenue_per_month["Sales of Product 4"])} dollars.")

#Visualize the units sold per month for each product
def barplotunits(x, y, title, color):
    plt.figure(figsize=(10, 6))
    sns.barplot(x=x, y=y, color=color)
    plt.title(title, fontsize=16)
    plt.xticks(fontsize=12, rotation=45)
    plt.xlabel("Months", fontsize=12)
    plt.ylabel("Units Sold", fontsize=12)
    return plt.show()
barplotunits(units_sold_monthly["Month of Sale"], units_sold_monthly["Units of Product 1"], "Units of Product 1 Sold Per Month", "blue")
barplotunits(units_sold_monthly["Month of Sale"], units_sold_monthly["Units of Product 2"], "Units of Product 2 Sold Per Month", "orange")
barplotunits(units_sold_monthly["Month of Sale"], units_sold_monthly["Units of Product 3"], "Units of Product 3 Sold Per Month", "green")
barplotunits(units_sold_monthly["Month of Sale"], units_sold_monthly["Units of Product 4"], "Units of Product 4 Sold Per Month", "red")