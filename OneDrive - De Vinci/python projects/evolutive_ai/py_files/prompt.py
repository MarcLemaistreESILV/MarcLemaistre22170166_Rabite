import time
import main
import tkinter as tk
from tkinter import ttk
   

#first we ask the user for the parameters
root = tk.Tk()
root_title = tk.Label(text = "Hello, see and change the parameters before running the simulation")
root.title('Tkinter Window - Center')
button_launch = ttk.Button(root, text="Run simuation", command= lambda: main.plot(400, 400, [0,0,0,0]))
textbox_paramter_1_val = tk.StringVar()
textbox_paramter_1 = ttk.Entry(root,textvariable=textbox_paramter_1_val)

button_launch.pack()
textbox_paramter_1.pack()
window_width = 300
window_height = 200

# get the screen dimension
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# find the center point
center_x = int(screen_width/2 - window_width / 2)
center_y = int(screen_height/2 - window_height / 2)
root.attributes('-alpha',1)
# set the position of the window to the center of the screen
root.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')
root.iconbitmap('../evolutive_ai/sources/icone.ico')
root_title.pack()
root.mainloop()
