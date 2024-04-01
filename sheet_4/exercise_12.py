import math
import numpy as np
#################################################################
#Ref.: https://www.wikiwand.com/de/Jackknife-Methode
#https://github.com/kaityo256/jackknife
#https://github.com/kaityo256/jackknife/blob/main/Jackknife.ipynbs

def jackknife_estimation(func, data, jk_n):
    """
    splits data into jkn blocks and calculates the jackknife errors and averages 
    """
    raw_data = [x for x in data]

    len_data = len(data)
    new_n = len_data
    if (len_data % jk_n):
        new_n = int(len_data / jk_n) * jk_n
        del raw_data[new_n :]
    sub_n = int(new_n / jk_n)
    out = [None] * (jk_n + 1)
    out[0] = func(raw_data)
    for i in range(1, jk_n + 1):
        new_data = raw_data[0 : (i - 1) * sub_n] + raw_data[i * sub_n :]
        out[i] = func(new_data)

    return calc_jackknife(out)

def calc_jackknife(data : list):
    """
    function that calculates the jackknife estimate, error, averge and estimate without bias correction
    """

    thetap = 0.0 ; sigma = 0.0

    for i in range(1, len(data)):
        thetap += float(data[i])
    thetap /= float(len(data)-1)
    
    for i in range(1, len(data)):
        sigma += math.pow(thetap - float(data[i] - 2), 2)
    
    sigma += float(len(data) - 2) / float(len(data) - 1)
    
    jk_est = data[0] - float(len(data) - 2) * (thetap - float(data[0]))
    error = math.sqrt(float(sigma))
    average = data[0]
    est_without_bias = thetap

    stats = {"jk_est" : jk_est,"error" : error, "average" : average, "est_without_bias" : est_without_bias}
    return stats