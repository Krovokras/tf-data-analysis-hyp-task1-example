import pandas as pd
import numpy as np
from scipy.stats import norm

chat_id = 1134491798 # Ваш chat ID, не меняйте название переменной

def solution(x_success: int, 
             x_cnt: int, 
             y_success: int, 
             y_cnt: int) -> bool:
  
    p1 = x_success / x_cnt
    p2 = y_success / y_cnt
    
   
    se = np.sqrt(p1*(1-p1)/x_cnt + p2*(1-p2)/y_cnt)
    
   
    z = (p1 - p2) / se
    
   
    p_value = norm.sf(abs(z))*2
    
   
    if p_value < 0.06:
        return True
    else:
        return False
