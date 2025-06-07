#Machine Learning
import pandas as pd

"""
#Lesson 2: Basic Data Exploration
#Load the data
melbourne_file_path = "C:/Users/DEKATECH/Road to Dev (Python)/melb_data.csv"
melbourne_data = pd.read_csv(melbourne_file_path)
melbourne_data.describe()
iowa_file_path = "C:/Users/DEKATECH/Road to Dev (Python)/train.csv"
iowa_data = pd.read_csv(iowa_file_path)
iowa_data.describe()
"""

"""
#Lesson 3: Your First Machine Learning Model
melbourne_file_path = "C:/Users/DEKATECH/Road to Dev (Python)/melb_data.csv"
melbourne_data = pd.read_csv(melbourne_file_path)
melbourne_data.describe()
#The columns property prints out the variables in a dataframe
melbourne_data.columns
#You can select a subset of data using the dot notation and selecting with a column list
#Dot notation (select the prediction target)
y = melbourne_data.Price
print(y)
#Selecting a column list which we an also all features
melbourne_features = ['Rooms', 'Price', 'Distance', 'YearBuilt', 'Lattitude', 'Longtitude', 'Propertycount']
X = melbourne_data[melbourne_features]
X.describe()
X.head()
#Scikit-learn is used to build models and store data in dataframes. It involves:
#Define the model
#Fit the model
#Predict the data using the model
#Evaluate the model's prediction
#Below is an example:
from sklearn.tree import DecisionTreeRegressor
melbourne_model = DecisionTreeRegressor(random_state=1)
melbourne_model.fit(X, y)
#Now make predictions using the fitted model
print(X.head())
print("The predictions are:\n", melbourne_model.predict(X.head()))
"""

"""
#Lesson 4: Model Validation
#Model quality can be summarized into a single metric, using Mean Absolute Error (MAE). Here's a breakdown:
actual = 150000
predicted = 100000
error = actual - predicted
#The MAE returns the average of the absolute values of the errors in our model.
melbourne_file_path = "C:/Users/DEKATECH/Road to Dev (Python)/melb_data.csv"
melbourne_data = pd.read_csv(melbourne_file_path)
filtered_melbourne_data = melbourne_data.dropna(axis=0)
y = filtered_melbourne_data.Price
melbourne_features = ['Rooms', 'Bathroom', 'Landsize', 'BuildingArea', 'YearBuilt', 'Lattitude', 'Longtitude']
X = filtered_melbourne_data[melbourne_features]
from sklearn.tree import DecisionTreeRegressor
melbourne_model = DecisionTreeRegressor()
melbourne_model.fit(X, y)
from sklearn.metrics import mean_absolute_error
predicted_home_prices = melbourne_model.predict(X)
mean_absolute_error(y, predicted_home_prices)
#The problem with the "in-sample" scores like above is because the model becomes inconsistent with new data.
#Scikit-learn has a function that breaks the data into two pieces, one for training and the other for validation.
from sklearn.model_selection import train_test_split
train_X, val_X, train_y, val_y = train_test_split(X, y, random_state=0)
melbourne_model = DecisionTreeRegressor()
melbourne_model.fit(train_X, train_y)
val_predictions = melbourne_model.predict(val_X)
print(mean_absolute_error(val_y, val_predictions))
"""

"""
#Lesson 5: Underfitting and Overfitting
#Overfitting is a phenomenon where a model matches the training data perfectly but fails with new data.
#Underfitting is when a model fails to capture important distinctions and patterns in data.
melbourne_file_path = 'C:/Users/DEKATECH/Road to Dev (Python)/melb_data.csv'
melbourne_data = pd.read_csv(melbourne_file_path)
filtered_melbourne_data = melbourne_data.dropna(axis=0)
y = filtered_melbourne_data.Price
melbourne_features = ['Rooms', 'Bathroom', 'Landsize', 'BuildingArea', 'YearBuilt', 'Lattitude', 'Longtitude']
X = filtered_melbourne_data[melbourne_features]
from sklearn.model_selection import train_test_split
train_X, val_X, train_y, val_y = train_test_split(X, y,random_state = 0)
from sklearn.metrics import mean_absolute_error
from sklearn.tree import DecisionTreeRegressor
def get_mae(max_leaf_nodes, train_X, val_X, train_y, val_y):
    model = DecisionTreeRegressor(max_leaf_nodes=max_leaf_nodes, random_state=0)
    model.fit(train_X, train_y)
    preds_val = model.predict(val_X)
    mae = mean_absolute_error(val_y, preds_val)
    return(mae)
for max_leaf_nodes in [5, 50, 500, 5000]:
    my_mae = get_mae(max_leaf_nodes, train_X, val_X, train_y, val_y)
    print("Max leaf nodes: %d  \t\t Mean Absolute Error:  %d" %(max_leaf_nodes, my_mae))
"""

"""
#Lesson 6: Random Forests
#The problem with Decision Tree is overfitting and underfitting. But random forests clears up these two problems.
melbourne_file_path = 'C:/Users/DEKATECH/Road to Dev (Python)/melb_data.csv'
melbourne_data = pd.read_csv(melbourne_file_path)
melbourne_data = melbourne_data.dropna(axis=0)
y = melbourne_data.Price
melbourne_features = ['Rooms', 'Bathroom', 'Landsize', 'BuildingArea', 'YearBuilt', 'Lattitude', 'Longtitude']
X = melbourne_data[melbourne_features]
from sklearn.model_selection import train_test_split
train_X, val_X, train_y, val_y = train_test_split(X, y,random_state = 0)
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error
forest_model = RandomForestRegressor(random_state=1)
forest_model.fit(train_X, train_y)
melb_pred = forest_model.predict(val_X)
print(mean_absolute_error(val_y, melb_pred))
"""


#Intermediate Machine Learning
"""
#Lesson 1: Introduction
#We'll tackle missing values, categorical variables, design pipelines, implement cross-validation, XGBoost, and avoid leakage
import pandas as pd
from sklearn.model_selection import train_test_split
#Read the data
X_full = pd.read_csv("C:/Users/DEKATECH/ML and data analysis/train1.csv")
X_test_full = pd.read_csv("C:/Users/DEKATECH/ML and data analysis/test1.csv")
#Obtain target and predictors
y = X_full.SalePrice
features = ['LotArea', 'YearBuilt', '1stFlrSF', '2ndFlrSF', 'FullBath', 'BedroomAbvGr','TotRmsAbvGrd']
X = X_full[features].copy()
X_test = X_test_full[features].copy()
#Break off validation set from training data
X_train, X_valid, y_train, y_valid = train_test_split(X, y, train_size=0.8, test_size=0.2, random_state=0)
#Show few rows of data to understand what you're working with
X_train.head()
#Include different random forest models
from sklearn.ensemble import RandomForestRegressor
model_1 = RandomForestRegressor(n_estimators=50, random_state=0)
model_2 = RandomForestRegressor(n_estimators=100, random_state=0)
model_3 = RandomForestRegressor(n_estimators=100, criterion='absolute_error', random_state=0)
model_4 = RandomForestRegressor(n_estimators=200, min_samples_split=20, random_state=0)
model_5 = RandomForestRegressor(n_estimators=100, max_depth=7, random_state=0)
models = [model_1, model_2, model_3, model_4, model_5]
#Include a function to compare the models and select the best
from sklearn.metrics import mean_absolute_error
def score_model(model, X_t=X_train, X_v=X_valid, y_t=y_train, y_v=y_valid):
    model.fit(X_t, y_t)
    preds = model.predict(X_v)
    return mean_absolute_error(y_v, preds)
for i in range(0, len(models)):
    mae = score_model(models[i])
    print("Model %d MAE: %d" % (i+1, mae))
"""

"""
#Lesson 2: Missing Values
#There are 3 approaches to deal with missing values: Drop columns with missing values, imputation and extension to imputation
#The problem with dropping columns is that the model loses a lot of data. However, imputation fills in the gaps.
#First we define a model
import pandas as pd
from sklearn.model_selection import train_test_split
data = pd.read_csv("C:/Users/DEKATECH/ML and data analysis/melb_data.csv")
y = data.Price
pred = data.drop(['Price'], axis=1)
X = pred.select_dtypes(exclude=['object'])
X_train, X_valid, y_train, y_valid = train_test_split(X, y, train_size=0.8, test_size=0.2, random_state=0)
#Then we define a function to measure the quality of each approach
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error
def score_dataset(X_train, X_valid, y_train, y_valid):
    model = RandomForestRegressor(n_estimators=10, random_state=0)
    model.fit(X_train, y_train)
    preds = model.predict(X_valid)
    return mean_absolute_error(y_valid, preds)
#Score from the first approach
#Get names of columns with missing values
cols_with_missing = [col for col in X_train.columns if X_train[col].isnull().any()]
#Drop columns with missing values in training and validation data
reduced_X_train = X_train.drop(cols_with_missing, axis=1)
reduced_X_valid = X_valid.drop(cols_with_missing, axis=1)
print("MAE from approach 1 (Drop columns with missing values):")
print(score_dataset(reduced_X_train, reduced_X_valid, y_train, y_valid))
#Next we use SimpleImputer to do the second approach (replace missing values)
from sklearn.impute import SimpleImputer
my_imputer = SimpleImputer()
imputed_X_train = pd.DataFrame(my_imputer.fit_transform(X_train))
imputed_X_valid = pd.DataFrame(my_imputer.transform(X_valid))
#Imputation removes column names, so we'll have to put them back
imputed_X_train.columns = X_train.columns
imputed_X_valid.columns = X_valid.columns
print("MAE from approach 2 (Imputation):")
print(score_dataset(imputed_X_train, imputed_X_valid, y_train, y_valid))
#Next we'll impute missing values and at the same time keep track of which values were imputed
X_train_plus = X_train.copy()
X_valid_plus = X_valid.copy()
for col in cols_with_missing:
    X_train_plus[col+'_was_missing'] = X_train_plus[col].isnull()
    X_valid_plus[col+'_was_missing'] = X_valid_plus[col].isnull()
my_imputer1 = SimpleImputer()
imputed_X_train_plus = pd.DataFrame(my_imputer1.fit_transform(X_train_plus))
imputed_X_valid_plus = pd.DataFrame(my_imputer1.transform(X_valid_plus))
imputed_X_train_plus.columns = X_train_plus.columns
imputed_X_valid_plus.columns = X_valid_plus.columns
print("MAE from approach 3 (Extension to imputation):")
print(score_dataset(imputed_X_train_plus, imputed_X_valid_plus, y_train, y_valid))
#Before all this, it would make sense to do some preliminary investigation
print(X_train.shape)
missing_val_count_by_column = (X_train.isnull().sum())
print(missing_val_count_by_column[missing_val_count_by_column > 0])
"""

"""
#Lesson 3: Categorical Variables
#A categorical variable is one that takes a limited number of values.
#Approaches to preprocess categorical variable: dropping categorical variables, ordinal encoding and one-hot encoding.
#Ordinal encoding assigns each unique value to a different integer. These work for values that have a predetermined ranking.
#One-hot encoding creates new columns indicating the presence (or absence) of each possible value in the original data. This approach works well if there is no clear ordering of the values.
import pandas as pd
from sklearn.model_selection import train_test_split
data = pd.read_csv("C:/Users/DEKATECH/ML and data analysis/melb_data.csv")
y = data.Price
X = data.drop(['Price'], axis=1)
X_train_full, X_valid_full, y_train, y_valid = train_test_split(X, y, train_size=0.8, test_size=0.2, random_state=0)
cols_with_missing = [col for col in X_train_full.columns if X_train_full[col].isnull().any()]
X_train_full.drop(cols_with_missing, axis=1, inplace=True)
X_valid_full.drop(cols_with_missing, axis=1, inplace=True)
# "Cardinality" means the number of unique values in a column
# Select categorical columns with relatively low cardinality (convenient but arbitrary)
low_cardinality_cols = [cname for cname in X_train_full.columns if X_train_full[cname].nunique() < 10 and X_train_full[cname].dtype=="object"]
#Select numerical columns
numerical_cols = [cname for cname in X_train_full.columns if X_train_full[cname].dtype in ['int64', 'float64']]
#Keep selected columns only
my_cols = low_cardinality_cols + numerical_cols
X_train = X_train_full[my_cols].copy()
X_valid = X_valid_full[my_cols].copy()
#Let's take a peek
print(X_train.head())
#Next we obtain a list of all categorical variables in the training data
s = (X_train.dtypes=='object')
object_cols = list(s[s].index)
print("Categorical variables: ", object_cols)
#We define a function to measure the quality of each approach
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error
def score_dataset(X_train, X_valid, y_train, y_valid):
    model = RandomForestRegressor(n_estimators=100, random_state=0)
    model.fit(X_train, y_train)
    preds = model.predict(X_valid)
    return mean_absolute_error(y_valid, preds)
#Score from approach 1: Dropping columns with categorical variables
drop_X_train = X_train.select_dtypes(exclude=['object'])
drop_X_valid = X_valid.select_dtypes(exclude=['object'])
print("MAE from approach 1: ", score_dataset(drop_X_train, drop_X_valid, y_train, y_valid))
#Score from approach 2: Ordinal encoding
from sklearn.preprocessing import OrdinalEncoder
label_X_train = X_train.copy()
label_X_valid = X_valid.copy()
ordinal_encoder = OrdinalEncoder()
label_X_train[object_cols] = ordinal_encoder.fit_transform(X_train[object_cols])
label_X_valid[object_cols] = ordinal_encoder.transform(X_valid[object_cols])
print("MAE from approach 2: ", score_dataset(label_X_train, label_X_valid, y_train, y_valid))
#Score from approach 3: One-hot encoder
from sklearn.preprocessing import OneHotEncoder
OH_encoder = OneHotEncoder(handle_unknown='ignore', sparse_output=False)
OH_cols_train = pd.DataFrame(OH_encoder.fit_transform(X_train[object_cols]))
OH_cols_valid = pd.DataFrame(OH_encoder.transform(X_valid[object_cols]))
OH_cols_train.index = X_train.index
OH_cols_valid.index = X_valid.index
num_X_train = X_train.drop(object_cols, axis=1)
num_X_valid = X_valid.drop(object_cols, axis=1)
OH_X_train = pd.concat([num_X_train, OH_cols_train], axis=1)
OH_X_valid = pd.concat([num_X_valid, OH_cols_valid], axis=1)
OH_X_train.columns = OH_X_train.columns.astype(str)
OH_X_valid.columns = OH_X_valid.columns.astype(str)
print("MAE from approach 3: ", score_dataset(OH_X_train, OH_X_valid, y_train, y_valid))
"""

"""
#Lesson 4: Pipelines
#Pipelines are a simple way to keep data preprocessing and modeling code organized.
import pandas as pd
from sklearn.model_selection import train_test_split
data = pd.read_csv("C:/Users/DEKATECH/ML and data analysis/melb_data.csv")
y = data.Price
X = data.drop(['Price'], axis=1)
X_train_full, X_valid_full, y_train, y_valid = train_test_split(X, y, train_size=0.8, test_size=0.2, random_state=0)
categorical_cols = [cname for cname in X_train_full.columns if X_train_full[cname].nunique() < 10 and X_train_full[cname].dtype=='object']
numerical_cols = [cname for cname in X_train_full.columns if X_train_full[cname].dtype in ['int64', 'float64']]
my_cols = categorical_cols + numerical_cols
X_train = X_train_full[my_cols].copy()
X_valid = X_valid_full[my_cols].copy()
#print(X_train.head())
#Now for the pipeline. 
#1.) First define preprocessing steps
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import OneHotEncoder
#1.1.) Preprocessing for numerical data
numerical_transformer = SimpleImputer(strategy='constant')
#1.2.) Preprocessing for categorical data
categorical_transformer = Pipeline(steps=[
    ('imputer', SimpleImputer(strategy='most_frequent')),
    ('onehot', OneHotEncoder(handle_unknown='ignore'))
])
#1.3) Bundle preprocessing for categorical and numerical data
preprocessor = ColumnTransformer(
    transformers=[
        ('num', numerical_transformer, numerical_cols),
        ('cat', categorical_transformer, categorical_cols)
    ]
)
#2.) Next we define the model
from sklearn.ensemble import RandomForestRegressor
model = RandomForestRegressor(n_estimators=100, random_state=0)
#3.) Create and evaluate the pipeline
from sklearn.metrics import mean_absolute_error
my_pipeline = Pipeline(steps=[
    ('preprocessor', preprocessor),
    ('model', model)
])
my_pipeline.fit(X_train, y_train)
preds = my_pipeline.predict(X_valid)
score = mean_absolute_error(y_valid, preds)
print('MAE: ', score)
"""

"""
#Lesson 5: Cross Validation
#Cross validation is a process of running the modeling process on different subsets of the data to get multiple measures of model quality.
#It is more optimal to use cross-validation for smaller datasets.
import pandas as pd
data = pd.read_csv("C:/Users/DEKATECH/ML and data analysis/melb_data.csv")
cols_to_use = ['Rooms', 'Distance', 'Landsize', 'BuildingArea', 'YearBuilt']
X = data[cols_to_use]
y = data.Price
#Next define a pipeline to fill in missing values and random forest to make predictions
from sklearn.ensemble import RandomForestRegressor
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
my_pipeline = Pipeline(steps=[
    ('preprocessor', SimpleImputer()),
    ('model', RandomForestRegressor(n_estimators=50, random_state=0))
])
#Next we obtain cross-validation scores
from sklearn.model_selection import cross_val_score
scores = -1 * cross_val_score(my_pipeline, X, y, cv=5, scoring='neg_mean_absolute_error')
print('MAE scores:\n', scores)
#Then we get the average to get a single measure of model quality
print("Average measure of model quality: ", scores.mean())
"""

"""
#Lesson 6: Gradient/XG Boost
#Gradient Boosting is a method that goes through cycles to iteratively add models into an ensemble.
import pandas as pd
from sklearn.model_selection import train_test_split
data = pd.read_csv("C:/Users/DEKATECH/ML and data analysis/melb_data.csv")
cols_to_use = ['Rooms', 'Distance', 'Landsize', 'BuildingArea', 'YearBuilt']
X = data[cols_to_use]
y = data.Price
X_train, X_valid, y_train, y_valid = train_test_split(X, y)
#Next we add the xgboost library
from xgboost import XGBRegressor
my_model = XGBRegressor()
my_model.fit(X_train, y_train)
#Then we make predictions and evaluate the model
from sklearn.metrics import mean_absolute_error
preds = my_model.predict(X_valid)
print("MAE: ", mean_absolute_error(y_valid, preds))
#We can tune some parameters to affect accuracy and training speed.
my_model = XGBRegressor(n_estimators=500)
my_model.fit(X_train, y_train)
#We can also add early_stopping_rounds
my_model = XGBRegressor(n_estimators=500, early_stopping_rounds=5)
my_model.fit(X_train, y_train, eval_set=[(X_valid, y_valid)], verbose=False)
#We can also add learning_rate
my_model = XGBRegressor(n_estimators=500, learning_rate=0.05, early_stopping_rounds=5)
my_model.fit(X_train, y_train, eval_set=[(X_valid, y_valid)], verbose=False)
#And n_jobs
my_model = XGBRegressor(n_estimators=500, learning_rate=0.05, n_jobs=4, early_stopping_rounds=5)
my_model.fit(X_train, y_train, eval_set=[(X_valid, y_valid)], verbose=False)
preds1 = my_model.predict(X_valid)
print("MAE: ", mean_absolute_error(y_valid, preds1))
"""

"""
#Lesson 7: Data Leakage
#This happens when training data contains information about the target, but similar data will not be available when the model is used for prediction.
#This simply means the model will look accurate, then becomes very inaccurate when the model is used to make decisions.
#There are two main types of leakage: target leakage and train-test contamination.
#Target leakage occurs when predictors include data that will not be available by the time predictions are made.
#Train-test contamination occurs when the training data isn't distinguished from the validation data.
#Example:
import pandas as pd
data = pd.read_csv("C:/Users/DEKATECH/ML and data analysis/credit_card.csv", true_values=['yes'], false_values=['no'])
y = data.card
X = data.drop(['card'], axis=1)
print('Number of rows in the dataset', X.shape[0])
print(X.head())
from sklearn.pipeline import make_pipeline
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import cross_val_score
my_pipeline = make_pipeline(RandomForestClassifier(n_estimators=100))
cv_scores = cross_val_score(my_pipeline, X, y, cv=5, scoring='accuracy')
print('Cross-validation accuracy: %f' % cv_scores.mean())
#Let's do some basic data comparison
expenditures_cardholders = X.expenditure[y]
expenditures_noncardholders = X.expenditure[~y]
print('Fraction of those who did not receive a card and had no expenditures: %.2f' %((expenditures_noncardholders == 0).mean()))
print('Fraction of those who received a card and had no expenditures: %.2f' %((expenditures_cardholders == 0).mean()))
#We see that there are no expenditures for those who did not receive a card, and 2% of the people who received a card had no expenditures.
#This seems like a case of target leakage, so let's fix it.
#First, drop leaky predictors
pot_leaks = ['expenditure', 'share', 'active', 'majorcards']
X2 = X.drop(pot_leaks, axis=1)
cv_scores = cross_val_score(my_pipeline, X2, y, cv=5, scoring='accuracy')
print('Cross-val accuracy: %f' % cv_scores.mean())
"""