from tkinter import *
from tkinter import ttk

root = Tk()
root.title("Dogs4U")
root.geometry("800x500")

label_title = Label(root, text="Dogs4U", )
label_title.grid(row=0,column=1)

text_1 = "Welcome to Dogs4U! Specify any of the dog attributes and we will recommend a dog 4 U!"
label_directions = Label(root, text=text_1)
label_directions.grid(row=1, column=1)

dog_attrib_1 = "Average adult dog weight"
label_directions = Label(root, text=dog_attrib_1)
label_directions.grid(row=3, column=1)

dog_attrib_2 = "Average adult dog energy level"
label_directions = Label(root, text=dog_attrib_2)
label_directions.grid(row=4, column=1)

def selected(event):
        attrib_1 = clicked_1.get()
        attrib_2 = clicked_2.get()
        if attrib_1 == "<40 lbs" and attrib_2 == "medium":
            result = Label(root, text="Corgy")
        else:
            result = Label(root, "Lab")
        result.grid(row= 7,column=1)

options_1 = [
    "No preference",
    "<40 lbs",
    "40-80 lbs",
    ">80 lbs"
]
options_2 = [
    "No preference",
    "Low",
    "Medium",
    "High"
]

clicked_1 = StringVar()
clicked_1.set(options_1[0])
clicked_2 = StringVar()
clicked_2.set(options_2[0])

drop_1 = OptionMenu(root, clicked_1, *options_1, command=selected)
drop_1.grid(row=3, column =2)
drop_2 = OptionMenu(root, clicked_2, *options_2)
drop_2.grid(row=4, column =2)




root.mainloop()
