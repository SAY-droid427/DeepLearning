import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

dataset = pd.read_csv('/home/sayani/Desktop/DeepLearning/Simple Linear Regression/Salary_Data.csv')

X = dataset.iloc[:,:-1].values
y = dataset.iloc[:,1:2].values


# Splitting the data into test and training models
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=1/3,random_state=0)

# Fitting simple linear regression to the training set
from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(X_train, y_train)

# Predicting the test set results
y_pred = regressor.predict(X_test)
print(y_test)
print(y_pred)

# Visualising the training set results
plt.scatter(X_train,y_train, color = 'red')
plt.plot(X_train, regressor.predict(X_train),color='blue')
plt.title('Salary vs Years Of Experience')
plt.xlabel('Years of experience')
plt.ylabel('Salary')
plt.show()

# Visulaising the test set results
plt.scatter(X_test,y_test,color = 'red')
plt.plot(X_test, y_pred,color = 'blue')
plt.title('Salary vs Years Of Experience')
plt.xlabel('Years of experience')
plt.ylabel('Salary')
plt.show()
