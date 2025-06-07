import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.model_selection import cross_val_score
from xgboost import XGBRegressor

car_sales = pd.read_csv("C:/Users/DEKATECH/Data analysis projects/Easy/car.csv")
print(car_sales.head())

cols_with_msg_val = [col for col in car_sales.columns if car_sales[col].isnull().any()]
print(cols_with_msg_val)

car_sales['Price_in_thousands'] = car_sales['Price_in_thousands'].fillna(car_sales['Price_in_thousands'].mean())
car_sales['Engine_size'] = car_sales['Engine_size'].fillna(car_sales['Engine_size'].mean())
car_sales['Horsepower'] = car_sales['Horsepower'].fillna(car_sales['Horsepower'].mean())
car_sales['Fuel_efficiency'] = car_sales['Fuel_efficiency'].fillna(car_sales['Fuel_efficiency'].mean())

X = car_sales[['Engine_size', 'Fuel_efficiency', 'Horsepower', 'sales']]
y = car_sales.Price_in_thousands

# train_X, test_X, train_y, test_y = train_test_split(X, y, test_size=0.2, random_state=0)

# my_pipeline = Pipeline(steps=[
#     ('preprocessor', SimpleImputer()),
#     ('model', RandomForestRegressor(n_estimators=50, random_state=0))
# ])
# scores = -1 * cross_val_score(my_pipeline, X, y, cv=5, scoring='neg_mean_absolute_error')
# print(scores.mean()) MAE: 5.1

X["EngineSize_to_Horsepower"] = X["Engine_size"] / X["Horsepower"]
X["FuelEfficiency_to_EngineSize"] = X["Fuel_efficiency"] / X["Engine_size"]
X["FuelEfficiency_to_Horsepower"] = X["Fuel_efficiency"] / X["Horsepower"]
X["Sales_to_EngineSize"] = X["sales"] / X["Engine_size"]
X["Sales_to_Horsepower"] = X["sales"] / X["Horsepower"]
X["Sales_to_FuelEfficiency"] = X["sales"] / X["Fuel_efficiency"]
model = RandomForestRegressor(criterion='absolute_error', random_state=0)
scores = cross_val_score(model, X, y, cv=5, scoring='neg_mean_absolute_error')
score = -1 * scores.mean()
print(f"MAE Score: {score:.4}")