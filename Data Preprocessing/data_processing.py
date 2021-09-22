# Importing libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Importing the dataset
dataset = pd.read_csv('/home/sayani/Desktop/DeepLearning/Data Preprocessing/Data.csv')
X = dataset.iloc[:,:-1].values
y = dataset.iloc[:,3].values

# Taking care of the missing data
from sklearn.impute import SimpleImputer
imputer = SimpleImputer(missing_values = np.nan, strategy = 'mean',verbose=0)
imputer = imputer.fit(X[:,1:3])
X[:,1:3] = imputer.transform(X[:,1:3])

# Encoding categorical data
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
from sklearn.compose import ColumnTransformer

columnTransformer = ColumnTransformer([('Country',OneHotEncoder(),[0])],remainder='passthrough')
X=columnTransformer.fit_transform(X)
print(X)

label_encoder_y = LabelEncoder()
y=label_encoder_y.fit_transform(y)
print(y)


# Splitting the data into training set and test set
from sklearn.model_selection import train_test_split
X_train,X_test,y_train,y_test = train_test_split(X,y,test_size = 0.2)


# Feature scaling
from sklearn.preprocessing import StandardScaler
sc_x=StandardScaler()
X_train = sc_x.fit_transform(X_train)
X_test = sc_x.transform(X_test)
