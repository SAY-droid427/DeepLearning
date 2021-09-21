# Importing libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Importing the dataset
dataset = pd.read_csv('/home/sayani/Desktop/DeepLearning/Data Preprocessing/Data.csv')
X = dataset.iloc[:,:-1].values
y = dataset.iloc[:,3].values

print(X)
print(y)
