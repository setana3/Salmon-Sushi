#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pandas as pd


tal = pd.read_csv('/Users/setana/code/Python/Advanced-Python/Homework3/CSV/Tallinn.csv',
                         sep=';')

wlf = pd.read_csv('/Users/setana/code/Python/Advanced-Python/Homework3/CSV/geographical_coordinates.csv',
                         sep=',')



### Compare IATA and show the whole row with iloc[num]
for item1, frame1 in tal['IATA'].iteritems():
    # print(tal.iloc[item1])
    for item2, frame2 in wlf['IATA'].iteritems():
        if frame1 == frame2:
            print(wlf.iloc[item2]['Country'] + " has longitude of " + str(wlf.iloc[item2]["Longitude"]) +
                  " and latitude of " + str(wlf.iloc[item2]["Latitude"]))
        
        
        