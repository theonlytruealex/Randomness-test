import customtkinter as ctk
import tkinter as tk
 
# Basic parameters and initializations
# Supported modes : Light, Dark, System
ctk.set_appearance_mode("System") 
 
# Supported themes : green, dark-blue, blue
ctk.set_default_color_theme("green")    
 
appWidth, appHeight = 400, 400
 
# App Class
class App(ctk.CTk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
 
        self.title("GUI Application")
        self.geometry(f"{appWidth}x{appHeight}")
 
        # Length Label
        self.lenLabel = ctk.CTkLabel(self,
                                     text="Sequence Length")
        self.lenLabel.grid(row=0, column=0,
                           padx=20, pady=20,
                           sticky="ew")
 
        # Length Field
        self.lenEntry = ctk.CTkEntry(self,
                            placeholder_text="30")
        self.lenEntry.grid(row=0, column=1,
                           columnspan=3, padx=20,
                           pady=20, sticky="ew")
        
        # Bit Sequence Label
        self.bitSeqLabel = ctk.CTkLabel(self,
                                      text="Bit Sequence")
        self.bitSeqLabel.grid(row=1, column=0,
                            padx=20, pady=20,
                            sticky="ew")
 
        # Name Entry Field
        self.bitSeqEntry = ctk.CTkEntry(self)
        self.bitSeqEntry.grid(row=1, column=1,
                            columnspan=3, padx=20,
                            pady=20, sticky="ew")
 
        # Generate Button
        self.generateResultsButton = ctk.CTkButton(self,
                                         text="Generate Results")
        self.generateResultsButton.grid(row=5, column=1,
                                        columnspan=2,
                                        padx=20, pady=20,
                                        sticky="ew")
if __name__ == "__main__":
    app = App()
    app.mainloop()