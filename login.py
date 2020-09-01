from tkinter import * #Tkinter is Python's de-facto standard GUI (Graphical User Interface) package. It is a thin object-oriented layer on top of Tcl/Tk. Tkinter is not the only GuiProgramming toolkit for Python.
from PIL import ImageTk #for jpg image
from tkinter import messagebox, ttk
import pymysql
class Login_System:
    def __init__(self, root):
        self.root = root
        self.root.title("Login")
        self.root.geometry("3840x2160+0+0")
        # for image
        self.bg_icon=ImageTk.PhotoImage(file="Images/evil.jpg")
        self.user_icon = ImageTk.PhotoImage(file="Images/user.png")
        self.pass_icon = ImageTk.PhotoImage(file="Images/download.png")
        #self.logo_icon = ImageTk.PhotoImage(file="Images/lg.png")
        #variables
        self.uname = StringVar()
        self.pname = StringVar()
        bglabel = Label(self.root, image=self.bg_icon).pack()
        title=Label(self.root,text="Login System", bg="yellow", font=("times new roman", 40, "bold"), fg="red")
        title.place(x=0,y=0,relwidth=1)
        Login_Frame=Frame(self.root,bg="white")
        Login_Frame.place(x=300,y=150)
        #logo=Label(Login_Frame,image=self.logo_icon).grid(row=0,column=0,pady=20)


        lbl_user = Label(Login_Frame,bg="white",text="USERNAME",image=self.user_icon,compound=LEFT,font=("times new roman",20,"bold")).grid(row=1, column=0, padx=20,pady=10)
        txtuser = Entry(Login_Frame,bd=5, relief=GROOVE, textvariable=self.uname, font=("",15),).grid(row=1,column=2,padx=20)
        lbl_pass = Label(Login_Frame,bg="white",text="PASSWORD",image=self.pass_icon,compound=LEFT,font=("times new roman" ,20, "bold")).grid(row=2, column=0, padx=20,pady=10)
        txtpass = Entry(Login_Frame, bd=5, relief=GROOVE, textvariable=self.pname, font=("", 15),).grid(row=2, column=2, padx=20)
        btn = Button(Login_Frame, text="LOGIN",command=self.log, font=("times new roman", 20, "bold"), bg="yellow", fg="red").grid(row=3, column=2, padx=20, pady=10)
        btn1 = Button(Login_Frame,text="Register new account", command=self.register_win,font=("times new roman", 20, "bold"), bg="yellow").grid(row=3, column=4, padx=2, pady=10)
        btn2 = Button(Login_Frame,text="Forget password", command=self.forget_password,font=("times new roman", 20, "bold"), bg="yellow").grid(row=5, column=4, padx=2, pady=10)


    def log(self):
        if self.uname.get() == "" or self.pname.get() == "":
            messagebox.showerror("Error", "All fields are required")

        else:
            con = pymysql.connect(host="localhost", user="root", password="", database="stm")
            cur = con.cursor() # a database cursor is a control structure that enables traversal over the records in a database
            cur.execute("select password from registration where email=%s ", self.uname.get())
            row = cur.fetchone()
            #print(row[0],self.pname.get())
            if row[0] == self.pname.get():

                messagebox.showinfo("SUCCESSFULY",f"welcome{self.uname.get()}")
                self.root.destroy()
                import student

            else:
                messagebox.showerror("Error","Incorrect info")

    def passwordfn(self):
        if self.combo_que.get() == "" or self.txt_password == "" or self.answer_var == "":
            messagebox.showerror("Error", "All fields are required",parent = self.root2)

        else:
            try:
                con = pymysql.connect(host="localhost", user="root", password="", database="stm")
                cur = con.cursor()  # it help to execute the query
                cur.execute("select * from registration where email=%s and question=%s and answer=%s ", (self.uname.get(),self.answer_var))
                row2 = cur.fetchone()
                if row2 == None:
                    messagebox.showerror("Error", "Please enter correct answer")
                else:
                    con = pymysql.connect(host="localhost", user="root", password="", database="stm")
                    cur = con.cursor()  # it help to execute the query
                    cur.execute("update registration set password = %s where email=%s",
                                (self.password, self.uname))

                    con.commit()  # save command in our database as it is
                    con.close()
                    messagebox.showinfo("Successful","Password update")


            except Exception as es:
                messagebox.showerror("Error", f"Error due to {str(es)}")

    def forget_password(self):
      if self.uname.get() == "":
        messagebox.showerror("Error","Please enter email",parent = self.root)


      else:
          try:
              con = pymysql.connect(host="localhost", user="root", password="", database="stm")
              cur = con.cursor() #it help to execute the query
              cur.execute("select * from registration where email=%s ", self.uname.get())
              row = cur.fetchone()
              if row == None:
                  messagebox.showerror("Error", "Please enter valid email")
              else:
                  self.root2 = Toplevel()  # this window will above login window
                  self.root2.title("Forget Password")
                  self.root2.geometry("400x400+400+400")
                  self.root2.focus_force()  # to focus curcor on this window
                  self.root2.grab_set()  # if we click outside this window our window wont disappear
                  t = Label(self.root2, text="Forget Password", bg="yellow", font=("times new roman", 40, "bold"),
                            fg="red").place(x=0, y=0, relwidth=1)

                  lbl_ques = Label(self.root2, bg="white", text="QUESTION", font=("times new roman", 15, "bold")).place(
                      x=0, y=200)

                  self.security_que = StringVar()
                  self.combo_que = ttk.Combobox(self.root2, textvariable=self.security_que,
                                                font=("times new roman", 15, "italic"), state="readonly")
                  self.combo_que["values"] = ("Pet Name", "Birth place", "Best Friend")
                  self.combo_que.place(x=150, y=200, width=200, height=30)

                  self.answer_var = StringVar()
                  lbl_answer = Label(self.root2, bg="white", text="ANSWER", font=("times new roman", 15, "bold")).place(
                      x=10, y=250)
                  self.txt_answer = Entry(self.root2, textvariable=self.answer_var, font=("", 15), ).place(x=150, y=250)

                  self.password = StringVar()
                  lbl_password = Label(self.root2, bg="white", text="Password",
                                       font=("times new roman", 15, "bold")).place(
                      x=10, y=300)
                  self.txt_password = Entry(self.root2, textvariable=self.password, font=("", 15), ).place(x=150,
                                                                                                             y=300)

                  btn3 = Button(self.root2, text="Change Password", command=self.passwordfn,
                                font=("times new roman", 20, "bold"), bg="yellow").place(
                      x=10, y=350)

                  con.commit()  # save command in our database as it is
                  con.close()


          except Exception as es:

              messagebox.showerror("Error", f"Error due to {str(es)}")








    def register_win(self):
        self.root.destroy()
        import register



A=Tk()
ob=Login_System(A)
A.mainloop() #A. mainloop() is a method on the main window which we execute when we want to run our application. This method will loop forever, waiting for events from the user, until the user exits the program – either by closing the window, or by terminating the program with a keyboard interrupt in the console.
