import pandas as pd
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn import preprocessing
from sklearn import datasets, linear_model
from sklearn.metrics import mean_squared_error, r2_score
import matplotlib.pyplot as plot
from scipy import stats

#from sklearn import tree
##from sklearn.linear_model import LinearRegression
#from sklearn.metrics import mean_squared_error, r2_score

url = 'https://raw.githubusercontent.com/WHPAN0108/BHT-DataScience-S23/main/regression/data/Fish.csv'
df = pd.read_csv(url)
#df = dataframe.values




##### TASK 1
# no na values in data frame
print(df.isnull().values.any())

# before continuing, we need to convert the labels from y to some numeric values 
le = preprocessing.LabelEncoder()
le.fit(df['Species'])
#print(le)

df['categorical_species'] = le.transform(df['Species'])

# split data into features X and labels y
X= df.loc[:,[ "Length1", "Length2", "Length3", "Height", "Width", "categorical_species"]]#.values
y=df["Weight"]#.values # what we want to predict


print('######################################################################')
print('                             TASK 1                                \n    ')
X_train, X_test, y_train, y_test = train_test_split(X,y ,
                                   random_state=104, 
                                   test_size=0.3, train_size=0.7, 
                                   shuffle=True)




print('Task 1 Linear Regression')

## Linear regression
model_1 = LinearRegression()
model_1.fit(X_train, y_train)

# predicting labels (species) on test set
y_pred = model_1.predict(X_test)

# The root mean squared error on test set
print("Root mean squared error: %.2f" % float(format(np.sqrt(mean_squared_error(y_test, y_pred)), '.3f')))
# R2 on test set
print("Coefficient of determination: %.2f" % r2_score(y_test, y_pred))


# Plot outputs

#assert X.size == y.size
#plt.plot(y_train, model_1.predict(X_train), color = 'blue', label='Model Plot')
for col in X_test.columns:
   plt.scatter(X_test[col], y_pred, s=10)
plt.show()
# plt.scatter(X_test, y_test, color="black")
# plt.plot(X_test, y_pred, color="blue", linewidth=3)

# plt.xticks(())
# plt.yticks(())

# plt.show()

print('\n')



print('Task 1 Random Forest')
# # # create random forest regression
random_forest_1 = RandomForestRegressor(n_estimators=100,
                                  random_state=0)
 
# fit the regressor with x and y data
random_forest_1.fit(X_train, y_train.ravel())

# predicting labels (species) on test set
y_pred = random_forest_1.predict(X_test)

# RMSE (Root Mean Square Error) on test set
print("Root mean squared error: %.2f" % float(format(np.sqrt(mean_squared_error(y_test, y_pred)), '.3f')))
# R2 on test set
print("Coefficient of determination: %.2f" % r2_score(y_test, y_pred))

for col in X_test.columns:
   plt.scatter(X_test[col], y_pred, s=10)
plt.show()
# print(X_train.shape)
# print(X_test.shape)
# print(y_test.shape)
# print(y_train.shape)
# print(y_pred.shape)




print('\n')
# TASK 2
print('######################################################################')
print('                             TASK 2                                \n    ')
# we need 70% of each fish in training and 30% in test
# split 70/30 for each species
x_train, x_test, y_train, y_test = train_test_split(X, y,  train_size=0.7, stratify=X['categorical_species'])
# x_train = x_train.values#.reshape(-1, 6)#.reshape(-1, 1)
# x_test = x_test.values#.reshape(-1, 6)#.reshape(-1, 1)
# y_train = y_train.values
# y_test = y_test.values
""" print(x_train)
print(x_test)
print(y_train)
print(y_test) """

print('Task 2 Linear Regression')
## Linear regression
model_2 = LinearRegression()
model_2.fit(x_train, y_train)

# predicting labels (species) on test set
y_pred = model_2.predict(x_test)

# The mean squared error on test set
print("Root mean squared error: %.2f" % float(format(np.sqrt(mean_squared_error(y_test, y_pred)), '.3f')))
# R2 on test set
print("Coefficient of determination: %.2f" % r2_score(y_test, y_pred))
for col in x_test.columns:
   plt.scatter(x_test[col], y_pred, s=10)
plt.show()

print('\n')

print('Task 2 Random Forest')
## Random forest 
random_forest_2 = RandomForestRegressor(n_estimators=100,
                                   random_state=0)
 
# fit the regressor with x and y data
random_forest_2.fit(x_train, y_train.ravel())

# predicting labels (species) on test set
y_pred = random_forest_2.predict(x_test)

# RMSE (Root Mean Square Error) on test set
print("Root mean squared error: %.2f" % float(format(np.sqrt(mean_squared_error(y_test, y_pred)), '.3f')))
# R2 on test set
print("Coefficient of determination: %.2f" % r2_score(y_test, y_pred))
for col in x_test.columns:
   plt.scatter(x_test[col], y_pred, s=10)
plt.show()

print('\n')



#### Compare results
# The models applying Random Forest Regression perform better in both task 1 and task , with either one of the train-test split options
# The Random Forest Models have the smaller RMSE values, meaning the models fit the dataset better 
# Additionally, they yield the higher R2 values.
