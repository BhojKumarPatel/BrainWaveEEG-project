#!/usr/bin/python3
# tain.py
# Xavier Vasques 13/04/2021

import platform; print(platform.platform())
import sys; print("Python", sys.version)
import numpy; print("NumPy", numpy.__version__)
import scipy; print("SciPy", scipy.__version__)

import os
import numpy as np
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.neural_network import MLPClassifier
import pandas as pd
from joblib import dump
from sklearn import preprocessing
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier

def train():

    # Load directory paths for persisting model

    MODEL_DIR = './'
    MODEL_PATH_LDA = 'lda.joblib'
    MODEL_PATH_NN = 'nn.joblib'
    MODEL_PATH_RF = 'rf.joblib'
      
    # Load, read and normalize training data
    training = "./train.csv"
    data_train = pd.read_csv(training)
        
    y_train = data_train['# Letter'].values
    X_train = data_train.drop(data_train.loc[:, 'Line':'# Letter'].columns, axis = 1)

    print("Shape of the training data")
    print(X_train.shape)
    print(y_train.shape)
        
    # Data normalization (0,1)
    X_train = preprocessing.normalize(X_train, norm='l2')
    
    # Models training
    
    # Linear Discrimant Analysis (Default parameters)
    clf_lda = LinearDiscriminantAnalysis()
    clf_lda.fit(X_train, y_train)
    
    # Save model
    from joblib import dump
    dump(clf_lda, MODEL_PATH_LDA)
        
    # Neural Networks multi-layer perceptron (MLP) algorithm
    clf_NN = MLPClassifier(solver='adam', activation='relu', alpha=0.0001, hidden_layer_sizes=(500,), random_state=0, max_iter=1000)
    clf_NN.fit(X_train, y_train)
       
    # Save model
    from joblib import dump, load
    dump(clf_NN, MODEL_PATH_NN)

    # Random Forest Classifier -- Another model to try
    clf_rf = RandomForestClassifier(n_estimators=100, random_state=42)
    clf_rf.fit(X_train, y_train)
       
    # Save model 
    from joblib import dump, load
    dump(clf_rf, MODEL_PATH_RF)
        
if __name__ == '__main__':
    train()
