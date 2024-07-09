import scipy.special as sc

def serial(seq:str = "0,1,1,0,0,1,1,1,0,1, 1,0,0,1,0,1,0,1,1,1, 0,1,1,0,1,0,1,1,1,0, 1,0,1,0,0,1,0,1,1,0.", alpha:float = 0.05, m: int = 3):
    if alpha >= 1 or alpha <= 0: 
        print("a")
        return 0, "Alpha has to be between 0 and 1.", 1, 1
    if m < 3:
        return 0, "M too small. Please send an appropriatly sized m.", 1, 1
    
    # cleaning the input
    seq = "".join(c for c in seq if c == '1' or c == '0')
    n = len(seq)

    # We choose 32  as the cut-
    # off point because log2(32) - 2 is 3,
    # the smallest m for which we can add m-3 bits to end of the sequence
    if n < 32:
        return 0, "Sequence too short. Please send a longer sequence.", 1, 1
    
    # calculate how big m can be, m <= log2(n) - 2
    max_m = -3
    n_log = 1
    while n_log <= n:
        n_log *= 2
        max_m += 1
    if m > max_m:
        return 0, "M too big. Please send an appropriatly sized m.", 1, 1
    
    # test 1
    seq = seq + seq[0:m - 3]
    m -= 2
    psi_2 = 0
    for i in range(0, pow(2, m)):
        frequency = 0
        for j in range(0, n):
            if i == int(seq[j:j + m], 2):
                frequency += 1
        frequency *= frequency
        frequency = (frequency * 1.0) / (n * 1.0)
        psi_2 += frequency
    psi_2 *= pow(2, m)
    psi_2 -= n

    # test 2
    m += 1
    seq += seq[m - 2]
    psi_1 = 0
    for i in range(0, pow(2, m)):
        frequency = 0
        for j in range(0, n):
            if i == int(seq[j:j + m], 2):
                frequency += 1
        frequency *= frequency
        frequency = (frequency * 1.0) / (n * 1.0)
        psi_1 += frequency
    psi_1 *= pow(2, m)
    psi_1 -= n

    # test 3
    m += 1
    seq += seq[m - 2]
    psi_0 = 0
    for i in range(0, pow(2, m)):
        frequency = 0
        for j in range(0, n):
            if i == int(seq[j:j + m], 2):
                frequency += 1
        frequency *= frequency
        frequency = (frequency * 1.0) / (n * 1.0)
        psi_0 += frequency
    psi_0 *= pow(2, m)
    psi_0 -= n
    
    stat_0 = psi_0 - psi_1
    stat_1 = psi_0 - 2 * psi_1 + psi_2

    p_val1 = sc.gammainc(stat_0 / 2, pow(2, m - 2))
    p_val2 =  sc.gammainc(stat_1 / 2, pow(2, m - 3))
    print(p_val1, p_val2)
    if p_val1 <= alpha and p_val2 > alpha:
        return 0, "P-value1 is not greater than alpha, the Sequence is not pseudo-random for a significance level of {}".format(alpha), p_val1, p_val2
    if p_val2 <= alpha and p_val1 > alpha:
        return 0, "P-value2 is not greater than alpha, the Sequence is not pseudo-random for a significance level of {}".format(alpha), p_val1, p_val2
    if p_val1 <= alpha and p_val2 <= alpha:
        return 0, "The p-values are not greater than alpha, the Sequence is not pseudo-random for a significance level of {}".format(alpha), p_val1, p_val2
    if p_val1 > alpha and p_val2 > alpha:
        return 1, "The sequence is pseudo-random for a significance level of {}".format(alpha), p_val1, p_val2

    return 1, "all good chief", p_val1, p_val2
