#Author name: Rushabh Shah
#Original date: 04/28/2017
#Last modification date: '04/28/2017
#Description: This program is using the 'Panda' library to perform data analysis on the structured data- csv file. The program is 1st finding the maximum and minimum of 2 columns
             #Them, it's grouping the csv by Agency Name and Complaint Type columns using groupby method, then if finds the unique value for a column 'Agency Name', deletes unwanted columns
             #which doesnt have any data and isn't useful for any anaysis, and finds the dimension of data frame after deleting rows and columns to confirm rows and columns are deleted
             #Even performs melting on the data frame,creates a nbew csv with condition on certain columns and will have selective rows and then copies the new data frame in a new
             #csv called final2.csv, finally whatever operations were performed on the readCSV frame is copied to a csv final.csv.

import csv
from csv import reader
import math
import pandas as pd
import matplotlib.pyplot as plt


def liboperations():
    readCSV = pd.read_csv('311_Service_Requests_from_2010_to_Present.csv', low_memory = False)  #reading csv file and saving it in a data frame using panda library
    print(type(readCSV))
    #pefroming max min operaions on 2 columns
    print("The maximum latitude is:\n",readCSV['Latitude'].max())
    print("The minimum latitude is:\n",readCSV['Latitude'].min())
    print("The maximum longitude is:\n",readCSV['Longitude'].max())
    print("The minimum longitude is:\n",readCSV['Longitude'].min())
    print('Before deleting columns the dimension are :',readCSV.shape)
    print()
    print()

    #qyuerying the data
    qry1 = readCSV.groupby(['Agency Name','Complaint Type'])
    size = readCSV.groupby(['Agency Name']).count()
    print(size)
    count = readCSV['Complaint Type'].value_counts()
    #print('the size is: ',count)

    
    
    #printing unique values of a column
    a = readCSV['Agency Name'].unique()
    print('************************************************')
    print('Unique agency names are :',a)
    print()
    #deleting unwanted columns
    
    del readCSV['Landmark']  
    del readCSV['School Name']
    del readCSV['School Number']
    del readCSV['School Address']
    del readCSV['School Code']
    del readCSV['School Phone Number']
    
    print('After deleting columns the dimension are :',readCSV.shape)
    print()

    #sorting the csv file in descending order on the Agency column
    readCSV = readCSV.sort_values(['Agency'], ascending = [0])
    
    #performing melting on the data fram, source: stackoverflow
    melt = pd.melt(readCSV, id_vars = 'Agency Name')
    print('After performin melting')
    print(melt.iloc[0:5,])
    print()
    print()

    
    #creating a new csv file final2 with agency name as 'ew York City Police Department' and Compalint type as 'Illegal Parking'
    dummy = readCSV[(readCSV['Agency Name'] == 'New York City Police Department') & (readCSV['Complaint Type'] == 'Illegal Parking')]
    print('After applying conditions, the final result will have: ',dummy.shape)  #prints the dimension of data frame dummy, i.e number of rows and columns
    print()
    dummy.to_csv('final2.csv')  #creating new csv file

    
    #copying the readCSV file to another csv after selecting what rows we want, conditon is on school city
    readCSV = readCSV[readCSV['School City'] !='Unspecified']
    print('After deleting rows with no school city, the dimension are :',readCSV.shape)
    print()
    readCSV.to_csv('final.csv')  #copying the update data frame to a new csv

def main():
    liboperations()

main()
