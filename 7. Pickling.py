# -*- coding: utf-8 -*-
"""
Created on Thu Aug 17 23:29:36 2017

@author: Daniel
"""

import quandl
import pandas as pd
import pickle

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
        
        if main_df.empty:
            main_df = df
        else:
            main_df = main_df.join(df)
            
    print(main_df.head())
    
    #Pickling out using Python's pickle library. Can be done in two lines using with statement.
    pickle_out = open("fiddy_states.pickle", "wb")
    pickle.dump(main_df, pickle_out)
    pickle_out.close
    
#grab_initial_state_data()

#Pickling in using Python's pickle library. Can be done in two lines using with statement.
pickle_in = open("fiddy_states.pickle", "rb")
HPI_data = pickle.load(pickle_in)
print(HPI_data)

#Pickling out using pandas' built in pickle function.
HPI_data.to_pickle("pickle.pickle")

#Pickling in using pandas' built in pickle function.
HPI_data2 = pd.read_pickle("pickle.pickle")

print(HPI_data2)