import gui_sketch
import tkinter
import tkinter.messagebox
import customtkinter
import math
 
def monobit(self, input_frame):
    bitSeq = self.bitSeqEntry.get().strip()
    sigLvlText = self.sigLvlEntry.get().strip()
    ok = 0
    try:
        alpha = float(sigLvlText)
    except ValueError as e:
        ok = 1
    # check if the input is a bit sequence
    for ch in bitSeq:
        if ch != '1' and ch != '0':
            ok = 1
            break
    if ok == 1:
        self.errorLabel = customtkinter.CTkLabel(input_frame,
                                        text="The data you entered does not have the correct format.\n Retry!\n")
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
    out_text += "Significance level: " + sigLvlText + "\n\n"
    out_text += "Binary Sequence: " + bitSeq + "\n\n"
    n = 0
    s = 0
    for ch in bitSeq:
        n = n + 1
        s = s + int(ch)
    s = s - n
    s = abs(s) / math.sqrt(n)
    out_text += "The test's statistic: " + str(s) + "\n\n"
    p_value = math.erfc(s / math.sqrt(2))
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