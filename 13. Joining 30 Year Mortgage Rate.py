# -*- coding: utf-8 -*-
"""
Created on Wed Aug 23 18:00:33 2017

@author: Daniel

Part 13 - Joining 30 year mortgage rate - p.13 Data Analysis with Python and Pandas Tutorial
https://www.youtube.com/watch?v=FvamL5oA_EE
"""

import quandl
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import style

style.use('fivethirtyeight')

api_key = open("QuandlAPIKey.txt", "r").read()

def mortgage_30y():
    df = quandl.get("FMAC/MORTG", trim_start="1975-01-01", authtoken=api_key)
    df["Value"] = ((df["Value"] - df["Value"][0]) / df["Value"][0]) * 100.0
    
    #The data points are at the start of the month whereas the rest of our data is at the end of the month.
    #We're resampling to get consistent indicies.
    #Can't just resample by month straight away because there aren't enough data points for resampling initially.
    df = df.resample("D").mean()
    df = df.resample("M").mean()
    
    df.columns = ["M30"]
    return df
    
    
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

m30 = mortgage_30y()
HPI_data = pd.read_pickle("fiddy_states.pickle")
HPI_bench = HPI_Benchmark()

#Joining the 30 year mortgage rate to the datat set.
state_HPI_M30 = HPI_data.join(m30)
print(state_HPI_M30.corr()["M30"].describe())