# -*- coding: utf-8 -*-
"""
Created on Sun Aug 13 02:30:44 2017

@author: Rush
"""

newuser = input("input username")
file = open("names.txt", "a+") #opening file that stores usernames
file.write("\n" + newuser)
file.close()
newpass = input("input password")
#opening password file
file = open("passwords.txt", "a+")
file.write("\n" + newpass) #writing password to file   
file.close()
print("account created")