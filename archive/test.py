from tkinter import *
import os
os.system('clear')

root = Tk()
root.title("name")
root.geometry("600x600")

myLabel = Label(root, text="Hullo")
myLabel.pack()

myTextbox = Entry(root, width=30)
myTextbox.pack()

def hello():
    hello_label = Label(root, text="Hello"+myTextbox.get())
    hello_label.pack()

myButton = Button(root, text="Submit", command =hello)
myButton.pack()

root.mainloop()