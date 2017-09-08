#Author: Rushabh Shah
#Original Creation Date: 04/29/2017
#Last modification Date: 04/29/2017
#Description: This program mainly identifies the concept words and their frequencies and prints as well as stores the concepts and their frequencies in a text file and on the console
             #in sorted order with the highest frequency concept as the 1st word.
from collections import defaultdict

#this function reads the scrubbed file and then using the defaultdict function finds the count/ frequency of all the concepts in the scrubbed abstract file.    
def final_analysis():
    scrubbed = open('Final_Scrubbed.txt','r')
    r = scrubbed.read()
    analyze_token = defaultdict(int)  #creates an instance of defaultdict
    #the for loop calculates frequency of all the unique concepts
    for word in r.split():
        analyze_token[word] += 1
    #this line of code prepares a list of the concepts and their frequencies and in the sorted order
    analyze_list = [(k, analyze_token[k]) for k in sorted(analyze_token, key = analyze_token.get, reverse=True)]
    #save the result of concepts and their frequencies in a text file and print on the console
    tokens_frequency = open('Concept_Frequency.txt', 'w')
    tokens_frequency.write("The Concept words List and their frequency are \n")
    print("The Concept List and their frequency are:  \n")
    total = 0  #to calculate how many total words are there
    unique =0  #to calculate how many unqiue words are there finally
    for key,value in analyze_list:
        unique = unique + 1  #increment count of unique words
        print(key + ' - ' + str(value))
        total = total + int(value)  #calculates the total frequencies
        tokens_frequency.write(key + ' - ' + str(value) + '\n')
    tokens_frequency.write('The number of unique words in the abstract are :' + str(unique))
    print('The total number of words are :',total)
    print('the number of unique words are :',unique)

def main():
    final_analysis()

main()
