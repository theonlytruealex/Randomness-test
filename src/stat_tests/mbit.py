import gui_sketch
import tkinter
import tkinter.messagebox
import customtkinter
import math
from scipy.special import gammainc, gammaincc
import numpy as np
 
def mbit(self, input_frame):
    alpha = self.alphaEntry.get().strip()
    bitSeq = self.bitSeqEntry.get().strip()
    #print(bitSeq)
    M_param = self.MEntry.get().strip()
    alpha = float(alpha)  # Convert alpha to float  
    #print(alpha)  
    M_param = int(M_param)  # Convert M_param to int
    #print(M_param)

    n = len(bitSeq) # number of bits
    nr_blocks = n // M_param  # number of blocks

    ok = 0
    ok_ch = 0
    if alpha >= 1: ok = 1
    if M_param < 0.1 * n: ok = 1
    
    # check if the input is a bit sequence
    for ch in bitSeq:
        if ch != '1' and ch != '0':
            ok = 1
            ok_ch = 1
            break

    reasons = ""
    if ok == 1:
        if M_param <= 0.1 * n:
            reasons += "!!! M < 0.1 * number of bits\n"
        if alpha >= 1:
            reasons += "!!! Wrong alpha, not in (0,1)\n"
        if ok_ch == 1:
            reasons += "!!! Wrong sequence of bits, only 0's and 1's allowed\n"

        self.errorLabel = customtkinter.CTkLabel(input_frame,
                text="The data you entered does not have the correct format.\n\n" + reasons + "\n Retry!\n")
        self.errorLabel.grid(row=5, column=1,
                            padx=20, pady=20,
                            sticky="ew")
        self.sigLvlEntry.delete(0, customtkinter.END)
        self.bitSeqEntry.delete(0, customtkinter.END)
        return
            
    for widgets in self.main_frame.winfo_children():
        widgets.destroy()
    output_frame = customtkinter.CTkFrame(self.main_frame, corner_radius=0, fg_color="transparent")
    output_frame.grid(row=0, column=0, rowspan=2, columnspan=5, pady=20,  sticky="nsew")
    output_frame.grid_columnconfigure((1, 2, 3, 4, 5), weight=1)
    out_text = "Null Hypothesis (H0):\nThe generated binary sequence is pseudo-random\n"
    out_text += "Alternative Hypothesis (HA):\nThe generated binary sequence is not pseudo-random\n\n"
    alpha_str = str(alpha)
    out_text += "Significance level (alpha): " + alpha_str + "\n\n"
    out_text += "Binary Sequence: " + bitSeq + "\n\n"


    stats = 0.0
    for i in range(nr_blocks):
        seq_current = bitSeq[i * M_param : (i + 1) * M_param]
        sum_current = 0.0
        for ch in seq_current:
            sum_current += int(ch)
        sum_current /= M_param

        sum_current -= 0.5

        stats += sum_current * sum_current
    
    chi_squared = stats    
    stats *= 4 * M_param

    p_value = gammainc(nr_blocks / 2, chi_squared / 2) 
    
    out_text += "The test's statistic: " + str(stats) + "\n\n"
    out_text += "P-value: " + str(p_value) + "\n\n"
    out_text += "Hypothesis check:\n"
    result = ""
    if alpha < p_value:
        out_text += "P-value > alpha\n\n"
        result += "H0 is accepted\nHA is rejected"
    else:
        out_text += "P-value < alpha\n\n"
        result += "H0 is rejected\nHA is accepted"
    resultLabel = customtkinter.CTkLabel(output_frame,
                                        font=customtkinter.CTkFont(size=17, weight="normal"),
                                        text=out_text)
    resultLabel.grid(row=4, column=3,
                            padx=20, pady=20,
                            sticky="ew")
    final_resultLabel = customtkinter.CTkLabel(output_frame, fg_color="red", 
                                        font=customtkinter.CTkFont(size=25, weight="normal"),
                                        text=result)
    final_resultLabel.grid(row=10, column=3,
                            padx=20, pady=20,
                            sticky="ew")