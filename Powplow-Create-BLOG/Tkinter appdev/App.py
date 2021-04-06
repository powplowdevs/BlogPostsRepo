#IMPORTS
import tkinter as tk
import random

#HEIGHT AND WIDTH OF OUT APLICATIONS SCREEN
HEIGHT = 500
WIDTH = 600
#COLORS
COLORS = ["red","orange","yellow","green","blue","pink","purple"]

#FUNCTION USED TO GET INFO FROM TEXT BOX
def getInfo(entery, label):
    label.destroy()
    label = tk.Label(frame, bg="orange", text=entery)
    label.place(relx=.5, rely=.4)

#FUNCTION USED TO CHANGE FRAME'S COLOR
def newColor(enterys):
    global root
    
    root.destroy()
    
    root = tk.Tk()
    
    canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
    canvas.pack()

    frame = tk.Frame(root, bg=random.choice(COLORS))
    frame.place(relwidth=1, relheight=1)  
    
    title = tk.Label(frame, text="Simple tkinter python program!")
    title.place(relx=.36, rely=.2)
    
    entery = tk.Entry(frame, bg = "green")
    entery.place(relx=.4, rely=.3)

    label = tk.Label(frame, bg="orange")
    label.place(relx=.5, rely=.4)
    
    button = tk.Button(root, text="Submit", command = lambda: getInfo(entery.get(), label))
    button.pack(side="left")
    
    button_color = tk.Button(root, text="New color", command = lambda: newColor(entery.get()))
    button_color.pack(side="left")    


#ROOT IS OUR MAIN SCREEN
root = tk.Tk()

#CANVAS IS WHAT WE PUT WIGETS ON
canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
canvas.pack()

#A FRAME IS LIKE A DIFFRENT CANVAS THAT GOES WITHIN THE CANVAS
frame = tk.Frame(root, bg="grey")
frame.place(relwidth=1, relheight=1)

#OUR TITLE
title = tk.Label(frame, text="Simple tkinter python program!")
title.place(relx=.36, rely=.2)

#OUR ENTERY IS A TEXT BOX
entery = tk.Entry(frame, bg = "green")
entery.place(relx=.4, rely=.3)

#A LABEL TO PUT OR TEXT FROM THE ENTERY
label = tk.Label(frame, bg="orange")
label.place(relx=.5, rely=.4)

#BUTTONS
button = tk.Button(root, text="Submit", command = lambda: getInfo(entery.get(), label))
#BUTTON COMMAND CALLS A FUNCTION ON CLICK THIS ONE CALLS THE getInfo FUNCTION
button.pack(side="left")
#THIS IS THE BUTTON THAT WILL CHANGE COLORS 
button_color = tk.Button(root, text="New color", command = lambda: newColor(entery.get()))
button_color.pack(side="left")

root.mainloop() 

