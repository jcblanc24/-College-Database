import sqlite3
import time
import tkinter
import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkcalendar import DateEntry
from tkinter import messagebox
import receipt_backend


class Receipt(tk.Frame):
    def __init__(self, master=None, **kw):
        super().__init__(master, **kw)
        self.master = master
        self.pack()

        self.RECEIPT = StringVar()
        self.Student_Name = StringVar()
        self.Admission = StringVar()
        self.Date = StringVar()
        self.Branch = StringVar()
        self.Semester = StringVar()
        self.Total_amount = StringVar()
        self.Paid = StringVar()
        self.Balance = StringVar()

        self.create_frame()
        self.create_label()
        self.create_entry()
        self.create_scroll_bar()
        self.create_button()
        self.display()

    def OneSelected(self, event):
        global id
        try:
            self.curItem = self.receipt_table.focus()
            self.contents = (self.receipt_table.item(self.curItem))
            self.selecteditem = self.contents['values']
            self.id = self.selecteditem[0]

            self.RECEIPT.set('')
            self.RECEIPT.set(self.selecteditem[1])

            self.Student_Name.set('')
            self.Student_Name.set(self.selecteditem[2])

            self.Admission.set('')
            self.Admission.set(self.selecteditem[3])

            self.Date.set('')
            self.Date.set(self.selecteditem[4])

            self.Branch.set('')
            self.Branch.set(self.selecteditem[5])

            self.Semester.set('')
            self.Semester.set(self.selecteditem[6])

            self.Total_amount.set('')
            self.Total_amount.set(self.selecteditem[7])

            self.Paid.set('')
            self.Paid.set(self.selecteditem[8])

            self.Balance.set('')
            self.Balance.set(self.selecteditem[9])
        except IndexError:
            tkinter.messagebox.showwarning('', 'Please Select A Something !', icon="warning")

    def Save(self):
        if self.RECEIPT.get() == "" or self.Student_Name.get() == "" or self.Admission.get() == "" or \
                self.Date.get() == "" or self.Branch.get() == "" or self.Semester.get() == "" or \
                self.Total_amount.get() == "" or self.Paid.get() == "":
            tkinter.messagebox.showwarning('', 'Please Complete The Required Field', icon="warning")
        else:
            receipt_backend.insert(self.RECEIPT.get(), self.Student_Name.get(), self.Admission.get(),
                                   self.Date.get(), self.Branch.get(), self.Semester.get(),
                                   self.Total_amount.get(), self.Paid.get(), self.Balance.get())
            tkinter.messagebox.showinfo("Success", "Receipt Saved Successfully")

    def Update(self):
        self.receipt_table.delete(*self.receipt_table.get_children())
        self.conn = sqlite3.connect('UE.db')
        self.cur = self.conn.cursor()
        self.cur.execute("UPDATE `fee` SET `receipts` = ?, `name` = ?, `admin` =?, `date` = ?,  "
                         "`branch` = ?, `semester` = ?, `total` = ?, `paid` = ?, "
                         "`due` = ? WHERE `id` = ?",
                         (str(self.RECEIPT.get()), str(self.Student_Name.get()),
                          str(self.Admission.get()), str(self.Date.get()),
                          str(self.Branch.get()), str(self.Semester.get()),
                          str(self.Total_amount.get()), str(self.Paid.get()),
                          str(self.Balance.get()), str(id)))
        self.conn.commit()
        self.cur.execute("SELECT * FROM `fee` ORDER BY `name` ASC")
        self.fetch = self.cur.fetchall()
        for data in self.fetch:
            self.receipt_table.insert('', 'end', values=(data))
        self.cur.close()
        self.conn.close()

    def display(self):
        if len(receipt_backend.view()) != 0:
            self.receipt_table.delete(*self.receipt_table.get_children())
            for row in receipt_backend.view():
                self.receipt_table.insert('', END, values=row)

    def Reset(self):
        self.RECEIPT.set('')
        self.Student_Name.set('')
        self.Admission.set('')
        self.Branch.set('')
        self.Semester.set('')
        self.Paid.set('')
        self.Balance.set('')

    def delete(self):
        if not self.receipt_table.selection():
            result = tkinter.messagebox.showwarning('', 'Please Select Something First!', icon="warning")
        else:
            result = tkinter.messagebox.askquestion('', 'Are you sure you want to delete this record?', icon="warning")
            if result == 'yes':
                self.curItem = self.receipt_table.focus()
                self.contents = (self.receipt_table.item(self.curItem))
                self.selecteditem = self.contents['values']
                self.receipt_table.delete(self.curItem)
                self.conn = sqlite3.connect("UE.db")
                self.cursor = self.conn.cursor()
                self.cursor.execute("DELETE FROM `fee` WHERE `id` = %d" % self.selecteditem[0])
                self.conn.commit()
                self.cursor.close()
                self.conn.close()

    def Receipt(self):
        self.display_receipt.delete('1.0', END)
        self.display_receipt.insert(END, '\t\tRECEIPT' + '\n\n')
        self.display_receipt.insert(
            END, '\tReceipt No.\t      :' + self.RECEIPT.get() + '\n')
        self.display_receipt.insert(END, '\tStudent Name  :' +
                                    self.Student_Name.get() + '\n')
        self.display_receipt.insert(END, '\tAdmission No.\t:' +
                                    self.Admission.get() + '\n')
        self.display_receipt.insert(
            END, '\tDate\t          : ' + self.Date.get() + '\n')
        self.display_receipt.insert(
            END, '\tBranch\t          :' + self.Branch.get() + '\n')
        self.display_receipt.insert(
            END, '\tSemester \t        :' + self.Semester.get() + '\n\n')

        try:
            x1 = int(self.Total_amount.get())
            x2 = int(self.Paid.get())
            x3 = int(x1 - x2)

            self.display_receipt.insert(END, '\tTotal Amount  :' + str(x1) + '\n')
            self.display_receipt.insert(END, '\tPaid Amount   :' + str(x2) + '\n')
            self.display_receipt.insert(END, '\tBalance\t         :' + str(x3) + '\n')
            self.Balance.set(x3)
        except ValueError:
            pass

    def exit(self):
        Exit = tkinter.messagebox.askyesno("Logout System", "Confirm, if you want to Exit")
        if Exit > 0:
            self.master.destroy()
            return

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
                                  relief='ridge', bd=10, bg='aquamarine4', fg='White', text='INFORMATION')
        self.Frame_1.place(x=35, y=105, width=700, height=300)

        self.Frame_2 = LabelFrame(self.master,
                                  font=('Courier', 15, 'bold'),
                                  relief='ridge', bd=10, fg='White', bg='aquamarine4', text='FEE RECEIPT')
        self.Frame_2.place(x=770, y=105, width=550, height=300)

        self.Frame_3 = LabelFrame(self.master, width=1180, height=70, font=('Courier', 10, 'bold'),
                                  bg='aquamarine4', relief='ridge', bd=13, fg='White')
        self.Frame_3.place(x=75, y=665)

        self.Frame_4 = LabelFrame(self.master, font=('Courier', 10, 'bold'),
                                  bg='aquamarine4', relief='ridge', bd=13, fg='White')
        self.Frame_4.place(x=22, y=450, width=1300, height=200)

    # -------------------------------- Labels -------------------------------------------------------
    def create_label(self):
        label_title1 = Label(frame_title, text='FEE REPORT', font=('Courier', 20, 'bold'),
                             bg='aquamarine4', fg='White').pack()

        self.label_Receipt = Label(self.Frame_1, text='Receipt No', font=('Courier', 16), bg='aquamarine4',
                                   fg='White')
        self.label_Receipt.place(x=10, y=20)

        self.Student_name_label = Label(self.Frame_1, text='Student Name', font=('Courier', 16), bg='aquamarine4',
                                        fg='White')
        self.Student_name_label.place(x=10, y=60)

        self.label_Admission = Label(self.Frame_1, text='Admission No', font=('Courier', 16), bg='aquamarine4',
                                     fg='White')
        self.label_Admission.place(x=10, y=100)

        self.Date_label = Label(self.Frame_1, text='Date', font=('Courier', 16), bg='aquamarine4',
                                fg='White')
        self.Date_label.place(x=10, y=140)

        self.Branch_label = Label(self.Frame_1, text='Branch', font=('Courier', 16), bg='aquamarine4',
                                  fg='White')
        self.Branch_label.place(x=10, y=180)

        self.Semester_label = Label(self.Frame_1, text='Session', font=('Courier', 16), bg='aquamarine4',
                                    fg='White')
        self.Semester_label.place(x=10, y=220)

        self.TOTAL_AMOUNT_label = Label(self.Frame_1, text='TOTAL AMOUNT', font=('Courier', 16), bg='aquamarine4',
                                        fg='White')
        self.TOTAL_AMOUNT_label.place(x=375, y=100)

        self.PAID_label = Label(self.Frame_1, text='PAID AMOUNT', font=('Courier', 16), bg='aquamarine4',
                                fg='White')
        self.PAID_label.place(x=375, y=140)

        self.BALANCE_label = Label(self.Frame_1, text='BALANCE', font=('Courier', 16), bg='aquamarine4',
                                   fg='White')
        self.BALANCE_label.place(x=375, y=180)

    # -------------------------------- Entry -------------------------------------------------------
    def create_entry(self):
        self.Entry_receipt = Entry(self.Frame_1, font=('arial', 10), textvariable=self.RECEIPT)
        self.Entry_receipt.focus()
        self.Entry_receipt.place(x=190, y=20)

        self.Entry_StudentName = Entry(self.Frame_1, font=('arial', 10), textvariable=self.Student_Name)
        self.Entry_StudentName.place(x=190, y=60)

        self.Entry_Admission = Entry(self.Frame_1, font=('arial', 10), textvariable=self.Admission)
        self.Entry_Admission.place(x=190, y=100)

        self.Entry_date = DateEntry(self.Frame_1, font=('arial', 12), date_pattern='dd/mm/yyyy', textvariable=self.Date)
        self.Entry_date.place(x=190, y=140, width=145)

        self.Entry_branch = ttk.Combobox(self.Frame_1, values=(' ', 'Computer Science', 'Science Of Education',
                                                               'Business Management'),
                                         font=('arial', 10), width=21, textvariable=self.Branch)
        self.Entry_branch.place(x=190, y=180, width=145)

        self.Entry_semester = ttk.Combobox(self.Frame_1, values=(' ', 'FIRST', 'SECOND'),
                                           font=('arial', 10), textvariable=self.Semester)
        self.Entry_semester.place(x=190, y=220, width=145)

        self.Entry_total_amount = Entry(self.Frame_1, font=('arial', 12), bg='Azure2', textvariable=self.Total_amount,
                                        state='readonly')
        self.Entry_total_amount.place(x=540, y=100, width=100, height=25)
        self.Total_amount.set(24000)

        self.Entry_paid = Entry(self.Frame_1, font=('arial', 12), bg='Azure2', textvariable=self.Paid)
        self.Entry_paid.place(x=540, y=140, width=100, height=25)
        self.Paid.set(0.0)

        self.Entry_balance = Entry(self.Frame_1, font=('arial', 12), bg='Azure2', textvariable=self.Balance, )
        self.Entry_balance.place(x=540, y=180, width=100, height=25)
        self.Balance.set(0.0)

    # -------------------------------- Scroll Bar And Text -------------------------------------------------------
    def create_scroll_bar(self):
        global receipt_table
        global display_receipt

        self.x_scroll = Scrollbar(self.Frame_4, orient=HORIZONTAL)
        self.y_scroll = Scrollbar(self.Frame_4, orient=VERTICAL)
        self.receipt_table = tkinter.ttk.Treeview(self.Frame_4,
                                                  column=('No', 'receipt_no', 'student_name', 'admission_no', 'date',
                                                          'branch', 'semester', 'total_amount', 'paid_amount'),
                                                  xscrollcommand=self.x_scroll.set, yscrollcommand=self.y_scroll.set)

        self.x_scroll.pack(side=BOTTOM, fill=X)
        self.y_scroll.pack(side=RIGHT, fill=Y)
        self.x_scroll.config(command=self.receipt_table.xview)
        self.y_scroll.config(command=self.receipt_table.yview)

        self.receipt_table.heading('receipt_no', text='Receipt No')
        self.receipt_table.heading('student_name', text='Student Name')
        self.receipt_table.heading('admission_no', text='Admission No')
        self.receipt_table.heading('date', text='Date')
        self.receipt_table.heading('branch', text='Branch')
        self.receipt_table.heading('semester', text='Semester')
        self.receipt_table.heading('total_amount', text='Total Amount')
        self.receipt_table.heading('paid_amount', text='Paid Amount')
        self.receipt_table.heading('No', text='No')
        self.receipt_table['show'] = 'headings'
        self.receipt_table.column('receipt_no', width=70)
        self.receipt_table.column('No', width=30)
        self.receipt_table.pack(fill=BOTH, expand=1)
        self.receipt_table.bind('<Double-Button-1>', self.OneSelected)

        self.display_receipt = Text(self.Frame_2, font=('arial', 14, 'bold'), bg='Azure2')
        self.display_receipt.place(x=0, y=0, width=530, height=265)

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
                                    fg="White", width=12, command=self.Update)
        self.button_update.place(x=500, y=2)
        self.button_update.config(activebackground="#41B77F", relief=RAISED)

        self.button_delete = Button(self.Frame_3, text='DELETE', font=('Courier', 15, 'bold'), bg='aquamarine4',
                                    fg="White", width=12, command=self.delete)
        self.button_delete.place(x=665, y=2)
        self.button_delete.config(activebackground="#41B77F", relief=RAISED)

        self.button_receipt = Button(self.Frame_3, text='RECEIPT', font=('Courier', 15, 'bold'), bg='aquamarine4',
                                     fg="White", width=12, command=self.Receipt)
        self.button_receipt.place(x=830, y=2)
        self.button_receipt.config(activebackground="#41B77F", relief=RAISED)

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

app = Receipt(master=root)
app.mainloop()
