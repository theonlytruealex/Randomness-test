
import math

def autocorrelation(bitstr:str, alpha:float, d: int):
    
    l = [0 if ch == '0' else 1 for ch in bitstr.strip()]
    print("sequence: ", l)
    n = len(l)
    e = [0 for i in range(n-d)]
    print("n: ", n)
    
    sum = 0
    for i in range(n-d):
        e[i] = l[i] ^ l[i + d]
        sum += e[i]
    
    print("e: ", e)
    s_obs = 2 * sum - n + d
    print("S_nd: ", s_obs)
    s_obs = abs(s_obs)/math.sqrt(n-d)
    print("s_obs: ", s_obs)
    
    p_val = math.erfc(s_obs/math.sqrt(2))
    
    p_val = int(p_val * 1000)/1000;
    
    return p_val
    
    
    