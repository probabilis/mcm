import numpy as np
import random
import math
import matplotlib.pyplot as plt

#################################################

def mean_std_error(numbers):
    mean = sum(numbers) / len(numbers)
    squared_diff = [(x - mean) ** 2 for x in numbers]
    std_dev = math.sqrt(sum(squared_diff) / (len(numbers) - 1))
    std_error = std_dev / math.sqrt(len(numbers))
    return mean, std_error

def generate_uniform_samples(n):
    return [random.uniform(0, 1) for _ in range(n)]

def test_uniform_distribution(k, k_prime):

    #uniformed gerenated samples from random.uniform module
    numbers = generate_uniform_samples(10000)
    
    #Calculating <x^k>
    x_k_values = [x**k for x in numbers]
    mean_x_k, std_error_x_k = mean_std_error(x_k_values)
    
    #Calculating <x^k * x'^k'>
    x_k_x_prime_k_prime_values = [x**k * numbers[i+1] ** k_prime for i, x in enumerate(numbers[:-1])]
    mean_x_k_x_prime_k_prime, std_error_x_k_x_prime_k_prime = mean_std_error(x_k_x_prime_k_prime_values)
    
    # Calculating expected values based on the formulas
    expected_xk = 1 / (k + 1)
    expected_x_k_x_prime_k_prime = 1 / (k + 1) * 1 / (k_prime + 1)
    
    print(f"For k = {k}:")
    print(f"Expected <x^k>: {expected_x_k}")
    print(f"Calculated <x^k>: {mean_x_k} ± {std_error_x_k}")
    
    print(f"\nFor k' = {k_prime}:")
    print(f"Expected <x^k * x'^k'>: {expected_x_k_x_prime_k_prime}")
    print(f"Calculated <x^k * x'^k'>: {mean_x_k_x_prime_k_prime} ± {std_error_x_k_x_prime_k_prime}")

# Test for k = 1 and k' = 1
test_uniform_distribution(1, 1)