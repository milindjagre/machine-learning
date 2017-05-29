# -*- coding: utf-8 -*-
"""
This python file demonstrates the concepts
we are going to cover in Data Preprocessing

"""

# IMPORTING THE LIBRARIES
# numpy contains mathematical operations
import numpy as np
# matplotlib.pyplot helps to plot charts and graphs
import matplotlib.pyplot as plt
# pandas is used to import and manage datasets
import pandas as pd

# pandas library is used for reading Data.csv file
datasets = pd.read_csv('Data.csv')
# creating metrics of independent variables/predictors
X = datasets.iloc[:, :-1].values
# creating metric of dependent/response variable
y = datasets.iloc[:, 3].values

# MISSING DATA IMPUTATION
# lets see the missing data before imputation
X[:, 2:3]
# importing Imputer class from sklearn.preprocessing library
from sklearn.preprocessing import Imputer
# creating an Imputer object, with necessary parameters
imputer = Imputer(missing_values = 'NaN', strategy = 'mean', axis=0)
# fitting imputer object for independent variables X
imputer = imputer.fit(X[:, 1:3])
# transforming these independent variables to replace 
# missing values with the mean of corresponding column
X[:, 1:3] = imputer.transform(X[:, 1:3])
# printing the contents for the confirmation
X[:, 2:3]

# CATEGORICAL VARIABLES CONVERSION
# importing LabelEncoder class from sklearn.preprocessing library
from sklearn.preprocessing import LabelEncoder
# create an object for LabelEncoder class
labelencoder_X = LabelEncoder()
# doing fit and transform for independent variable Country
X[:, 0] = labelencoder_X.fit_transform(X[:, 0])
# above approach is not suitable for this dataset, therefore
# we will create the DUMMY VARIABLES for Country variable
# for doing this, we will use OneHotEncoder class from same library
from sklearn.preprocessing import OneHotEncoder
# creating an object for OneHotEncoder class with variable=Country
onehotencoder = OneHotEncoder(categorical_features = [0])
# doing fit and transform for the Country categorical variable
X = onehotencoder.fit_transform(X).toarray()
# dependent variable Purchased can be converted using LabelEncoder()
# as it does not require creation of DUMMY VARIABLE
# creating dependent variable object for LabelEncoder() class
labelencoder_y = LabelEncoder()
# doing the fit and transform for dependent variable Purchased
y = labelencoder_y.fit_transform(y)

# SPLITTING THE DATASET INTO TRAINING AND TEST SET
# importing the library for doing this operation
from sklearn.cross_validation import train_test_split
# performing the SPLIT operation on the input dataset
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2)

# FEATURE SCALING
# importing StandardScaler class from sklearn.preprocessing library
from sklearn.preprocessing import StandardScaler
# creating StandardScaler object
sc_X = StandardScaler()
# doing feature scaling for independent variables
# doing both FIT and TRANSFORM for sc_X object
X_train = sc_X.fit_transform(X_train)
# since sc_X is already fitted for X_train,
# only transformation is needed for X_test
X_test = sc_X.transform(X_test)
