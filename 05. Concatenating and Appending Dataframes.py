# -*- coding: utf-8 -*-
"""
Created on Fri Aug  4 19:33:07 2017

@author: Daniel

Part 5 - Concatenating and Appending dataframes - p.5 Data Analysis with Python and Pandas Tutorial
https://www.youtube.com/watch?v=ylIRlTFt_Fk
"""

import pandas as pd

df1 = pd.DataFrame({"HPI": [80, 85, 88, 85],
                    "Int_rate": [2, 3 ,2, 2],
                    "US_GDP_Thousands": [50, 55, 65, 55]},
                    index = [2001, 2002, 2003, 2004])

df2 = pd.DataFrame({"HPI": [80, 85, 88, 85],
                    "Int_rate": [2, 3, 2, 2],
                    "US_GDP_Thousands": [50, 55, 65, 55]},
                    index = [2005, 2006, 2007, 2008])

df3 = pd.DataFrame({"HPI": [80, 85, 88, 85],
                    "Int_rate": [2, 3, 2, 2],
                    "Low_tier_HPI": [50, 52, 50, 53]},
                    index = [2001, 2002, 2003, 2004])

##Simple concatenate.
##This works because df1 and df2 have the same columns and the indcies are a continuation of each other.
#concat = pd.concat([df1, df2])
#print(concat)

##This shows how the simple concatenation fails.
#concat = pd.concat([df1, df2, df3])
#print(concat)

##Appending just adds to the end.
#df4 = df1.append(df2)
#print(df4)

##We run into similar problems like we did with concatenate.
#df4 = df1.append(df3)
#print(df4)

#You can append a series to get things to line up correctly. It's not super efficient.
s = pd.Series([80, 2, 50], index = ["HPI", "Int_rate", "US_GDP_Thousands"])
df4 = df1.append(s, ignore_index=True)
print(df4)