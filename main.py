# importing the tkinter module for the making of the GUI
from tkinter import *
from tkinter.ttk import *

# importing strftime function to retrieve the system's time
from time import strftime

# creating the tkinter window
root = Tk()
root.title("Clock")
# making the GUI a widget
root.overrideredirect(1)

# this function is used to display the time on the label
def time():
    string = strftime('%I:%M:%S %p')
    label.config(text = string)
    label.after(1000, time)  # 1000 = 1 second

# styling the label widget so that the clock will look more attractive
label = Label(root, font = ('calibri', 40, 'bold'),
                            background = 'black',
                            foreground = 'cyan')

# placing clock at the centre of the tkinter window
label.pack(anchor='center')

time()

mainloop()

