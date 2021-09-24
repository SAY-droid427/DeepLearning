# Import data
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Read data from csv file
dataset = pd.read_csv('/home/sayani/Desktop/DeepLearning/Multiple Linear Regression/50_Startups.csv')
X = dataset.iloc[:,:-1].values
y = dataset.iloc[:,4].values


# Pre-processing the categorical data
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
from sklearn.compose import ColumnTransformer

columnTransformer = ColumnTransformer([('State',OneHotEncoder(),[3])],remainder='passthrough')
X = columnTransformer.fit_transform(X)

# Avoiding dummy variable trap
X = X[:,1:]
print(X)

# Split data into training and test set
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X,y,train_size=0.2,random_state=0)


