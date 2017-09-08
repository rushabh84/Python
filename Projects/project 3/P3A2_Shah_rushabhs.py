#Author: Rushabh Shah
#Original creation date: 05/ 04/ 2017
#Last modification date: 05/07/2017
#Description: This program takes data from tables and stores it in 3 data frames. The merged dataframe is split into 2 based on sensor names and using mean() average humidity and
#             humidity and temperature are calculated. Also, the 2 data frames are grouped by Date and and for each group calculates the average humidity and temperature(per day average)
#             Also, finds the average humidity and temperature for the merged table, inlcudes rows for sensors A and B, throughout the entire period. Lastly, asks user for
#             the start time and end time, and checking the validity of these time period entered, calculates the average humidity and temperature in that given range

import pandas as pd
import sqlite3

connection = sqlite3.connect("project3.db")
cursor = connection.cursor()

#this function gets the data from tables sensorA, sensorB and sensors and stores them in 3 data frames. Using data frame of the sensors table creates 2 data frames based on the sensor name
#and for each of the 2 created data frames calculates average humidity and temperature and calls the operations_perday function
def create_frames():
    df_A = pd.read_sql_query("SELECT * from sensorA", connection, coerce_float = True, parse_dates = None)
    df_B = pd.read_sql_query("SELECT * from sensorB", connection, coerce_float = True, parse_dates = None)
    df_total = pd.read_sql_query("SELECT * from sensors", connection, coerce_float = True, parse_dates = None)
    
    #Operation: calculate average humidity for the whole period for each sensor
    #from the df_total data frame create 2 new dta frames for sensor A and B based on their sensorName
    df_sensA = df_total[(df_total['sensorName'] == 'A')]
    df_sensB = df_total[(df_total['sensorName'] == 'B')]
    avg_humidity_A = round(df_sensA['Humidity'].mean(),3)
    avg_humidity_B = round(df_sensB['Humidity'].mean(),3)
    print('The calculations are done for a total of ',df_sensA['sens_id'].count(),' data points')
    print('The average humidity for sensor A throughout the period is',avg_humidity_A)
    print('The average humidity for sensor B throughout the period is',avg_humidity_B)
    
    #Operation: calculate average temperature for the whole period for each sensor
    avg_temp_A = round(df_sensA['Temperature'].mean(),3)
    avg_temp_B = round(df_sensB['Temperature'].mean(),3)
    print('The calculations are done for a total of ',df_sensB['sens_id'].count(),' data points')
    print('The average temperature for sensor A throughout the period is',avg_temp_A)
    print('The average temperature for sensor B throughout the period is',avg_temp_B)
    #call mehtod to calculate average humidity and temperature per day for each sensor
    operations_perday(df_A, df_B)
    return df_sensA, df_sensB,df_total
    

#this fucntion works on the individual data frames for sensor A and B, converts the timestamp value into datetime and then that into date, gets the unique values of date for both sensors
#and then groups by both the data frames based on date, and calculates the mean value of temperature and humidity for each group and convert this conversio to list to have results for each
#unique value in the group
def operations_perday(a,b):
    #split timeframe column into time
    a['Timea'] = pd.to_datetime(a['Time'])
    b['Timeb'] = pd.to_datetime(b['Time'])
    #converting the datetime type into date uing the date method to perform operations for each day
    a['Date'] = (a['Timea']).dt.date
    b['Date'] = (b['Timeb']).dt.date
    #find unique dates for each sensor and make a list of dates
    unique_dates_A = a['Date'].unique()
    unique_dates_B = b['Date'].unique()
    #group by data frames a and b by Date and find mean for column humidity and temperature
    #and convert the mean into list using values.tolist()
    avg_hum_perday_A = a.groupby('Date')['Humidity'].mean().values.tolist()
    avg_temp_perday_A = a.groupby('Date')['Temperature'].mean().values.tolist()
    avg_hum_perday_B = b.groupby('Date')['Humidity'].mean().values.tolist()
    avg_temp_perday_B = b.groupby('Date')['Temperature'].mean().values.tolist()
    #get the size of uniqe entries after grouping by Date column
    size = len(avg_hum_perday_A)
    #print the average humditity and temprature per day for sensor A and sensor B
    print('********************************************************')
    print('The calculations are done for sensor A individually for ',a['Date'].count(),' data points')
    print('Average humidity per day for sensor A')
    #the for loops prints average humidity and temperature for each day for sensor A
    for each in range(size):
        print('For date',str(unique_dates_A[each]),' average humidity is: ',round(avg_hum_perday_A[each],3))
    print('Average temperature per day for sensor A')
    for each in range(size):
        print('For date',str(unique_dates_A[each]),' average temperature is: ',round(avg_temp_perday_A[each],3))
    #the for loops prints average humidity and temperature for each day for sensor B
    print('********************************************************')
    print('The calculations are done for sensor B individually for ',b['Date'].count(),' data points')
    print('Average humidity per day for sensor B')
    for each in range(size):
        print('For date',str(unique_dates_B[each]),' average humidity is: ',round(avg_hum_perday_B[each],3))
    print('Average temperature per day for sensor B')
    for each in range(size):
        print('For date',str(unique_dates_B[each]),' average temperature is: ',round(avg_temp_perday_B[each],3))
    #call function user_time_period
    user_time_period(a, b)
    
        
#this function asks user for the enter the start time and the end time and if the inputs are in the time range of the data set, calculates average humidity and temperature
#within that time range for sensor A and B, and if no data within that range then simply prints message saying no data
def user_time_period(a,b):
    right_input = 0
    #since minimum and maximum time for both sensors are same, just finding min and max for one sensor
    min_time = a['Timea'].min()
    max_time = a['Timea'].max()
    print('********************************************************')
    print('The time frame for the data set are as follows')
    print('The minimum time for the dataset is: ',min_time)
    print('The maximum time for the dataset is: ',max_time)
    print('*******************************************************')
    print('The Date format should be MM-DD-YYYY HH:MM:SS AM/PM.')
    begin = 0
    end = 0
    #ask use for an input for end times, and while and if loop makes sure that correct time is entered and
    #enter isnt counted as input
    
    #if you just enter MM-DD-YYY then it wont raise an exception and by default take 00:00:00 as the time
    while right_input == 0:
        try:
            entry = input('Enter the start time period to calculate average of temperature and humidity.')
            if entry != "":
                begin = pd.to_datetime(entry)
                break
        except ValueError:
            print('You happen to enter invalid date, please try again \n')
            
    
    #ask use for an input for end times, and while and if loop makes sure that correct time is entered and
    #enter isnt counted as input
    right_input = 0
    while right_input == 0:
        try:
            entry = input('Enter the end time period to calculate average of temperature and humidity.')
            if entry != "":
                end = pd.to_datetime(entry)
                break
        except ValueError:
            print('You happen to enter invalid date, please try again \n')
        
    #if the start time is lesser than the minimum time for sensors, then make the start time as the minimum time 
    if begin < min_time:
        print('The start time is lesser than the minimum time. So we will calculate average from the start time.')
        begin = min_time
    #if the end time is greater than the maximum time for sensors, then make the end time as the maximum time
    if end > max_time:
        print('The end time is greater than the maximum time. So we will calculate average till the end time.')
        end = max_time
    #calculate average only if end time is greater than start time, this condition and the abover if conditions takes care of all possibility
    #if start and end time both are greater than maximum time or lesser than minimum time
    print('The calculations for average humidity and temperature are done between ',begin,' and ',end)
    if begin <= end:
        #make sub dataframes for sensor A and B within the given range using conditions that time should be within minimum and maximum time
        a_range = a[(a['Timea'] >= begin) & (a['Timea'] <= end)]
        b_range = b[(b['Timeb'] >= begin) & (b['Timeb'] <= end)]
        #if there is data for sensor A in the given range , then calculate average humidity and temperature otherwise print no data within the range
        if a_range.size ==0:
            print('There is no data for sensor A between the dates entered by the user, cant calculate average. Try entering between ',min_time,' and ',max_time)
        else:
            #prints the number of data points used to calculate the average values
            print('The calculations for sensor A are done for a total of ',a_range['Timea'].count(),' data points')
            avg_humidity = round(a_range['Humidity'].mean(),3)
            avg_temp = round(a_range['Temperature'].mean(),3)
            print('The average humidity in the given time period range is: ',avg_humidity)
            print('The average temperature in the given time period range is: ',avg_temp)
        #if there is data for sensor B in the given range , then calculate average humidity and temperature otherwise print no data within the range
        if b_range.size ==0:
            print('There is no data for sensor B between the dates entered by the user, cant calculate average')
        else:
            #prints the number of data points used to calculate the average values
            print('The calculations for sensor B are done for a total of ',b_range['Timeb'].count(),' data points')
            avg_humidity = round(b_range['Humidity'].mean(),3)
            avg_temp = round(b_range['Temperature'].mean(),3)
            print('The average humidity in the given time period range is: ',avg_humidity)
            print('The average temperature in the given time period range is: ',avg_temp)
    else:
        print('The start time happens to be greater than the end time, you entered incorrect/ invalid data. Try entering valid inputs and RERUN the program')
        

#this fucntion works with the merged table and calculates the average humidity and temperature for the whole period including values for sensor A as well as B
def operations_whole(df_total):
    #get total count for each table, total humidity anf temperature for both tables
    total_rows = df_total['sens_id'].count()
    #calculate average of humidity and temperature across the whole period for sensors table
    avg_temp = round(df_total['Temperature'].mean(),3)
    avg_humidity = round(df_total['Humidity'].mean(),3)
    #print avg temperature and humidity and number of data points
    print('**************************************************************************')
    print('Operations for entire data set. The calculations are done for a total of ',total_rows,' data points')
    print('The average humidity for the entire data set is: ',avg_humidity)
    print('The average temperature for the entire data set is:', avg_temp)
    
#calls all the functions in the program
def main():
    a,b,total = create_frames()
    operations_whole(total)

#starting point of the program
main()
