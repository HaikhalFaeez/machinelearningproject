# -*- coding: utf-8 -*-
"""Project 19 - Titanic Survival Prediction.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/138TYgMXXcd7MzAYQa8ROiAhzHr7t2W0J

1.  To predict the survival rate on a titanic (survived or not survived) - Binary Classification Problem
2.  ML Model - Logistic Regression Model (Supervised ML)
2.  Work Flow

    *   Collect Titanic Survival Data - Kaggle Dataset
    *   Data Pre-Processing
    *   Data Analysis
    *   Train-Test Split
    *   Machine Learning Models - Logistic Regression Model (Supervised ML)
    *   Develop Prediction System - Feed new data to the trained model to predict the survival rate of the passenger on the titanic

Import the Dependencies
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

"""Data Collection & Pre-Processing"""

titanic_data = pd.read_csv('/content/titanic.csv')

titanic_data.head()

titanic_data.shape

titanic_data.info()

titanic_data.isnull().sum()

"""Handling the missing values"""

# drop cabin columns from the dataframe since the missing value is too much

titanic_data = titanic_data.drop(columns='Cabin', axis=1)

# replace missing values in Age column with mean value

titanic_data['Age'].fillna(titanic_data['Age'].mean(), inplace=True)

# replace missing values in Embarked column with mode value

print(titanic_data['Embarked'].mode())
titanic_data['Embarked'].fillna(titanic_data['Embarked'].mode()[0], inplace=True)

titanic_data.isnull().sum()

"""Data Analysis"""

titanic_data.describe()

titanic_data['Survived'].value_counts()

"""0 --> Not Survived

1 --> Survived

Data Visualization
"""

sns.set()

# making a count plot for 'Survived' column

sns.countplot(x='Survived', data=titanic_data)

titanic_data['Sex'].value_counts()

# making a count plot for 'Sex' column

sns.countplot(x='Sex', data=titanic_data)

# number of survivors based on their gender

sns.countplot(x='Sex', hue='Survived', data=titanic_data)

# making a count plot for 'Pclass' column

sns.countplot(x='Pclass', data=titanic_data)

# number of survivors based on their Pclass

sns.countplot(x='Pclass', hue='Survived', data=titanic_data)

"""Label Encoding"""

titanic_data['Sex'].value_counts()

titanic_data['Embarked'].value_counts()

titanic_data.replace({'Sex':{'male':0, 'female':1}, 'Embarked':{'S':0, 'C':1, 'Q':2}}, inplace=True)

titanic_data.head()

X = titanic_data.drop(columns=['PassengerId', 'Survived', 'Name', 'Ticket'], axis=1)
Y = titanic_data['Survived']

print(X)

print(Y)

"""Train-Test Split"""

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=2)

print(X.shape, X_train.shape, X_test.shape)

"""Machine Learning Training - Logistic Regression Model"""

model = LogisticRegression()

model.fit(X_train, Y_train)

"""Model Evaluation"""

# accuracy on training data

train_data_prediction = model.predict(X_train)
train_data_accuracy = accuracy_score(Y_train, train_data_prediction)
print('Training data accuracy = ', train_data_accuracy)

# accuracy on test data

test_data_prediction = model.predict(X_test)
test_data_accuracy = accuracy_score(Y_test, test_data_prediction)
print('Test data accuracy = ', test_data_accuracy)

"""Predictive System"""

input_data = ()

input_data_as_numpy_array = np.asarray(input_data)

input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)

prediction = model.predict(input_data_reshaped)
print(prediction)

if (prediction[0] == 0):
  print('The person did not survived')

else:
  print('The person survived')