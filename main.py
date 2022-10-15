from tkinter import *
from tkinter import ttk
import math

root = Tk()
root.title("Dogs4U")
root.geometry("500x300")

root.iconbitmap('c:/users/corie/pycharmprojects/Dogs4U/2.ico')
label_title = Label(root, text="Dogs4U", font=16)
label_title.grid(row=0,column=1, columnspan=6)

intro_1 = "\nWelcome to Dogs4U! \n\nSpecify any of the dog attributes and we will recommend a dogs 4 U!\n\n"
label_directions = Label(root, text=intro_1)
label_directions.grid(row=1, column=1, columnspan=6, rowspan = 5)

# result logic
def submitclick():
    attrib_1 = drop_1.get()
    attrib_2 = drop_2.get()
    global result
    global result_label
    if attrib_1 == "No preference":
        list_1 = sum(list(size_dict.values()), [])
        if attrib_2 == "No preference":
            list_2 = sum(list(activity_dict.values()), [])
        else:
            list_2 = activity_dict.get(attrib_2)
    elif attrib_2 == "No preference":
        list_2 = sum(list(activity_dict.values()), [])
        list_1 = size_dict.get(attrib_1)
    else:
        list_1 = size_dict.get(attrib_1)
        list_2 = activity_dict.get(attrib_2)
    result_list = [value for value in list_1 if value in list_2]
    if len(result_list) < 1:
        result = "There are no dogs that match all the attributes"
    else:
        result = result_list[0]
        for i in range(1, len(result_list)):
            result += "\n" + result_list[i]

# result window
    top = Toplevel()
    top.title("Dogs4U Result")
    top.iconbitmap('c:/users/corie/pycharmprojects/Dogs4U/2.ico')
    w = 500
    h = max(300,math.ceil(len(result_list)/4)*100)
    top.geometry(f"{w}x{h}")
    intro2 = "Based on the selected attributes, below is the recommended dog 4 U!"
    label_result = Label(top, text=intro2,)
    label_result.grid(row=0, column=1, padx=10)
    result_label = Label(top, text=result)
    result_label.grid(row=1, column=1,padx=10, pady=50)
    close_result = Button(top, text="Try Again", command=top.destroy)
    close_result.grid(row=2,column=1)


# drop down option labels
dog_attrib_1 = "Average adult dog weight"
label_directions = Label(root, text=dog_attrib_1)
label_directions.grid(row=6, column=1, pady=10)

dog_attrib_2 = "Average adult dog energy level"
label_directions = Label(root, text=dog_attrib_2)
label_directions.grid(row=7, column=1, pady=10)

blank_space = Label(root, text="")
blank_space.grid(row=8, column=1, padx=10)

submit_button = Button(root, text="Submit", padx=20, pady=10, command = submitclick)
submit_button.grid(row=9, column=2)


# drop down options
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

drop_1 = ttk.Combobox(root, value=options_1)
drop_1.current(0)
drop_1.grid(row=6, column =2, pady=10)

drop_2 = ttk.Combobox(root, value=options_2)
drop_2.current(0)
drop_2.grid(row=7, column =2,pady=10)

# dictionary of dog breeds
size_dict = {
    "<40 lbs":
        ["French Bulldogs",
        "Beagles",
        "Dachshunds",
        "Corgis",
        "Yorkshire Terriers",
        "Cavalier King Charles Spaniels",
        "Miniature Schnauzers"],
    "40-80 lbs":
        ["Labrador Retrievers",
        "Golden Retrievers",
        "Poodles",
        "Bulldogs",
        "German Shorthaired Pointers",
        "Australian Shepherds",
        "Boxers",
        "Siberian Huskies"],
    ">80 lbs":
        ["German Shepherds",
        "Rottweilers",
        "Doberman Pinschers",
        "Great Danes"]
    }

activity_dict = {
    "Low":
        ["French Bulldogs",
        "Golden Retrievers",
        "Bulldogs",
        "Rottweilers",
        "Dachshunds",
        "Cavalier King Charles Spaniels",
        "Miniature Schnauzers"],
    "Medium":
        ["Poodles",
        "Beagles",
        "Corgis",
        "Yorkshire Terriers",
        "Boxers",
        "Great Danes",
        "Bernese Mountain Dogs"],
    "High":
        ["Labrador Retrievers",
        "German Shepherds",
        "German Shorthaired Pointers"
        "Australian Shepherds",
        "Doberman Pinschers",
        "Siberian Huskies"]
    }




root.mainloop()
