import sqlite3
from tkinter import *

root = Tk()
root.geometry("400x400")


#Create a database or connect to one
conn = sqlite3.connect('address_book.db')


#create a cursor
c = conn.cursor()


#create table
'''
c.execute("""CREATE TABLE addresses (
        first_name text,
        last_name text,
        address text,
        city text,
        state text,
        zipcode integer
        )""")
'''

#Create Submit Function
def submit():
        #Create a database or connect to one
        conn = sqlite3.connect('address_book.db')
        #create a cursor
        c = conn.cursor()
        c.execute("INSERT INTO addresses VALUES (:fentry,:lentry,:aentry,:centry,:sentry,:zentry)",
                {
                        'fentry': fentry.get(),
                        'lentry': lentry.get(),
                        'aentry': aentry.get(),
                        'centry': centry.get(),
                        'sentry': sentry.get(),
                        'zentry': zentry.get()
                }

                )
        #clear the text boxes
        fentry.delete(0,END)
        lentry.delete(0,END)
        aentry.delete(0,END)
        centry.delete(0,END)
        sentry.delete(0,END)
        zentry.delete(0,END)
        #commit changes
        conn.commit()
        #Close connection
        conn.close()

#create query function
def query():
        #Create a database or connect to one
        conn = sqlite3.connect('address_book.db')
        #create a cursor
        c = conn.cursor()
        #query the data base
        c.execute("SELECT *, oid FROM addresses")
        records = c.fetchall()
        #print (records)

        #loop through results
        print_records = " "
        for record in records:
                print_records += str(record) + "\n"
        query_label = Label(root,text=print_records)
        query_label.grid(row=8,column=0,columnspan=2)
        #commit changes
        conn.commit()
        #Close connection
        conn.close()





#create textboxes
fentry = Entry(root,width=30)
lentry = Entry(root,width=30)
aentry = Entry(root,width=30)
centry = Entry(root,width=30)
sentry = Entry(root,width=30)
zentry = Entry(root,width=30)

fentry.grid(row=0,column=1)
lentry.grid(row=1,column=1)
aentry.grid(row=2,column=1)
centry.grid(row=3,column=1)
sentry.grid(row=4,column=1)
zentry.grid(row=5,column=1)

#create text box lables
flabel = Label(root,text="First name")
llabel = Label(root,text="Last name")
alabel = Label(root,text="Address")
clabel = Label(root,text="City")
slabel = Label(root,text="State")
zlabel = Label(root,text="Zip Code")

flabel.grid(row=0,column=0)
llabel.grid(row=1,column=0)
alabel.grid(row=2,column=0)
clabel.grid(row=3,column=0)
slabel.grid(row=4,column=0)
zlabel.grid(row=5,column=0)

#create submit button
submit_btn = Button(root,text="Add Record To Database",command=submit)
submit_btn.grid(row=6,column=0,columnspan=2,pady=10,padx=10,ipadx=100)

#Create a query  button
qbutton = Button(root,text="Show Records",command=query)
qbutton.grid(row=7,column=0,columnspan=2,pady=10,padx=10,ipadx=137)

#commit changes
conn.commit()

#Close connection
conn.close()


root.mainloop()
