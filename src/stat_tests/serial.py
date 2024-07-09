def serial(seq:str, alpha:float, m: int):
    if alpha >= 1 or alpha <= 0: 
        print("a")
        return 0, "Alpha has to be between 0 and 1."
    if m < 3:
        return 0, "M too small. Please send an appropriatly sized m."
    
    # cleaning the input
    seq = "".join(c for c in seq if c == '1' or c == '0')
    n = len(seq)

    # We choose 32  as the cut-
    # off point because log2(32) - 2 is 3,
    # the smallest m for which we can add m-3 bits to end of the sequence
    if n < 32:
        return 0, "Sequence too short. Please send a longer sequence."
    
    # calculate how big m can be, m <= log2(n) - 2
    max_m = -3
    n_log = 1
    while n_log <= n:
        n_log *= 2
        max_m += 1
    if m > max_m:
        return 0, "M too big. Please send an appropriatly sized m."
     
    
    return 1, "all good chief"