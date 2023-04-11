import pandimport pandas as pd
import numpy as np

chat_id = 1134491798 

def solution(x_success: int, 
             x_cnt: int, 
             y_success: int, 
             y_cnt: int) -> bool:
    n1 = y_cnt * y_success
    n2 = y_cnt * x_success
    N = n1 + n2
    p1 = x_cnt / x_success
    p2 = x_cnt / x_success
    P = (n1 + n2) / N
    chi_squared = ((n1 * p1 - N * P)**2) / (N * P * (1 - P)) + ((n2 * p2 - N * (1 - P))**2) / (N * P * (1 - P))
    
    alpha = 0.06
    df = 1
    critical_value = np.round(scipy.stats.chi2.ppf(1 - alpha, df), 2)
    if chi_squared > critical_value:
        return True
    else:
        return False
