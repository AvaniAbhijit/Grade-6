#Task 1 : Change the title of the application to " My Application"
#Task 2: Run the code and see the title of the application.
#Task 3: Uncomment line no 12 and run the code.
# Observe the changes and understand the use of pack() method.

import tkinter as tk #imports the Tkinter module and aliases it as tk.
                     #So instead of using "tkinter" all the time we can use "tk".
window=tk.Tk() # creates the main window for our Tkinter application
               # and assigns it to the variable "window".
window.title("Title of window") # sets the title of the window to "Title".
window.geometry("400x300") # sets the size of the window to 400 pixels width and 300 pixels height.
heading=tk.Label(window,text="Heading of your application")
# creates a label widget and assigns it to the variable "heading".
#the first value "window" indicates that the label has to be placed on "window".
#The sentence to be added in label should be given in the text parameter.

'''heading.pack()'''  #widgets will be available only when we use pack() method.

window.mainloop() # keeps the window open until we close it.
