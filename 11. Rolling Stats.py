# -*- coding: utf-8 -*-
"""
Created on Tue Aug 22 19:33:28 2017

@author: Daniel

Part 11 - Rolling statistics - p.11 Data Analysis with Python and Pandas Tutorial
https://www.youtube.com/watch?v=FRzfD1FtrsQ
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

##Set the moving average for 12 periods (a year in this case).
#HPI_data["TX12MA"] = pd.rolling_mean(HPI_data["TX"], 12)
#
##Calculate the standard deviation for 12 periods (a year in this case).
#HPI_data["TX12STD"] = pd.rolling_std(HPI_data["TX"], 12)
#
###Use this to drop the first few records before the moving average is calculated.
##HPI_data.dropna(inplace=True)
#
#print(HPI_data[["TX", "TX12MA", "TX12STD"]].head())

#Calculate the rolling correlation between Texas and Alaska for 12 periods (a year on this case).
TX_AK_12corr = pd.rolling_corr(HPI_data["TX"], HPI_data["AK"], 12)

fig = plt.figure()
ax1 = plt.subplot2grid((2,1), (0,0))
ax2 = plt.subplot2grid((2,1), (1,0), sharex=ax1)

##Plotting the moving average and standard deviation on two different graphs, but with the same axis.
#HPI_data[["TX", "TX12MA"]].plot(ax=ax1)
#HPI_data["TX12STD"].plot(ax=ax2)

HPI_data["TX"].plot(ax=ax1, label="TX HPI")
HPI_data["AK"].plot(ax=ax1, label="AK HPI")
TX_AK_12corr.plot(ax=ax2, label="TX_AK_12corr")

plt.legend(loc=4)
plt.show()
