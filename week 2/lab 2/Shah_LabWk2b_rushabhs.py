# -*- coding: utf-8 -*-
"""
Created on Tue Mar 28 20:09:15 2017

@author: Rush
"""

#from bs4 import BeautifulSoup
import requests
r = requests.get('http://www.bigrigg.net')
#print(r)
from bs4 import BeautifulSoup
soup = BeautifulSoup(r.text, 'html.parser') #convert request object to BeautifulSoup object
print(soup.prettify)
