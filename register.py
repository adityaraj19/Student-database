from tkinter import *
from PIL import ImageTk
from tkinter import ttk
from tkinter import messagebox
import pymysql


class register:
    def __init__(self, root):
        self.root = root
        self.root.title("Registration")
        self.root.geometry("3840x2160+0+0")
        self.bg_icon = ImageTk.PhotoImage(file="Images/bck.jpg")
        bglabel = Label(self.root, image=self.bg_icon).place(x=495, y=0)

        self.left_icon = ImageTk.PhotoImage(file="Images/BG.jfif")
        bglabel = Label(self.root, image=self.left_icon).place(x=0, y=0)

        # ===========Frame================================================
        registration_Frame = Frame(self.root, bg="white")
        registration_Frame.place(x=500, y=150, width=1020, height=600)
        title = Label(registration_Frame, text="Registration", bg="white", font=("times new roman", 40, "bold"),
                      fg="green")
        title.place(x=200, y=10)

        self.fname_var = StringVar()
        lbl_fname = Label(registration_Frame, bg="white", text="FIRSTNAME", font=("times new roman", 15, "bold")).place(
            x=0, y=100)
        self.txt_fname = Entry(registration_Frame, textvariable=self.fname_var, font=("", 15), ).place(x=150, y=100)

        self.lname_var = StringVar()
        lbl_lname = Label(registration_Frame, bg="white", text="LASTNAME", font=("times new roman", 15, "bold")).place(
            x=500, y=100)
        self.txt_lname = Entry(registration_Frame, textvariable=self.lname_var, font=("", 15), ).place(x=700, y=100)

        self.contact_var = StringVar()
        lbl_contact = Label(registration_Frame, bg="white", text="CONTACT", font=("times new roman", 15, "bold")).place(
            x=0, y=150)
        self.txt_contact = Entry(registration_Frame, textvariable=self.contact_var, font=("", 15), ).place(x=150, y=150)

        self.email_var = StringVar()
        lbl_email = Label(registration_Frame, bg="white", text="EMAIL", font=("times new roman", 15, "bold")).place(
            x=500, y=150)
        self.txt_email = Entry(registration_Frame, textvariable=self.email_var, font=("", 15), ).place(x=700, y=150)

        lbl_ques = Label(registration_Frame, bg="white", text="QUESTION", font=("times new roman", 15, "bold")).place(
            x=0, y=200)

        self.security_que = StringVar()
        self.combo_que = ttk.Combobox(registration_Frame, textvariable=self.security_que,
                                      font=("times new roman", 15, "italic"), state="readonly")
        self.combo_que["values"] = ("Pet Name", "Birth place", "Best Friend")
        self.combo_que.place(x=150, y=200, width=200, height=30)

        self.answer_var = StringVar()
        lbl_answer = Label(registration_Frame, bg="white", text="ANSWER", font=("times new roman", 15, "bold")).place(
            x=500, y=200)
        self.txt_answer = Entry(registration_Frame, textvariable=self.answer_var, font=("", 15), ).place(x=700, y=200)

        self.password_var = StringVar()
        lbl_password = Label(registration_Frame, bg="white", text="PASSWORD",
                             font=("times new roman", 15, "bold")).place(
            x=0, y=250)
        self.txt_password = Entry(registration_Frame, textvariable=self.password_var, font=("", 15), ).place(x=150,
                                                                                                             y=250)

        self.confirmpass_var = StringVar()
        lbl_confirmpassword = Label(registration_Frame, bg="white", text="CONFIRM",
                                    font=("times new roman", 15, "bold")).place(
            x=500, y=250)
        self.txt_confirmpassword = Entry(registration_Frame, textvariable=self.confirmpass_var, font=("", 15), ).place(
            x=700, y=250)

        btn_register = Button(registration_Frame, command=self.register, text="REGISTER NOW",
                              font=("times new roman", 20, "bold"), cursor="hand2", bg="green").place(x=0, y=500,
                                                                                                      width=300)

        self.check_var = IntVar()
        check = Checkbutton(registration_Frame, onvalue=1, offvalue=0, text="I agree with terms and condition",
                            variable=self.check_var, bg="white", font=("times new roman", 20, "bold")).place(x=0, y=400)

        # =====anotherframe=======================================================================

        signup_Frame = Frame(self.root, bg="gray")
        signup_Frame.place(x=0, y=150, width=500, height=600)

        btn_sign = Button(signup_Frame,command=self.login_win, text="Sign up", font=("times new roman", 20, "bold"),
                          bg="green").place(x=0, y=500, width=300)

    def register(self):

        if self.fname_var.get() == "" or self.lname_var.get() == "" or self.email_var.get() == "" or self.contact_var.get() == "" or self.password_var.get() == "" or self.confirmpass_var.get() == "" or self.security_que.get() == "" or self.answer_var.get() == "" or self.security_que == "":
            messagebox.showerror("Error", "All fields are required")

        elif self.password_var.get() != self.confirmpass_var.get():
            messagebox.showerror("Error", "Password not matching")

        elif self.check_var.get() == 0:
            messagebox.showerror("Error", "Please agree to our terms and condition")


        else:
            try:
                con = pymysql.connect(host="localhost", user="root", password="", database="stm")
                cur = con.cursor()
                cur.execute("select email from registration where email=%s ", self.email_var.get())
                row = cur.fetchone()
                if row != None:
                    messagebox.showerror("Error", "Email already exist")
                else:

                    cur.execute(
                        "insert into registration (f_name,l_name,contact,email,question,answer,password) values(%s,%s,%s,%s,%s,%s,%s)",
                        (
                            self.fname_var.get(),
                            self.lname_var.get(),
                            self.contact_var.get(),
                            self.email_var.get(),
                            self.security_que.get(),
                            self.answer_var.get(),
                            self.password_var.get()
                        )
                        )
                    con.commit()  # save command in our database as it is
                    con.close()
                    messagebox.showinfo("REGISTRATION SUCCESSFULY", f"welcome {self.fname_var.get()}")


            except Exception as es:

                messagebox.showerror("Error", f"Error due to {str(es)}")

    def login_win(self):
        self.root.destroy()
        import login


root = Tk()
ob = register(root)
root.mainloop()

