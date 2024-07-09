
import math

def autocorrelation(bitstr:str, alpha:float, d: int):
    
    l = [0 if ch == '0' else 1 for ch in bitstr.strip()]
    n = len(l)
    e = [0 for i in range(n-d)]
    
    sum = 0
    for i in range(n-d):
        e[i] = l[i] ^ l[i + d]
        sum += e[i]
    
    s_obs = 2 * sum - n + d
    s_obs = abs(s_obs)/math.sqrt(n-d)
    
    p_val = math.erfc(s_obs/math.sqrt(2))
    
    return p_val
    
    
    