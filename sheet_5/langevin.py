# -*- coding: utf-8 -*-
"""
Created on Mon Dec  7 17:17:28 2020

@author: Denes Sexty
"""
import numpy as np
import matplotlib.pyplot as plt

#global badcount

import math

# resarr[0] is evaluated on the whole sample
# resarr[i], i>0 is evaluated on such that the i-th subsample is left out.
#output: jkarr[0] is the jk estimate
# jkarr[1] is the error
# jkarr [2] is the average of resarr[1:]
#jkarr[3] is the estimate without bias correction
def calc_jackknife( resarr):
  fakt =  float(len(resarr)-2)/float(len(resarr)-1)
  thetap = float(0.0)
  sigma= float(0.0)
  for i in range(1,len(resarr)):
      thetap+=float(resarr[i])
      sigma+=math.pow(float(resarr[0])-float(resarr[i]),2)
  sigma*=fakt  
  thetap/=float(len(resarr)-1)
  jkarr=[None]*4
  jkarr[1]=math.sqrt(float(sigma))
  jkarr[0]=resarr[0] - float(len(resarr)-2)*(thetap-float(resarr[0]))
  jkarr[3]=thetap
  jkarr[2]=resarr[0]
  return jkarr


# function takes a list as input and calculates some observable
# dataset is a list with the data
#jkn is the number of jackknife samples
# if #data is not divisible by jkn, than some data is discarded
def jackknife_estimation(function,dataset,jkn=10):
    datan=len(dataset)
    newn=datan
    if (datan % jkn):
        newn=int(datan/jkn)*jkn
        del dataset[newn:]
    subn=int(newn/jkn)
    resarr=[None]*(jkn+1)
    resarr[0]=function(dataset)
    for i in range(1,jkn+1):
        mydataset=dataset[0:(i-1)*subn]+dataset[i*subn:]
        resarr[i]=function(mydataset)
    return calc_jackknife(resarr)





def Langevin_update(x,deltatau,noiseamp):
    newx=x+(2.0/x-x)*deltatau + np.random.normal(scale=noiseamp)
    global badcount
    if (newx<0.0): 
        badcount+=1
        return x
    return newx



def Langevin_evol(x0,deltatau,tmax,therm=None):
    x=x0
    tau=0
    xarray=[]
    noiseamp=np.sqrt(2.0*deltatau)
    while True:
        x=Langevin_update(x,deltatau,noiseamp)
        if (therm==None): xarray.append(x)
        else: 
            if tau>= therm: xarray.append(x)
        tau+=deltatau
        if (tau>tmax): break
    plt.plot(xarray)
    plt.show()
    return xarray
    

badcount=0

runs=[]
taumax=200

dtaus=[0.03,0.01,0.003,0.001]
dtsqr=[x*x for x in dtaus]
xavr=[]
xerr=[]

for dtau in dtaus:  
  runs=[]
  for i in range(200):
     runs.append(np.mean(Langevin_evol(0.1,dtau,taumax,therm=10.0)))
     # for lloking at langevin time evolution 
     # runs.append(Langevin_evol(0.1,dtau,taumax,therm=10.0))
  jkres=jackknife_estimation(np.mean,runs,jkn=100)
  xavr.append(jkres[0])
  xerr.append(jkres[1])
  
plt.errorbar(dtaus,xavr,xerr)
plt.show()



