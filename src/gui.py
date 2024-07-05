import tkinter
import customtkinter  # the lib we are using for better aspect 

# !!!! very important !!!!
#
# when building the gui, use the customtkinter version of elements
#
# !!!!!!!!

root_tk = tkinter.Tk()  # create the Tk window like you normally do
root_tk.geometry("400x240")
root_tk.title("CustomTkinter Test")

def button_function():
    print("button pressed")

# use CTkButton instead of tkinter Button!!!
# see online more references
button = customtkinter.CTkButton(master=root_tk, corner_radius=10, command=button_function)
button.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

root_tk.mainloop()