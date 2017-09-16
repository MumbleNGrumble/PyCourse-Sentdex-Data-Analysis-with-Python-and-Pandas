# -*- coding: utf-8 -*-
"""
Created on Tue Aug 22 18:48:19 2017

@author: Daniel

Part 9 - Resampling - p.9 Data Analysis with Python and Pandas Tutorial
https://www.youtube.com/watch?v=p_Fn_BksF9k
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

#Resampling Texas data by year, taking the average of the year (average is default for resampling).
TX1yr = HPI_data["TX"].resample("A", how="mean")
print(TX1yr.head())

fig = plt.figure()
ax1 = plt.subplot2grid((1,1), (0,0))

HPI_data["TX"].plot(ax=ax1, label="Monthly TX HPI")
TX1yr.plot(ax=ax1, label="Yearly TX HPI")

plt.legend(loc=4)   #Location 4 is the lower right hand corner of the graph.
plt.show()
