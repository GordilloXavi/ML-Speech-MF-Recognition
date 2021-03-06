import pickle
import time
import numpy as np
import pandas as pd
from sklearn.model_selection import cross_val_score
import os
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier

df = pd.read_csv('dataSet.csv')
df.replace('male', 0, inplace = True)
df.replace('female', 1, inplace = True)
X = df.drop(['label', 'Q75', 'skew', 'kurt', 'modindx'], axis = 1)
y = df['label']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=42) #Play with hyperparameters

est = int(input("Choose number of estimators (100 recommended): "))

rfc = RandomForestClassifier(n_estimators = est) #Modify hyperparameters to increase accuracy
print("Training model...")
start = time.time() # Start calculating training time
rfc.fit(X_train, y_train)

#Saves the trained model to a binary file
f = open("trained_classifier.bin", 'wb')
serial_rfc = pickle.dump(rfc, f)

scores = cross_val_score(rfc, X, y, cv = 50)
print("Done", end='\n\n')
#Calculates the accuracy score

#Calculates the training time
end = time.time()
print("Training time: ", round(end-start,2), "s")
print('Acuracy: ', round(scores.mean()*100,4), '%')
print("Model saved as trained_classifier.bin")
