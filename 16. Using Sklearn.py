# -*- coding: utf-8 -*-
"""
Created on Fri Aug 25 19:52:38 2017

@author: Daniel

Part 16 - Scikit Learn Incorporation - p.16 Data Analysis with Python and Pandas Tutorial
https://www.youtube.com/watch?v=t4319ffzRg0
"""

import pandas as pd
import numpy as np
from sklearn import svm, preprocessing, cross_validation

def create_labels(cur_hpi, fut_hpi):
    if fut_hpi > cur_hpi:
        return 1
    else:
        return 0

housing_data = pd.read_pickle("HPI.pickle")

housing_data = housing_data.pct_change()
housing_data.replace([np.inf, -np.inf], np.nan, inplace=True)
housing_data["US_HPI_future"] = housing_data["United States"].shift(-1)
housing_data.dropna(inplace=True)
housing_data["label"] = list(map(create_labels, housing_data["United States"], housing_data["US_HPI_future"]))

print(housing_data.head())

#Features, usually represented by a capital X.
#Need to drop label and US_HPI_future because they're 100% correlated and would throw off the ML model.
X = np.array(housing_data.drop(["label", "US_HPI_future"], 1))
X = preprocessing.scale(X)

y = np.array(housing_data["label"])

X_train, X_test, y_train, y_test = cross_validation.train_test_split(X, y, test_size=0.2)

clf = svm.SVC(kernel="linear")
clf.fit(X_train, y_train)

print(clf.score(X_test, y_test))