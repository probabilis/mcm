import sys

print( sys.float_info )

def calc_beta(T):
    k_B = 1.380649 * 10E-23 #m2 kg s-2 K-1
    return 1/(k_B * T)

beta_max = calc_beta(0.00000000000001) #7 * 10E35
print("beta max:", beta_max)
beta_min = calc_beta(10000000000) #70 * 10E10
print("beta min:", beta_min)

beta_min = 10E+10 ; beta_max = 10E+100

delta_beta = (beta_max - beta_min) / 100000
print("db", delta_beta)