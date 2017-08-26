# -*- coding: utf-8 -*-
"""
Created on Thu Aug 24 21:36:43 2017

@author: Daniel

Part 14 - Adding other economic indicators - p.14 Data Analysis with Python and Pandas Tutorial
https://www.youtube.com/watch?v=pxZy5jHID_A
"""

import datetime
import quandl
import pandas as pd
import pandas_datareader.data as web
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

def mortgage_30y():
    df = quandl.get("FMAC/MORTG", trim_start="1975-01-01", authtoken=api_key)
    df["Value"] = ((df["Value"] - df["Value"][0]) / df["Value"][0]) * 100.0
    df = df.resample("D").mean()
    df = df.resample("M").mean()    
    df.columns = ["M30"]
    return df

def sp500_data():
    #S&P 500 data is no longer hosted on Quandl. Changed function to pull data from Yahoo.
    start = datetime.datetime(1975, 1, 1)
    end = datetime.datetime(2017, 8 , 24)
    df = web.DataReader("^GSPC", "yahoo", start, end)
    df["Adj Close"] = ((df["Adj Close"] - df["Adj Close"][0]) / df["Adj Close"][0]) * 100.0
    df = df.resample("M").mean()
    df.rename(columns={"Adj Close": "sp500"}, inplace=True)
    df = df["sp500"]
    return df
#    df = quandl.get("YAHOO/INDEX_GSPC", trim_start="1975-01-01", authtoken=api_key)
#    df["Adjusted Close"] = ((df["Adjusted Close"] - df["Adjustd Close"][0]) / df["Adjusted Close"][0]) * 100.0
#    df = df.resample("M")
#    df.rename(columns={"Adjusted Close": "sp500"}, inplace=True)
#    df = df["sp500"]
#    return df

def gdp_data():
    #This GDP data set is for Brazil, not the US. Not sure why his tutorial used this.
    df = quandl.get("BCB/4385", trim_start="1975-01-01", authtoken=api_key)
    df["Value"] = ((df["Value"] - df["Value"][0]) / df["Value"][0]) * 100.0
    df = df.resample("M").mean()
    df.rename(columns={"Value": "GDP"}, inplace=True)
    df = df["GDP"]
    return df

def us_unemployment():
    #The original data set referenced (ECPI/JOB_G) is no longer hosted on Quandl. I think this is the closest substitute.
    df = quandl.get("BLSE/CEU9000000001", trim_start="1975-01-01", authtoken=api_key)
    df["Value"] = ((df["Value"] - df["Value"][0]) / df["Value"][0]) * 100.0
    df = df.resample("D").mean()
    df = df.resample("M").mean()
    df.rename(columns={"Value": "Unemployment Rate"}, inplace=True)
    return df

#grab_initial_state_data()

sp500 = sp500_data()
US_GDP = gdp_data()
US_unemployment = us_unemployment()
m30 = mortgage_30y()
HPI_data = pd.read_pickle("fiddy_states.pickle")
HPI_bench = HPI_Benchmark()

HPI = HPI_data.join([HPI_bench, m30, US_unemployment, US_GDP, sp500])
HPI.dropna(inplace=True)
print(HPI)

#The correlaction with the additional economic indicators seem off since they're all positively correlated with each other.
#I would expect the unemployment rate to be negatively correlated with the GDP and S&P500.
#Pretty sure this is a result of pulling incorrect/replacement data sets.
print(HPI.corr())

HPI.to_pickle("HPI.pickle")