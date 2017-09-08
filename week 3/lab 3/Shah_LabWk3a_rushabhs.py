#author: Rushabh Shah
#andrew-id: rushabhs
#Creation date: 04/04/2017
#Last modification date: 04/05/2017

import random
#task 1, A function in input monthly rainfall and calculate the average monthly rainfall and total rainfall anually
def listoperation():
    #a dcitionary that holds the key and corresponding month as the value
    month_dictionary = {1:'January', 2: 'February', 3: 'March', 4:'April', 5: 'May', 6: 'June', 7: 'July', 8: 'August', 9: 'September', 10: 'October', 11: 'November', 12: ' December'}
    monsoon_list = []
    month = 1
    total = 0.0
    #while loop to get inputs for 12 months
    while month <= 12:
        rainfall = float(input('Enter the rainfall for month: ')) #get input for rainfall from user
        monsoon_list.append(rainfall)  #append the values for rainfall in the list
        total = total + rainfall  #add the rainfall for each month to the accumulator variable
        month += 1  #increment month by 1 as this is the condition to exit while loop
    print('The total rainfall for the year is', total)
    average_rainfall = total / len(monsoon_list)  #caculate average monthly rainfall
    print('The average monthly rainfall is',average_rainfall)
    element_max = max(monsoon_list)  #find the maximum value for rainfall from the list
    index_max = monsoon_list.index(element_max)  #get the index of the maximum value from the list
    element_min = min(monsoon_list)  #find the minimum value for rainfall from the list
    index_min = monsoon_list.index(element_min)  #get the index of the minimum value from the list
    print('The month with the highest rainfall is ',month_dictionary[index_max+1])
    print('The month with the lowest rainfall is ',month_dictionary[index_min+1])  #adding one to index_min since the key starts from 0
        

#task 2, converts sentence with running words into a string where words are seperated by spaces
def stringoperation(sentence):
    pos = 0
    my_string = ""
    for c in sentence:
        #if condition checks if the character is uppercase and it is not the 1st character of string (because 1st character needs to stay uppercase), and condition true then include a space
        if c.isupper() and pos > 0:  
            my_string += " "  #adds a space before adding this charcter to my_string
            my_string += c.lower()  #converts this character to lowercase before adding it to my_string
        else:
            my_string += c  #even when if condition fails, adding character to my_string without converting it to lowercase
        pos += 1
    print('The string after sepearting ther words is ',my_string)
    


#task 3- a quiz to text whether user knows the capital or not
def dictionaryoperations():
    right= 0
    wrong = 0
    usa = {'Texas': 'Austin', 'Georgia': 'Atlanta', 'Kentucky': 'Frankfurt', 'Massachusetts': 'Boston', 'Nebraska': 'Lincoln', 'Virginia': 'Richmond', 'New York': 'Albany', 'Montana': 'Helena', 'Maine': 'Augusta', 'Arizona': 'Phoenix'}
    states = usa.keys()
    r=1
    while r <=10:
        key = random.choice(list(usa.keys()))  #randomly selects the keys from the dictionary usa
        capital = input('Enter the capital of '+key+' :')  #asks user for their answer
        if capital.lower() == usa[key].lower():  #compares if the user's guess and the capital matches or not
            right += 1  #increments right if the guess was correct
        else:
            wrong += 1  #increments wrong if the guess was correct
        usa.pop(key)  #pops the key value from the dictionary, so same state won't be asked to the user
        r = r+1  #condition to exit while loop
    print('Number of correct answers you could guess are: ', right)
    print("Number of incorrect answers you could guess are:", wrong)


    
#main function
def main():
    listoperation()
    print('Enter a sentence and make sure first character of each word is uppercase and the words are running together')
    sentence = input('Please enter a sentence: ')
    stringoperation(sentence)
    dictionaryoperations()
    
# Call the main function.
main()




    
