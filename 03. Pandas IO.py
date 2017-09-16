# -*- coding: utf-8 -*-
"""
Created on Thu Aug  3 18:13:46 2017

@author: Daniel

Part 3 - IO Basics - p.3 Data Analysis with Python and Pandas Tutorial
https://www.youtube.com/watch?v=9Z7wvippeko
"""

import pandas as pd

#How to read in a file.
df = pd.read_csv("ZILL-Z77006_MLP.csv")
print(df.head())

##How to output a file.
#df.set_index("Date", inplace=True)
#df.to_csv("newcsv2.csv")
#
##How to read in a file and set an index at the same time.
#df = pd.read_csv("newcsv2.csv", index_col=0)
#print(df.head())
#
##How to rename a column.
##Remember that the first column has been set to an index so it's no longer considered a column.
#df.columns = ["Austin_HPI"]
#print(df.head())
#
##New CSV output will have the renamed header.
#df.to_csv("newcsv3.csv")
#
##Output a CSV with no headers (just the data only).
#df.to_csv("newcsv4.csv", header=False)
#
##Read in a file that has no headers, name the columns, and set the index.
#df = pd.read_csv("newcsv4.csv", names=["Date", "Austin_HPI"], index_col=0)
#print(df.head())
#
##Convert data frame to HTML table output.
#df.to_html("example.html")

#How to rename a column after it's loaded into a data frame.
#Date isn't being set as the index this example to show that you can rename one column at a time.
df = pd.read_csv("newcsv4.csv", names=["Date", "Austin_HPI"])
print(df.head())

df.rename(columns={"Austin_HPI":"77006_HPI"}, inplace=True)
print(df.head())