# -*- coding: utf-8 -*-
"""Project 8 - Breast Cancer Classification.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1lo-EUmUqIKH1ppSMirzHNcm86j6nweOX

1.  To classify the breast cancer either the cancer is benign tumor or malignant tumor - Binary Classification Problem
2.  ML Model - Logistic Regression Model (Supervised ML)
3.  Work Flow

    *   Collect Fine Needle Aspiration Data (A Type of Biopsy Procedure) - Kaggle Dataset
    *   Data Pre-Processing
    *   Train-Test Split
    *   Machine Learning Training - Logistic Regression Model (Supervised ML)
    *   Develop Prediction System - Feed new data to trained model to predict the breast cancer condition
    *   Saving the Trained Model in .sav File

Import the Dependencies
"""

import numpy as np
import pandas as pd
import sklearn.datasets
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

"""Data Collection & Pre-Processing"""

cancer_data = sklearn.datasets.load_breast_cancer()

print(cancer_data)

data_frame = pd.DataFrame(cancer_data.data, columns = cancer_data.feature_names)

data_frame.head()

data_frame['label'] = cancer_data.target

data_frame.tail()

data_frame.shape

data_frame.info()

data_frame.isnull().sum()

data_frame.describe()

data_frame['label'].value_counts()

"""1 --> Benign

0 --> Malignant
"""

data_frame.groupby('label').mean()

X = data_frame.drop(columns = 'label', axis = 1)
Y = data_frame['label']

print(X)

print(Y)

"""Train-Test Split"""

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size = 0.2, random_state = 2)

print(X.shape, X_train.shape, X_test.shape)

"""Machine Learning Training - Logistic Regression Model"""

model = LogisticRegression()

model.fit(X_train, Y_train)

"""Model Evaluation"""

#accuracy for training data

X_train_prediction = model.predict(X_train)
Train_data_accuracy = accuracy_score(Y_train, X_train_prediction)
print(Train_data_accuracy)

#accuracy for test data

X_test_prediction = model.predict(X_test)
Test_data_accuracy = accuracy_score(Y_test, X_test_prediction)
print(Test_data_accuracy)

"""Making A Predictive System"""

input_data = (12.45,15.7,82.57,477.1,0.1278,0.17,0.1578,0.08089,0.2087,0.07613,0.3345,0.8902,2.217,27.19,0.00751,0.03345,0.03672,0.01137,0.02165,0.005082,15.47,23.75,103.4,741.6,0.1791,0.5249,0.5355,0.1741,0.3985,0.1244)

np_array = np.asarray(input_data)

data_reshaped = np_array.reshape(1,-1)

prediction = model.predict(data_reshaped)
print(prediction)

if (prediction[0] == 0):
  print('The Breast Cancer is Malignant')

else:
  print('The Breast Cancer is Benign')

"""Saving the Trained Model"""

import pickle

filename = 'breast_model.sav'

pickle.dump(model, open(filename, 'wb'))

loaded_model = pickle.load(open('breast_model.sav', 'rb'))

input_data = (13.54,14.36,87.46,566.3,0.09779,0.08129,0.06664,0.04781,0.1885,0.05766,0.2699,0.7886,2.058,23.56,0.008462,0.0146,0.02387,0.01315,0.0198,0.0023,15.11,19.26,99.7,711.2,0.144,0.1773,0.239,0.1288,0.2977,0.07259)

np_array = np.asarray(input_data)

data_reshaped = np_array.reshape(1,-1)

prediction = model.predict(data_reshaped)
print(prediction)

if (prediction[0] == 0):
  print('The Breast Cancer is Malignant')

else:
  print('The Breast Cancer is Benign')