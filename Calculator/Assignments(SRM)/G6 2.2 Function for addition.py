#Task 1:  Run the code and check why label and button are not visible on the window?
#Task 2: Once the button is visible, click on the button and check the label text.
#Task 3: Make the change such that when the button is clicked, the calculator label should be changed.

import tkinter as tk
def add():#function to execute when button is clicked
    answer.config(text="I perform addition") #use the variable which is holding the label
                                            #widget and use config() to change the text of that label.

window=tk.Tk()
window.title("Calculator Application")
window.geometry("400x300")
text=tk.Label(window,text="Calculator")

button=tk.Button(window,text="+",command=add) #the name of the function should be given
                #in command parameter. This will call the function
                #when button is cliked and executes the specified task.


answer=tk.Label(window,text="Answer")

window.mainloop()
