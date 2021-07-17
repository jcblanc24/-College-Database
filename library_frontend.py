import sqlite3
import time
import tkinter as tk
import tkinter.ttk
from tkinter import *
from tkinter import ttk
from tkcalendar import DateEntry
import library_backend
from tkinter import messagebox


class Library(tk.Frame):
    def __init__(self, master=None, **kw):
        super().__init__(master, **kw)
        self.master = master

        self.Member = StringVar()
        self.Reference = StringVar()
        self.FName = StringVar()
        self.LName = StringVar()
        self.Address = StringVar()
        self.Mobil = StringVar()
        self.ID_Book = StringVar()
        self.Book_Title = StringVar()
        self.Author = StringVar()
        self.Date_Borrowed = StringVar()
        self.Date_Due = StringVar()
        self.Day_Loan = StringVar()
        self.Editions = StringVar()
        self.Yr_Of_Pub = StringVar()
        self.List_of_Books = [' C', ' Operating System', ' Web Development', ' Data Science', ' Algorithms', ' Android']

        self.create_frame()
        self.create_label()
        self.create_entry()
        self.create_scroll_bar()
        self.create_button()
        self.display()

    def OneSelected(self, event):
        global id
        try:
            self.curItem = self.data_table.focus()
            self.contents = (self.data_table.item(self.curItem))
            self.selecteditem = self.contents['values']
            self.id = self.selecteditem[0]

            self.Member.set('')
            self.Member.set(self.selecteditem[1])

            self.Reference.set('')
            self.Reference.set(self.selecteditem[2])

            self.FName.set('')
            self.FName.set(self.selecteditem[3])

            self.LName.set('')
            self.LName.set(self.selecteditem[4])

            self.Address.set('')
            self.Address.set(self.selecteditem[5])

            self.Mobil.set('')
            self.Mobil.set(self.selecteditem[6])

            self.ID_Book.set('')
            self.ID_Book.set(self.selecteditem[7])

            self.Book_Title.set('')
            self.Book_Title.set(self.selecteditem[8])

            self.Author.set('')
            self.Author.set(self.selecteditem[9])

            self.Date_Borrowed.set('')
            self.Date_Borrowed.set(self.selecteditem[10])

            self.Date_Due.set('')
            self.Date_Due.set(self.selecteditem[11])

            self.Day_Loan.set('')
            self.Day_Loan.set(self.selecteditem[12])
        except IndexError:
            tkinter.messagebox.showwarning('', 'Please Select A Student !', icon="warning")

    def Save(self):
        if self.Member.get() == "" or self.Reference.get() == "" or self.FName.get() == "" or \
                self.LName.get() == "" or self.Address.get() == "" or self.Mobil.get() == "" or \
                self.ID_Book.get() == "" or self.Book_Title.get() == "" or self.Author.get() == "" or \
                self.Date_Borrowed.get() == "" or self.Date_Due.get() == "" or self.Day_Loan.get() == "":
            tkinter.messagebox.showwarning('', 'Please Complete The Required Field', icon="warning")
        else:
            library_backend.insert(self.Member.get(), self.Reference.get(), self.FName.get(),
                                   self.LName.get(), self.Address.get(), self.Mobil.get(),
                                   self.ID_Book.get(), self.Book_Title.get(), self.Author.get(),
                                   self.Date_Borrowed.get(), self.Date_Due.get(), self.Day_Loan.get())
            tkinter.messagebox.showinfo("Success", "Loan Saved Successfully")

    def display(self):
        if len(library_backend.view()) != 0:
            self.data_table.delete(*self.data_table.get_children())
            for row in library_backend.view():
                self.data_table.insert('', END, values=row)

    def Reset(self):
        self.Member.set('')
        self.Reference.set('')
        self.FName.set('')
        self.LName.set('')
        self.Address.set('')
        self.Mobil.set('')
        self.ID_Book.set('')
        self.Book_Title.set('')
        self.Author.set('')
        self.Day_Loan.set('')
        self.Display_Layout.delete('1.0', END)

    def Update(self):
        self.data_table.delete(*self.data_table.get_children())
        self.conn = sqlite3.connect('UE.db')
        self.cur = self.conn.cursor()
        self.cur.execute("UPDATE `fee` SET `member_type` = ?, `reference_no` = ?, `firstname` =?, `lastname` = ?,  "
                         "`address` = ?, `mobile_no` = ?, `ID_book` = ?, `title` = ?, `author` = ? WHERE `id` = ?",
                         (str(self.Member.get()), str(self.Reference.get()),
                          str(self.FName.get()), str(self.LName.get()),
                          str(self.Address.get()), str(self.Mobil.get()),
                          str(self.ID_Book.get()), str(self.Book_Title.get()),
                          str(self.Author.get()), str(id)))
        self.conn.commit()
        self.cur.execute("SELECT * FROM `fee` ORDER BY `name` ASC")
        self.fetch = self.cur.fetchall()
        for data in self.fetch:
            self.data_table.insert('', 'end', values=(data))
        self.cur.close()
        self.conn.close()

    def delete(self):
        if not self.data_table.selection():
            result = tkinter.messagebox.showwarning('', 'Please Select Something First!', icon="warning")
        else:
            result = tkinter.messagebox.askquestion('', 'Are you sure you want to delete this record?', icon="warning")
            if result == 'yes':
                self.curItem = self.data_table.focus()
                self.contents = (self.data_table.item(self.curItem))
                self.selecteditem = self.contents['values']
                self.data_table.delete(self.curItem)
                self.conn = sqlite3.connect("UE.db")
                self.cursor = self.conn.cursor()
                self.cursor.execute("DELETE FROM `library` WHERE `id` = %d" % self.selecteditem[0])
                self.conn.commit()
                self.cursor.close()
                self.conn.close()

    def exit(self):
        Exit = tkinter.messagebox.askyesno("Logout System", "Confirm, if you want to Exit")
        if Exit > 0:
            self.master.destroy()
            return

    def Details(self):
        self.Display_Layout.delete('1.0', END)
        self.Display_Layout.insert(END, '\n\n')
        self.Display_Layout.insert(END, 'Book ID: ' + self.ID_Book.get() + '\n')
        self.Display_Layout.insert(END, 'Title: ' + self.Book_Title.get() + '\n')
        self.Display_Layout.insert(END, 'Author:  ' + self.Author.get() + '\n')
        self.Display_Layout.insert(END, 'Edition: ' + self.Editions.get() + '\n')
        self.Display_Layout.insert(END, 'Year of Published: \t' + self.Yr_Of_Pub.get() + '\n')
        self.Display_Layout.insert(END, 'Date Borrowed: ' + self.Date_Borrowed.get() + '\n')
        self.Display_Layout.insert(END, 'Date Due:' + self.Date_Due.get() + '\n')
        self.Display_Layout.insert(END, 'Days in Loan: ' + self.Day_Loan.get() + '\n')

    def SelectedBook(self, event):
        value_List = str(self.book_list.get(self.book_list.curselection()))
        val = value_List

        if val == ' C':
            self.ID_Book.set('ISBN 525341')
            self.Book_Title.set('Programming using C')
            self.Author.set('Gail Guzon')
            self.Yr_Of_Pub.set('2019')
            self.Editions.set('5th')

            import datetime

            days1 = datetime.date.today()
            days2 = datetime.timedelta(days=14)
            days3 = (days1 + days2)
            self.Date_Borrowed.set(days1)
            self.Day_Loan.set('14')
            self.Date_Due.set(days3)
            self.Details()
        elif val == ' Operating System':
            self.ID_Book.set('ISBN 536453')
            self.Book_Title.set('OS Concepts ')
            self.Author.set('Marry Ann Goroy')
            self.Yr_Of_Pub.set('2019')
            self.Editions.set('4th')

            import datetime

            days1 = datetime.date.today()
            days2 = datetime.timedelta(days=12)
            days3 = (days1 + days2)
            self.Date_Borrowed.set(days1)
            self.Day_Loan.set('12')
            self.Date_Due.set(days3)
            self.Details()
        elif val == ' Web Development':
            self.ID_Book.set('ISBN 543548')
            self.Book_Title.set('Web Development ')
            self.Author.set('Jhazel Alarcon')
            self.Yr_Of_Pub.set('2019')
            self.Editions.set('3rd')

            import datetime

            days1 = datetime.date.today()
            days2 = datetime.timedelta(days=15)
            days3 = (days1 + days2)
            self.Date_Borrowed.set(days1)
            self.Day_Loan.set('15')
            self.Date_Due.set(days3)
            self.Details()
        elif val == ' Data Science':
            self.ID_Book.set('ISBN 835764')
            self.Book_Title.set('Data Science Concept ')
            self.Author.set('Ryan Manaay')
            self.Yr_Of_Pub.set('2019')
            self.Editions.set('3rd')

            import datetime

            days1 = datetime.date.today()
            days2 = datetime.timedelta(days=15)
            days3 = (days1 + days2)
            self.Date_Borrowed.set(days1)
            self.Day_Loan.set('15')
            self.Date_Due.set(days3)
            self.Details()
        elif val == ' Algorithms':
            self.ID_Book.set('ISBN 535674')
            self.Book_Title.set('Basics of Algorithm ')
            self.Author.set('Paul Angelo Niar')
            self.Yr_Of_Pub.set('2019')
            self.Editions.set('7th')

            import datetime

            days1 = datetime.date.today()
            days2 = datetime.timedelta(days=10)
            days3 = (days1 + days2)
            self.Date_Borrowed.set(days1)
            self.Day_Loan.set('10')
            self.Date_Due.set(days3)
            self.Details()
        elif val == ' Android':
            self.ID_Book.set('ISBN 356452')
            self.Book_Title.set('Android Programming')
            self.Author.set('Jomhel Dulla')
            self.Yr_Of_Pub.set('2019')
            self.Editions.set('4th')

            import datetime

            days1 = datetime.date.today()
            days2 = datetime.timedelta(days=9)
            days3 = (days1 + days2)
            self.Date_Borrowed.set(days1)
            self.Day_Loan.set('9')
            self.Date_Due.set(days3)
            self.Details()

    # -------------------------------- Frames -------------------------------------------------------
    def create_frame(self):
        global frame_title
        global Frame_2
        global Frame_3

        frame_title = Frame(self.master, bg="aquamarine4", bd=10, relief=SUNKEN)
        frame_title.pack()
        self.Main_Frame = LabelFrame(self.master, font=('Courier', 15, 'bold'),
                                     bg='aquamarine4', bd=15, fg='White', relief='ridge')
        self.Main_Frame.place(x=10, y=80, width=1330, height=350)

        self.Frame_1 = LabelFrame(self.master,
                                  font=('Courier', 15, 'bold'),
                                  relief='ridge', bd=10, bg='aquamarine4', fg='White', text='Library Membership Info')
        self.Frame_1.place(x=35, y=105, width=730, height=300)

        self.Frame_2 = LabelFrame(self.master,
                                  font=('Courier', 15, 'bold'),
                                  relief='ridge', bd=10, fg='White', bg='aquamarine4', text='Book Details')
        self.Frame_2.place(x=770, y=105, width=550, height=300)

        self.Frame_3 = LabelFrame(self.master, width=1180, height=70, font=('Courier', 10, 'bold'),
                                  bg='aquamarine4', relief='ridge', bd=13, fg='White')
        self.Frame_3.place(x=75, y=665)

        self.Frame_4 = LabelFrame(self.master, font=('Courier', 10, 'bold'),
                                  bg='aquamarine4', relief='ridge', bd=13, fg='White')
        self.Frame_4.place(x=22, y=450, width=1300, height=200)

    # -------------------------------- Labels -------------------------------------------------------
    def create_label(self):
        label_title1 = Label(frame_title, text='Library Management System', font=('Courier', 20, 'bold'),
                             bg='aquamarine4', fg='White').pack()

        self.label_member_type = Label(self.Frame_1, text='Member Type', font=('Courier', 16), bg='aquamarine4',
                                       fg='White')
        self.label_member_type.place(x=10, y=20)

        self.reference_label = Label(self.Frame_1, text='Reference No', font=('Courier', 16), bg='aquamarine4',
                                     fg='White')
        self.reference_label.place(x=10, y=60)

        self.label_fname = Label(self.Frame_1, text='First Name', font=('Courier', 16), bg='aquamarine4',
                                 fg='White')
        self.label_fname.place(x=10, y=100)

        self.label_lname = Label(self.Frame_1, text='Last Name', font=('Courier', 16), bg='aquamarine4',
                                 fg='White')
        self.label_lname.place(x=10, y=140)

        self.address_label = Label(self.Frame_1, text='Address', font=('Courier', 16), bg='aquamarine4',
                                   fg='White')
        self.address_label.place(x=10, y=180)

        self.mobil_label = Label(self.Frame_1, text='Mobil No', font=('Courier', 16), bg='aquamarine4',
                                 fg='White')
        self.mobil_label.place(x=10, y=220)

        self.id_book_label = Label(self.Frame_1, text='Book ID', font=('Courier', 16), bg='aquamarine4',
                                   fg='White')
        self.id_book_label.place(x=375, y=20)

        self.book_title_label = Label(self.Frame_1, text='Book Title', font=('Courier', 16), bg='aquamarine4',
                                      fg='White')
        self.book_title_label.place(x=375, y=60)

        self.author_label = Label(self.Frame_1, text='Author', font=('Courier', 16), bg='aquamarine4',
                                  fg='White')
        self.author_label.place(x=375, y=100)

        self.date_borrowed_label = Label(self.Frame_1, text='Date Borrowed', font=('Courier', 16), bg='aquamarine4',
                                         fg='White')
        self.date_borrowed_label.place(x=375, y=140)

        self.date_due_label = Label(self.Frame_1, text='Date Due', font=('Courier', 16), bg='aquamarine4',
                                    fg='White')
        self.date_due_label.place(x=375, y=180)

        self.day_in_loan_label = Label(self.Frame_1, text='Day in Loan', font=('Courier', 16), bg='aquamarine4',
                                       fg='White')
        self.day_in_loan_label.place(x=375, y=220)

    # -------------------------------- Entry -------------------------------------------------------
    def create_entry(self):
        self.Entry_member_type = ttk.Combobox(self.Frame_1, values=(' ', 'Student', 'Staff Member'),
                                              font=('arial', 10), textvariable=self.Member)
        self.Entry_member_type.place(x=190, y=20, width=145)

        self.Entry_reference = Entry(self.Frame_1, font=('arial', 10), textvariable=self.Reference)
        self.Entry_reference.place(x=190, y=60)

        self.Entry_fname = Entry(self.Frame_1, font=('arial', 10), textvariable=self.FName)
        self.Entry_fname.place(x=190, y=100)

        self.Entry_lname = Entry(self.Frame_1, font=('arial', 10), textvariable=self.LName)
        self.Entry_lname.place(x=190, y=140)

        self.Entry_address = Entry(self.Frame_1, font=('arial', 10), textvariable=self.Address)
        self.Entry_address.place(x=190, y=180)

        self.Entry_mobil = Entry(self.Frame_1, font=('arial', 10), textvariable=self.Mobil)
        self.Entry_mobil.place(x=190, y=220)

        self.Entry_id_book = Entry(self.Frame_1, font=('arial', 10), textvariable=self.ID_Book)
        self.Entry_id_book.place(x=560, y=20)

        self.Entry_book_title = Entry(self.Frame_1, font=('arial', 10), textvariable=self.Book_Title)
        self.Entry_book_title.place(x=560, y=60)

        self.Entry_author = Entry(self.Frame_1, font=('arial', 10), textvariable=self.Author)
        self.Entry_author.place(x=560, y=100)

        self.Entry_date_borrowed = DateEntry(self.Frame_1, font=('arial', 12), date_pattern='dd/mm/yyyy',
                                             textvariable=self.Date_Borrowed)
        self.Entry_date_borrowed.place(x=560, y=140, width=145)

        self.Entry_date_due = DateEntry(self.Frame_1, font=('arial', 12), date_pattern='dd/mm/yyyy',
                                        textvariable=self.Date_Due)
        self.Entry_date_due.place(x=560, y=180, width=145)

        self.Entry_day_loan = Entry(self.Frame_1, font=('arial', 10), textvariable=self.Day_Loan)
        self.Entry_day_loan.place(x=560, y=220)

    # -------------------------------- Scroll Bar And Text -------------------------------------------------------
    def create_scroll_bar(self):
        global data_table

        self.y_scroll1 = Scrollbar(self.Frame_2)
        self.y_scroll1.place(x=260, y=132, anchor=CENTER, height=265)

        self.book_list = Listbox(self.Frame_2, font=('arial', 13, 'bold'), bg='Azure2')
        self.book_list.bind('<<ListboxSelect>>', self.SelectedBook)
        self.book_list.place(x=0, y=0, width=255, height=265)
        self.y_scroll1.config(command=self.book_list.yview)

        self.Display_Layout = Text(self.Frame_2, font=('arial', 13, 'bold'), bg='Azure2')
        self.Display_Layout.place(x=270, y=0, width=260, height=265)

        self.x_scroll = Scrollbar(self.Frame_4, orient=HORIZONTAL)
        self.y_scroll = Scrollbar(self.Frame_4, orient=VERTICAL)
        self.data_table = tkinter.ttk.Treeview(self.Frame_4,
                                               column=('No', 'member', 'reference', 'fname', 'lname',
                                                       'address', 'mobil', 'book_id', 'book_title', 'author',
                                                       'date_borrowed', 'date_due', 'day_loan'),
                                               xscrollcommand=self.x_scroll.set, yscrollcommand=self.y_scroll.set)

        self.x_scroll.pack(side=BOTTOM, fill=X)
        self.y_scroll.pack(side=RIGHT, fill=Y)
        self.x_scroll.config(command=self.data_table.xview)
        self.y_scroll.config(command=self.data_table.yview)

        self.data_table.heading('No', text='No')
        self.data_table.heading('member', text='Member')
        self.data_table.heading('reference', text='Reference No')
        self.data_table.heading('fname', text='First Name')
        self.data_table.heading('lname', text='Last Name')
        self.data_table.heading('address', text='Address')
        self.data_table.heading('mobil', text='Mobil No')
        self.data_table.heading('book_id', text='Book ID')
        self.data_table.heading('book_title', text='Book Title')
        self.data_table.heading('author', text='Author')
        self.data_table.heading('date_borrowed', text='Date Borrowed')
        self.data_table.heading('date_due', text='Date Due')
        self.data_table.heading('day_loan', text='Day in Loan')
        self.data_table['show'] = 'headings'
        self.data_table.column('No', width=30)
        self.data_table.pack(fill=BOTH, expand=1)
        self.data_table.bind('<Double-Button-1>', self.OneSelected)

        for items in self.List_of_Books:
            self.book_list.insert(END, items)

    # -------------------------------- Button -------------------------------------------------------

    def create_button(self):
        self.button_save = Button(self.Frame_3, text="SAVE", font=('Courier', 15, 'bold'), bg='aquamarine4', fg="White",
                                  width=12, command=self.Save)
        self.button_save.place(x=5, y=2)
        self.button_save.config(activebackground="#41B77F", relief=RAISED)

        self.button_display = Button(self.Frame_3, text='DISPLAY', font=('Courier', 15, 'bold'), bg='aquamarine4',
                                     fg="White", width=12, command=self.display)
        self.button_display.place(x=170, y=2)
        self.button_display.config(activebackground="#41B77F", relief=RAISED)

        self.button_reset = Button(self.Frame_3, text='RESET', font=('Courier', 15, 'bold'), bg='aquamarine4',
                                   fg="White", width=12, command=self.Reset)
        self.button_reset.place(x=335, y=2)
        self.button_reset.config(activebackground="#41B77F", relief=RAISED)

        self.button_update = Button(self.Frame_3, text='UPDATE', font=('Courier', 15, 'bold'), bg='aquamarine4',
                                    fg="White", width=12, command=self.update)
        self.button_update.place(x=500, y=2)
        self.button_update.config(activebackground="#41B77F", relief=RAISED)

        self.button_delete = Button(self.Frame_3, text='DELETE', font=('Courier', 15, 'bold'), bg='aquamarine4',
                                    fg="White", width=12, command=self.delete)
        self.button_delete.place(x=665, y=2)
        self.button_delete.config(activebackground="#41B77F", relief=RAISED)

        self.button_SEARCH = Button(self.Frame_3, text='SEARCH', font=('Courier', 15, 'bold'), bg='aquamarine4',
                                    fg="White", width=12)
        self.button_SEARCH.place(x=830, y=2)
        self.button_SEARCH.config(activebackground="#41B77F", relief=RAISED)

        self.button_exit = Button(self.Frame_3, text='EXIT', font=('Courier', 15, 'bold'), bg='aquamarine4',
                                  fg="White", width=12, command=self.exit)
        self.button_exit.place(x=995, y=2)
        self.button_exit.config(activebackground="#41B77F", relief=RAISED)

        self.localtime = time.asctime(time.localtime(time.time()))
        self.lbl_time = Label(self.master, text=self.localtime, fg="white", font=("Courier", 16), bg="aquamarine4")
        self.lbl_time.place(x=1017, y=50)


root = tk.Tk()
root.geometry("1350x750")
root.resizable(False, False)
root.title("Université Espoir")
root.iconbitmap("logo1.ICO")
root.config(background="aquamarine4")

app = Library(master=root)
app.mainloop()
