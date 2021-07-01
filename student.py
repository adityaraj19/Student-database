from tkinter import*
from  tkinter import ttk #provide combobox
import  pymysql
class student:
    def __init__(self,root):
        self.r=root
        self.r.title("Student Management System")
        self.r.geometry("3840x2160+0+0")
        title=Label(self.r,text="Student management System",bg="yellow",font=("times new roman",40,"bold"),fg="red")
        title.pack(side=TOP,fill=X)
        #------VARIABLES---------------------------------------------------------------


        self.roll_no = StringVar()
        self.name = StringVar()
        self.email = StringVar()
        self.dob = StringVar()
        self.Address = StringVar()
        self.gender = StringVar()
        self.contact = StringVar()
        self.search_by=StringVar()
        self.search_txt=StringVar()



        #-----------------------Frame1--------------------------------------------------

        Frame1=Frame(self.r,bd=4,relief=RIDGE,bg="blue")
        Frame1.place(x=0,y=70,width=450,height=700)
        f1_title=Label(Frame1,text="Manage Student",font=("times new roman",40,"bold"),bg="blue")
        f1_title.grid(row=0,column=0,pady=0)
        lbl_roll=Label(Frame1,text="Roll Number", font=("times new roman",20,"bold"),bg="blue")
        lbl_roll.grid(row=2,column=0,padx=20,pady=10,sticky="w")
        txt_roll=Entry(Frame1,textvar=self.roll_no,font=("times new roman",15,"bold"),relief=GROOVE, bd=5)
        txt_roll.place(x=200,y=85,width=200,height=30)


        lbl_name = Label(Frame1, text="Name", font=("times new roman", 20, "bold"), bg="blue")
        lbl_name.grid(row=4, column=0, padx=20, pady=10, sticky="w")
        txt_name = Entry(Frame1,textvar=self.name, font=("times new roman", 15, "bold"), relief=GROOVE, bd=5)
        txt_name.place(x=200, y=140, width=200, height=30)


        lbl_email = Label(Frame1, text="Email", font=("times new roman", 20, "bold"), bg="blue")
        lbl_email.grid(row=6, column=0, padx=20, pady=10, sticky="w")
        txt_email = Entry(Frame1,textvar=self.email, font=("times new roman", 15, "bold"), relief=GROOVE, bd=5)
        txt_email.place(x=200, y=190, width=200, height=30)

        lbl_gender = Label(Frame1, text="Gender", font=("times new roman", 20, "bold"), bg="blue")
        lbl_gender.grid(row=8, column=0, padx=20, pady=10, sticky="w")
        combo_gen= ttk.Combobox(Frame1,textvariable=self.gender,font=("times new roman", 15, "italic"),state="readonly")
        combo_gen["values"]=("Male","Female","Other")
        combo_gen.place(x=200,y=250,width=200, height=30)
        lbl_contact = Label(Frame1, text="Contact", font=("times new roman", 20, "bold"), bg="blue")
        lbl_contact.grid(row=10, column=0, padx=20, pady=10, sticky="w")
        txt_contact = Entry(Frame1,textvar=self.contact, font=("times new roman", 15, "bold"), relief=GROOVE, bd=5)
        txt_contact.place(x=200, y=310, width=200, height=30)

        lbl_dob = Label(Frame1, text="DOB", font=("times new roman", 20, "bold"), bg="blue")
        lbl_dob.grid(row=12, column=0, padx=20, pady=10, sticky="w")
        txt_dob = Entry(Frame1, textvar=self.dob,font=("times new roman", 15, "bold"), relief=GROOVE, bd=5)
        txt_dob.place(x=200, y=365, width=200, height=30)

        lbl_address = Label(Frame1, text="Address", font=("times new roman", 20, "bold"), bg="blue")
        lbl_address.grid(row=14, column=0, padx=20, pady=10, sticky="w")
        self.txt_address = Text(Frame1, font=("times new roman", 15, "bold"), relief=GROOVE, bd=5)
        self.txt_address.place(x=200, y=420, width=200, height=100)

        #-------------button---------------------------------------------------------------------------------------------
        btn_add = Button(Frame1,text="Add", font=("times new roman", 20, "bold"), bg="yellow",command=self.add_student).place(x=10,y=550, width=100, height=50)
        btn_delete = Button(Frame1,text="Delete", font=("times new roman", 20, "bold"), bg="yellow",command=self.delete_data).place(x=120,y=550, width=100, height=50)
        btn_update = Button(Frame1,text="Update", font=("times new roman", 20, "bold"), bg="yellow" , command=self.update).place(x=230,y=550, width=100, height=50)
        btn_clear = Button(Frame1,text="Clear", command=self.clear, font=("times new roman", 20, "bold"), bg="yellow").place(x=340,y=550, width=100, height=50)


        #-----------------------Frame2--------------------------------------------------

        Frame2 = Frame(self.r, bd=4, relief=RIDGE, bg="blue")
        Frame2.place(x=500, y=70, width=1000, height=700)
        lbl_search = Label(Frame2, text="Search By", font=("times new roman", 20, "bold"), bg="blue").grid(row=0, column=0, padx=20, pady=10, sticky="w")
        combo_search = ttk.Combobox(Frame2,textvariable=self.search_by, font=("times new roman", 15, "italic"), state="readonly")
        combo_search["values"] = ("Roll_no", "Name", "Contact")
        combo_search.place(x=150,y=15,width=150, height=30)


        txt_search = Entry(Frame2,textvariable=self.search_txt, font=("times new roman", 15, "bold"), relief=GROOVE, bd=5)
        txt_search.place(x=325, y=15, width=200, height=30)
        btn_search=Button(Frame2,text="Search",command=self.search, font=("times new roman", 15, "bold"), bg="yellow").place(x=550, y=15, width=100, height=25)
        btn_show=Button(Frame2,text="Show", command=self.fetch,font=("times new roman", 15, "bold"), bg="yellow").place(x=700,y=15, width=100, height=25)

        #----------Table Frame---------------------------------------------------------------------------------------------------------
        Tablef = Frame(Frame2, bd=4, relief=RIDGE, bg="blue")
        Tablef.place(x=0, y=70, width=994, height=625)
        scroll_x=Scrollbar(Tablef,orient=HORIZONTAL)
        scroll_y=Scrollbar(Tablef,orient=VERTICAL)

        self.S_table=ttk.Treeview(Tablef,columns=("Roll","Name","Email","Gender","Contact","DOB","Address"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.S_table.xview)
        scroll_y.config(command=self.S_table.yview)
        self.S_table.heading("Roll", text="Roll no.")
        self.S_table.heading("Name", text="Name")
        self.S_table.heading("Email", text="Email")
        self.S_table.heading("Contact", text="Contact")
        self.S_table.heading("Gender", text="Gender")
        self.S_table.heading("DOB", text="DOB")
        self.S_table.heading("Address", text="Address")
        self.S_table["show"]="headings"
        self.S_table.pack(fill=BOTH,expand=1)
        self.S_table.bind("<ButtonRelease-1>",self.cursor)
        self.fetch()


    def add_student(self):
        con=pymysql.connect(host="localhost",user="root",password="",database="stm")
        cun=con.cursor()
        cun.execute("insert into students values(%s,%s,%s,%s,%s,%s,%s)",
                    (
            self.roll_no.get(),
            self.name.get(),
            self.email.get(),
            self.gender.get(),
            self.contact.get(),
            self.dob.get(),
            self.txt_address.get("1.0",END)
        ))
        con.commit() #save query of database
        self.fetch()
        self.clear
        con.close()




    def fetch(self):
        con = pymysql.connect(host="localhost", user="root", password="", database="stm")
        cun = con.cursor()
        cun.execute("select * from students")
        rows=cun.fetchall()
        if len(rows)!=0:
            for row in rows:
                self.S_table.insert("",END,values=row)
                con.commit()
        con.close()




    def clear(self):
        self.roll_no.set("")
        self.name.set("")
        self.email.set("")
        self.gender.set("")
        self.dob.set("")
        self.contact.set("")
        self.txt_address.delete(1.0, END)



    def cursor(self, eve):
        cursor_row=self.S_table.focus()
        content=self.S_table.item(cursor_row)
        row=content["values"]
        self.roll_no.set(row[0])
        self.name.set(row[1])
        self.email.set(row[2])
        self.gender.set(row[3])
        self.dob.set(row[5])
        self.contact.set(row[4])
        self.txt_address.delete(1.0, END)
        self.txt_address.insert(END,row[6])



    def update(self):
        con = pymysql.connect(host="localhost", user="root", password="", database="stm")
        cun = con.cursor()
        cun.execute("update students name=%s,email=%s,contact=%s,gender=%s,dob=%s,address=%s where roll_no=%s",
                    (
                        self.name.get(),
                        self.email.get(),
                        self.contact.get(),
                        self.gender.get(),
                        self.dob.get(),
                        self.txt_address.get("1.0", END),
                        self.roll_no.get()

                    ))
        con.commit()
        self.fetch()
        self.clear
        con.close()



    def delete_data(self):
        con = pymysql.connect(host="localhost", user="root", password="", database="stm")
        cun = con.cursor()
        cun.execute("delete from students where roll_no=%s",self.roll_no.get())
        con.commit()
        con.close()
        self.fetch()
        self.clear()


    def search(self):
        con = pymysql.connect(host="localhost", user="root", password="", database="stm")
        cun = con.cursor()
        cun.execute("select * from students where"+str(self.search_by.get())+"LIKE %"+str(self.search_txt.get())+"%")
        rows=cun.fetchall()
        if len(rows) != 0:
            self.S_table.delete(*self.S_table.get_children())
            for row in rows:
                self.S_table.insert("",END,values=row)
                con.commit()
        con.close()












B=Tk()
ob=student(B)
B.mainloop()
