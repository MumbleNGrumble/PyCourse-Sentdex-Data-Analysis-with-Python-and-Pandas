# -*- coding: utf-8 -*-
"""
Created on Fri Aug 25 19:15:22 2017

@author: Daniel

Part 15 - Rolling Apply and Mapping Functions - p.15 Data Analysis with Python and Pandas Tutorial
https://www.youtube.com/watch?v=uLqmM6ExPvo
"""

import quandl
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import style
import numpy as np
from statistics import mean

style.use('fivethirtyeight')

api_key = open("QuandlAPIKey.txt", "r").read()

def create_labels(cur_hpi, fut_hpi):
    if fut_hpi > cur_hpi:
        return 1
    else:
        return 0

def moving_average(values):
#Using this to show the rolling apply example. There are more efficient ways to approach the moving average.
    return mean(values)

housing_data = pd.read_pickle("HPI.pickle")

#Identifying percent change from period to period rather form the initial value.
housing_data = housing_data.pct_change()
housing_data.replace([np.inf, -np.inf], np.nan, inplace=True)

#Shifting the HPI backwards one index allows us to see the "future" value at the present time.
housing_data["US_HPI_future"] = housing_data["United States"].shift(-1)
housing_data.dropna(inplace=True)

#Using mapping function to add a column of values that are returned from a function.
housing_data["label"] = list(map(create_labels, housing_data["United States"], housing_data["US_HPI_future"]))

print(housing_data.head())

#Using Panda's rolling apply on a custom function.
housing_data["ma_apply_example"] = housing_data["M30"].rolling(window=10).apply(moving_average)

print(housing_data.tail())