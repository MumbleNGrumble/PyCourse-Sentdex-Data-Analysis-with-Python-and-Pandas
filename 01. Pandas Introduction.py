# -*- coding: utf-8 -*-
"""
Created on Tue Aug  1 19:49:05 2017

@author: Daniel

Part 1 - Data Analysis with Python and Pandas Tutorial Introduction
https://www.youtube.com/watch?v=Iqjy9UqKKuo
"""

import pandas as pd
import datetime
import pandas_datareader.data as web
import matplotlib.pyplot as plt
from matplotlib import style

style.use('ggplot')

start = datetime.datetime(2010, 1, 1)
end = datetime.datetime(2015, 1, 1)

df = web.DataReader("XOM", "yahoo", start, end)

print(df.head())

df['Adj Close'].plot()

plt.show