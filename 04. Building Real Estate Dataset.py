# -*- coding: utf-8 -*-
"""
Created on Thu Aug  3 18:45:26 2017

@author: Daniel

Part 4 - Building dataset - p.4 Data Analysis with Python and Pandas Tutorial
https://www.youtube.com/watch?v=3GpvWlVinf0
"""

import quandl
import pandas as pd

api_key = open("QuandlAPIKey.txt", "r").read()
#df = quandl.get("FMAC/HPI_AK", authtoken=api_key)
#print(df.head())

fiddy_states = pd.read_html("https://simple.wikipedia.org/wiki/List_of_U.S._states")

##This is a list:
#print(fiddy_states)
#
##This is a data frame:
#print(fiddy_states[0])

#This is a column:
print(fiddy_states[0][0])

for abbv in fiddy_states[0][0][1:]:
    print("FMAC/HPI_" + str(abbv))