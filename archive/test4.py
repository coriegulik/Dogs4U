from tkinter import *

root = Tk()
root.geometry("600x600")

def myClick():
    hello = "Hello " + e.get()
    myLabel = Label(root, text = hello)
    myLabel.pack()

#creating a labelwidget
myButton = Button(root, text="Enter your name!", padx=50, pady=50, command=myClick, fg="blue", bg="red")

myButton.pack()

e =Entry(root, width=50, bg="yellow", borderwidth=5)
e.pack()
e.get
e.insert(0, "Enter your Name: ")

root.mainloop()