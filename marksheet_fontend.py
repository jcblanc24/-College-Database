import sqlite3
import time
import tkinter
import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkcalendar import DateEntry
import marcksheet_backend
from tkinter import messagebox


class MarkingSheet(tk.Frame):
    def __init__(self, master=None, **kw):
        super().__init__(master, **kw)
        self.master = master

        self.Name = StringVar()
        self.ID_s = StringVar()
        self.Branch = StringVar()
        self.Date = StringVar()
        self.Session = StringVar()
        self.Address = StringVar()
        self.Contact = StringVar()
        self.Email = StringVar()
        self.marks1 = DoubleVar()
        self.marks2 = DoubleVar()
        self.marks3 = DoubleVar()
        self.marks4 = DoubleVar()
        self.marks5 = DoubleVar()
        self.grand_tot = DoubleVar()
        self.percentage = DoubleVar()
        self.cgpa = DoubleVar()
        self.grade = StringVar()
        self.division = StringVar()
        self.result = StringVar()
        self.variables_1 = StringVar(value='65')
        self.variables_2 = StringVar(value='100')
        self.variables_3 = StringVar(value='500')

        self.create_frame()
        self.create_label()
        self.create_entry()
        self.create_button()
        self.create_scroll_bar()
        self.display()

    def OneSelected(self, event):
        global id
        try:
            self.curItem = self.marks_table.focus()
            self.contents = (self.marks_table.item(self.curItem))
            self.selecteditem = self.contents['values']
            self.id = self.selecteditem[0]

            self.Name.set('')
            self.Name.set(self.selecteditem[1])

            self.ID_s.set('')
            self.ID_s.set(self.selecteditem[2])

            self.Branch.set('')
            self.Branch.set(self.selecteditem[3])

            self.Date.set('')
            self.Date.set(self.selecteditem[4])

            self.Session.set('')
            self.Session.set(self.selecteditem[5])

            self.Address.set('')
            self.Address.set(self.selecteditem[6])

            self.Contact.set('')
            self.Contact.set(self.selecteditem[7])

            self.Email.set('')
            self.Email.set(self.selecteditem[8])

            self.marks1.set('')
            self.marks1.set(self.selecteditem[9])

            self.marks2.set('')
            self.marks2.set(self.selecteditem[10])

            self.marks3.set('')
            self.marks3.set(self.selecteditem[11])

            self.marks4.set('')
            self.marks4.set(self.selecteditem[12])

            self.marks5.set('')
            self.marks5.set(self.selecteditem[13])
        except IndexError:
            tkinter.messagebox.showwarning('', 'Please Select A Student !', icon="warning")

    def save(self):
        if self.Name.get() == "" or self.ID_s.get() == "" or self.Branch.get() == "" or \
                self.Date.get() == "" or self.Session.get() == "" or self.Address.get() == "" or \
                self.Contact.get() == "" or self.Email.get() == "":
            tkinter.messagebox.showwarning('', 'Please Complete The Required Field', icon="warning")
        else:
            try:
                marcksheet_backend.insert(self.Name.get(), self.ID_s.get(), self.Branch.get(),
                                          self.Date.get(), self.Session.get(), self.Address.get(),
                                          self.Contact.get(), self.Email.get(), self.marks1.get(),
                                          self.marks2.get(), self.marks3.get(), self.marks4.get(),
                                          self.marks5.get(), self.grand_tot.get(),
                                          self.percentage.get(), self.cgpa.get(), self.grade.get(),
                                          self.division.get(), self.result.get())
                tkinter.messagebox.showinfo("Success", "Data Added Successfully")
            except AttributeError:
                pass

    def display(self):
        if len(marcksheet_backend.view()) != 0:
            self.marks_table.delete(*self.marks_table.get_children())
            for row in marcksheet_backend.view():
                self.marks_table.insert('', END, values=row)

    def Reset(self):
        self.Name.set('')
        self.ID_s.set('')
        self.Branch.set('')
        self.Session.set('')
        self.Address.set('')
        self.Contact.set('')
        self.Email.set('')
        self.marks1.set('')
        self.marks2.set('')
        self.marks3.set('')
        self.marks4.set('')
        self.marks5.set('')
        self.grand_tot.set('')
        self.percentage.set('')
        self.cgpa.set('')
        self.grade.set('')
        self.division.set('')
        self.result.set('')

    def update(self):
        self.marks_table.delete(*self.marks_table.get_children())
        self.conn = sqlite3.connect('UE.db')
        self.cur = self.conn.cursor()
        self.cur.execute("UPDATE `marks` SET `name` = ?, `ID_s` = ?, `branch` =?, `date` = ?,  "
                         "`session` = ?, `address` = ?, `contact` = ?, `email` = ?, "
                         "`marks1` = ?, `marks2` = ?, `marks3` = ?, `marks4` = ?, `marks5` = ?, `grand_tot` = ?,"
                         "`percentage` = ?, `cgpa` = ?, `grade` = ?, `division` = ?, `result` = ? WHERE `id` = ?",
                         (str(self.Name.get()), str(self.ID_s.get()),
                          str(self.Branch.get()), str(self.Date.get()),
                          str(self.Session.get()), str(self.Address.get()),
                          str(self.Contact.get()), str(self.Email.get()),
                          str(self.marks1.get()), str(self.marks2.get()), str(self.marks3.get()),
                          str(self.marks4.get()), str(self.marks5.get()), str(self.grand_tot.get()),
                          str(self.percentage.get()), str(self.cgpa.get()),
                          str(self.grade.get()), str(self.division.get()), str(self.result.get()), str(id)))
        self.conn.commit()
        self.cur.execute("SELECT * FROM `marks` ORDER BY `name` ASC")
        self.fetch = self.cur.fetchall()
        for data in self.fetch:
            self.marks_table.insert('', 'end', values=(data))
        self.cur.close()
        self.conn.close()

    def exit(self):
        Exit = tkinter.messagebox.askyesno("Logout System", "Confirm, if you want to Exit")
        if Exit > 0:
            self.master.destroy()
            return

    def Compute(self):
        self.num1 = (self.marks1.get())
        self.num2 = (self.marks2.get())
        self.num3 = (self.marks3.get())
        self.num4 = (self.marks4.get())
        self.num5 = (self.marks5.get())

        if self.num1 > 100:
            tkinter.messagebox.askokcancel('Attention', 'Please enter Correct Marks (French)')
            return
        if self.num2 > 100:
            tkinter.messagebox.askokcancel('Attention', 'Please enter Correct Marks (English)')
            return
        if self.num3 > 100:
            tkinter.messagebox.askokcancel('Attention', 'Please enter Correct Marks (Calculus)')
            return
        if self.num4 > 100:
            tkinter.messagebox.askokcancel('Attention', 'Please enter Correct Marks (Python)')
            return
        if self.num5 > 100:
            tkinter.messagebox.askokcancel('Attention', 'Please enter Correct Marks (Apologetic)')
            return

        self.TOTAL = self.num1 + self.num2 + self.num3 + self.num4 + self.num5
        self.grand_tot.set(self.TOTAL)

        self.Percentage = ((self.num1 + self.num2 + self.num3 + self.num4 + self.num5) * 100) / 500
        self.percentage.set(self.Percentage)

        self.c_grades = (((self.num1 + self.num2 + self.num3 + self.num4 + self.num5) * 100) / 500) / 9.5
        self.cgpa.set(round(self.c_grades, 1))

        if self.c_grades > 10:
            self.cgpa.set(10)

        if (((self.num1 + self.num2 + self.num3 + self.num4 + self.num5) * 100) / 500) <= 40:
            self.grades = 'G'
        elif (((self.num1 + self.num2 + self.num3 + self.num4 + self.num5) * 100) / 500) <= 50:
            self.grades = 'F'
        elif (((self.num1 + self.num2 + self.num3 + self.num4 + self.num5) * 100) / 500) <= 60:
            self.grades = 'E'
        elif (((self.num1 + self.num2 + self.num3 + self.num4 + self.num5) * 100) / 500) <= 70:
            self.grades = 'D'
        elif (((self.num1 + self.num2 + self.num3 + self.num4 + self.num5) * 100) / 500) <= 80:
            self.grades = 'C'
        elif (((self.num1 + self.num2 + self.num3 + self.num4 + self.num5) * 100) / 500) <= 90:
            self.grades = 'B'
        else:
            self.grades = 'A'

        self.grade.set(self.grades)

        self.count = 0
        if self.num1 < 65:
            self.count = self.count + 1
        if self.num2 < 65:
            self.count = self.count + 1
        if self.num3 < 65:
            self.count = self.count + 1
        if self.num4 < 65:
            self.count = self.count + 1
        if self.num5 < 65:
            self.count = self.count + 1

        if self.count == 0:
            self.result.set('PASS')
        elif self.count == 1 or self.count == 2:
            self.result.set('SUPPLY')
        else:
            self.result.set('FAIL')

        if self.Percentage <= 45 and self.result != "FAIL":
            self.division.set('THIRD')
        elif self.Percentage <= 60 and self.result != "FAIL":
            self.division.set('SECOND')
        elif self.Percentage <= 100:
            self.division.set('FIRST')

    # -------------------------------- Frame -------------------------------------------------------
    def create_frame(self):
        self.Marks_Frame_1 = LabelFrame(self.master, font=('Courier', 20, 'bold'),
                                        bg='aquamarine4',
                                        bd=10, text='Student Details', relief='ridge', fg='White')
        self.Marks_Frame_1.place(x=10, y=20, width=1330, height=260)

        self.Marks_Frame_2 = LabelFrame(self.master, font=('Courier', 20, 'bold'),
                                        bg='aquamarine4', bd=10
                                        , text='Grades Point Obtained', relief='ridge', fg='White')
        self.Marks_Frame_2.place(x=40, y=300, width=1270, height=420)

        self.Marks_Frame_3 = LabelFrame(self.Marks_Frame_1, font=('Courier', 20, 'bold'),
                                        bg='aquamarine4', bd=10, relief='ridge', fg='White')
        self.Marks_Frame_3.place(x=710, y=0, width=595, height=210)

    # -------------------------------- Label -------------------------------------------------------
    def create_label(self):
        self.student_name_label = Label(self.Marks_Frame_1, text='Student Name', font=('Courier', 16), bg='aquamarine4',
                                        fg='White')
        self.student_name_label.place(x=10, y=20)

        self.student_id_label = Label(self.Marks_Frame_1, text='Student ID', font=('Courier', 16), bg='aquamarine4',
                                      fg='White')
        self.student_id_label.place(x=10, y=60)

        self.label_branch = Label(self.Marks_Frame_1, text='Branch', font=('Courier', 16), bg='aquamarine4',
                                  fg='White')
        self.label_branch.place(x=10, y=100)

        self.date_label = Label(self.Marks_Frame_1, text='Date', font=('Courier', 16),
                                bg='aquamarine4', fg='White')
        self.date_label.place(x=10, y=140)

        self.session_label = Label(self.Marks_Frame_1, text='Session', font=('Courier', 16),
                                   bg='aquamarine4', fg='White')
        self.session_label.place(x=10, y=180)

        self.address_label = Label(self.Marks_Frame_1, text='Address', font=('Courier', 14), bg='aquamarine4',
                                   fg='White')
        self.address_label.place(x=375, y=20)

        self.contact_label = Label(self.Marks_Frame_1, text='Contact No', font=('Courier', 14), bg='aquamarine4',
                                   fg='White')
        self.contact_label.place(x=375, y=60)

        self.email_label = Label(self.Marks_Frame_1, text='Email', font=('Courier', 14), bg='aquamarine4',
                                 fg='White')
        self.email_label.place(x=375, y=100)

        self.subject_label = Label(self.Marks_Frame_2, text='SUBJECT', font=('Courier', 16, 'bold'), bg='aquamarine4',
                                   fg='White')
        self.subject_label.place(x=50, y=20)

        self.marks_label = Label(self.Marks_Frame_2, text='MARKS OBTAINED', font=('Courier', 16, 'bold'),
                                 bg='aquamarine4', fg='White')
        self.marks_label.place(x=270, y=20)

        self.passing_label = Label(self.Marks_Frame_2, text='PASSING MARKS', font=('Courier', 16, 'bold'),
                                   bg='aquamarine4', fg='White')
        self.passing_label.place(x=550, y=20)

        self.total_label = Label(self.Marks_Frame_2, text='TOTAL MARKS', font=('Courier', 16, 'bold'), bg='aquamarine4',
                                 fg='White')
        self.total_label.place(x=800, y=20)

        self.french_label = Label(self.Marks_Frame_2, text='French', font=('Courier', 16), bg='aquamarine4',
                                  fg='White')
        self.french_label.place(x=50, y=60)

        self.english_label = Label(self.Marks_Frame_2, text='English', font=('Courier', 14), bg='aquamarine4',
                                   fg='White')
        self.english_label.place(x=50, y=100)

        self.calculus_label = Label(self.Marks_Frame_2, text='Calculus', font=('Courier', 14), bg='aquamarine4',
                                    fg='White')
        self.calculus_label.place(x=50, y=140)

        self.python_label = Label(self.Marks_Frame_2, text='Python', font=('Courier', 14), bg='aquamarine4',
                                  fg='White')
        self.python_label.place(x=50, y=180)

        self.apoogetic_label = Label(self.Marks_Frame_2, text='Apologetic', font=('Courier', 14), bg='aquamarine4',
                                     fg='White')
        self.apoogetic_label.place(x=50, y=220)

        self.total_label = Label(self.Marks_Frame_2, text='GRAND TOTAL', font=('Courier', 16, 'bold'), bg='aquamarine4',
                                 fg='White')
        self.total_label.place(x=50, y=260)

        self.percentage_label = Label(self.Marks_Frame_2, text='PERCENTAGE', font=('Courier', 16, 'bold'),
                                      bg='aquamarine4',
                                      fg='White')
        self.percentage_label.place(x=50, y=300)

        self.division_label = Label(self.Marks_Frame_2, text='DIVISION', font=('Courier', 16, 'bold'),
                                    bg='aquamarine4', fg='White')
        self.division_label.place(x=50, y=340)

        self.gpa_label = Label(self.Marks_Frame_2, text='GPA', font=('Courier', 16, 'bold'),
                               bg='aquamarine4', fg='White')
        self.gpa_label.place(x=620, y=300)

        self.result_label = Label(self.Marks_Frame_2, text='RESULT', font=('Courier', 16, 'bold'),
                                  bg='aquamarine4', fg='White')
        self.result_label.place(x=600, y=340)

        self.grade_label = Label(self.Marks_Frame_2, text='GRADE', font=('Courier', 16, 'bold'),
                                 bg='aquamarine4', fg='White')
        self.grade_label.place(x=1060, y=300)

    # -------------------------------- Entry -------------------------------------------------------
    def create_entry(self):
        self.Entry_student_name = Entry(self.Marks_Frame_1, font=('arial', 10), textvariable=self.Name)
        self.Entry_student_name.focus()
        self.Entry_student_name.place(x=190, y=20)

        self.Entry_Entry_student_id = Entry(self.Marks_Frame_1, font=('arial', 10), textvariable=self.ID_s)
        self.Entry_Entry_student_id.place(x=190, y=60)

        self.Entry_branch = ttk.Combobox(self.Marks_Frame_1, values=(' ', 'Computer Science', 'Science Of Education',
                                                                     'Business Management'),
                                         font=('arial', 10), width=21, textvariable=self.Branch)
        self.Entry_branch.place(x=190, y=100, width=145)

        self.Entry_date_of_birth = DateEntry(self.Marks_Frame_1, font=('arial', 10), date_pattern='dd/mm/yyyy'
                                             , textvariable=self.Date)
        self.Entry_date_of_birth.place(x=190, y=140, width=145)

        self.Entry_semester = ttk.Combobox(self.Marks_Frame_1, values=(' ', 'FIRST', 'SECOND'),
                                           font=('arial', 10), textvariable=self.Session)
        self.Entry_semester.place(x=190, y=180, width=145)

        self.Entry_address = Entry(self.Marks_Frame_1, font=('arial', 10), textvariable=self.Address)
        self.Entry_address.place(x=540, y=20)

        self.Entry_contact = Entry(self.Marks_Frame_1, font=('arial', 10), textvariable=self.Contact)
        self.Entry_contact.place(x=540, y=60)

        self.Entry_email = Entry(self.Marks_Frame_1, font=('arial', 10), textvariable=self.Email)
        self.Entry_email.place(x=540, y=100)

        self.Entry_note1 = Entry(self.Marks_Frame_2, font=('arial', 12), bg='Azure2', textvariable=self.marks1)
        self.Entry_note1.place(x=330, y=57, width=70, height=25)

        self.Entry_note2 = Entry(self.Marks_Frame_2, font=('arial', 12), bg='Azure2', textvariable=self.marks2)
        self.Entry_note2.place(x=330, y=97, width=70, height=25)

        self.Entry_note3 = Entry(self.Marks_Frame_2, font=('arial', 12), bg='Azure2', textvariable=self.marks3)
        self.Entry_note3.place(x=330, y=137, width=70, height=25)

        self.Entry_note4 = Entry(self.Marks_Frame_2, font=('arial', 12), bg='Azure2', textvariable=self.marks4)
        self.Entry_note4.place(x=330, y=177, width=70, height=25)

        self.Entry_note5 = Entry(self.Marks_Frame_2, font=('arial', 12), bg='Azure2', textvariable=self.marks5)
        self.Entry_note5.place(x=330, y=217, width=70, height=25)

        self.Entry_total_std = Entry(self.Marks_Frame_2, font=('arial', 12), bg='Azure2', textvariable=self.grand_tot,
                                     state='readonly')
        self.Entry_total_std.place(x=330, y=257, width=70, height=25)

        self.Entry_percentage = Entry(self.Marks_Frame_2, font=('arial', 12, 'bold'), bg='Azure2',
                                      textvariable=self.percentage, state='readonly')
        self.Entry_percentage.place(x=330, y=297, width=70, height=25)

        self.Entry_division = Entry(self.Marks_Frame_2, font=('arial', 12, 'bold'), bg='Azure2',
                                    textvariable=self.division, state='readonly')
        self.Entry_division.place(x=313, y=337, width=100, height=25)

        self.pass_note1 = Entry(self.Marks_Frame_2, font=('arial', 12), bg='Azure2', textvariable=self.variables_1,
                                state='readonly')
        self.pass_note1.place(x=600, y=57, width=70, height=25)

        self.pass_note2 = Entry(self.Marks_Frame_2, font=('arial', 12), bg='Azure2', textvariable=self.variables_1,
                                state='readonly')
        self.pass_note2.place(x=600, y=97, width=70, height=25)

        self.pass_note3 = Entry(self.Marks_Frame_2, font=('arial', 12), bg='Azure2', textvariable=self.variables_1,
                                state='readonly')
        self.pass_note3.place(x=600, y=137, width=70, height=25)

        self.pass_note4 = Entry(self.Marks_Frame_2, font=('arial', 12), bg='Azure2', textvariable=self.variables_1,
                                state='readonly')
        self.pass_note4.place(x=600, y=177, width=70, height=25)

        self.pass_note5 = Entry(self.Marks_Frame_2, font=('arial', 12), bg='Azure2', textvariable=self.variables_1,
                                state='readonly')
        self.pass_note5.place(x=600, y=217, width=70, height=25)

        self.Entry_total1 = Entry(self.Marks_Frame_2, font=('arial', 12), bg='Azure2', textvariable=self.variables_2,
                                  state='readonly')
        self.Entry_total1.place(x=840, y=57, width=70, height=25)

        self.Entry_total2 = Entry(self.Marks_Frame_2, font=('arial', 12), bg='Azure2',
                                  textvariable=self.variables_2, state='readonly')
        self.Entry_total2.place(x=840, y=97, width=70, height=25)

        self.Entry_total3 = Entry(self.Marks_Frame_2, font=('arial', 12), bg='Azure2',
                                  textvariable=self.variables_2, state='readonly')
        self.Entry_total3.place(x=840, y=137, width=70, height=25)

        self.Entry_total4 = Entry(self.Marks_Frame_2, font=('arial', 12), bg='Azure2', textvariable=self.variables_2,
                                  state='readonly')
        self.Entry_total4.place(x=840, y=177, width=70, height=25)

        self.Entry_total5 = Entry(self.Marks_Frame_2, font=('arial', 12), bg='Azure2', textvariable=self.variables_2,
                                  state='readonly')
        self.Entry_total5.place(x=840, y=217, width=70, height=25)

        self.Entry_grand_total_point = Entry(self.Marks_Frame_2, font=('arial', 12), bg='Azure2', state='readonly',
                                             textvariable=self.variables_3)
        self.Entry_grand_total_point.place(x=840, y=257, width=70, height=25)

        self.total_gpa = Entry(self.Marks_Frame_2, font=('arial', 12, 'bold'), bg='Azure2', textvariable=self.cgpa,
                               state='readonly')
        self.total_gpa.place(x=840, y=297, width=70, height=25)

        self.result_total = Entry(self.Marks_Frame_2, font=('arial', 12, 'bold'), bg='Azure2', textvariable=self.result,
                                  state='readonly')
        self.result_total.place(x=825, y=337, width=100, height=25)

        self.total_grade = Entry(self.Marks_Frame_2, font=('arial', 12, 'bold'), bg='Azure2', textvariable=self.grade,
                                 state='readonly')
        self.total_grade.place(x=1175, y=297, width=70, height=25)

    def create_button(self):
        self.button_compute = Button(self.Marks_Frame_2, text='COMPUTE', font=('Courier', 15, 'bold'), bg='aquamarine4',
                                     fg="White", width=10, command=self.Compute)
        self.button_compute.place(x=1030, y=57)
        self.button_compute.config(activebackground="#41B77F", relief=RAISED)

        self.button_save = Button(self.Marks_Frame_2, text="SAVE", font=('Courier', 15, 'bold'), bg='aquamarine4',
                                  fg="White", width=10, command=self.save)
        self.button_save.place(x=1030, y=120)
        self.button_save.config(activebackground="#41B77F", relief=RAISED)

        self.button_reset = Button(self.Marks_Frame_2, text='RESET', font=('Courier', 15, 'bold'), bg='aquamarine4',
                                   fg="White", width=10, command=self.Reset)
        self.button_reset.place(x=1030, y=183)
        self.button_reset.config(activebackground="#41B77F", relief=RAISED)

        self.button_exit = Button(self.Marks_Frame_2, text='EXIT', font=('Courier', 15, 'bold'), bg='aquamarine4',
                                  fg="White", width=10, command=self.exit)
        self.button_exit.place(x=1030, y=246)
        self.button_exit.config(activebackground="#41B77F", relief=RAISED)

        self.button_display = Button(self.Marks_Frame_1, text='DISPLAY', font=('Courier', 15, 'bold'), bg='aquamarine4',
                                     fg="White", width=10, command=self.display)
        self.button_display.place(x=540, y=150)
        self.button_display.config(activebackground="#41B77F", relief=RAISED)

        self.button_update = Button(self.Marks_Frame_1, text='UPDATE', font=('Courier', 15, 'bold'), bg='aquamarine4',
                                    fg="White", width=10, command=self.update)
        self.button_update.place(x=375, y=150)
        self.button_update.config(activebackground="#41B77F", relief=RAISED)

        # -------------------------------- SCROLL BAR -------------------------------------------------------

    def create_scroll_bar(self):
        global marks_table
        self.scroll_x = Scrollbar(self.Marks_Frame_3, orient=HORIZONTAL)
        self.scroll_y = Scrollbar(self.Marks_Frame_3, orient=VERTICAL)

        self.marks_table = tkinter.ttk.Treeview(self.Marks_Frame_3, column=('roll no', 'student_name',
                                                                            'student_id', 'branch', 'date',
                                                                            'session', 'address', 'contact_no',
                                                                            'email',
                                                                            'french', 'english', 'calculus',
                                                                            'python',
                                                                            'apologetic', 'total',
                                                                            'percentage', 'gpa',
                                                                            'grade',
                                                                            'division', 'result'),
                                                xscrollcommand=self.scroll_x.set, yscrollcommand=self.scroll_y.set)

        self.scroll_x.pack(side=BOTTOM, fill=X)
        self.scroll_y.pack(side=RIGHT, fill=Y)

        self.scroll_x.config(command=self.marks_table.xview)
        self.scroll_y.config(command=self.marks_table.yview)

        self.marks_table.heading('roll no', text='Roll No')
        self.marks_table.heading('student_name', text='Student Name')
        self.marks_table.heading('student_id', text='Student ID')
        self.marks_table.heading('branch', text='Branch')
        self.marks_table.heading('date', text='Date')
        self.marks_table.heading('session', text='Session')
        self.marks_table.heading('address', text='Address')
        self.marks_table.heading('contact_no', text='Contact No')
        self.marks_table.heading('email', text='Email')
        self.marks_table.heading('french', text='French')
        self.marks_table.heading('english', text='English')
        self.marks_table.heading('calculus', text='Calculus')
        self.marks_table.heading('python', text='Python')
        self.marks_table.heading('apologetic', text='Apologetic')
        self.marks_table.heading('total', text='Total')
        self.marks_table.heading('percentage', text='Percentage')
        self.marks_table.heading('division', text='Division')
        self.marks_table.heading('gpa', text='GPA')
        self.marks_table.heading('result', text='Result')
        self.marks_table.heading('grade', text='Grade')

        self.marks_table['show'] = 'headings'
        self.marks_table.column('roll no', width=50)
        self.marks_table.pack(fill=BOTH, expand=1)
        self.marks_table.bind('<Double-Button-1>', self.OneSelected)

        self.localtime = time.asctime(time.localtime(time.time()))
        self.lbl_time = Label(self.master, text=self.localtime, fg="white", font=("Courier", 16), bg="aquamarine4")
        self.lbl_time.place(x=1017, y=0)


root = tk.Tk()
root.geometry("1350x750")
root.resizable(False, False)
root.title("Université Espoir")
root.iconbitmap("logo1.ICO")
root.config(background="aquamarine4")

app = MarkingSheet(master=root)
app.mainloop()
