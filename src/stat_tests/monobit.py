import gui_sketch
import tkinter
import tkinter.messagebox
import customtkinter
 
def monobit(self, input_frame):
    try:
        sigLvl = float(self.sigLvlEntry.get().strip())
    except ValueError as e:
        self.errorLabel = customtkinter.CTkLabel(input_frame,
                                        text="The data you entered does not have the correct format.\n Retry!\n")
        self.errorLabel.grid(row=5, column=1,
                            padx=20, pady=20,
                            sticky="ew")
        self.sigLvlEntry.delete(0, customtkinter.END)
        self.bitSeqEntry.delete(0, customtkinter.END)

    bitSeq = self.bitSeqEntry.get().strip()
    for i in bitSeq:
        pass