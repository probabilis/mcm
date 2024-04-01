# -*- coding: utf-8 -*-
"""
Created on Fri Nov  5 20:02:50 2021

@author: denes
"""

import numpy as np
import os
import matplotlib.pyplot as plt


def avr(numbers):
    sum=0.0
    for x in numbers:
        sum+=x
    return sum/len(numbers)

def variance(numbers):
    sum2=0.0
    xbar=avr(numbers)
    for x in numbers:
        sum2+=(x-xbar)*(x-xbar)
    return sum2/(len(numbers)-1)  
    
def avrwerr(numbers):
    return [avr(numbers),np.sqrt(variance(numbers)/len(numbers))]

def blocking(numbers,Nb):
    newarr=[avr(data[i*Nb:(i+1)*Nb])   for i in range(int(len(numbers)/Nb))    ]
    return newarr


data=[]
F=open("datafile.txt","r")
for line in F:
    data.append(float(line))
   
#data=np.random.rand(100000)   
   
