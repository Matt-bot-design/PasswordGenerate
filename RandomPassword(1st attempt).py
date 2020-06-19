# -*- coding: utf-8 -*-
"""
Created on Thu Jun 18 22:24:08 2020

@author: Matthew Davids
"""


import random
import string

def password_gen(length):
    # string.digits contains numbers and they are strings
    charac = string.ascii_letters + string.digits 
    # string.ascii_letters is concatenation of the lowercase and uppercase constants
    psw = "" 
    # empty variable psw

    for i in range(length): # iterating over the range of the password from length
        psw += random.choice(charac) #assigning psw to random choice of characters
        # So it will add random strings to psw variable
    print("Password: " + psw)
    # It will print out the random characters of uppercase, lowercase and digits 
    