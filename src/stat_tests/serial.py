import scipy.special as sc
import gui_sketch
import tkinter
import tkinter.messagebox
import customtkinter

def serial_results(self, res: int, reasoning: str, p_value1: float = 0, p_value2: float = 0, alpha: float = 0):
    for widgets in self.main_frame.winfo_children():
        widgets.destroy()
    if res != -1:
        output_frame = customtkinter.CTkFrame(self.main_frame, corner_radius=0, fg_color="transparent")
        output_frame.grid(row=0, column=0, rowspan=2, columnspan=5, pady=20,  sticky="nsew")
        output_frame.grid_columnconfigure((1, 2, 3, 4, 5), weight=1)
        out_text = "Null Hypothesis (H0):\nThe generated binary sequence is pseudo-random\n"
        out_text += "Alternative Hypothesis (HA):\nThe generated binary sequence is not pseudo-random\n\n"
        out_text += "Significance level: " + str(alpha) + "\n\n"
        out_text += "P-values: " + str(p_value1) + " and " +  str(p_value2) + "\n\n"
        out_text += reasoning
        if res == 0:
            out_text += "H0 is rejected\nHA is accepted"
        else:
            out_text += "H0 is accepted\nHA is rejected"
    else:
        output_frame = customtkinter.CTkFrame(self.main_frame, corner_radius=0, fg_color="red")
        output_frame.grid(row=0, column=0, rowspan=2, columnspan=5, pady=20,  sticky="nsew")
        output_frame.grid_columnconfigure((1, 2, 3, 4, 5), weight=1)
        out_text = reasoning
    resultLabel = customtkinter.CTkLabel(output_frame,
                                        font=customtkinter.CTkFont(size=17, weight="normal"),
                                        text=out_text)
    resultLabel.grid(row=4, column=3,
                            padx=20, pady=20,
                            sticky="ew")

def serial(self, seq: str, alpha: float, m: int):
    if alpha >= 1 or alpha <= 0:
        serial_results(self, -1, "Alpha has to be between 0 and 1.")
        return
    if m < 3:
        serial_results(self, -1, "M too small. Please send an appropriatly sized m.")
        return
    
    # cleaning the input
    seq = "".join(c for c in seq if c == '1' or c == '0')
    n = len(seq)

    # We choose 32  as the cut-
    # off point because log2(32) - 2 is 3,
    # the smallest m for which we can add m-3 bits to end of the sequence
    if n < 32:
        serial_results(self, -1, "Sequence too short. Please send a longer sequence.")
        return
    
    # calculate how big m can be, m <= log2(n) - 2
    max_m = -3
    n_log = 1
    while n_log <= n:
        n_log *= 2
        max_m += 1
    if m > max_m:
        serial_results(self, -1, "M too big. Please send an appropriatly sized m.")
        return
    
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
        serial_results(self, 0,
                       "P-value1 is not greater than alpha.\nThe Sequence is not pseudo-random for a significance level of\n{}\n\n".format(alpha), \
                        p_val1, p_val2, alpha)
    elif p_val2 <= alpha and p_val1 > alpha:
        serial_results(self, 0,
                       "P-value2 is not greater than alpha.\nThe Sequence is not pseudo-random for a significance level of\n{}\n\n".format(alpha), \
                        p_val1, p_val2, alpha)
    elif p_val1 <= alpha and p_val2 <= alpha:
        serial_results(self, 0,
                       "The p-values are not greater than alpha.\nThe Sequence is not pseudo-random for a significance level of\n{}\n\n".format(alpha), \
                        p_val1, p_val2, alpha)
    elif p_val1 > alpha and p_val2 > alpha:
        serial_results(self, 1, "The sequence is pseudo-random for a significance level of\n{}\n\n".format(alpha), p_val1, p_val2)
    else:
        serial_results(self, 1, "Logical impossiblity, all's not good chief", p_val1, p_val2)
    return
