#Author: Rushabh Shah
#Original Creation date: 04/02/2017 
#Last modification date: 04/07/2017
#Description: This program is a basic program that asks user for his first name and last name and then welcomes the user using a print statement.

#welcome is a function that asks user for his first name and last name and welcomes the user
def welcome():
    first_name = input('Please identify yourself. Enter your first name \n') #this variable stores the first name of the user
    last_name = input('Please identify yourself. Enter your first name \n') #this variable stores the last name of the user
    print('Hello ',first_name,' ',last_name,'. This program is going to welcome a user and ask him to input galloons of gas, and give him a menu',\
          'with a list of conversions he/ she can perform, and once choosing the option will pefrom the conversion with the galloons of gas',\
          'and ask user if he wants to do another conversion or not. Program gracefully exits when user enters no for another conversion.')

#main function is ran as the program starts and calls the welcome function
def main():
    welcome()

main()
