# -*- coding: utf-8 -*-
"""
Created on Fri Jul 21 19:58:13 2017

@author: Rush
"""
#Communicate with google and openweather api in the pytho application
import requests
import urllib.parse
from pprint import pprint  #print json data in a good way
def main():
    topic()
    google_map()
    
    
def topic():
    city = 'New York'
    response = requests.get("http://api.openweathermap.org/data/2.5/weather?q="+city+"&appid=366edc656c6f5640b0dd0bad7cccdeba")
    weather = response.json()  #fetch json data and unpack it into weather
    pprint(weather)  #print json response in a pretty way
    print('The temperature is: ',weather['main']['temp'])
    print('The description is :', weather['weather'][0]['description'])
    
 
def google_map():
    api = 'http://maps.googleapis.com/maps/api/geocode/json?'
    address = 'lhr'  #London
    url = api + urllib.parse.urlencode({'address':address})  #add address to the api, urlencode takes care of space and everythig, eg: San Jose
    json_data = requests.get(url).json()
    #pprint(json_data)
    json_status = json_data['status']
    if json_status == 'OK':
        print('The API status s ',json_status)
        formatted_address = json_data['results'][0]['formatted_address']
        print('The formatted address is: ',formatted_address)#we want the address in a proper format
        #extract long name for all the address components ;which is a list
        print('The components of the formatted address are')
        for each in json_data['results'][0]['address_components']:
            print(each['long_name'])
                                      
                                      
main()