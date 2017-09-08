#Author: Rushabh Shah
#Original creation date: 04/ 25/ 2017
#Last modification date: 04/27/2017
#Description: This program performs web-scraping on a url and extracts all the urls from the master website using looping. Then performs scraping on each url and
             #extracts abstract for each of the website and stores in an external text file and prints the abstract on the monitor

import requests
from bs4 import BeautifulSoup
import nltk

r = requests.get('http://appft.uspto.gov/netacgi/nph-Parser?Sect1=PTO2&Sect2=HITOFF&u=%2Fnetahtml%2FPTO%2Fsearch-adv.html&r=0&p=1&f=S&l=50&Query=aanm%2F%22carnegie+mellon%22+AND+PD%2F4%2F1%2F2016-%3E6%2F30%2F2016&d=PG01')
soup = BeautifulSoup(r.text, 'html.parser') #convert request object to BeautifulSoup object
#print(soup.prettify)  #displays the prettified version of soup
href_list = list()

#this function performs web scraping and extracts all urls from the response
def parse_soup():
    print()
    urlabs = list()  #list createdto store only the unique urls
    table = soup.find("table")

    #extracting urls using looping, only the ones inside the table tag have to be extracted (decided by observing the soup output)
    for row in table.findAll('a'):
        if row.has_attr('href'):  #if link has attribute href in it, means it has hyperlink then append the value for href attribute to ths href_list
            href_list.append('http://appft.uspto.gov' + row.get('href'))  #this line appends hyperlinks value for the href attribute to the hyperlink to the href_list
            

    #this for loop is to only store the unique urls, as for one website we get 2 corresponding urls, so using for loop to only store alternate urls in the new list
    #for loop from 0 to len(href_list) and increment by 2, so gets alterante and unique urls
    for i in range(0, len(href_list),2):
        urlabs.append(href_list[i])
    return urlabs

#this method loops through the elements of the list with 15 urls and perfroms web scraping on it and extracts abstract from each url and saves it in a text file
def parse_all(a):
    abstract = open('URL_Abstract.txt', 'w')  #open a file in write mode
    #perform web scraping for all the urls in list a
    print('The abstract for the 15 urls are as follows: ')
    print('*******************************************************************')
    for elements in a:
        r = requests.get(elements)
        soup = BeautifulSoup(r.text, 'html.parser')
        p = soup.findAll('p')  #returns a list of all p tags and the abstract is between the 2 pair of <p> </p>
        current_abstract = p[1].text  #there are 3 pairs of <p></p> tags but the 2 pair which will be at index 1 has abstract as text
        print(current_abstract)  #prints the abstract for all urls on the monitor
        abstract.write(current_abstract  + '\n')  #writes abstract for all the urls in the url_abstract.txt file
    print('*******************************************************************')
        
    
#main function is the one where all other functions are called
def main():
    urls = parse_soup()  #returns a list of all unique 15 urls and store it in urls
    parse_all(urls)  #calls parse_all method and pass urls as arguement
    
#call to main function
main()
    
