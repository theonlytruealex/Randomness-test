import gui_sketch
import tkinter
import tkinter.messagebox
import customtkinter
 
def serial(self):

    # Length Label
    self.lenLabel = customtkinter.CTkLabel(self,
                                    text="Sequence Length")
    self.lenLabel.grid(row=0, column=1,
                        padx=20, pady=10,
                        sticky="ew")

    # Length Field
    self.lenEntry = customtkinter.CTkEntry(self,
                        width=200)
    self.lenEntry.grid(row=0, column=2,
                        columnspan=3, padx=20,
                        pady=10, sticky="ew")
    
    # Bit Sequence Label
    self.bitSeqLabel = customtkinter.CTkLabel(self,
                                    text="Bit Sequence")
    self.bitSeqLabel.grid(row=1, column=1,
                        padx=20, pady=10,
                        sticky="ew")

    # Bit sequence field
    self.bitSeqEntry = customtkinter.CTkEntry(self)
    self.bitSeqEntry.grid(row=1, column=2,
                        columnspan=3, padx=20,
                        pady=10, sticky="ew")
    
    # Significance level Label
    self.bitSeqLabel = customtkinter.CTkLabel(self,
                                    text="Significance level")
    self.bitSeqLabel.grid(row=2, column=1,
                        padx=20, pady=10,
                        sticky="ew")

    # Significance level field
    self.bitSeqEntry = customtkinter.CTkEntry(self)
    self.bitSeqEntry.grid(row=2, column=2,
                        columnspan=3, padx=20,
                        pady=10, sticky="ew")
    
    # Subsequence size Label
    self.bitSeqLabel = customtkinter.CTkLabel(self,
                                    text="Subsequence size")
    self.bitSeqLabel.grid(row=3, column=1,
                        padx=20, pady=10,
                        sticky="ew")

    # Subsequence size field
    self.bitSeqEntry = customtkinter.CTkEntry(self)
    self.bitSeqEntry.grid(row=3, column=2,
                        columnspan=3, padx=20,
                        pady=10, sticky="ew")

    # Generate Button
    self.generateResultsButton = customtkinter.CTkButton(self,
                                        text="Generate Results")
    self.generateResultsButton.grid(row=4, column=1,
                                    columnspan=2,
                                    padx=20, pady=10,
                                    sticky="ew")