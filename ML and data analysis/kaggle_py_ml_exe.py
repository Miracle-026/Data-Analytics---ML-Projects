#Python exercises
#Function to calculate the area of a cirle
def area(radius):
    return 3.142 * (radius)**2
area(22)

#Create a list of 10 random numbers and sort them in ascending order
import random
num = [random.randint(1, 20) for _ in range(10)]
num.sort()
print(num)

#Write a Python program to load the Boston housing dataset and perform exploratory data analysis.
import pandas as pd
boston_url = "C:/Users/DEKATECH/Road to Dev(Python)/housingdata.csv"
boston_data = pd.read_csv(boston_url)
boston_data.head()

#Implement a k-means clustering algorithm to cluster customers based on their buying behaviour
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
df = pd.DataFrame(boston_data.data, columns=boston_data.feature_names)
features = ['RM', 'NOX', 'DIS', 'RAD', 'TAX']
scaler = StandardScaler()
scaled_features = scaler.fit_transform(df[features])
K = 5
KMeans.fit(scaled_features)
cluster_labels = KMeans.labels_
df['cluster'] = cluster_labels
print("Cluster centers:")
print(KMeans.cluster_centers_)
print("Cluster labels:")
print(df[['cluster']])

#Create a random forest classifier to classify handwritten digits.

#Write a Python program to load the Titanic dataset and perform feature engineering.

#Implement a support vector machine (SVM) classifier to classify breast cancer tumors.

#Create a neural network to classify handwritten digits using Keras.

#Write a Python program to load the Wine dataset and perform clustering.

#Implement a logistic regression model to classify credit card transactions.

#Create a k-nearest neighbors (KNN) classifier to classify iris flowers.

#Write a Python program to load the MNIST dataset and perform image classification.

#Implement a gradient boosting classifier to classify credit card transactions.

#Create a principal component analysis (PCA) to reduce the dimensionality of a dataset.

#Write a Python program to load the IMDB dataset and perform sentiment analysis.

#Implement a random forest regressor to predict house prices.

#Create a neural network to predict stock prices using Keras.

#Write a Python program to load the 20 Newsgroups dataset and perform text classification.

#Implement a support vector regressor (SVR) to predict energy consumption.

#Create a k-means clustering algorithm to cluster customers based on their demographics.

#Write a Python program to load the CIFAR-10 dataset and perform image classification.

#Implement a gradient boosting regressor to predict energy consumption.

#Create a decision tree regressor to predict house prices.

#Write a Python program to load the Reuters dataset and perform text classification.

#Implement a random forest classifier to classify credit card transactions.

#Create a neural network to classify handwritten digits using TensorFlow.

#Write a Python program to load the Fashion MNIST dataset and perform image classification.

#Implement a k-nearest neighbors (KNN) regressor to predict house prices.

#Create a principal component analysis (PCA) to reduce the dimensionality of a dataset.

#Write a Python program to load the Stanford Sentiment Treebank dataset and perform sentiment analysis.