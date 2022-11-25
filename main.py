from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image
from urllib.request import urlopen
import requests
from io import BytesIO

# home window
root = Tk()
root.title("Dogs4U")
root.geometry("400x300")

root.iconbitmap('c:/users/corie/pycharmprojects/Dogs4U/2.ico')
label_title = Label(root, text="Dogs4U", font=16)
label_title.grid(row=0,column=1, columnspan=6)

intro_1 = "\nWelcome to Dogs4U! \n\nSpecify any of the dog attributes and we will recommend a dogs 4 U!\n\n"
label_directions = Label(root, text=intro_1)
label_directions.grid(row=1, column=1, columnspan=6, rowspan = 5)


# drop down option labels for home window
dog_attrib_1 = "Average adult dog weight"
label_directions = Label(root, text=dog_attrib_1)
label_directions.grid(row=6, column=1, pady=10)

dog_attrib_2 = "Average adult dog energy level"
label_directions = Label(root, text=dog_attrib_2)
label_directions.grid(row=7, column=1, pady=10)

dog_attrib_3 = "Average adult dog noise level"
label_directions = Label(root, text=dog_attrib_3)
label_directions.grid(row=8, column=1, pady=10)


# makes list of dog breeds based on options chosen
def submitclick():

    global result_list  # list of dogs recommended

    # gathers user inputs
    attrib_1 = drop_1.get()
    attrib_2 = drop_2.get()
    attrib_3 = drop_3.get()

    # making result_list of dog breeds matching attributes
    if attrib_1 == "No preference":
        list_1 = sum(list(size_dict.values()), [])
    else:
        list_1 = size_dict.get(attrib_1)
    if attrib_2 == "No preference":
        list_2 = list_1
    else:
        list_2 = list(set(list_1).intersection(activity_dict.get(attrib_2)))
    if attrib_3 == "No preference":
        result_list = list_2
    else:
        result_list = list(set(list_2).intersection(noise_dict.get(attrib_3)))

    # opening window for results
    if len(result_list) < 1:
        exit_window()
    else:
        result_window()


# submit
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

drop_3 = ttk.Combobox(root, value=options_2)
drop_3.current(0)
drop_3.grid(row=8, column =2,pady=10)

# dictionary of dog breeds based on size
size_dict = {
    "<40 lbs":
        ["French Bulldog",
        "Beagle",
        "Dachshund",
        "Corgi",
        "Yorkshire Terrier",
        "Cavalier King Charles Spaniel",
        "Miniature Schnauzer"],
    "40-80 lbs":
        ["Labrador Retriever",
        "Golden Retriever",
        "Poodle",
        "Bulldog",
        "German Shorthaired Pointer",
        "Australian Shepherd",
        "Boxer",
        "Siberian Husky"],
    ">80 lbs":
        ["German Shepherd",
        "Rottweiler",
        "Doberman Pinscher",
        "Great Dane"]
    }

# dictionary of dog breeds based on activity
activity_dict = {
    "Low":
        ["French Bulldog",
        "Golden Retriever",
        "Bulldog",
        "Rottweiler",
        "Dachshund",
        "Cavalier King Charles Spaniel",
        "Miniature Schnauzer"],
    "Medium":
        ["Poodle",
        "Beagle",
        "Corgi",
        "Yorkshire Terrier",
        "Boxer",
        "Great Dane",
        "Bernese Mountain Dog"],
    "High":
        ["Labrador Retriever",
        "German Shepherd",
        "German Shorthaired Pointer"
        "Australian Shepherd",
        "Doberman Pinscher",
        "Siberian Husky"]
    }

# dictionary of dog breeds based on noise
noise_dict = {
    "Low":
        ["French Bulldog",
        "Golden Retriever",
        "Bulldog",
        "Rottweiler",
        ],
    "Medium":
        ["Labrador Retriever",
        "German Shepherd",
        "German Shorthaired Pointer"
        "Australian Shepherd",
        "Yorkshire Terrier",
        "Boxer",
        "Cavalier King Charles Spaniel",
        "Doberman Pinscher",
        "Great Dane",
        "Bernese Mountain Dog"],
    "High":
        ["Poodle",
        "Beagle",
        "Corgi",
        "Dachshund",
        "Miniature Schnauzer",
        "Siberian Husky"]
    }
# dictionary of dog breed to url ending
url_dict = {
    "Labrador Retriever": "labrador_retriever",
    "French Bulldog": "french_bulldog",
    "Golden Retriever":	"golden_retriever",
    "German Shepherd": "german_shepherd",
    "Poodle": "poodle",
    "Bulldog": "bulldog",
    "Beagle": "beagle",
    "Rottweiler": "rotweiler",
    "German Shorthaired Pointer": "german_shorthaired_pointer",
    "Dachshund": "dachshund",
    "Corgi": "pembroke_welsh_corgi",
    "Australian Shepherd": "australian_shepherd",
    "Yorkshire Terrier": "yorkshire_terrier",
    "Boxer": "boxer",
    "Cavalier King Charles Spaniel": "cavalier_king_charles_spaniel",
    "Doberman Pinscher": "doberman_pinscher",
    "Great Dane": "great_dane",
    "Miniature Schnauzer":	"miniature_schnauzer",
    "Siberian Husky": "siberian_husky",
    "Bernese Mountain":	"bernese_mountain"
}







# result window with no matching dogs
def exit_window():
    top = Toplevel()
    top.title("Dogs4U Result")
    top.iconbitmap('c:/users/corie/pycharmprojects/Dogs4U/2.ico')
    top.geometry("400x300")
    intro2 = "Based on the selected attributes, below is the recommended dog 4 U!"
    label_result1 = Label(top, text=intro2,)
    label_result1.grid(row=0, column=0, columnspan=3)
    result = "There are no dogs that match all the attributes"
    label_result2 = Label(top, text=result)
    label_result2.grid(row=2, column=1)
    label_close = Button(top, text="Try Again", command=top.destroy)
    label_close.grid(row=3,column=1)







# microservice url
restAPI = "http://natenate60.xyz:4004/"


# result window
def result_window():
    global top, label_photo, image_num, result, label_result2, result_list

    top = Toplevel()
    top.title("Dogs4U Result")
    top.iconbitmap('c:/users/corie/pycharmprojects/Dogs4U/2.ico')
    top.geometry("400x300")
    intro2 = "Based on the selected attributes, below is the recommended dog 4 U!"
    label_result1 = Label(top, text=intro2,)
    label_result1.grid(row=0, column=0, columnspan=3)

    # dog breed image
    image_num = 0
    result = result_list[image_num]
    response = restAPI+url_dict.get(result_list[image_num])
    get_image(response)                                         # calls function that interacts with image microservice
    label_photo = Label(top, image=photo)
    label_photo.grid(row=1, column=0, columnspan=3)
    label_result2 = Label(top, text=result)
    label_result2.grid(row=2, column=1)

    # buttons to scroll
    label_close = Button(top, text="Try Again", command=top.destroy)
    label_close.grid(row=3,column=1)
    label_next = Button(top, text=">>", command=lambda: forward(image_num+1))
    label_next.grid(row=3,column=2)
    label_previous = Button(top, text="<<", command=lambda: back(image_num-1))
    label_previous.grid(row=3,column=0)


def forward(next):
    global label_photo, label_next, response, image_num, label_result2, result_list

    if next >= len(result_list):
        label_next = Button(top, text=">>", state=DISABLED)
    else:
        image_num= next
        label_photo.grid_forget()
        label_result2.grid_forget()
        result = result_list[image_num]
        label_result2 = Label(top, text=result)
        label_result2.grid(row=2, column=1)
        response = restAPI+url_dict.get(result_list[image_num])
        get_image(response)
        label_photo = Label(top, image=photo)
        label_photo.grid(row=1, column=0, columnspan=3)


def back(previous):
    global label_photo, label_previous, response, image_num, label_result2, result_list

    if previous < 0:
        label_previous = Button(top, text="<<", state=DISABLED)
    else:
        image_num= previous
        label_photo.grid_forget()
        label_result2.grid_forget()
        result = result_list[image_num]
        label_result2 = Label(top, text=result)
        label_result2.grid(row=2, column=1)
        response = restAPI+url_dict.get(result_list[image_num])
        get_image(response)
        label_photo = Label(top, image=photo)
        label_photo.grid(row=1, column=0, columnspan=3)


def resize(photo_p):
    global width2, length2

    resize_w = 350
    resize_l = 210
    resize_r = 5/3
    a_ratio = photo_p.width()/photo_p.height()

    if a_ratio > resize_r:
        width2 = int(resize_w)
        length2 = int(resize_w/a_ratio)
    else:
        length2 = int(resize_l)
        width2 = int(resize_l*a_ratio)


def get_image(url):
    # calls on image microservice REST API to get link to image

    print("Getting image from " + url)
    global photo

    response = requests.get(url).text
    u = urlopen(response)
    raw_data = u.read()
    u.close()
    photo_p = ImageTk.PhotoImage(data=raw_data)
    resize(photo_p)
    r = requests.get(response)
    pilImage = Image.open(BytesIO(r.content))
    resized = pilImage.resize((width2,length2),Image.ANTIALIAS)
    photo = ImageTk.PhotoImage(resized)


root.mainloop()
