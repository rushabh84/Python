# -*- coding: utf-8 -*-
"""
Created on Sun Jul 16 21:45:17 2017

@author: Rush
"""

import requests
from bs4 import BeautifulSoup
page = requests.get('http://appft.uspto.gov/netacgi/nph-Parser?Sect1=PTO2&Sect2=HITOFF&u=%2Fnetahtml%2FPTO%2Fsearch-adv.html&r=0&p=1&f=S&l=50&Query=aanm%2F%22carnegie+mellon%22+AND+PD%2F4%2F1%2F2016-%3E6%2F30%2F2016&d=PG01')
r = requests.get('https://api.github.com/events')   #r is response object

variables = {'name':'Rush', 'last':'Shah'}                
r2 = requests.post('http://httpbin.org/get', params= variables)
print('The details for the response object r2 are:')
print(page.url)
#print(r2.text)
#print(page.status_code == requests.codes.ok)
print((page.headers))
#print(r.json())
#print(r2.encoding)
contents = page.content
#print(contents)


#BeautifulSoup
soup = BeautifulSoup(page.text, 'html.parser')
print(type(soup.html.parent))
print(soup.string)  #since there are multiple strings and it doesn't know which one to refer, it returns none
print('*****************************************************')
#print(soup.get_text())
print(soup.find('a').attrs)
print('*****************************************************')
#print(soup.prettify())
for tag in soup.find_all(True):
    print(tag.name)