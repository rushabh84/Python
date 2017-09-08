# Author : Prashanth Raja
# Date of Creation : 12th December 2016
# Date of Modification : 12th December 2016
# Description : 1. Creates dataframes for sensor A and sensor B from the corresponding database tables
#               2. Creates a visualization plot that represents all data points for a specific sensor for a specific time frame


import sqlite3
import glob
import os
import sys
import re
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import style
import matplotlib.dates as mdates


# Connecting to the sensor Database connection

connection = sqlite3.connect("sensor.db")
cursor = connection.cursor()

# creating dataframes from the database tables

A_sensor = pd.read_sql_query("SELECT * FROM Sensor_A",connection,\
                  index_col=None, coerce_float=True, params=None, parse_dates=None, chunksize=None)
B_sensor = pd.read_sql_query("SELECT * FROM Sensor_B",connection,\
                  index_col=None, coerce_float=True, params=None, parse_dates=None, chunksize=None)

# converting the time column to actual datetime and creating a date column

A_sensor['Time'] = pd.to_datetime(A_sensor['Time'])
B_sensor['Time'] = pd.to_datetime(B_sensor['Time'])

A_sensor['Date'] = (A_sensor['Time']).dt.date
B_sensor['Date'] = (B_sensor['Time']).dt.date


# Getting the user input for start and end time

check = True
while check:
    try:
        Start_time = pd.to_datetime(input("""Enter the start time period for which you need the average of temperature and humidity
        The Date format should be MM-DD-YYYY HH:MM:SS AM/PM: """))
        check = False
    except ValueError:
        print('Invalid date! Please enter the date in proper format!!\n')

check = True
while check:
    try:
        End_time = pd.to_datetime(input("""\nEnter the end time period for which you need the average of temperature and humidity
        The Date format should be MM-DD-YYYY HH:MM:SS AM/PM: """))
        check = False
    except ValueError:
        print('Invalid date! Please enter the date in proper format!!\n')

if Start_time < min(A_sensor.Time):
    if End_time > max(A_sensor.Time):
        print("""The starting and ending limit exceed the start and end date of available sensor data.
        Therfore, the minimum and maximum date of the data is considered!\n""")
    else:
        print("""The start limit is less than minimum date of available data.
        Therfore, the minimum date of the data is considered!\n""")
elif End_time > max(A_sensor.Time):
    print("""The end limit is greater than maximum end date of available data.
    Therfore, the maximum date of the data is considered!\n""")

print("\nThe timeframe entered is - ",Start_time,"to",End_time,"\n")

class OutofBounds(Exception):
    """Raise for my specific kind of exception"""
    pass

# The dataset is filtered for the corresponding time range

if Start_time <= End_time:
    sensor_A_filter = A_sensor[(pd.to_datetime(A_sensor.Time) >= Start_time) & (pd.to_datetime(A_sensor.Time) <= End_time)]
    sensor_B_filter = B_sensor[(pd.to_datetime(B_sensor.Time) >= Start_time) & (pd.to_datetime(B_sensor.Time) <= End_time)]
    if sensor_A_filter.size == 0 and sensor_B_filter.size == 0:
        print("The data is not available for the specified dates! The data is available for the period:",min(A_sensor.Time),"to",max(A_sensor.Time),"\n")
    else:
        while True:
            try:
                option = int(input('''Below are three graph options:
1. Temperature and Humidity for Sensor A
2. Temperature and Humidity for Sensor B
3. Temperature and Humidity for both Sensor A and Sensor B

Enter your option: '''))

                if type(option) != int:
                    raise ValueError
                elif option < 1 or option > 3:
                    raise OutofBounds
                break

            except ValueError:
                print('Please enter options in integer values!')

            except OutofBounds:
                print('Please enter a valid option between 1 and 3')

        if option == 1:
                
            style.use('fivethirtyeight')

            # plotting the Temperature for sensor A for the specified timeframe
            ax1 = plt.subplot(211)
            ax1.plot(sensor_A_filter["Time"],sensor_A_filter["Temperature"],'b')
            ax1.set_ylabel('Temperature')
            ax1.set_title('VARIATION OF TEMPERATURE ACROSS TIME')
            ax1.set_ylim([75, 90])
            ax1.legend(['A'], loc='upper right')
            xfmt = mdates.DateFormatter('%d-%m-%y %H:%M')
            ax1.xaxis.set_major_formatter(xfmt)

            plt.subplots_adjust(hspace=.5)

            # plotting the Humidity for sensor A for the specified timeframe
            ax2 = plt.subplot(212)
            ax2.plot(sensor_A_filter["Time"],sensor_A_filter["Humidity"],'b')
            ax2.set_xlabel('Time')
            ax2.set_ylabel('Humidity')
            ax2.set_title('VARIATION OF HUMIDITY ACROSS TIME')
            ax2.set_ylim([10, 40])
            ax2.legend(['A'], loc='upper right')
            xfmt1 = mdates.DateFormatter('%d-%m-%y %H:%M')
            ax2.xaxis.set_major_formatter(xfmt1)

            plt.show()
                
        elif option == 2:
                
            style.use('fivethirtyeight')

            # plotting the Temperature for sensor B for the specified timeframe
            ax1 = plt.subplot(211)
            ax1.plot(sensor_B_filter["Time"],sensor_B_filter["Temperature"],'g')
            ax1.set_ylabel('Temperature')
            ax1.set_title('VARIATION OF TEMPERATURE ACROSS TIME')
            ax1.set_ylim([75, 90])
            ax1.legend(['B'], loc='upper right')
            xfmt = mdates.DateFormatter('%d-%m-%y %H:%M')
            ax1.xaxis.set_major_formatter(xfmt)

            plt.subplots_adjust(hspace=.5)

            # plotting the Humidity for sensor B for the specified timeframe
            ax2 = plt.subplot(212)
            ax2.plot(sensor_B_filter["Time"],sensor_B_filter["Humidity"],'g')
            ax2.set_xlabel('Time')
            ax2.set_ylabel('Humidity')
            ax2.set_title('VARIATION OF HUMIDITY ACROSS TIME')
            ax2.set_ylim([10, 40])
            ax2.legend(['B'], loc='upper right')
            xfmt1 = mdates.DateFormatter('%d-%m-%y %H:%M')
            ax2.xaxis.set_major_formatter(xfmt1)

            plt.show()
                
        elif option == 3:
                
            style.use('fivethirtyeight')
                
            # plotting the Temperature for sensor A and sensor B for the specified timeframe
            ax1 = plt.subplot(211)
            ax1.plot(sensor_A_filter["Time"],sensor_A_filter["Temperature"],'b')
            ax1.plot(sensor_B_filter["Time"],sensor_B_filter["Temperature"],'g')
            ax1.set_ylabel('Temperature')
            ax1.set_title('VARIATION OF TEMPERATURE ACROSS TIME')
            ax1.set_ylim([75, 90])
            ax1.legend(['A', 'B'], loc='upper right')
            xfmt = mdates.DateFormatter('%d-%m-%y %H:%M')
            ax1.xaxis.set_major_formatter(xfmt)

            plt.subplots_adjust(hspace=.5)

            # plotting the Temperature for sensor A and sensor B for the specified timeframe
            ax2 = plt.subplot(212)
            ax2.plot(sensor_A_filter["Time"],sensor_A_filter["Humidity"],'b')
            ax2.plot(sensor_B_filter["Time"],sensor_B_filter["Humidity"],'g')
            ax2.set_xlabel('Time')
            ax2.set_ylabel('Humidity')
            ax2.set_title('VARIATION OF HUMIDITY ACROSS TIME')
            ax2.set_ylim([10, 40])
            ax2.legend(['A', 'B'], loc='upper right')
            xfmt1 = mdates.DateFormatter('%d-%m-%y %H:%M')
            ax2.xaxis.set_major_formatter(xfmt1)

            plt.show()

else:
    print("The start time is greater than the end time! Please change it accordingly!!\n")
P3A3_RAJA_prashanr.py
Open with
Displaying P3A1_RAJA_prashanr.py.