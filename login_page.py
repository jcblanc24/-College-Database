import tkinter as tk
import tkinter.ttk
from tkinter import *
from tkinter import messagebox


class Loging(tk.Frame):
    def __init__(self, master=None, **kw):
        super().__init__(master, **kw)
        self.master = master

        self.U_name = StringVar()
        self.Password = StringVar()

        self.create_frame()
        self.create_label()
        self.create_entry()
        self.create_button()

    def create_frame(self):
        self.Frame_1 = LabelFrame(self.master, relief='ridge', bg='aquamarine4', bd=15,
                                  font=('arial', 20, 'bold'))
        self.Frame_1.place(x=370, y=150, width=660, height=180)

        self.Frame_2 = LabelFrame(self.master, width=315, height=80, relief='ridge', bg='aquamarine4', bd=15,
                                  font=('arial', 20, 'bold'))
        self.Frame_2.place(x=530, y=335)

    def create_label(self):
        label_heading = Label(self.master, text='Database Login', font=('arial', 55, 'bold'), bg='aquamarine4',
                              fg='white')
        label_heading.place(x=420, y=50)

        label_username = Label(self.Frame_1, text='Username', font=('arial', 22, 'bold'), bg='aquamarine4',
                               fg='White', bd=20)
        label_username.place(x=0, y=0)

        pwd_label = Label(self.Frame_1, text='Password', font=('arial', 22, 'bold'), bg='aquamarine4',
                          fg='White', bd=20)
        pwd_label.place(x=0, y=60)

    def create_entry(self):
        self.username_entry = Entry(self.Frame_1, font=('arial', 20, 'bold'), textvariable=self.U_name)
        self.username_entry.focus()
        self.username_entry.place(x=200, y=15)

        self.password_entry = Entry(self.Frame_1, font=('arial', 20, 'bold'), show='*', textvariable=self.Password)
        self.password_entry.place(x=200, y=75)

    def Login(self):
        self.password_reference = "Blanc1"

        self.Uname = (self.U_name.get())
        self.Password_enter = (self.Password.get())

        if self.Uname == 'jcblanc' and self.Password_enter == self.password_reference:
            self.master.destroy()
            import menu_page
        else:
            if self.Password_enter != self.password_reference:
                tkinter.messagebox.showerror('Error', 'Wrong Password')
            if self.Uname != 'jcblanc':
                tkinter.messagebox.showerror('Error', 'Wrong Username')

            self.U_name.set("")
            self.Password.set("")

    def exit(self):
        Exit = tkinter.messagebox.askyesno("Logout System", "Confirm, if you want to Exit")
        if Exit > 0:
            self.master.destroy()
            return

    def create_button(self):
        self.button_conn = Button(self.Frame_2, text='Login', width=10, height=1, font=('Courier', 15, 'bold'),
                                  bg='aquamarine4', fg="White")
        self.button_conn.config(activebackground="#41B77F", relief=RAISED, command=self.Login)
        self.button_conn.place(x=5, y=5)

        self.button_quit = Button(self.Frame_2, text='Exit', width=10, height=1, font=('Courier', 15, 'bold'),
                                  bg='aquamarine4', fg="White", command=self.exit)
        self.button_quit.config(activebackground="#41B77F", relief=RAISED)
        self.button_quit.place(x=150, y=5)


root = tk.Tk()
root.geometry("1350x750")
root.resizable(False, False)
root.title("Université Espoir")
root.iconbitmap("logo1.ICO")
root.config(background="aquamarine4")

app = Loging(master=root)
app.mainloop()
