# -*- coding: utf-8 -*-
"""
Created on Sun Aug  6 14:32:16 2017

@author: Rush
"""
import pandas as pd
url_template = "http://climate.weather.gc.ca/climateData/bulkdata_e.html?format=csv&stationID=5415&Year={year}&Month={month}&timeframe=1&submit=Download+Data"
url = url_template.format(month=3, year=2012)

weather_mar2012 = pd.read_csv(url, skiprows=16, index_col='Date/Time', parse_dates=True, encoding='latin1')
weather_mar2012