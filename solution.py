from scipy import stats
import pandas as pd
import numpy as np

chat_id = 1134491798 

def solution(x_success: int, x_cnt: int, y_success: int, y_cnt: int, alpha: float = 0.06) -> bool:
    p1 = x_success / x_cnt
    p2 = y_success / y_cnt
    p_combined = (x_success + y_success) / (x_cnt + y_cnt)
    difference = p1 - p2
    z_value = difference / (p_combined * (1 - p_combined) * (1/x_cnt + 1/y_cnt)) ** 0.5
    p_value = 1 - stats.norm.cdf(z_value)
    return p_value < alpha
x_success = 1000
x_cnt = 3000
y_success = 5000
y_cnt = 6400
print(solution(x_success, x_cnt, y_success, y_cnt))
