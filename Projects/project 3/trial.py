#Author: Rushabh Shah
#Original creation date: 05/ 03/ 2017
#Last modification date: 
#Description:
import pandas as pd
import sqlite3

connection = sqlite3.connect("proj.db")
cursor = connection.cursor()


def readCSVfiles():
    combine = list()
    combine2 = list()
    filename = ['A1.csv','A2.csv','A3.csv','A4.csv','A5.csv']
    filename2 = ['B1.csv','B2.csv','B3.csv','B4.csv','B5.csv']
    for each in range(5):
        sensors = pd.read_csv(filename[each], usecols = [0,1,2,3], header = 0,\
                          encoding='iso-8859-1', skiprows = 1)
        sensors2 = pd.read_csv(filename2[each], usecols = [0,1,2,3], header = 0, encoding = 'iso-8859-1', skiprows = 1)
            #print(sensors)
        combine.append(sensors)
        combine2.append(sensors2)
    return combine, combine2

    
    

def drop_tables():
    cursor.execute("""DROP TABLE sensorA;""")
    cursor.execute("""DROP TABLE sensorB;""")



def create_tables():
    sql_command = """CREATE TABLE sensorA(sens_id INTEGER PRIMARY KEY,  sensorName CHAR(1), Time VARCHAR(40), Temperature Number(6,3), Humidity Number(5,2));"""
    cursor.execute(sql_command)
    sql_command = """CREATE TABLE sensorB(sens_id INTEGER PRIMARY KEY,  sensorName CHAR(1), Time TimeStamp, Temperature Number(6,3), Humidity Number(5,2));"""
    cursor.execute(sql_command)




def insert_tablesA(a):
    total = 0
    for p in a:
        plist = p.values.tolist()  #converting data frame into list
        #if total ==0:
         #   print(plist)
        for line in plist:
            total += 1
            impl_str = """INSERT INTO sensorA (sens_id, sensorName, Time, Temperature, Humidity) VALUES ("{id}", "{name}", "{timestamp}", "{temperature}", "{humidity}");"""
            #assign respective value to columns of table using format 
            sql_command = impl_str.format(id = total, name = 'A', timestamp = line[1], temperature = line[2], humidity = line[3])
            cursor.execute(sql_command)
    print('Hurrrahhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhh')

def insert_tablesB(b):
    total = 0
    for p in b:
        plist2 = p.values.tolist()  #converting data frame into list
        #if total ==0:
         #   print(plist)
        for line in plist2:
            total += 1
            impl_str = """INSERT INTO sensorB (sens_id, sensorName, Time, Temperature, Humidity) VALUES ("{id}", "{name}", "{timestamp}", "{temperature}", "{humidity}");"""
            #assign respective value to columns of table using format 
            sql_command = impl_str.format(id = total, name = 'B', timestamp = line[1], temperature = line[2], humidity = line[3])
            cursor.execute(sql_command)
            
            
    print('Blahhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhh')



def select_sensors():
    cursor.execute("SELECT * FROM sensorA") 
    print("Extracting all the records from the sensor A table. The details of sensors are:")
    result = cursor.fetchall()  #extracts all records and stores in result
    print('*******************************************************')
    for r in result:
        print(r)
        
    cursor.execute("SELECT * FROM sensorB") 
    print("Extracting all the records from the sensor B table. The details of sensors are:")
    result = cursor.fetchall()  #extracts all records and stores in result
    print('*******************************************************')
    for r in result:
        print(r)

def main():
    final_A, final_B = readCSVfiles()
    #drop_tables()
    create_tables()
    insert_tablesA(final_A)
    insert_tablesB(final_B)
    select_sensors()
    connection.commit()
    connection.close()

main()
