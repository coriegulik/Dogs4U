from tkinter import *
from tkinter import ttk
import sqlite3

root = Tk()
root.title("Dogs4U")
root.geometry("800x500")




label_title = Label(root, text="Dogs4U", )
label_title.grid(row=0,column=1,columnspan=6)



# create table
# c.execute("""CREATE TABLE addresses(
#         first_name text,
#         last_name text,
#         address text,
#         city text
#         state text,
#         zipcode integer
#         )""")



# Create submit funciton for database
def submit():
    #Clear the Text Boxes
    f_name.delete(0, END)
    l_name.delete(0, END)
    address.delete(0, END)
    city.delete(0, END)
    state.delete(0, END)
    zipcode.delete(0, END)

    # create or connect to a database
    conn = sqlite3.connect('address_book.db')

    # create cursor
    c = conn.cursor()

    #insert into table
    c.execute("INSERT INTO addresses VALUES (:f_name1, :l_name1, :address1, :city1, :state1, :zipcode1)",
            {
                'f_name1': f_name.get(),
                'l_name1': l_name.get(),
                'address1': address.get(),
                'city1': city.get(),
                'state1': state.get(),
                'zipcode1': zipcode.get()
            })


    # commit changes
    conn.commit()

    # close connection
    conn.close()

# create text boxes
f_name = Entry(root, width=30)
f_name.grid(row=0, column=1, padx=20)

l_name = Entry(root, width=30)
l_name.grid(row=1, column=1)

address = Entry(root, width=30)
address.grid(row=2, column=1)

city = Entry(root, width=30)
city.grid(row=3, column=1)

state = Entry(root, width=30)
state.grid(row=4, column=1)

zipcode = Entry(root, width=30)
zipcode.grid(row=5, column=1)

#create text box labels
f_name_label = Label(root, text="First Name")
f_name_label.grid(row=0, column=0)

l_name_label = Label(root, text="Last Name")
l_name_label.grid(row=1, column=0)

address_label = Label(root, text="address")
address_label.grid(row=2, column=0)

city_label = Label(root, text="city")
city_label.grid(row=3, column=0)

state_label = Label(root, text="state")
state_label.grid(row=4, column=0)

zipcode_label = Label(root, text="zipcode")
zipcode_label.grid(row=5, column=0)

# create submit button
submit_btn = Button(root, text="Add Record to Database", command=submit)
submit_btn.grid(row=6, column=0, columnspan=2, pady=10, padx=10, ipadx=100)




root.mainloop()
