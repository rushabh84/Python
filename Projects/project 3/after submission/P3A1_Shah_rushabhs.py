#Author: Rushabh Shah
#Original creation date: 05/ 03/ 2017
#Last modification date: 05/ 06/ 2017
#Description: This program reads data from 10 csv files, and creates 3 tables, tow for inidivual sensors A and B
#             and one which is the merged version of two tables, program also inserts data from csv files into
#             tables and also selects al rows from tables to print the records on the console
import pandas as pd
import sqlite3

connection = sqlite3.connect("project3.db")
cursor = connection.cursor()

#this function reads contents from all 10 csv files into 2 lists, one for sensor A and for sensor B
def readCSVfiles():
    combine = list()
    combine2 = list()
    filename = ['A1.csv','A2.csv','A3.csv','A4.csv','A5.csv']
    filename2 = ['B1.csv','B2.csv','B3.csv','B4.csv','B5.csv']
    #loop through csv files and append all the rows from each csv in respective lists
    #however attributes like usecols, encoding were added for removing unnecessary columns and right format of data being entered
    #skiprows makes sure that the first row which is plottile is ignored and heading = 0 doesnt add the heading rows
    for each in range(5):
        sensors = pd.read_csv(filename[each], usecols = [0,1,2,3], header = 0,\
                          encoding='iso-8859-1', skiprows = 1)
        sensors2 = pd.read_csv(filename2[each], usecols = [0,1,2,3], header = 0, encoding = 'iso-8859-1', skiprows = 1)
        combine.append(sensors)
        combine2.append(sensors2)
    
    return combine, combine2

    
    
#everytime you run this program drop tables so you can recreate them
def drop_tables():
    cursor.execute("""DROP TABLE sensorA;""")
    cursor.execute("""DROP TABLE sensorB;""")
    cursor.execute("""DROP TABLE sensors;""")


#creating 3 tables, one for sensor A, sensorB and one which has data of both tables combined
#can let user work with merged or individual tables as they require
def create_tables():
    sql_command = """CREATE TABLE sensorA(sens_id INTEGER PRIMARY KEY,  sensorName CHAR(1), Time TimeStamp, Temperature Number(6,3), Humidity Number(5,2));"""
    cursor.execute(sql_command)
    sql_command = """CREATE TABLE sensorB(sens_id INTEGER PRIMARY KEY,  sensorName CHAR(1), Time TimeStamp, Temperature Number(6,3), Humidity Number(5,2));"""
    cursor.execute(sql_command)
    sql_command = """CREATE TABLE sensors(sens_id INTEGER PRIMARY KEY,  sensorName CHAR(1), Time TimeStamp, Temperature Number(6,3), Humidity Number(5,2));"""
    cursor.execute(sql_command)



#this function inserts data from list to table A, and data is inserted using loop which 1st converts each element of list which is data frame
#into list and then loops through each row of list and adds to table sensorA
def insert_tablesA(a):
    total = 0
    for p in a:
        plist = p.values.tolist()  #converting data frame into list
        for line in plist:
            total += 1
            impl_str = """INSERT INTO sensorA (sens_id, sensorName, Time, Temperature, Humidity) VALUES ("{id}", "{name}", "{timestamp}", "{temperature}", "{humidity}");"""
            #assign respective value to columns of table using format 
            sql_command = impl_str.format(id = total, name = 'A', timestamp = line[1], temperature = line[2], humidity = line[3])
            cursor.execute(sql_command)
    
#this function inserts data from list to table sensorB, and data is inserted using loop which 1st converts each element of list which is data frame
#into list and then loops through each row of list and adds to table sensorB
def insert_tablesB(b):
    total = 0
    for p in b:
        plist2 = p.values.tolist()  #converting data frame into list
        for line in plist2:
            total += 1
            impl_str = """INSERT INTO sensorB (sens_id, sensorName, Time, Temperature, Humidity) VALUES ("{id}", "{name}", "{timestamp}", "{temperature}", "{humidity}");"""
            #assign respective value to columns of table using format 
            sql_command = impl_str.format(id = total, name = 'B', timestamp = line[1], temperature = line[2], humidity = line[3])
            cursor.execute(sql_command)
            
#this function inserts data from list to table sensors, and data is inserted using loop which 1st converts each element of list which is data frame
#into list and then loops through each row of list and adds to table sensors           
def insert_tables(a,b):
    total = 0
    #add rows from 1st list which has data for sensor A
    for p in a:
        plist = p.values.tolist()  #converting data frame into list
        for line in plist:
            total += 1
            impl_str = """INSERT INTO sensors (sens_id, sensorName, Time, Temperature, Humidity) VALUES ("{id}", "{name}", "{timestamp}", "{temperature}", "{humidity}");"""
            #assign respective value to columns of table using format 
            sql_command = impl_str.format(id = total, name = 'A', timestamp = line[1], temperature = line[2], humidity = line[3])
            cursor.execute(sql_command)
    #add rows from 1st list which has data for sensor B
    for p in b:
        plist2 = p.values.tolist()  #converting data frame into list
        for line in plist2:
            total += 1
            impl_str = """INSERT INTO sensors (sens_id, sensorName, Time, Temperature, Humidity) VALUES ("{id}", "{name}", "{timestamp}", "{temperature}", "{humidity}");"""
            #assign respective value to columns of table using format 
            sql_command = impl_str.format(id = total, name = 'B', timestamp = line[1], temperature = line[2], humidity = line[3])
            cursor.execute(sql_command)
    
#this function selects all the rows from inidividual tables sensorA and sensorB
def select_sensors():
    cursor.execute("SELECT * FROM sensorA") 
    print("Extracting all the records from the sensor A table. The details of sensors are:")
    result = cursor.fetchall()  #extracts all records and stores in result
    print('*******************************************************')
    for r in result:
        print(r)
    print('*******************************************************')
    
    cursor.execute("SELECT * FROM sensorB") 
    print("Extracting all the records from the sensor B table. The details of sensors are:")
    result = cursor.fetchall()  #extracts all records and stores in result
    print('*******************************************************')
    for r in result:
        print(r)
    print('*******************************************************')

#this function selects all the rows from merged tables sensors
def select_merged_tables():
    cursor.execute("SELECT * FROM sensors") 
    print("Extracting all the records from the sensors table. The details of sensors are:")
    result = cursor.fetchall()  #extracts all records and stores in result
    print('*******************************************************')
    for r in result:
        print(r)
    print('*******************************************************')
    
#calls all other functions to create tables, insert data into tables and select all ros from tables    
def main():
    final_A, final_B = readCSVfiles()
    #drop_tables()
    create_tables()
    insert_tablesA(final_A)
    insert_tablesB(final_B)
    insert_tables(final_A, final_B)
    #select_sensors()
    select_merged_tables()
    connection.commit()
    connection.close()

#starting point of program
main()
