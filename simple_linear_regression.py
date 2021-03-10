# -*- coding: utf-8 -*-
"""Simple Linear Regression.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1YSGUrWY3sm1e1Fspulq1D0TJDV5FjBfC
"""

# Commented out IPython magic to ensure Python compatibility.
#Importing the libraries
import numpy as np
import pandas as pd
from sklearn.model_selection import KFold
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error 
from sklearn import metrics 
import matplotlib.pyplot as plt
# %matplotlib inline

#Reading the csv file (data file)
link = "http://bit.ly/w-data"
read_data = pd.read_csv(link)
print("Imported Successfully")

#Know the number of rows and columns of the data file
read_data.shape

#Print the data as per the number of rows you get above
read_data.head(25)

#Visualizing the Data
x = list(read_data['Hours'])
y = list(read_data['Scores'])
plt.scatter(x, y, c='green', s=100, alpha=0.7)
plt.xlabel('Hours Studied by the Student')
plt.ylabel('Percentage obtained by the Student')
plt.title('Hours Vs Percentage')
plt.show()

#Preparing the data using kfold cross validation 
dataX = read_data.iloc[:, :-1].values  
dataY = read_data.iloc[:, 1].values  
#prepare cross validatation
kfold=KFold(5,shuffle=True,random_state=1)
#enumerate splits
for train_ix, test_ix in kfold.split(dataX):
  #select rows for train and test
  trainX,trainY,testX,testY = dataX[train_ix],dataY[train_ix],dataX[test_ix],dataY[test_ix]

#Training the data  
#define model
model=LinearRegression()
#fit model
model.fit(trainX,trainY)
print("Training Complete")

#Equation to plot the regression line

#Y = mX + c

# y --> dependant variable
# m --> slope of line
# X --> independant variable
# c --> y-intercept

line = model.coef_*dataX + model.intercept_

# Plotting for the test data
plt.scatter(dataX, dataY, c='hotpink', s=100, alpha=0.7)
plt.plot(dataX, line);
plt.show()

#Predicting the data

#Displaying the test data that would be used for prediction
print(testX)
pred_Y = model.predict(testX)
#Changing the dimension of the test data and storing in another variable 
import copy
t_X = copy.deepcopy(testX)
t_X.shape=(5,)

#Displaying the difference between the actual output and predicted output
df = pd.DataFrame({'Hours':t_X, 'Actual Percentage': testY, 'Predicted Percentage': pred_Y})  
print(df)

#Testing the predictions on manually inserted data
h = np.array([[8.8]])
p = model.predict(h)
print('Hours: ', int(h) , ' --->  Predicted Percentage: ', int(p))

# Calculation of Mean Squared Error (MSE) 
print("Mean Squared Error: {:.2f}".format(mean_squared_error(testY,pred_Y)))

# Calculation of Root Mean Squared Error (RMSE) 
print("Root Mean Squared Error: {:.2f}".format(np.sqrt(mean_squared_error(testY,pred_Y))))

# Calculation of Mean Absolute Error (MAE)  
print("Mean Absolute Error: {:.2f}".format(metrics.mean_absolute_error(testY,pred_Y)))