#!/usr/bin/python3

import math



# function takes a list as input and calculates some observable
# dataset is a list with the data
#jkn is the number of jackknife samples, i.e. blocksize: N_b=len(dataset)/jkn
# if #data is not divisible by jkn, then some data is discarded
#returns: jkarr[0] is the jackknife estimate
# jkarr[1] is the error
# jkarr [2] is the average of resarr[1:]
# jkarr[3] is the estimate without bias correctio
def jackknife_estimation(function,rawdataset,jkn=10):
#this line is needed to make it work for numpy arrays
    dataset=[x for x in rawdataset]
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


  # resarr[0] is evaluated on the whole sample
# resarr[i], i>0 is evaluated on a sample such that the i-th subsample is left out.
#output: jkarr[0] is the jackknife estimate
# jkarr[1] is the error
# jkarr [2] is the average of resarr[1:]
# jkarr[3] is the estimate without bias correction
def calc_jackknife( resarr):
  fakt =  float(len(resarr)-2)/float(len(resarr)-1)
  thetap = float(0.0)
  sigma= float(0.0)
  for i in range(1,len(resarr)):
      thetap+=float(resarr[i])
  thetap/=float(len(resarr)-1)
  for i in range(1,len(resarr)):    
      sigma+=math.pow(thetap-float(resarr[i]),2)
  sigma*=fakt  
  jkarr=[None]*4
  jkarr[1]=math.sqrt(float(sigma))
  jkarr[0]=resarr[0] - float(len(resarr)-2)*(thetap-float(resarr[0]))
  jkarr[3]=thetap
  jkarr[2]=resarr[0]
  return jkarr
