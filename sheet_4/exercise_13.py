import numpy as np
import pandas as pd
from exercise_12 import jackknife_estimation

#################################################################

def pi_sampling(N : int, d = 10):

    samples_df = pd.DataFrame(np.random.rand(N, d))
    norm_d = (samples_df**2).sum(axis=1)
    is_in_ball = norm_d < 1
    ns = is_in_ball.astype(int)

    pi_est = (2**10 * 120 * ns.sum()/N)**(1/5)

    print(f"Estimated PI for N = {N} is :", pi_est)
    return pi_est


#_ = pi_sampling(N = 10000)

#################################################################

def blocking(data, numbers, Nb):
    """
    blocking function from Prof. Sexty
    """
    out = [np.mean(data[i*Nb : (i+1) * Nb]) for i in range( int(len(numbers) / Nb ))]
    return out

def classical_error(N : int, N_samp : int):

    N_raw = np.arange(N)
    N_b = int(N / N_samp)

    N_blocks = blocking(N_raw, N_raw, N_b)

    pi_est = [pi_sampling(int(N_block)) for N_block in N_blocks]
    pi_est_average = np.mean(pi_est)
    pi_est_var = np.var(pi_est)
    print("---------------------------------------------------------------------------------")
    print(f"Estimated PI average from {N_samp} samples of total N = {N} is :", pi_est_average)
    print(f"Estiamted PI variance from {N_samp} samples of total N = {N} is :", pi_est_var)
    print("Error to PI :", abs(np.pi - pi_est_average))
    return pi_est_average, pi_est_var


#_ = classical_error(10000, 100)

#################################################################

def jackknife_error(N : int, N_samp : int):

    N_raw = np.arange(N)
    N_b = int(N / N_samp)

    N_blocks = blocking(N_raw, N_raw, N_b)

    pi_est = [pi_sampling(int(N_block)) for N_block in N_blocks]
    stats_jk = jackknife_estimation(np.mean, pi_est, 10)

    jk_est = stats_jk["jk_est"]
    error =  stats_jk["error"]
    average = stats_jk["average"]
    est_without_bias = stats_jk["est_without_bias"]


    print("---------------------------------------------------------------------------------")
    print("JK estimated", jk_est)
    print("JK Error ", error)
    print("Average", average)
    print("Estimated without Bias", est_without_bias)
    
    #print(f"Estimated PI average from {N_samp} samples of total N = {N} is :", pi_est_average)
    #print(f"Estiamted PI variance from {N_samp} samples of total N = {N} is :", pi_est_var)
    #print("Error to PI :", abs(np.pi - pi_est_average))
    return

jackknife_error(10000, 100)