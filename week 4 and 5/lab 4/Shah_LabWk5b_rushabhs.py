#Author: Rushabh Shah
#Originalk creation date: 04/19/2017
#Last modification date: 04/21/2017
#Description: this program performs webscraping on a website and uses beautifulsoup and nltk library to find all the unique tags in the soup ouput, all the hyperlinks and tokenize all words.

import requests
from bs4 import BeautifulSoup
import nltk
r = requests.get('http://www.bigrigg.net')
print(r.text)
print()
print()
soup = BeautifulSoup(r.text, 'html.parser') #convert request object to BeautifulSoup object
print('The prettified version is of the HTML source code is: ')
print(soup.prettify)  #displays the prettified version of soup
t = set()  #create set

#this for loop, prints all the tags in sequence and also prints all the unique tags just to have a better idea about the unique tags and all the tags in HTML source code
for tag in soup.find_all():  #to loop throughall lines 
    #to add all unique tags have used set
    print(tag.name)  #prints all the tag names
    t.add(tag.name)  #adds tag names to set, just to add all the unique tags 
print('The unique tags in the html doc are: ')
print(t)  #just to print unique tags
print()


href_list = []

#this funciton prints the hyperlinkes without the text and displays hyperlinks as list
def print_list():
    print('Printing hyperlink as lists: ')
    print()
    for link in soup.find_all('a'):  #finds all the lines from soup which has 'a' in it
        if link.has_attr('href'):  #if link has attribute href in it, means it has hyperlink then append the value for href attribute to ths href_list
            href_list.append(link.get('href'))  #this line appends hyperlinks value for the href attribute to the hyperlink to the href_list
    print(href_list)
    print()
  
#this funciton prints the hyperlinkes without the text and displays hyperlinks as strings
def print_string():
    print('Printing hyperlink as strings: ')
    print()
    for hyperlinks in soup.find_all('a'):  #finds all the lines from soup which has 'a' in it
        href_list.append(hyperlinks.get('href') + '\n')  #this line appends hyperlinks value for the href attribute to the hyperlink to the href_list 
    s = ''.join(href_list)  #since we need to display the hyperlinks of the tags as string, converting list into a string by using ''.join
    print(s)

#this function calls other functions and tokenizes the text of soup object    
def main():
    print_list()
    print_string()
    tokenwords = nltk.word_tokenize(soup.get_text())  #nltk.word_tokenize will return list of tokenized words and saves it in list tokenwords
    print('Tokenized words')
    print()
    print(tokenwords)  #print thelist of tokenized words
    print('___________________________________________________________________________')
    print('Tokenized words after spit')
    print()
    print(soup.get_text().split())  #print the list of tokenized words after splitting it

main()
