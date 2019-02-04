#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb  4 09:55:15 2019

@author: ricardo assis
"""
ip = []
num = 168

while num is not 0:
    rep = num%2
    num = num //2
    ip.append(rep)
    
ip.reverse()
print(ip)  


    
    