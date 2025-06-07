import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import calendar

product_sales = pd.read_csv("C:/Users/DEKATECH/Data analysis projects/Easy/product_sales.csv")
#print(product_sales)

"""
Answer these questions:
1. How many products were sold in total?
2. What is the total revenue generated from all products?
3. Which product had the highest sales?
4. What is the average number of units sold per product?
5. How many unique products are there?
6. Discuss any trends or patterns you observe in the sales data.
"""

# 1. How many products were sold in total?
total_products_sold = product_sales['Total Units'].sum()
#print(f"The total number of products sold is: {total_products_sold}")

# 2. What is the total revenue generated from all products?
total_revenue = (product_sales['Total Profit']).sum()
#print(f"The total revenue generated from all products is: ${total_revenue:.2f}")

# 3. Which product had the highest sales?
product_cols = ['Cream', 'Detergent', 'Moisturizer', 'Sanitizer', 'Shampoo', 'Soap']
total_sales_by_product = product_sales[product_cols].sum()
highest_selling_product = total_sales_by_product.idxmax()
highest_selling_value = total_sales_by_product.max()
#print(f"The product with the highest sales is: {highest_selling_product}, selling {highest_selling_value} units.")

# 4. What is the average number of units sold per product?
average_units_sold = product_sales['Total Units'].mean()
#print(f"The average number of units sold per product is: {average_units_sold:.2f}")

# 5. How many unique products are there?
unique_products = product_sales[product_cols].nunique()
#print(f"The number of unique products is: {unique_products}")

# 6. Discuss any trends or patterns you observe in the sales data.
# Observing trends or patterns in the sales data
units_sold_monthly = product_sales.groupby(['Month'])[['Cream', 'Detergent', 'Moisturizer', 'Sanitizer', 'Shampoo', 'Soap']].sum().reset_index()
def barplot(x, y, title, color):
    plt.figure(figsize=(10, 6))
    sns.barplot(x=x, y=y, color=color)
    plt.title(title)
    plt.xlabel('Products')
    plt.ylabel('Units Sold')
    plt.xticks(rotation=45)
    return plt.show()
"""
barplot(units_sold_monthly['Month'], units_sold_monthly['Cream'], 'Total Units of Cream Sold Per Month', 'skyblue')
barplot(units_sold_monthly['Month'], units_sold_monthly['Detergent'], 'Total Units of Detergent Sold Per Month', 'skyblue')
barplot(units_sold_monthly['Month'], units_sold_monthly['Moisturizer'], 'Total Units of Moisturizer Sold Per Month', 'skyblue')
barplot(units_sold_monthly['Month'], units_sold_monthly['Sanitizer'], 'Total Units of Sanitizer Sold Per Month', 'skyblue')
barplot(units_sold_monthly['Month'], units_sold_monthly['Shampoo'], 'Total Units of Shampoo Sold Per Month', 'skyblue')
barplot(units_sold_monthly['Month'], units_sold_monthly['Soap'], 'Total Units of Soap Sold Per Month', 'skyblue')
"""
revenue_per_month = product_sales.groupby(['Month'])[['Total Profit']].sum().reset_index()
#print(revenue_per_month)
def barplot1(x, y, title, color):
    plt.figure(figsize=(10, 6))
    sns.barplot(x=x, y=y, color=color)
    plt.title(title)
    plt.xlabel('Months')
    plt.ylabel('Revenue generated')
    plt.xticks(rotation=45)
    return plt.show()
#barplot1(revenue_per_month['Month'], revenue_per_month['Total Profit'], 'Total Revenue Generated Per Month', 'skyblue')
month_cream = units_sold_monthly['Month'].idxmax()+1
month_name_cream = calendar.month_name[month_cream]
print(f"Cream sold the highest in {month_name_cream}, selling {units_sold_monthly['Cream'].max()} units.")
month_detergent = units_sold_monthly['Month'].idxmax()+1
month_name_detergent = calendar.month_name[month_detergent]
print(f"Detergent sold the highest in {month_name_detergent}, selling {units_sold_monthly['Detergent'].max()} units.")
month_moisturizer = units_sold_monthly['Month'].idxmax()+1
month_name_moisturizer = calendar.month_name[month_moisturizer]
print(f"Moisturizer sold the highest in {month_name_moisturizer}, selling {units_sold_monthly['Moisturizer'].max()} units.")
month_sanitizer = units_sold_monthly['Month'].idxmax()+1
month_name_sanitizer = calendar.month_name[month_sanitizer]
print(f"Sanitizer sold the highest in {month_name_sanitizer}, selling {units_sold_monthly['Sanitizer'].max()} units.")
month_shampoo = units_sold_monthly['Month'].idxmax()+1
month_name_shampoo = calendar.month_name[month_shampoo]
print(f"Shampoo sold the highest in {month_name_shampoo}, selling {units_sold_monthly['Shampoo'].max()} units.")
month_soap = units_sold_monthly['Month'].idxmax()+1
month_name_soap = calendar.month_name[month_soap]
print(f"Soap sold the highest in {month_name_soap}, selling {units_sold_monthly['Soap'].max()} units.")
