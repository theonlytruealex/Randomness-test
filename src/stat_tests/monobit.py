import gui_sketch
import tkinter
import tkinter.messagebox
import customtkinter
 
def monobit(self, input_frame):
    bitSeq = self.bitSeqEntry.get().strip()
    sigLvlText = self.sigLvlEntry.get().strip()
    try:
        sigLvl = float(sigLvlText)
    except ValueError as e:
        self.errorLabel = customtkinter.CTkLabel(input_frame,
                                        text="The data you entered does not have the correct format.\n Retry!\n")
        self.errorLabel.grid(row=5, column=1,
                            padx=20, pady=20,
                            sticky="ew")
        self.sigLvlEntry.delete(0, customtkinter.END)
        self.bitSeqEntry.delete(0, customtkinter.END)
        
    for widgets in self.main_frame.winfo_children():
        widgets.destroy()
    output_frame = customtkinter.CTkFrame(self.main_frame, corner_radius=0, fg_color="transparent")
    output_frame.grid(row=0, column=0, rowspan=2, columnspan=5, pady=20,  sticky="nsew")
    output_frame.grid_columnconfigure((1, 2, 3, 4, 5), weight=1)
    out_text = "Null Hypothesis (H0): The generated binary sequence is pseudo-random\n"
    out_text += "Alternative Hypothesis (HA): The generated binary sequence is not pseudo-random\n"
    out_text += "Significance level: " + sigLvlText + "\n"
    out_text += "Binary Sequence: " + bitSeq + "\n"

    textBox = customtkinter.CTkTextbox(output_frame)
    textBox.insert('end', out_text)