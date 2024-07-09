import numpy as np
import tkinter
from tkinter import messagebox
import customtkinter
import monobit
import mbit
import autocorrelation
import serial
import runs
import numpy as np
from scipy.special import erfc

def runs(seq:str, alpha:float):
    if alpha >= 1 or alpha <= 0: 
        return "Alpha has to be between 0 and 1."

    n = len(seq)
    n_1 = seq.count("1")
    
    # the proportion of "1" in the binary sequence
    ratio = float (n_1 / n)

    # testing monobit
    # if the test fails, then the algorithm stops
    nr1 = abs(ratio - 0.5)
    nr2 = float (2 / np.sqrt(n))

    if nr1 >= nr2:
        return "Monobit test failed, the sequence is NOT pseudorandom."

    # the number of "gaps" and "blocks"
    stat = 1
    for i in range(0, n-1):
        if seq[i] != seq[i + 1]:
            stat = stat + 1

    # to ignore division by zero warning
    np.seterr(divide='ignore', invalid='ignore')

    a = stat - 2 * n * ratio * (1 - ratio) 
    b = 2 * np.sqrt(2 * n) * ratio * (1 - ratio)
    p_value = erfc(a / b)

    if p_value > alpha:
        return "All good chief, the sequence is pseudorandom."

    return "Test failed, the sequence is NOT pseudorandom."
    

