from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("images")
root.geometry("800x500")

my_pic1 = Image.open("images/1.jpg")
resized1 = my_pic1.resize((300,225), Image.ANTIALIAS)

my_img1 = ImageTk.PhotoImage(resized1)

my_img2 = ImageTk.PhotoImage(Image.open("images/2.JPG"))
my_img3 = ImageTk.PhotoImage(Image.open("images/3.JPG"))
my_img4 = ImageTk.PhotoImage(Image.open("images/4.JPG"))

image_list = [my_img1, my_img2, my_img3, my_img4]

my_label = Label(image=my_img1)
my_label.grid(row=0,column=0, columnspan=3)


button_back = Button(root, text="<<")
button_exit = Button(root, text="EXIT PROGRAM", command = root.quit)
button_forward = Button(root, text=">>")

button_back.grid(row=1, column=0)
button_exit.grid(row=1, column=1)
button_forward.grid(row=1,column=2)


root.mainloop()