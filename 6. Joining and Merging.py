# -*- coding: utf-8 -*-
"""
Created on Tue Aug 15 19:50:57 2017

@author: Daniel

Part 6 - Joining and Merging Dataframes - p.6 Data Analysis with Python and Pandas Tutorial
https://www.youtube.com/watch?v=XMjSGGej9y8
"""

import pandas as pd

df1 = pd.DataFrame({"HPI": [80, 85, 88, 85],
                    "Int_rate": [2, 3, 2, 2],
                    "US_GDP_Thousands": [50, 55, 65, 55]},
                    index = [2001, 2002, 2003, 2004])

df2 = pd.DataFrame({"HPI": [80, 85, 88, 85],
                    "Int_rate": [2, 3, 2, 2],
                    "US_GDP_Thousands": [50, 55, 65, 55]},
                    index = [2005, 2006, 2007, 2008])

df3 = pd.DataFrame({"HPI": [80, 85, 88, 85],
                    "Unemployment": [7, 8, 9, 6],
                    "Low_tier_HPI": [50, 52, 50, 53]},
                    index = [2001, 2002, 2003, 2004])

df1x = pd.DataFrame({"Year": [2001, 2002, 2003, 2004],
                    "Int_rate": [2, 3, 2, 2],
                    "US_GDP_Thousands": [50, 55, 65, 55]})

df3x = pd.DataFrame({"Year": [2001, 2003, 2004, 2005],
                    "Unemployment": [7, 8, 9, 6],
                    "Low_tier_HPI": [50, 52, 50, 53]})

##Merging ignores indcies. You declare which column you want to merge on.
##The situation below creates duplicated data amongst the rows and columns.
#print(pd.merge(df1, df2, on="HPI"))

##You can merge on multiple columns by merging a list of column headers.
##You lose the index though.
#print(pd.merge(df1, df2, on=["HPI", "Int_rate"]))

##Can declare how = left, right, inner, or outer on merge. Works the same way as a SQL join.
##By default, merge does an inner join.
#merged = pd.merge(df1x, df3x, on="Year", how="outer")
#merged.set_index("Year", inplace=True)
#print(merged)

#Joining dataframes.
#Prepping dataframes for a join. The dataframes can't share a column so the index is set to the common column.
df1.set_index("HPI", inplace=True)
df3.set_index("HPI", inplace=True)

#This causes data duplication still, but indicies are honored.
joined = df1.join(df3)
print(joined)

#Each has their own reason why you might use it.
#If you have dataframes that have similar data between them, you would use a merge or join.
#Use a merge when the index doesn't matter to you. Use a join when the index does matter to you.
#Use concatenation or append to elongate data. Concatenate can also be used to add columns.