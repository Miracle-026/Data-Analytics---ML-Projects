#Feature Engineering
"""
#Lesson 1: Introduction
#Feature engineering is the process of creating new input features or modifying existing ones to improve the performance of a machine learning model. 
#It involves transforming raw data into a format that makes it easier for the model to learn patterns and make accurate predictions.
import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import cross_val_score
df = pd.read_csv("C:/Users/DEKATECH/ML and data analysis/concrete.csv")
#print(df.head())
#First let's establish a baseline by training the model on unaugumented dataset.
X = df.copy()
y = X.pop("CompressiveStrength")
baseline = RandomForestRegressor(criterion='absolute_error', random_state=0)
baseline_score = cross_val_score(baseline, X, y, cv=5, scoring='neg_mean_absolute_error')
baseline_score = -1 * baseline_score.mean()
#print(f"MAE Baseline Score: {baseline_score:.4}")
#It might be good practice to add ratios
X['FCRatio'] = X['FineAggregate'] / X['CoarseAggregate']
X['AggCmtRatio'] = (X['CoarseAggregate'] + X['FineAggregate']) / X['Cement']
X['WtrCmtRatio'] = X['Water'] / X['Cement']
model = RandomForestRegressor(criterion='absolute_error', random_state=0)
score = cross_val_score(model, X, y, cv=5, scoring='neg_mean_absolute_error')
score = -1 * score.mean()
print(f"MAE Score with Ratio Features: {score:.4}")
"""

#Lesson 2: Mutual Information
#Mutual information is a measure of how much knowing one piece of information tells you about another piece of information.
#It detects any kind of relationship in a dataset and describes them in terms of uncertainty.
import pandas as pd
from sklearn.model_selection import cross_val_score
from sklearn.ensemble import RandomForestRegressor
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
sns.set_style("whitegrid")
#plt.style.use("seaborn-whitegrid")
df = pd.read_csv("C:/Users/DEKATECH/ML and data analysis/automobile_data.csv")
df.replace('?', np.nan, inplace=True)
cols_with_msg_vals = [col for col in df.columns if df[col].isnull().any()]
print(cols_with_msg_vals)
df['normalized-losses'] = df['normalized-losses'].fillna(df['normalized-losses'].mean())
df['num-of-doors'] = df['num-of-doors'].fillna(df['num-of-doors'].mean())
df['']
#print(df.head())
# X = df.copy()
# y = X.pop('price')
# for colname in X.select_dtypes('object'):
#     X[colname], _ = X[colname].factorize()
# discrete_features = X.dtypes == int
# from sklearn.feature_selection import mutual_info_regression
# def make_mi_scores(X, y, discrete_features):
#     mi_scores = mutual_info_regression(X, y, discrete_features=discrete_features)
#     mi_scores = pd.Series(mi_scores, name="MI Scores", index=X.columns)
#     mi_scores = mi_scores.sort_values(ascending=False)
#     return mi_scores
# mi_scores = make_mi_scores(X, y, discrete_features)
# print(f"MI Scores: {mi_scores:.3}")