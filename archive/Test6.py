from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("icons, imager, exit")
# root.iconbitmap('image.ico')

my_img = ImageTk.PhotoImage(Image.open("1.JPG"))
my_label = Label(image=my_img)
my_label.pack()




button_quit = Button(root, text="Exit", command=root.quit)
button_quit.pack()

root.mainloop()