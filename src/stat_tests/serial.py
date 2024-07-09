def serial(seq:str, alpha:float, m: int):
    if alpha >= 1 or alpha <= 0: 
        print("a")
        return 0, "alpha has to be between 0 and 1"
    print(seq)
    seq = "".join(c for c in seq if c == '1' or c == '0')
    print(seq)
    n = len(seq)
    if n < 2:
        return 0, "please send a longer sequence"
    
    # calculate how big m can be, m <= log2(n) - 2
    max_m = -3
    n_log = 1
    while n_log <= n:
        n_log *= 2
        max_m += 1
    if m > max_m:
        return 0, "please send an appropriate m"
    return 1, "all good chief"