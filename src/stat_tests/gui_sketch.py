# a file to help with the design of the gui
# use it and adapt it to your own taste
# serves as an implementation for the main menu module

import tkinter
from tkinter import filedialog
from tkinter import messagebox
import customtkinter
import monobit
import mbit
import autocorrelation
import serial
import runs
import numpy as np
from scipy.special import erfc
from PIL import Image, ImageTk
import genlatex
import time
import warnings

customtkinter.set_appearance_mode("System")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"

# global variable to hold file data
file_contents = ""

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        # configure window
        self.title("gui_sketch.py")
        self.geometry(f"{1000}x{900}")

        # configure grid layout (4x4)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure((2, 3), weight=0)
        self.grid_rowconfigure((0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10), weight=1)

        # create sidebar frame with widgets
        self.sidebar_frame = customtkinter.CTkFrame(self, width=140, corner_radius=10)
        self.sidebar_frame.grid(row=0, column=0, rowspan=11, sticky="nsew")
        
        self.logo_label = customtkinter.CTkLabel(self.sidebar_frame, text="Interactive Randomness Test", font=customtkinter.CTkFont(size=20, weight="bold"))
        self.logo_label.grid(row=0, column=0, padx=20, pady=(20, 10))
        self.sidebar_button_1 = customtkinter.CTkButton(self.sidebar_frame, command=self.monobit_event, text = "Monobit Test")
        self.sidebar_button_1.grid(row=1, column=0, padx=20, pady=10)
        self.sidebar_button_2 = customtkinter.CTkButton(self.sidebar_frame, command=self.mbit_event, text = "M-bit Test")
        self.sidebar_button_2.grid(row=2, column=0, padx=20, pady=10)
        self.sidebar_button_3 = customtkinter.CTkButton(self.sidebar_frame, command=self.autocorr_event, text = "Autocorrelation Test")
        self.sidebar_button_3.grid(row=3, column=0, padx=20, pady=10)
        self.sidebar_button_4 = customtkinter.CTkButton(self.sidebar_frame, command=self.runs_event, text = "Runs Test")
        self.sidebar_button_4.grid(row=4, column=0, padx=20, pady=10)
        self.sidebar_button_4 = customtkinter.CTkButton(self.sidebar_frame, command=self.serial_event, text = "Serial Test")
        self.sidebar_button_4.grid(row=5, column=0, padx=20, pady=10)
        self.appearance_mode_label = customtkinter.CTkLabel(self.sidebar_frame, text="Appearance Mode:", anchor="w")
        # the next line brings about that annoying space in the menu 
        self.sidebar_frame.grid_rowconfigure(6, weight=1)
        self.appearance_mode_label.grid(row=7, column=0, padx=20, pady=(10, 0))
        self.appearance_mode_optionemenu = customtkinter.CTkOptionMenu(self.sidebar_frame, values=["Light", "Dark", "System"],
                                                                       command=self.change_appearance_mode_event)
        self.appearance_mode_optionemenu.grid(row=8, column=0, padx=20, pady=(10, 10))
        self.scaling_label = customtkinter.CTkLabel(self.sidebar_frame, text="UI Scaling:", anchor="w")
        self.scaling_label.grid(row=9, column=0, padx=20, pady=(10, 0))
        self.scaling_optionemenu = customtkinter.CTkOptionMenu(self.sidebar_frame, values=["80%", "90%", "100%", "110%", "120%"],
                                                               command=self.change_scaling_event)
        self.scaling_optionemenu.grid(row=10, column=0, padx=20, pady=(10, 20))

        # main frame with input and execution details
        # render textboxs, labels, etc in this frame!!
        self.main_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")
        self.main_frame.grid(row=0, column=1, rowspan=10, columnspan=3, sticky="nsew")
        self.main_frame.grid_columnconfigure((0, 1, 2), weight=1)
        self.main_frame.grid_rowconfigure((0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11), weight=1)
        
        # create textbox
        self.main_label = customtkinter.CTkLabel(self.main_frame,
        font=customtkinter.CTkFont(size=17, weight="normal"),
        text = "Select the desired Randomness Test")
        self.main_label.grid(row=6, column=1, padx=(20, 0), pady=(20, 0), sticky="nsew")

        # set default values
        self.appearance_mode_optionemenu.set("Light")
        self.change_appearance_mode_event("Light")
        self.scaling_optionemenu.set("100%")

    def change_appearance_mode_event(self, new_appearance_mode: str):
        customtkinter.set_appearance_mode(new_appearance_mode)

    def change_scaling_event(self, new_scaling: str):
        new_scaling_float = int(new_scaling.replace("%", "")) / 100
        customtkinter.set_widget_scaling(new_scaling_float)

    def monobit_event(self):
        # important!!!!!
        # don't forget to clear the space you are going to render your objects to
        for widgets in self.main_frame.winfo_children():
            widgets.destroy()
        
        input_frame = customtkinter.CTkFrame(self.main_frame, corner_radius=0, fg_color="transparent")
        input_frame.grid(row=0, column=0, rowspan=2, columnspan=5, pady=20,  sticky="nsew")
        input_frame.grid_columnconfigure((1, 2, 3, 4, 5), weight=1)

        img = ImageTk.PhotoImage(Image.open("../../assets/Monobit.png").resize((650, 330)))
        image_serial = customtkinter.CTkFrame(self.main_frame, corner_radius=0, fg_color="gray92")
        image_serial.grid(row=3, column=0, rowspan=8, columnspan=5, pady=20,  sticky="nsew")
        image_serial.grid_columnconfigure((0, 1, 2, 3, 4), weight=1)
        image_serial.grid_rowconfigure((0, 1, 2, 3, 4, 5, 6, 7), weight=1)
        lbl = customtkinter.CTkLabel(image_serial, image=img, text="")
        lbl.grid(row=0, column=0,sticky="nsew")
        # Significance Level Label
        self.sigLvlLabel = customtkinter.CTkLabel(input_frame,
                                        text="Significance Level")
        self.sigLvlLabel.grid(row=0, column=1,
                            padx=20, pady=20,
                            sticky="ew")

        # Significance Level Field
        self.sigLvlEntry = customtkinter.CTkEntry(input_frame,
                            width=200)
        self.sigLvlEntry.grid(row=0, column=2,
                            columnspan=3, padx=20,
                            pady=20, sticky="ew")

        # Bit Sequence Label
        self.bitSeqLabel = customtkinter.CTkLabel(input_frame,
                                        text="Bit Sequence")
        self.bitSeqLabel.grid(row=1, column=1,
                            padx=20, pady=20,
                            sticky="ew")

        # Name Entry Field
        self.bitSeqEntry = customtkinter.CTkEntry(input_frame)
        self.bitSeqEntry.grid(row=1, column=2,
                            columnspan=3, padx=20,
                            pady=20, sticky="ew")
        # Generate Button
        self.generateResultsButton = customtkinter.CTkButton(input_frame,
                                            text="Generate Results", command=lambda: self.generateButton_monobit_event(input_frame))
        self.generateResultsButton.grid(row=4, column=1,
                                        columnspan=2,
                                        padx=20, pady=20,
                                        sticky="ew")
        
    def generateButton_monobit_event(self, input_frame):
        monobit.monobit(self, input_frame)

    def mbit_event(self):
        pass
    def autocorr_event(self):
        
        global file_contents
        file_contents = ""

        def open_file():
            global file_contents
            file_path = filedialog.askopenfilename()
            
            if file_path:
                with open(file_path, 'r', encoding='utf-8') as file:
                    file_contents = file.read()
        
        for widgets in self.main_frame.winfo_children():
            widgets.destroy()
        
        self.main_frame.grid_rowconfigure((2, 3, 4, 5, 6, 7, 8, 9, 10, 11), weight=0)
        self.main_frame.grid_rowconfigure(0, weight=1)
        self.main_frame.grid_rowconfigure(1, weight=3)
        input_frame = customtkinter.CTkFrame(self.main_frame, corner_radius=0, fg_color="transparent")
        input_frame.grid(row=0, column=0, rowspan=1, columnspan=5, pady=20,  sticky="nsew")
        input_frame.grid_columnconfigure((1, 2, 3, 4, 5), weight=1)
        # input_frame.grid_columnconfigure(3, weight=0)
        
        # sequence label
        self.bitSeqLabel = customtkinter.CTkLabel(input_frame,
                                        text="Bit Sequence")
        self.bitSeqLabel.grid(row=1, column=0, padx=20, pady=5,sticky="w")

        # sequence entry field
        self.bitSeqEntry = customtkinter.CTkEntry(input_frame)
        self.bitSeqEntry.grid(row=1, column=1, columnspan=5, padx=10, pady=5, sticky="ew")
        
        # alpha label
        self.alphaLabel = customtkinter.CTkLabel(input_frame,
                                        text="Significance Level (α)")
        self.alphaLabel.grid(row=2, column=0, padx=20, pady=5,sticky="w")

        # alpha entry field
        self.alphaEntry = customtkinter.CTkEntry(input_frame)
        self.alphaEntry.grid(row=2, column=1, columnspan=1, padx=10, pady=5, sticky="ew")
        
        # d param label
        self.DLabel = customtkinter.CTkLabel(input_frame,
                                        text="Shift coefficient (d)")
        self.DLabel.grid(row=3, column=0, padx=20, pady=5,sticky="w")

        # d param entry field
        self.DEntry = customtkinter.CTkEntry(input_frame)
        self.DEntry.grid(row=3, column=1, columnspan=1, padx=10, pady=5, sticky="ew")

        result_frame = customtkinter.CTkFrame(self.main_frame, corner_radius=0, fg_color="transparent")
        result_frame.grid(row=2, column=0, rowspan=9, columnspan=5, pady=150,  sticky="nsew")
        result_frame.grid_columnconfigure((0, 1, 2, 3, 4), weight=1)
        result_frame.grid_rowconfigure((0, 1), weight=1)
        
        image = customtkinter.CTkImage(light_image=Image.open("../../assets/autocorr/autocorr.png"), size=(500, 361))
        lbl = customtkinter.CTkLabel(result_frame, image=image, text="")
        lbl.grid(row=0, column=2, sticky="nsew")
        
        # Open file button
        self.generateResultsButton = customtkinter.CTkButton(input_frame, text="Open file", command=open_file)
        self.generateResultsButton.grid(row=4, column=0, columnspan=1, padx=20, pady=15, sticky="e")
        
        def generate_autocorr():
            p_val = 0
            global file_contents
            bit_sequence = self.bitSeqEntry.get()
            if bit_sequence != "":
                file_contents = ""
                alpha = self.alphaEntry.get()
                d_param = self.DEntry.get()
                alpha = float(alpha)  # Convert alpha to float
                d_param = int(d_param)  # Convert m_param to int
                p_val = autocorrelation.autocorrelation(bit_sequence, alpha, d_param)
            else:
                alpha = self.alphaEntry.get()
                d_param = self.DEntry.get()
                alpha = float(alpha)  # Convert alpha to float
                d_param = int(d_param)  # Convert m_param to int
                p_val = autocorrelation.autocorrelation(file_contents, alpha, d_param)
            
            # compute the 
            # clear frame
            for widgets in self.main_frame.winfo_children():
                widgets.destroy()
                
            self.main_frame.grid_rowconfigure((0,1,2), weight=1)
            self.main_frame.grid_rowconfigure((3, 4, 5, 6, 7, 8, 9, 10), weight=0)
            
            
            img = Image.open("../../assets/autocorr/autocorr_h.png")
            width, height = img.size
            image = customtkinter.CTkImage(light_image=img, size=(500, int(height / width * 550)))
            lbl = customtkinter.CTkLabel(self.main_frame, image=image, text="")
            lbl.grid(row=0, column=0, columnspan=3, sticky="wes")
            
            # get p_value tex 
            genlatex.gen_img(p_val, alpha)
            
            # wait 
            # time.sleep(0.1)
            
            # render 
            img = Image.open("../../assets/autocorr/temp/1.png")
            width, height = img.size
            image = customtkinter.CTkImage(light_image=img, size=(350, int(height / width * 350)))
            lbl = customtkinter.CTkLabel(self.main_frame, image=image, text="")
            lbl.grid(row=1, column=0, columnspan=3, sticky="nsew")
            
            
            img = Image.open("../../assets/autocorr/temp/2.png")
            width, height = img.size
            image = customtkinter.CTkImage(light_image=img, size=(500, int(height / width * 550)))
            lbl = customtkinter.CTkLabel(self.main_frame, image=image, text="")
            lbl.grid(row=2, column=0, columnspan=3, sticky="wen")
            
        # Generate Button
        self.generateResultsButton = customtkinter.CTkButton(input_frame,
                                            text="Generate Results", command=generate_autocorr)
        self.generateResultsButton.grid(row=4, column=5, columnspan=1, padx=20, pady=0, sticky="e")
            
             
        
        
    def serial_event(self):

        global file_contents
        file_contents = ""

        def open_file():
            global file_contents
            file_path = filedialog.askopenfilename()
            
            if file_path:
                with open(file_path, 'r', encoding='utf-8') as file:
                    file_contents = file.read()

        # Define a function to get the entry values and call serial.serial
        def serial_generate_results():
            global file_contents
            bit_sequence = self.bitSeqEntry.get()
            if bit_sequence != "":
                file_contents = ""
                alpha = self.alphaEntry.get()
                m_param = self.mParamEntry.get()
                alpha = float(alpha)  # Convert alpha to float
                m_param = int(m_param)  # Convert m_param to int
                serial.serial(self, bit_sequence, alpha, m_param)
            else:
                alpha = self.alphaEntry.get()
                m_param = self.mParamEntry.get()
                alpha = float(alpha)  # Convert alpha to float
                m_param = int(m_param)  # Convert m_param to int
                serial.serial(self, file_contents, alpha, m_param)

        # clean-up
        for widgets in self.main_frame.winfo_children():
            widgets.destroy()
        
        input_frame = customtkinter.CTkFrame(self.main_frame, corner_radius=0, fg_color="transparent")
        input_frame.grid(row=0, column=0, rowspan=2, columnspan=5, pady=20, sticky="nsew")
        input_frame.grid_columnconfigure((1, 2, 3, 4, 5), weight=1)
        
        # sequence label
        self.bitSeqLabel = customtkinter.CTkLabel(input_frame, text="Bit Sequence")
        self.bitSeqLabel.grid(row=1, column=0, padx=20, pady=5, sticky="w")

        # sequence entry field
        self.bitSeqEntry = customtkinter.CTkEntry(input_frame)
        self.bitSeqEntry.grid(row=1, column=1, columnspan=5, padx=10, pady=5, sticky="ew")
        
        # alpha label
        self.alphaLabel = customtkinter.CTkLabel(input_frame, text="Sensitivity coefficient (α)")
        self.alphaLabel.grid(row=2, column=0, padx=20, pady=5, sticky="w")

        # alpha entry field
        self.alphaEntry = customtkinter.CTkEntry(input_frame)
        self.alphaEntry.grid(row=2, column=1, columnspan=1, padx=10, pady=5, sticky="ew")
        
        # m param label
        self.mParamLabel = customtkinter.CTkLabel(input_frame, text="Subsequence length (m):")
        self.mParamLabel.grid(row=3, column=0, padx=20, pady=5, sticky="w")

        # m param entry field
        self.mParamEntry = customtkinter.CTkEntry(input_frame)
        self.mParamEntry.grid(row=3, column=1, columnspan=1, padx=10, pady=5, sticky="ew")

        img = ImageTk.PhotoImage(Image.open("../../assets/serial.png").resize((650, 525)))
        image_serial = customtkinter.CTkFrame(self.main_frame, corner_radius=0, fg_color="gray92")
        image_serial.grid(row=3, column=0, rowspan=8, columnspan=5, pady=20,  sticky="nsew")
        image_serial.grid_columnconfigure((0, 1, 2, 3, 4), weight=1)
        image_serial.grid_rowconfigure((0, 1, 2, 3, 4, 5, 6, 7), weight=1)
        lbl = customtkinter.CTkLabel(image_serial, image=img, text="")
        lbl.grid(row=0, column=0,sticky="nsew")

        # Open file button
        self.generateResultsButton = customtkinter.CTkButton(input_frame, text="Open file", command=open_file)
        self.generateResultsButton.grid(row=4, column=0, columnspan=1, padx=20, pady=15, sticky="e")

        # Generate Button
        self.generateResultsButton = customtkinter.CTkButton(input_frame, text="Generate Results", command=serial_generate_results)
        self.generateResultsButton.grid(row=4, column=5, columnspan=1, padx=20, pady=15, sticky="e")

    def runs_event(self):
        for widgets in self.main_frame.winfo_children():
            widgets.destroy()

        global file_contents
        file_contents = ""

        def open_file():
            global file_contents
            file_path = filedialog.askopenfilename()
            
            if file_path:
                with open(file_path, 'r', encoding='utf-8') as file:
                    file_contents = file.read()

        
        input_frame = customtkinter.CTkFrame(self.main_frame, corner_radius=0, fg_color="transparent")
        input_frame.grid(row=0, column=0, rowspan=2, columnspan=5, pady=20,  sticky="nsew")
        input_frame.grid_columnconfigure((1, 2, 3, 4, 5), weight=1)
        
        # sequence label
        self.bitSeqLabel = customtkinter.CTkLabel(input_frame,
                                        text="Bit Sequence")
        self.bitSeqLabel.grid(row=1, column=0, padx=20, pady=5,sticky="w")

        # sequence entry field
        self.bitSeqEntry = customtkinter.CTkEntry(input_frame)
        self.bitSeqEntry.grid(row=1, column=1, columnspan=5, padx=10, pady=5, sticky="ew")
        
        # alpha label
        self.alphaLabel = customtkinter.CTkLabel(input_frame,
                                        text="Sensitivity coefficient (α)")
        self.alphaLabel.grid(row=2, column=0, padx=20, pady=5,sticky="w")

        # alpha entry field
        self.alphaEntry = customtkinter.CTkEntry(input_frame)
        self.alphaEntry.grid(row=2, column=1, columnspan=1, padx=10, pady=5, sticky="ew")
        
        def runs_test():

            alpha = self.alphaEntry.get()
            alpha = float(alpha)  

            if alpha >= 1 or alpha <= 0:
                messagebox.showerror("Error", "Alpha has to be between 0 and 1.")
                return

            global file_contents
            bit_sequence = self.bitSeqEntry.get()
            if bit_sequence != "":
                 # validating the input
                try:
                    bit_sequence = float(self.bitSeqEntry.get())
                except ValueError:
                    messagebox.showerror("Error", "Please enter a valid integer for Bit Sequence.")
                    return
                bit_sequence = self.bitSeqEntry.get()
                file_contents = ""
                runs.runs(self, bit_sequence, alpha)
            else:
                runs.runs(self, file_contents, alpha)
            
        
        img = ImageTk.PhotoImage(Image.open("../../assets/alg_runs.png").resize((650, 525)))
        warnings.filterwarnings("ignore", category=UserWarning)
        image_runs = customtkinter.CTkFrame(self.main_frame, corner_radius=0, fg_color="gray92")
        image_runs.grid(row=3, column=0, rowspan=8, columnspan=5, pady=20,  sticky="nsew")
        image_runs.grid_columnconfigure((0, 1, 2, 3, 4), weight=1)
        image_runs.grid_rowconfigure((0, 1, 2, 3, 4, 5, 6, 7), weight=1)
        lbl = customtkinter.CTkLabel(image_runs, image=img, text="")
        lbl.grid(row=0, column=0,sticky="nsew")

        # Open file button
        self.generateResultsButton = customtkinter.CTkButton(input_frame, text="Open file", command=open_file)
        self.generateResultsButton.grid(row=4, column=0, columnspan=1, padx=20, pady=15, sticky="e")
        
        # Generate Button
        self.generateResultsButton = customtkinter.CTkButton(input_frame,
                                            text="Generate Results", command = runs_test)
        self.generateResultsButton.grid(row=4, column=5,
                                        columnspan=1,
                                        padx=20, pady=15,
                                        sticky="e")
if __name__ == "__main__":
    app = App()
    app.mainloop()