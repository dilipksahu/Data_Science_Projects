# Create A GUI to insert and show students from database
from tkinter import *
from tkinter import ttk
import pymysql
from tkinter import messagebox

class student:
    def __init__(self, root):
        self.root = root
        self.root.title("Student Management System")
        self.root.geometry("1360x700+0+0")
        root.tk.call('wm', 'iconphoto', root._w, PhotoImage(file='edit.png'))

        title = Label(self.root, text="Student Management System", bd=10, relief=GROOVE, font="lucida 40 bold",
                      bg="yellow", fg="red")
        title.pack(side=TOP, fill=X)

        # ********All Variables**********
        self.Roll_No = StringVar()
        self.name = StringVar()
        self.email = StringVar()
        self.gender = StringVar()
        self.contact = StringVar()
        self.dob = StringVar()
        self.Address=StringVar()
        self.search_by = StringVar()
        self.search_txt = StringVar()

        # *****************Manage Frames*******************
        frame = Frame(self.root, bd=4, relief=RIDGE, bg="crimson")
        frame.place(x=20, y=100, width=430, height=580)

        m_title = Label(frame, text="Manage Students Details", font="lucida 20 bold", bg="crimson", fg="white")
        m_title.grid(row=0, columnspan=2, pady=10)

        lbl_roll = Label(frame, text="Roll No.", bg="crimson", fg="white", font="lucida 15 bold")
        lbl_roll.grid(row=1, column=0, pady=10, padx=20, sticky='w')

        txt_Roll = Entry(frame, textvariable=self.Roll_No, font="lucida 15 bold", bd=5, relief=GROOVE)
        txt_Roll.grid(row=1, column=1, pady=10, padx=20, sticky='w')

        lbl_name = Label(frame, text="Name", bg="crimson", fg="white", font="lucida 15 bold")
        lbl_name.grid(row=2, column=0, pady=10, padx=20, sticky='w')

        txt_name = Entry(frame, textvariable=self.name, font="lucida 15 bold", bd=5, relief=GROOVE)
        txt_name.grid(row=2, column=1, pady=10, padx=20, sticky='w')

        lbl_Email = Label(frame, text="Email", bg="crimson", fg="white", font="lucida 15 bold")
        lbl_Email.grid(row=3, column=0, pady=10, padx=20, sticky='w')

        txt_Email = Entry(frame, textvariable=self.email, font="lucida 15 bold", bd=5, relief=GROOVE)
        txt_Email.grid(row=3, column=1, pady=10, padx=20, sticky='w')

        lbl_Gender = Label(frame, text="Gender", bg="crimson", fg="white", font="lucida 15 bold")
        lbl_Gender.grid(row=4, column=0, pady=10, padx=20, sticky='w')

        combo_gender = ttk.Combobox(frame, textvariable=self.gender, font="lucida 15 bold", state='readonly', width=19)
        combo_gender['values'] = ("Male", "Female", "Other")
        combo_gender.grid(row=4, column=1, pady=10, padx=20)

        lbl_Contact = Label(frame, text="Contact No.", bg="crimson", fg="white", font="lucida 15 bold")
        lbl_Contact.grid(row=5, column=0, pady=10, padx=20, sticky='w')

        txt_Contact = Entry(frame, text=self.contact, font="lucida 15 bold", bd=5, relief=GROOVE)
        txt_Contact.grid(row=5, column=1, pady=10, padx=20, sticky='w')

        lbl_Dob = Label(frame, text="D.O.B", bg="crimson", fg="white", font="lucida 15 bold")
        lbl_Dob.grid(row=6, column=0, pady=10, padx=20, sticky='w')

        txt_Dob = Entry(frame, text=self.dob, font="lucida 15 bold", bd=5, relief=GROOVE)
        txt_Dob.grid(row=6, column=1, pady=10, padx=20, sticky='w')

        lbl_Address = Label(frame, text="Address.", bg="crimson", fg="white", font="lucida 15 bold")
        lbl_Address.grid(row=7, column=0, pady=10, padx=20, sticky='w')

        txt_Address =  Entry(frame,textvariable=self.Address,  font="lucida 10 bold", bd=5, relief=SUNKEN)
        txt_Address.grid(row=7, column=1,ipadx=39,ipady=15, pady=10, padx=20, sticky='w')

        # ********************Buttons Frame*************************************
        btn_Frame = Frame(frame, bd=4, relief=RIDGE, bg="crimson")
        btn_Frame.place(x=15, y=500, width=420)

        Addbtn = Button(btn_Frame, text="Add", width=10, command=self.add_students).grid(row=0, column=0, padx=10,
                                                                                         pady=10)
        updatebtn = Button(btn_Frame, text="Update", width=10, command=self.update_data).grid(row=0, column=1, padx=10,
                                                                                              pady=10)
        deletebtn = Button(btn_Frame, text="Delete", width=10, command=self.delete_data).grid(row=0, column=2, padx=10,
                                                                                              pady=10)
        Clearbtn = Button(btn_Frame, text="Clear", width=10, command=self.clear_data).grid(row=0, column=3, padx=10,
                                                                                           pady=10)

        # ********************Detail Frame******************************
        Detail_Frame = Frame(self.root, bd=4, relief=RIDGE, bg="crimson")
        Detail_Frame.place(x=500, y=100, width=800, height=580)

        lbl_search = Label(Detail_Frame, text="Search BY", bg="crimson", fg="white", font="lucida 20 bold")
        lbl_search.grid(row=0, column=0, pady=10, padx=20, sticky="w")

        combo_search = ttk.Combobox(Detail_Frame, textvariable=self.search_by, width=10, font="lucida 13 bold",
                                    state="readonly")
        combo_search["values"] = ("Roll_No", "Name", "Contact")
        combo_search.grid(row=0, column=1, pady=10, padx=20)

        txt_search = Entry(Detail_Frame, textvariable=self.search_txt, width=20, bd=5, relief=GROOVE,
                           font="lucida 10 bold")
        txt_search.grid(row=0, column=2, pady=10, padx=20)

        searchbtn = Button(Detail_Frame, text="Search", width=10, pady=5, command=self.search_data).grid(row=0,
                                                                                                         column=3,
                                                                                                         pady=10,
                                                                                                         padx=10)
        showallbtn = Button(Detail_Frame, text="Show All", width=10, pady=5, command=self.fetch_data).grid(row=0,
                                                                                                           column=4,
                                                                                                           pady=10,
                                                                                                           padx=10)

        # ******************Table Frame****************************
        Table_Frame = Frame(Detail_Frame, bd=4, relief=RIDGE, bg="crimson")
        Table_Frame.place(x=10, y=70, width=760, height=500)

        scroll_x = Scrollbar(Table_Frame, orient=HORIZONTAL)
        scroll_y = Scrollbar(Table_Frame, orient=VERTICAL)
        self.Student_table = ttk.Treeview(Table_Frame,
                                          columns=("roll_no", "name", "email", "gender", "contact", "dob", "address"),
                                          xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.Student_table.xview)
        scroll_y.config(command=self.Student_table.yview)
        self.Student_table.heading("roll_no", text="Roll No.")
        self.Student_table.heading("name", text="Name")
        self.Student_table.heading("email", text="Email")
        self.Student_table.heading("gender", text="Gender")
        self.Student_table.heading("contact", text="Contact")
        self.Student_table.heading("dob", text="D.O.B")
        self.Student_table.heading("address", text="Address")
        self.Student_table["show"] = "headings"
        self.Student_table.column("roll_no", width=100)
        self.Student_table.column("name", width=100)
        self.Student_table.column("email", width=100)
        self.Student_table.column("gender", width=100)
        self.Student_table.column("contact", width=100)
        self.Student_table.column("dob", width=100)
        self.Student_table.column("address", width=150)
        self.Student_table.pack(fill=BOTH, expand=1)
        self.Student_table.bind("<ButtonRelease-1>", self.get_cursor)
        self.fetch_data()

    def add_students(self):
        if self.Roll_No.get() == "" or self.name.get() == "" or self.email.get() == "" or self.gender.get() == "" or self.contact.get() == "" or self.dob.get()=="" or self.Address.get()=="":
            messagebox.showerror("Error","All fields are required...!!!")
        #if self.Address.get()== "":
            #messagebox.showerror("Error","All fields are required...!!!")
        else:
            db = pymysql.connect(host='localhost', user='root', password='', database='student')
            cur = db.cursor()
            # cur.execute("insert into studentinfo values(%s,%s, %s, %s, %s, %s%, %s)", (self.Roll_No.get(),
                                                                                      # self.name.get(), self.email.get(),
                                                                                      # self.gender.get(), self.contact.get(),
                                                                                      # self.dob.get(),
                                                                                      # self.Address.get()))
                                                                                      
            cur.execute("insert into studentinfo values('{}','{}','{}','{}','{}','{}','{}')".format(self.Roll_No.get(),
                                                                                      self.name.get(), self.email.get(),
                                                                                      self.gender.get(), self.contact.get(),
                                                                                      self.dob.get(),
                                                                                      self.Address.get()))
            db.commit()
            self.fetch_data()
            self.clear_data()
            db.close()

    def fetch_data(self):
        db = pymysql.connect(host='localhost', user='root', password='', database='student')
        cur = db.cursor()
        cur.execute("select * from studentinfo")
        rows = cur.fetchall()
        if len(rows) != 0:
            self.Student_table.delete(*self.Student_table.get_children())
            for row in rows:
                self.Student_table.insert("", END, values=row)
            db.commit()
        db.close()

    def clear_data(self):
        self.Roll_No.set("")
        self.name.set("")
        self.email.set("")
        self.gender.set("")
        self.contact.set("")
        self.dob.set("")
        self.Address.set("")
        #self.txt_Address.delete("1.0", END)

    def get_cursor(self, ev):
        cursor_row = self.Student_table.focus()
        contents = self.Student_table.item(cursor_row)
        row = contents["values"]
        self.Roll_No.set(row[0])
        self.name.set(row[1])
        self.email.set(row[2])
        self.gender.set(row[3])
        self.contact.set(row[4])
        self.dob.set(row[5])
        self.Address.set(row[6])
        #self.txt_Address.delete("1.0", END)
        #self.txt_Address.insert(END, row[6])

    def update_data(self):
        db = pymysql.connect(host='localhost', user='root', password='', database='student')
        cur = db.cursor()
        cur.execute("update studentinfo set name=%s,email=%s,gender=%s,contact= %s,dob=%s,address=%s where roll_No=%s",
                    (self.name.get(),
                     self.email.get(), self.gender.get(), self.contact.get(), self.dob.get(),
                     self.Address.get(), self.Roll_No.get()))

        db.commit()
        self.fetch_data()
        self.clear_data()
        db.close()

    def delete_data(self):
        db = pymysql.connect(host='localhost', user='root', password='', database='student')
        cur = db.cursor()
        cur.execute("delete from studentinfo where roll_No=%s", self.Roll_No.get())
        db.commit()
        db.close()
        self.fetch_data()
        self.clear_data()

    def search_data(self):
        db = pymysql.connect(host='localhost', user='root', password='', database='student')
        cur = db.cursor()
        #cur.execute("SELECT * FROM studentinfo WHERE str(self.search_by.get()) LIKE %str(self.search_txt.get())% ")
        cur.execute("SELECT * FROM studentinfo WHERE {} = '{}'".format((self.search_by.get()),(self.search_txt.get())))
        rows = cur.fetchall()
        if len(rows) != 0:
            self.Student_table.delete(*self.Student_table.get_children())
            # self.Student_table.insert('',END,values=rows[0],rows[1],rows[2],rows[3],rows[4],rows[5],rows[6])
            for row in rows:
                self.Student_table.insert('', END, values=row)
            db.commit()
        db.close()


root = Tk()
obj = student(root)
root.mainloop()
