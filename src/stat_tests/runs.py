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

def runs(self, seq:str, alpha:float):

    if all(char in {'0', '1'} for char in seq) == False:
        messagebox.showerror("Error", "Please enter a valid integer for Bit Sequence.")
        return
    
    n = len(seq)
    n_1 = seq.count("1")
    
    # the proportion of "1" in the binary sequence
    ratio = float (n_1 / n)

    # testing monobit
    # if the test fails, then the algorithm stops
    nr1 = abs(ratio - 0.5)
    nr2 = float (2 / np.sqrt(n))

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

    for widgets in self.main_frame.winfo_children():
        widgets.destroy()
    output_frame = customtkinter.CTkFrame(self.main_frame, corner_radius=0, fg_color="transparent")
    output_frame.grid(row=0, column=0, rowspan=2, columnspan=5, pady=20,  sticky="nsew")
    output_frame.grid_columnconfigure((1, 2, 3, 4, 5), weight=1)
    out = "Null Hypothesis (H0):\nThe generated binary sequence is pseudo-random\n"
    out += "Alternative Hypothesis (HA):\nThe generated binary sequence is not pseudo-random\n\n"
    out += "Significance level: " + str(alpha) + "\n\n"
    out += "P-value: " + str(p_value) + "\n\n"
    result = ""
    if nr1 >= nr2:
        out += "The monobit test failed, therefore the Runs algorithm stops.\n\n"
        result += "H0 is rejected\nHA is accepted"
    else:
        if alpha < p_value:
            out += "The sequence is pseudo-random for a significance level of\n{}\n\n".format(alpha)
            result += "H0 is accepted\nHA is rejected"
        else:
            out += "P-value is not greater than alpha.\nThe Sequence is not pseudo-random for a significance level of\n{}\n\n".format(alpha)
            result += "H0 is rejected\nHA is accepted"
    
    # afisare
    resultLabel = customtkinter.CTkLabel(output_frame,
                                        font=customtkinter.CTkFont(size=17, weight="normal"),
                                        text=out)
    resultLabel.grid(row=4, column=3,
                            padx=20, pady=20,
                            sticky="ew")
    final_resultLabel = customtkinter.CTkLabel(output_frame, fg_color="blue", 
                                        font=customtkinter.CTkFont(size=25, weight="normal"),
                                        text=result)
    final_resultLabel.grid(row=10, column=3,
                            padx=20, pady=20,
                            sticky="ew")
    

