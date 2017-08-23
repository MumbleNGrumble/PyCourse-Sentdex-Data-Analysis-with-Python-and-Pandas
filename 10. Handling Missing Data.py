# -*- coding: utf-8 -*-
"""
Created on Tue Aug 22 19:11:53 2017

@author: Daniel

Part 10 - Handling Missing Data - p.10 Data Analysis with Python and Pandas Tutorial
https://www.youtube.com/watch?v=O5v4NrSCw_A
"""

import quandl
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import style

style.use('fivethirtyeight')

api_key = open("QuandlAPIKey.txt", "r").read()

def state_list():
    fiddy_states = pd.read_html("https://simple.wikipedia.org/wiki/List_of_U.S._states")
    return fiddy_states[0][0][1:]

def grab_initial_state_data():
    states = state_list()
    main_df = pd.DataFrame()
    
    for abbv in states:
        query = "FMAC/HPI_" + str(abbv)
        print(query)
        
        df = quandl.get(query, authtoken=api_key)
        df.columns = [str(abbv)]
#        This shows the precentage change all relative to the starting point.
        df[abbv] = ((df[abbv] - df[abbv][0]) / df[abbv][0]) * 100.0
        
        if main_df.empty:
            main_df = df
        else:
            main_df = main_df.join(df)
            
    print(main_df.head())
    
    main_df.to_pickle("fiddy_states.pickle")
    
def HPI_Benchmark():
    df = quandl.get("FMAC/HPI_USA", authtoken=api_key)
    df.rename(columns={"Value": "United States"}, inplace=True)
    df["United States"] = ((df["United States"] - df["United States"][0]) / df["United States"][0]) * 100.0
    return df

#grab_initial_state_data()

HPI_data = pd.read_pickle("fiddy_states.pickle")

#Different methods for handling missing data.
HPI_data["TX1yr"] = HPI_data["TX"].resample("A", how="mean")
print(HPI_data[["TX", "TX1yr"]].head())

##Option 1 - Drop all NaNs. Any row that contains NaN will be removed.
#HPI_data.dropna(inplace=True)

##Option 2 - Drop rows that only contain NaNs. Leave everything else.
##Option 2a - Specify a thresh parameter to apply a threshold for what should be dropped. Set a limit for the number of NaNs that can appear before being dropped.
#HPI_data.dropna(how="all", inplace=True)

##Option 3 - Fill in missing data from other time periods. Can be forward filled (ffill) or backward filled (bfilled).
#HPI_data.fillna(method="bfill", inplace=True)

#Option 3a - Can fill in with a specific value. What value gets used depends on the situation. Can specify a limit for fills.
HPI_data.fillna(value=-99999, limit=10, inplace=True)
print(HPI_data.isnull().values.sum())   #How to tell how many remaining NaNs are in the data set.

print(HPI_data[["TX", "TX1yr"]].head())

fig = plt.figure()
ax1 = plt.subplot2grid((1,1), (0,0))

HPI_data[["TX", "TX1yr"]].plot(ax=ax1)

plt.legend(loc=4)
plt.show()
