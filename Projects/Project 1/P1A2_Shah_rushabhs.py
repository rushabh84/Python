#Author: Rushabh Shah
#Original Creation date: 04/02/2017 
#Last modification date: 04/07/2017
#Description: This task of the program is welcoming the user after taking his first and last name. Then asks user for an input(galloons of gas) and performs 5 conversion with that input.

#welcome is a function that asks user for his first name and last name and welcomes the user
def welcome():
    first_name = input('Please identify yourself. Enter your first name \n') #this variable stores the first name of the user
    last_name = input('Please identify yourself. Enter your first name \n') #this variable stores the last name of the user
    print('Hello ',first_name,' ',last_name,'. This program is going to welcome a user and ask him to input galloons of gas, and give him a menu',\
          'with a list of conversions he/ she can perform, and once choosing the option will pefrom the conversion with the galloons of gas',\
          'and ask user if he wants to do another conversion or not. Program gracefully exits when user enters no for another conversion')

#this function asks user to enter an amount of gasoline, and has a try except block to handle incorrect/ invalid input(string value) for galloons of gas and asks user to enter
#another valid input for gasoline of gas.
def user_inputs():
    try:
        print('Conversion operations')
        option = input('Would like to perform the conversions with the amount of gasoline entered?'\
                       'Enter yes or no. \n')
        #while loop takes care if the user wants to perform five conversions again with a new value of galloons of gas, and if no lets a user gracefully exit the program
        while option.lower() == 'yes':
            gasoline_qty = float(input('Please enter the gallons of gasoline \n')) #this variable stores the quantity of gasoline in gallons user wants
            conversion(gasoline_qty)  #calls the fucntion conversion which performs all the 5 conversion
            print('Do you want to perform these 5 conversions with another value of gasoline?')
            option = input('Enter yes or no \n')
    except ValueError:
        print('It was an invalid input. Please enter valid gallons of gasoline')
        user_inputs()  #if invalid input for gasoline, ask user for a new input

    print("You don's want to peform any more conversion with the galloons of gas")

#this function peforms 5 conversion on the galloons of gas provided by user
def conversion(gallons):
    show_menu()  #calls this function to inform the 5 conversions that will be done
    print('Performing type 1 conversion : ')
    litres = gallons * 3.7854
    print('The number of litres are: ',litres, ' litres.')
    print('Performing type 2 conversion :')
    barrels = gallons / 42
    print('The number of barrels requires are: ',barrels, ' barrels.')
    print('Performing type 3 conversion :')
    pounds_CO2 = gallons * 20
    print('The amount of CO2 produced by gasoline is :',pounds_CO2, ' pounds.')
    print('Performing type 4 conversion :')
    ethanol = (gallons * 115000)/ 75700
    print('The amount of CO2 produced by gasoline is :',ethanol, ' galloons.')
    print('Performing type 5 conversion :')
    total_price = gallons * 4
    print('The total price for this quantity of gallons of gasoline is $',total_price, ' .')
        
         
# a function to display conversion options to the user
def show_menu():
    print('Types of conversion to be performed:')
    print('----------------------')
    print('1: Number of litres')
    print('2:Number of barrels of oil required to produce the gallons of gasoline specified')
    print('3:Number of pounds of CO2 produced')
    print('4:Equivalent energy amount of ethanol gallons')
    print('5:Price of the gasoline in US dollars')
    print()

    
#main function calls the welcome function and is ran as the program starts. Then it calls te welcome() function which welcomes the user, then
#calls user_inputs() which asks user for an input about the gasoline of gas and asks whether he/she wants to perform conversions with that
#If user says yes, from user_inputs, conversion() is called that performs all the 5 conversion on the galloons of gas
def main():
    welcome()
    user_inputs()
    print('Exiting the program, have a great day')

main()
