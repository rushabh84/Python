#Author: Rushabh Shah
#Original creation date: 05/ 04/ 2017
#Last modification date: 05/07/2017
#Description: This program takes data from tables and stores it in 3 data frames. The merged dataframe is split into 2 based on sensor names 
#             Then the program asks user for inputs to enter the end time and start time, option for visualizing
#             the data for sensor A or B, option to choose type of visualizations, and if the inputs are right
#             plots different graphs vs counts of different coluns in the given ranhe, or variation in
#             temperature and humidity in the given range for the chose sensor, if the dates were invalid or outside range
#             just prints start time is greater than end date and doesn't do any visualization

import pandas as pd
import sqlite3
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

#establish connection with database
connection = sqlite3.connect("project3.db")
cursor = connection.cursor()

#this function gets the data from tables sensorA, sensorB and sensors and stores them in 3 data frames. Using data frame pof the sensors table creates 2 data frames based on the sensor name
#and calls the operations_perday function
def create_frames():
    df_A = pd.read_sql_query("SELECT * from sensorA", connection, coerce_float = True, parse_dates = None)
    df_B = pd.read_sql_query("SELECT * from sensorB", connection, coerce_float = True, parse_dates = None)
    df_total = pd.read_sql_query("SELECT * from sensors", connection, coerce_float = True, parse_dates = None)
    
    #from the df_total data frame craete 2 new dta frames for sensor A and B based on their sensorName
    df_sensA = df_total[(df_total['sensorName'] == 'A')]
    df_sensB = df_total[(df_total['sensorName'] == 'B')]
    operations_perday(df_A, df_B)    
    return df_sensA, df_sensB,df_total
    

#this fucntion works on the individual data frames for sensor A and B, converts the timestamp value into datetime and then that into date, gets the unique values of date for both sensors
#and then calls the user_plot_time_period function to plot 
def operations_perday(a,b):
    #split timeframe column into time
    a['Timea'] = pd.to_datetime(a['Time'])
    b['Timeb'] = pd.to_datetime(b['Time'])
    #converting the datetime type into date uing the date method to perform operations for each day
    a['Date'] = (a['Timea']).dt.date
    b['Date'] = (b['Timeb']).dt.date
    #call to the function
    user_plot_time_period(a, b)
    
        
#this function asks user for the enter the start time and the end time and if the inputs are in the time range of the data set, then
#gives options to do different plots and does visualizations on the data frames within that time range for sensor A and B, 
#and if no data within that range then simply prints message saying no data
def user_plot_time_period(a,b):
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
    #perform visualization if end time is greater than start time, this condition and the abover if conditions takes care of all possibility
    #if start and end time both are greater than maximum time or lesser than minimum time
    if begin <= end:
        #make sub dataframes for sensor A and B within the given range using conditions that time should be within minimum and maximum time
        a_range = a[(a['Timea'] >= begin) & (a['Timea'] <= end)]
        b_range = b[(b['Timeb'] >= begin) & (b['Timeb'] <= end)]
        #if there is data for sensor A in the given range , then calculate average humidity and temperature otherwise print no data within the range
        if a_range.size == 0:
            print('There is no data for sensor A between the dates entered by the user, cant calculate average. Try entering between ',min_time,' and ',max_time)
        else:
            #Ask user to choose either of the 2 options for choosing sensors, and loop until user enters a correct choice
            print('Choose the sensor for which you to want to perform visualization and plot graphs')
            print('1.Sensor A    2.Sensor B')
            i = 0
            while True:
                try:
                    #if the input was either 1 or 2 then break as the right input is entered
                    i = int(input('Please enter your choice: '))
                    if i == 1 or i==2:
                        break
                    else:
                        print('Please enter one of the available options, choose 1 or 2' )
                except ValueError:
                    print('Please enter a valid integer input')
                    
            print('Do you want to see the graph for counts of different columns or variation in columns with time?')
            print('1.Variation                2.Count')
            j = 0
            #Ask user to choose either of the 2 options for type pf visualization, and loop until user enters a correct choice
            while True:
                try:
                    j = int(input('Please enter your choice: '))
                    #if the input was either 1 or 2 then break as the right input is entered
                    if j == 1 or j==2:
                        break
                    else:
                        print('Please enter one of the available options, choose 1 or 2' )
                except ValueError:
                   print('Please enter a valid integer input')
            print('The visualization is done for ',a_range['Temperature'].count,' data points.')     
            if i == 1:
                 #if option 1 is chosen for type of plots, then plot 3 different graphs for showing variation with time
                 if j == 1:
                     #plot graphs to show variation for sensors w.r.t temperature and humidity vs time
                     #used subplot to have 3 rows and 1 column to plot the graph in
                     gg = plt.subplot(311)
                     print('Visualizations for sensor A')
                     print('Visualization 1: Temperature vs Time')
                     plt.style.use('dark_background')  #to style the graph
                     gg.plot(a_range['Timea'],a_range['Temperature'],'b')  #plot time vs temperature
                     gg.set_ylim([70, 90])  #set limit of y axis
                     gg.set_ylabel('Temperature')
                     xfmt = mdates.DateFormatter('%d-%m-%y')  #set the formt of date on the x axis
                     gg.xaxis.set_major_formatter(xfmt)
                     gg.set_title('Temperature vs Time')  #set title of the graph
                     plt.subplots_adjust(hspace=0.3)
                     
                     gg2 = plt.subplot(313)
                     print('Visualization 2: Humidity vs Time')
                     plt.style.use('dark_background')  #to style the graph
                     gg2.plot(a_range['Timea'],a_range['Humidity'],'r')  #plot time vs humidity
                     gg2.set_ylim([10, 40])
                     gg2.set_ylabel('Humidity')
                     xfmt = mdates.DateFormatter('%d-%m-%y')  #set the formt of date on the x axis
                     gg2.xaxis.set_major_formatter(xfmt)
                     gg2.set_title('Humidity vs Time')  #set title of the graph
                     
                 else:
                     #if option 2 was chose, then plot the graphs for counts vs tempertaure, humidity and date
                     #shows the count for each unique value of the 3 quantities
                     print('Visualization 1: Counts vs date')
                     #plotting the count for each type of date
                     df1 = a_range['Date'].value_counts()  #gets counts for all unique values of status
                     df1.plot(kind='bar', x= 'Date', y='Counts', title = 'Date vs counts', rot = 0)
                     plt.show()
                     
                     print('Visualization 2: Counts vs date')
                     #plotting the count for each type of temperature using 
                     df1 = a_range['Temperature'].value_counts()  #gets counts for all unique values of status
                     df1.plot(kind='bar', x= 'Temperature', y='Counts', title = 'Temperature vs counts', rot = 0)
                     plt.show()
                     
                     print('Visualization 3: Humidity vs date')
                     #plotting the count for each type of humidity 
                     df1 = a_range['Humidity'].value_counts()  #gets counts for all unique values of status
                     df1.plot(kind='bar', x= 'Humidity', y='Counts', title = 'Humidity vs counts', rot = 0)
                     plt.show()
            else:
                if j == 1:
                    #plot graphs to show variation for sensors w.r.t temperature and humidity vs time
                    gg = plt.subplot(311)
                    print('Visualizations for sensor B')
                    print('Visualization 1: Temperature vs Time')
                    plt.style.use('dark_background')
                    gg.plot(b_range['Timeb'],b_range['Temperature'],'b')
                    gg.set_ylim([70, 90])
                    gg.set_ylabel('Temperature')
                    xfmt = mdates.DateFormatter('%d-%m-%y')
                    gg.xaxis.set_major_formatter(xfmt)
                    gg.set_title('Temperature vs Time')
                    plt.subplots_adjust(hspace=0.3)
                    
                    gg2 = plt.subplot(313)
                    print('Visualization 2: Humidity vs Time')
                    plt.style.use('dark_background')
                    gg2.plot(b_range['Timeb'],b_range['Humidity'],'r')
                    gg2.set_ylim([10, 40])
                    gg2.set_ylabel('Humidity')
                    xfmt = mdates.DateFormatter('%d-%m-%y')
                    gg2.xaxis.set_major_formatter(xfmt)
                    gg2.set_title('Humidity vs Time')
                else:
                    print('Visualization 1: Counts vs date')
                    #plotting the count for each type of date 
                    df1 = a_range['Date'].value_counts()  #gets counts for all unique values of status
                    df1.plot(kind='bar', x= 'Date', y='Counts', title = 'Date vs counts', rot = 0)
                    plt.show()
                    print() 
                    print('Visualization 2: Tempertature vs date')
                    #plotting the count for each type of temperature 
                    df1 = a_range['Temperature'].value_counts()  #gets counts for all unique values of status
                    df1.plot(kind='bar', x= 'Temperature', y='Counts', title = 'Temperature vs counts', rot = 0)
                    plt.show()
                     
                    print('Visualization 3: Humidity vs date')
                    #plotting the count for each type of humidity 
                    df1 = a_range['Humidity'].value_counts()  #gets counts for all unique values of status
                    df1.plot(kind='bar', x= 'Humidity', y='Counts', title = 'Humidity vs counts', rot = 0)
                    plt.show()
                    
    else:
        print('The start time happens to be greater than the end time, you entered incorrect/ invalid data. Try entering valid inputs and RERUN the program')
        

    
#calls all the functions in the program
def main():
    a,b,total = create_frames()
    
    
#starting point of the program
main()
