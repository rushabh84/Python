import sqlite3
import pandas as pd
import numpy as np

# Connecting to the sensor Database connection

connection = sqlite3.connect("sensor.db")
cursor = connection.cursor()

# creating dataframes from the database tables

A_sensor = pd.read_sql_query("SELECT * FROM SensorA",connection,\
                  index_col=None, coerce_float=True, params=None, parse_dates=None, chunksize=None)
B_sensor = pd.read_sql_query("SELECT * FROM SensorB",connection,\
                  index_col=None, coerce_float=True, params=None, parse_dates=None, chunksize=None)

# calculating the average temperature and humidity for the entire time period of sensor A
# calculating the number of datapoints for sensor A

print('*************** Avg. Temperature and Humidity for the entire period ***************\n')
print('*********************************** Sensor A **************************************')
print("Avg. Temperature:",round(A_sensor["Temperature"].mean(),2))
print("Avg. Humidity:",round(A_sensor["Humidity"].mean(),2))
print("No. of Data points:",A_sensor["Time"].count())

# calculating the average temperature and humidity for the entire time period of sensor B
# calculating the number of datapoints for sensor A

print('*********************************** Sensor B **************************************')
print("Avg. Temperature:",round(B_sensor["Temperature"].mean(),2))
print("Avg. Humidity:",round(B_sensor["Humidity"].mean(),2))
print("No. of Data points:",B_sensor["Time"].count(),"\n")

# converting the time column to actual datetime and creating a date column

A_sensor['Time'] = pd.to_datetime(A_sensor['Time'])
B_sensor['Time'] = pd.to_datetime(B_sensor['Time'])

A_sensor['Date'] = (A_sensor['Time']).dt.date
B_sensor['Date'] = (B_sensor['Time']).dt.date


# calculating the average temperature and humidity for each day of sensor A
# Gets the no. of data points for each day along with total no of datapoints for sensor A

print("****************** Mean of Temperature and Humidity for Sensor A ******************\n")

Date_mean_A = A_sensor.groupby(['Date']).agg([np.mean,np.size])
Date_mean_A = Date_mean_A.round({('Temperature', 'mean'): 2, ('Humidity', 'mean'): 2})

Date_mean_A[('Temperature', 'size')] = Date_mean_A[('Temperature', 'size')].astype(int)
Date_mean_A[('Humidity', 'size')] = Date_mean_A[('Humidity', 'size')].astype(int)

print(Date_mean_A)
print()
print("Total No. of Datapoints:",A_sensor["Time"].count())
print()

# calculating the average temperature and humidity for each day of sensor B
# Gets the no. of data points for each day along with total no of datapoints for sensor B

print("****************** Mean of Temperature and Humidity for Sensor B ******************\n")

Date_mean_B = B_sensor.groupby(['Date']).agg([np.mean,np.size])
Date_mean_B = Date_mean_B.round({('Temperature', 'mean'): 2, ('Humidity', 'mean'): 2})

Date_mean_B[('Temperature', 'size')] = Date_mean_B[('Temperature', 'size')].astype(int)
Date_mean_B[('Humidity', 'size')] = Date_mean_B[('Humidity', 'size')].astype(int)

print(Date_mean_B)
print()
print("Total No. of Datapoints:",B_sensor["Time"].count())
print()

# Getting the user input for start and end time

check = True
while check:
    try:
        Start_time = pd.to_datetime(input("""Enter the start time period for which you need the average of temperature and humidity.
                                    The Date format should be MM-DD-YYYY HH:MM:SS AM/PM: """))
        check = False
    except ValueError:
        print('Invalid date! Please enter the date in proper format!!\n')

check = True
while check:
    try:
        End_time = pd.to_datetime(input("""\nEnter the end time period for which you need the average of temperature and humidity.
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

# The dataset is filtered for the corresponding time range

if Start_time <= End_time:
    sensor_A_filter = A_sensor[(pd.to_datetime(A_sensor.Time) >= Start_time) & (pd.to_datetime(A_sensor.Time) <= End_time)]
    sensor_B_filter = B_sensor[(pd.to_datetime(B_sensor.Time) >= Start_time) & (pd.to_datetime(B_sensor.Time) <= End_time)]
    if sensor_A_filter.size == 0 and sensor_B_filter.size == 0:
        print("The data is not available for the specified dates! The data is available for the period:",min(A_sensor.Time),"to",max(A_sensor.Time),"\n")
    else:
        # calculating the average temperature and humidity for the specified timeframe for sensor A
        # Gets the no. of data points  in the specified timeframe for sensor A
        
        print("****************** Mean of Temperature and Humidity for Sensor A ******************")
        print("Avg. Temperature:",round(sensor_A_filter["Temperature"].mean(), 2))
        print("Avg. Humidity:",round(sensor_A_filter["Humidity"].mean(), 2))
        print("No. of Data points:",sensor_A_filter["Time"].count())

        # calculating the average temperature and humidity for the specified timeframe for sensor B
        # Gets the no. of data points  in the specified timeframe for sensor B
        
        print("****************** Mean of Temperature and Humidity for Sensor A ******************")
        print("Avg. Temperature:",round(sensor_B_filter["Temperature"].mean(), 2))
        print("Avg. Humidity:",round(sensor_B_filter["Humidity"].mean(), 2))
        print("No. of Data points:",sensor_B_filter["Time"].count(),"\n")

else:
    print("The start time is greater than the end time! Please change it accordingly!!\n")


# calculating the average temperature and humidity both sensor A and sensor B
# Gets the total no. of datapoints for both sensor A and sensor B

print("****************** Mean of Temperature and Humidity for Sensor A & Sensor B ******************")
tot_temp_mean = (A_sensor["Temperature"].sum()+B_sensor["Temperature"].sum())/(A_sensor["Time"].count()+B_sensor["Time"].count())
tot_hum_mean = (A_sensor["Humidity"].sum()+B_sensor["Humidity"].sum())/(A_sensor["Time"].count()+B_sensor["Time"].count())
print("Avg.Temperature (Sensor A & Sensor B):",round(tot_temp_mean,2))
print("Avg.Humidity (Sensor A & Sensor B):",round(tot_hum_mean,2))
print("No. of Data points (Sensor A & Sensor B):",A_sensor["Time"].count()+B_sensor["Time"].count())