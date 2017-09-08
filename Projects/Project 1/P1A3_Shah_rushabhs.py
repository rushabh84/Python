#Author: Rushabh Shah
#Original Creation date: 04/02/2017 
#Last modification date: 04/07/2017
#Description: This task of the Then it calls te welcome() function which welcomes the user, then
               #calls user_inputs() which asks user for an input about the gasoline of gas and asks whether he/she wants to perform conversions with that
               #If user says yes, from user_inputs, conversion() is called that performs all the 5 conversion on the galloons of gasprogram is welcoming the user after taking his first and last name. Then asks user for an input(galloons of gas) and a type of conversion
               #user would like to perform, and does that conversion. Then asks user if he would like to do another conversion, if yes does another conversion, if no gracefully exits.

#welcome is a function that asks user for his first name and last name and welcomes the user
def welcome():
    first_name = input('Please identify yourself. Enter your first name \n') #this variable stores the first name of the user
    last_name = input('Please identify yourself. Enter your first name \n') #this variable stores the last name of the user
    print('Hello ',first_name,' ',last_name,'. This program is going to calculate welcome a user and ask him to input galloons of gas, and give him a menu',\
          'with a list of conversions he/ she can perform, and once choosing the option will pefrom the conversion with the galloons of gas',\
          'and ask user if he wants to do another conversion or not. Program gracefully exits when user enters no for another conversion')

#this function asks user to enter an amount of gasoline, and has a try except block to handle incorrect/ invalid input(string value) for galloons of gas and asks user to enter
#another valid input for gasoline of gas. Asks user after a conversion is done, whether he would like to do another conversion or not. If no, user gracefully exits the program
def user_inputs():
    try:
        gasoline_qty = float(input('Please enter the gallons of gasoline \n')) #this variable stores the quantity of gasoline in gallons user wants
        option = input('Would like to perform an conversion with the amount of gasoline entered?'\
                       'Enter yes or no. \n')
        #checks whether the user wants to perform one more conversion with the galloons of gas
        while option.lower() == 'yes':
            conversion(gasoline_qty)  #calls the fucntion conversion which performs the conversion user will select
            print('Do you want to perform another conversion?')
            option = input('Enter yes or no \n')
    except ValueError:
        print('It was an invalid input. Please enter valid gallons of gasoline')
        user_inputs()  #if invalid input for gasoline, ask user for a new input
    print("You don't want to peform any more conversion with the galloons of gas")  #message shown when user is exiting the program


#this function peforms any 1 of the 5 conversions on the galloons of gas provided by user. User decides which conversion he/she wants to perform
def conversion(gallons):
    try:
        show_menu()  #calls this function to inform the 5 conversions that will be done
        choice_conversion = int(input('Enter what conversion do you want to perform \n'))  #gets the input for which conversion
        #if else condition to check the user's choice and do the appropriate conversio with galloons of gas
        if choice_conversion == 1:
            litres = gallons * 3.7854
            print('The number of litres are: ',litres, ' litres.')
        elif choice_conversion == 2:
            barrels = gallons / 42
            print('The number of barrels requires are: ',barrels, ' barrels.')
        elif choice_conversion == 3:
            pounds_CO2 = gallons * 20
            print('The amount of CO2 produced by gasoline is :',pounds_CO2, ' pounds.')
        elif choice_conversion == 4:
            ethanol = (gallons * 115000)/ 75700
            print('The amount of CO2 produced by gasoline is :',ethanol, ' galloons.')
        elif choice_conversion == 5:
            total_price = gallons * 4
            print('The total price for this quantity of gallons of gasoline is $',total_price, ' .')
        #if user inputs any other option not provided in the menu, then shows a message saying invalid choice and wont do any conversion for the user
        else:
            print('You entered an invalid choice. Please enter a valid choice from the menu.')
    except ValueError:
        print('Please enter one of the choices from the menu provided to you. Try again')
        conversion(gallons)
        
# a function to display conversion options to the user
def show_menu():
    print('Types of conversion:')
    print('----------------------')
    print('1: Number of litres')
    print('2:Number of barrels of oil required to produce the gallons of gasoline specified')
    print('3:Number of pounds of CO2 produced')
    print('4:Equivalent energy amount of ethanol gallons')
    print('5:Price of the gasoline in US dollars')
    print()

    
#main function calls the welcome function and is ran as the program starts.Then it calls te welcome() function which welcomes the user, then
#calls user_inputs() which asks user for an input about the gasoline of gas and choice of conversion and asks whether he/she wants to perform conversions with that
#If user says yes, from user_inputs, conversion() is called that performs the conversion chosen on the galloons of gas
def main():
    welcome()
    user_inputs()
    print('Exiting the program, have a great day')

main()
