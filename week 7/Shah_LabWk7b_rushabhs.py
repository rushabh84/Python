#Author: Rushabh Shah
#Original_creation_date: 05/02/2017
#Last_modification_date: 05/02/2017
#Description: This program is using the sqlite3 library and creating a table and does operations like inserting 5 records from am list into table created in database and prints all records
import sqlite3
connection = sqlite3.connect("roster.db")
cursor = connection.cursor()

#this function creates a table named student in the database roster.db
def create_student():
    sql_command = """CREATE TABLE student( std_id INTEGER PRIMARY KEY, fname VARCHAR(20), lname VARCHAR(30), gender CHAR(1));"""
    cursor.execute(sql_command)
    
#this function drops the table student at the end of the program
def drop_student():
    cursor.execute("""DROP TABLE student;""")
   
#this function inserts 5 records of student into the table student from the list holding records for 5 stduents    
def insert_student():
    student_data = [(1000,'Rushabh','Shah','m'), (2000,'Jay','Mehta','m'),(3000,'Jennifer','Lopez','f'),(4000,'Bethany','Lin','f'),(5000,'Ayan','Mehra','m')]
    for p in student_data:
        impl_str = """INSERT INTO student (std_id, fname, lname, gender) VALUES ("{id}", "{first}", "{last}", "{gender}");"""
        #assign respective value to columns of table using format 
        sql_command = impl_str.format(id = p[0], first = p[1], last=p[2], gender=p[3])
        cursor.execute(sql_command)

#this functio uses select statement to print all the records in the table
def select_student():
    cursor.execute("SELECT * FROM student") 
    print("Extracting all the records from the student table. The details of students are:")
    result = cursor.fetchall()  #extracts all records and stores in result
    print('*******************************************************')
    for r in result:
        print(r)

#calls other functions, 1st creates tables, then inserts, then selects and then drops the table student   
def main():
    create_student()
    insert_student()
    select_student()
    drop_student()
    connection.commit()
    connection.close()
    
#starting point of the program
main()
