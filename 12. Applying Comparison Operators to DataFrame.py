# -*- coding: utf-8 -*-
"""
Created on Tue Aug 22 20:10:23 2017

@author: Daniel

Part 12 - Applying Comparison Operators to DataFrame - p.12 Data Analysis with Python and Pandas Tutorial
https://www.youtube.com/watch?v=8mnLZGNrAzM
"""

import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import style

style.use('fivethirtyeight')

#6212.42 is a piece of bad data that needs to be removed.
bridge_height = {'meters':[10.26, 10.31, 10.27, 10.22, 10.23, 6212.42, 10.28, 10.25, 10.31]}

df = pd.DataFrame(bridge_height)

#Calculating the rolling standard deviation shows there is a clear jump at the bad data point.
df["STD"] = pd.rolling_std(df["meters"], 2)
print(df)

#We can grab the standard deviation for the data set from the descriptive statistics.
df_std = df.describe()["meters"]["std"]
print(df_std)

#This creates a new dataframe with only data points that are less than the standard deviation.
#In less obvious cases, we would use a multiplier to filter out bad data that doesn't meet a specific threshold.
df = df[(df["STD"] < df_std)]
print(df)

df["meters"].plot()
plt.show()