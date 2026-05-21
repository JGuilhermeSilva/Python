# importing only those functions
# which are needed
from tkinter import * 
from tkinter import ttk

# creating tkinter window
root = Tk()

# Adding widgets to the root window
Label(root, text = 'GeeksforGeeks', font =('Verdana', 15)).pack(side = TOP, pady = 10)

# Creating a photoimage object to use image
photo = PhotoImage(file = "musicas/pause.png")

# here, image option is used to
# set image on button
Button(root, image = photo).pack(side = TOP)

mainloop()