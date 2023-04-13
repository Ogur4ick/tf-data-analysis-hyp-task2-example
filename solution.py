import pandas as pd 
import numpy as np 
from scipy.stats import chisquare 
 
 
chat_id = 968976840 # Ваш chat ID, не меняйте название переменной 
 
def solution(x: np.array, y: np.array) -> bool: 
    n_intervals = 10 
    f_min = min(x.min(), y.min()) 
    f_max = max(x.max(), y.max()) 
    f_intervals = np.linspace(f_min, f_max, n_intervals+1) 
 
    
    hist_freq, _ = np.histogram(x, bins=f_intervals) 
    hist_freq = hist_freq / float(len(x)) 
    test_freq, _ = np.histogram(y, bins=f_intervals) 
    test_freq = test_freq / float(len(y)) 
 
    
    chisq, p_value = chisquare(test_freq, f_exp=hist_freq) 
    return p_value < 0.03
