from tkinter import *

root = Tk()
root.geometry("600x600")

def myClick():
    myLabel = Label(root, text="Look! I clicked a Button!!")
    myLabel.pack()

#creating a labelwidget
myButton = Button(root, text="Click Me!", padx=50, pady=50, command=myClick, fg="blue", bg="red")

myButton.pack()


root.mainloop()