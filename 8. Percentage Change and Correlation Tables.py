# -*- coding: utf-8 -*-
"""
Created on Mon Aug 21 19:40:50 2017

@author: Daniel

Part 8 - Percent Change and Correlation Tables - p.8 Data Analysis with Python and Pandas Tutorial
https://www.youtube.com/watch?v=P90mCSsGE1c
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
##        This shows the percentage change relative from period to period
#        df = df.pct_change()
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
#benchmark = HPI_Benchmark()

##How to add/modify columns.
#HPI_data["TX2"] = HPI_data["TX"] * 2
#print(HPI_data[["TX", "TX2"]])

##Plotting data. Everything converges at the base year.
#fig = plt.figure()
#ax1 = plt.subplot2grid((1,1), (0,0))
#HPI_data.plot(ax=ax1)
#benchmark.plot(ax=ax1, color="k", linewidth=10)
#plt.legend().remove()
#plt.show()

#Correlation table.
HPI_State_Correlation = HPI_data.corr()
print(HPI_State_Correlation)
print(HPI_State_Correlation.describe())