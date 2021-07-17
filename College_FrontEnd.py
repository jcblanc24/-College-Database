import sqlite3
import time
import tkinter.ttk
from tkinter import *
import tkinter as tk
from tkinter import ttk, filedialog
from tkcalendar import DateEntry
import college_BackEnd
from tkinter import messagebox
import fonction


class GuiStudent(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()

        self.FirstName = StringVar()
        self.LastName = StringVar()
        self.Gender = StringVar()
        self.DateOfBirth = StringVar()
        self.BirthCountry = StringVar()
        self.BirthCity = StringVar()
        self.Address = StringVar()
        self.PhoneNUmber = StringVar()
        self.Email = StringVar()
        self.Major = StringVar()
        self.Blood_Group = StringVar()
        self.Religion = StringVar()
        self.Parent = StringVar()
        self.Parent_Name = StringVar()
        self.Parent_Address = StringVar()
        self.Parent_Contact = StringVar()
        self.Parent_Email = StringVar()

        self.create_frame()
        self.create_label()
        self.create_entry()
        self.create_button()
        self.create_scroll_bar()
        self.create_canvas()
        self.display()

    def OneSelected(self, event):
        global id
        try:
            self.curItem = self.student_table.focus()
            self.contents = (self.student_table.item(self.curItem))
            self.selecteditem = self.contents['values']
            self.id = self.selecteditem[0]

            self.FirstName.set('')
            self.FirstName.set(self.selecteditem[1])

            self.LastName.set('')
            self.LastName.set(self.selecteditem[2])

            self.Gender.set('')
            self.Gender.set(self.selecteditem[3])

            self.DateOfBirth.set('')
            self.DateOfBirth.set(self.selecteditem[4])

            self.BirthCountry.set('')
            self.BirthCountry.set(self.selecteditem[5])

            self.BirthCity.set('')
            self.BirthCity.set(self.selecteditem[6])

            self.Address.set('')
            self.Address.set(self.selecteditem[7])

            self.PhoneNUmber.set('')
            self.PhoneNUmber.set(self.selecteditem[8])

            self.Email.set('')
            self.Email.set(self.selecteditem[9])

            self.Major.set('')
            self.Major.set(self.selecteditem[10])

            self.Blood_Group.set('')
            self.Blood_Group.set(self.selecteditem[11])

            self.Religion.set('')
            self.Religion.set(self.selecteditem[12])

            self.Parent.set('')
            self.Parent.set(self.selecteditem[16])

            self.Parent_Name.set('')
            self.Parent_Name.set(self.selecteditem[17])

            self.Parent_Address.set('')
            self.Parent_Address.set(self.selecteditem[18])

            self.Parent_Contact.set('')
            self.Parent_Contact.set(self.selecteditem[19])

            self.Parent_Email.set('')
            self.Parent_Email.set(self.selecteditem[20])
        except IndexError:
            tkinter.messagebox.showwarning('', 'Please Select A Student !', icon="warning")

    def add(self):
        try:
            self.verifier_first_name(self.FirstName.get())
            self.verifier_last_name(self.LastName.get())
            self.verifier_country(self.BirthCountry.get())
            self.verifier_city(self.BirthCity.get())
            self.verifier_phone(self.PhoneNUmber.get())
            self.verifier_major(self.Major.get())
            self.verifier_parent(self.Parent.get())
            self.verifier_parent_name(self.Parent_Name.get())
            self.verifier_contact_parent(self.Parent_Contact.get())

            if self.FirstName.get() == "" or self.LastName.get() == "" or self.Gender.get() == "" or \
                    self.DateOfBirth.get() == "" or self.BirthCountry.get() == "" or self.BirthCity.get() == "" or \
                    self.Address.get() == "" or self.PhoneNUmber.get() == "" or self.Email.get() == "" or \
                    self.Major.get() == "" or self.Blood_Group.get() == "" or self.Religion.get() == "" or \
                    self.Parent.get() == "" or self.Parent_Name.get() == "" or self.Parent_Address.get() == "" or \
                    self.Parent_Contact.get() == '' or self.Parent_Email.get() == "":
                tkinter.messagebox.showwarning('', 'Please Complete The Required Field', icon="warning")
            else:
                college_BackEnd.insert(self.FirstName.get(), self.LastName.get(), self.Gender.get(),
                                       self.DateOfBirth.get(), self.BirthCountry.get(), self.BirthCity.get(),
                                       self.Address.get(), self.PhoneNUmber.get(), self.Email.get(),
                                       self.Major.get(), self.Blood_Group.get(), self.Religion.get(),
                                       fonction.create_id_s(self.LastName.get()), self.calculer_age(),
                                       fonction.create_username_s(self.FirstName.get(), self.LastName.get()),
                                       self.Parent.get(), self.Parent_Name.get(), self.Parent_Address.get(),
                                       self.Parent_Contact.get(), self.Parent_Email.get(),
                                       time.asctime(time.localtime(time.time())),
                                       college_BackEnd.conver_image_to_bynary(self.get_image))
                tkinter.messagebox.showinfo("Success", "Data Added Successfully")
        except NameError:
            tkinter.messagebox.showwarning('',
                                           'Please Click On The "Open file" Button To Complete The Required Field '
                                           'By Adding A Photo', icon="warning")
        except AttributeError:
            pass
        except IndexError:
            pass

    def display(self):
        if len(college_BackEnd.view()) != 0:
            self.student_table.delete(*self.student_table.get_children())
            for row in college_BackEnd.view():
                self.student_table.insert('', END, values=row)

    def Reset(self):
        self.FirstName.set('')
        self.LastName.set('')
        self.Gender.set('')
        self.DateOfBirth.set('')
        self.BirthCountry.set('')
        self.BirthCity.set('')
        self.Address.set('')
        self.PhoneNUmber.set('')
        self.Email.set('')
        self.Major.set('')
        self.Blood_Group.set('')
        self.Religion.set('')
        self.Parent.set('')
        self.Parent_Name.set('')
        self.Parent_Address.set('')
        self.Parent_Contact.set('')
        self.Parent_Email.set('')

    def update(self):
        self.student_table.delete(*self.student_table.get_children())
        self.conn = sqlite3.connect('UE.db')
        self.cur = self.conn.cursor()
        self.cur.execute("UPDATE `students` SET `first_name` = ?, `last_name` = ?, `gender` =?, `date_of_birth` = ?,  "
                         "`birth_country` = ?, `birth_city` = ?, `address` = ?, `phone_number` = ?, "
                         "`email` = ?, `major` = ?, `blood_group` = ?, `religion` = ?, `parent` = ?, `Parent_Name` = ?,"
                         "`Parent_Address` = ?, `Parent_Contact` = ?, `Parent_Email` = ? WHERE `id` = ?",
                         (str(self.FirstName.get()), str(self.LastName.get()),
                          str(self.Gender.get()), str(self.DateOfBirth.get()),
                          str(self.BirthCountry.get()), str(self.BirthCity.get()),
                          str(self.Address.get()), str(self.PhoneNUmber.get()),
                          str(self.Email.get()), str(self.Major.get()), str(self.Blood_Group.get()),
                          str(self.Religion.get()), str(self.Parent.get()), str(self.Parent_Name.get()),
                          str(self.Parent_Address.get()), str(self.Parent_Contact.get()),
                          str(self.Parent_Email.get()), str(id)))
        self.conn.commit()
        self.cur.execute("SELECT * FROM `students` ORDER BY `last_name` ASC")
        self.fetch = self.cur.fetchall()
        for data in self.fetch:
            self.student_table.insert('', 'end', values=(data))
        self.cur.close()
        self.conn.close()

    def DeleteData(self):
        if not self.student_table.selection():
            result = tkinter.messagebox.showwarning('', 'Please Select Something First!', icon="warning")
        else:
            result = tkinter.messagebox.askquestion('', 'Are you sure you want to delete this record?', icon="warning")
            if result == 'yes':
                self.curItem = self.student_table.focus()
                self.contents = (self.student_table.item(self.curItem))
                self.selecteditem = self.contents['values']
                self.student_table.delete(self.curItem)
                self.conn = sqlite3.connect("UE.db")
                self.cursor = self.conn.cursor()
                self.cursor.execute("DELETE FROM `students` WHERE `id` = %d" % self.selecteditem[0])
                self.conn.commit()
                self.cursor.close()
                self.conn.close()

    def exit(self):
        Exit = tkinter.messagebox.askyesno("Logout System", "Confirm, if you want to Exit")
        if Exit > 0:
            self.master.destroy()
            return

    def create_frame(self):
        global frame_title
        global Frame_2
        global Frame_3

        frame_title = Frame(self.master, bg="aquamarine4", bd=10, relief=SUNKEN)
        frame_title.pack()
        self.Main_Frame = LabelFrame(self.master, width=1330, height=575, font=('Courier', 15, 'bold'),
                                     bg='aquamarine4', bd=15, fg='White', relief='ridge')
        self.Main_Frame.place(x=10, y=80)

        self.Frame_1 = LabelFrame(self.master, width=720, height=525,
                                  font=('Courier', 15, 'bold'),
                                  relief='ridge', bd=10, bg='aquamarine4', fg='White', text='STUDENT INFORMATION')
        self.Frame_1.place(x=35, y=105)

        self.Frame_2 = LabelFrame(self.master,
                                  font=('Courier', 15, 'bold'),
                                  relief='ridge', bd=10, fg='White', bg='aquamarine4', text='STUDENT DATABASE')
        self.Frame_2.place(x=770, y=105, width=550, height=525)

        self.Frame_3 = LabelFrame(self.master, width=1180, height=70, font=('Courier', 10, 'bold'),
                                  bg='aquamarine4', relief='ridge', bd=13, fg='White')
        self.Frame_3.place(x=75, y=665)

    # -------------------------------- Labels -------------------------------------------------------
    def create_label(self):
        label_title1 = Label(frame_title, text='Student Database Management System', font=('Courier', 20, 'bold'),
                             bg='aquamarine4', fg='White').pack()

        self.label_first_name = Label(self.Frame_1, text='First Name', font=('Courier', 16), bg='aquamarine4',
                                      fg='White')
        self.label_first_name.place(x=10, y=20)

        self.l_name_label = Label(self.Frame_1, text='Last Name', font=('Courier', 16), bg='aquamarine4',
                                  fg='White')
        self.l_name_label.place(x=10, y=60)

        self.label_gender = Label(self.Frame_1, text='Gender', font=('Courier', 16), bg='aquamarine4',
                                  fg='White')
        self.label_gender.place(x=10, y=100)

        self.date_of_birth_label = Label(self.Frame_1, text='Date Of Birth', font=('Courier', 16), bg='aquamarine4',
                                         fg='White')
        self.date_of_birth_label.place(x=10, y=140)

        self.birth_country_label = Label(self.Frame_1, text='Birth Country', font=('Courier', 16), bg='aquamarine4',
                                         fg='White')
        self.birth_country_label.place(x=10, y=180)

        self.birth_city_label = Label(self.Frame_1, text='Birth City', font=('Courier', 16), bg='aquamarine4',
                                      fg='White')
        self.birth_city_label.place(x=10, y=220)

        self.address_label = Label(self.Frame_1, text='Address', font=('Courier', 16), bg='aquamarine4',
                                   fg='White')
        self.address_label.place(x=10, y=260)

        self.phone_number_label = Label(self.Frame_1, text='Contact No', font=('Courier', 16), bg='aquamarine4',
                                        fg='White')
        self.phone_number_label.place(x=10, y=300)

        self.email_label = Label(self.Frame_1, text='Email', font=('Courier', 16), bg='aquamarine4',
                                 fg='White')
        self.email_label.place(x=10, y=340)

        self.major_label = Label(self.Frame_1, text='Major', font=('Courier', 16), bg='aquamarine4',
                                 fg='White')
        self.major_label.place(x=10, y=380)

        self.lbl_blood = Label(self.Frame_1, text='Blood Group', font=('Courier', 16), bg='aquamarine4',
                               fg='White')
        self.lbl_blood.place(x=10, y=420)

        self.lbl_religion = Label(self.Frame_1, text='Religion', font=('Courier', 16), bg='aquamarine4',
                                  fg='White')
        self.lbl_religion.place(x=10, y=460)

        self.parentname = Label(self.Frame_1, text='Parent', font=('Courier', 14), bg='aquamarine4',
                                fg='White')
        self.parentname.place(x=375, y=20)

        self.lbl_full_name_parent = Label(self.Frame_1, text='Parent Name', font=('Courier', 14), bg='aquamarine4',
                                          fg='White')
        self.lbl_full_name_parent.place(x=375, y=60)

        self.lbl_address_parent = Label(self.Frame_1, text='Parent Address', font=('Courier', 14), bg='aquamarine4',
                                        fg='White')
        self.lbl_address_parent.place(x=375, y=100)

        self.lbl_num_parent = Label(self.Frame_1, text='Parent Contact', font=('Courier', 14), bg='aquamarine4',
                                    fg='White')
        self.lbl_num_parent.place(x=375, y=140)

        self.lbl_email_name = Label(self.Frame_1, text='Parent Email', font=('Courier', 14), bg='aquamarine4',
                                    fg='White')
        self.lbl_email_name.place(x=375, y=180)

        self.lbl_photo = Label(self.Frame_1, text='Photo', font=('Courier', 14), bg='aquamarine4',
                               fg='White')
        self.lbl_photo.place(x=480, y=285)

    # -------------------------------- Entry -------------------------------------------------------
    def create_entry(self):
        self.Entry_fname = Entry(self.Frame_1, font=('arial', 10), textvariable=self.FirstName)
        self.Entry_fname.focus()
        self.Entry_fname.place(x=190, y=20)

        self.Entry_lName = Entry(self.Frame_1, font=('arial', 10), textvariable=self.LastName)
        self.Entry_lName.place(x=190, y=60)

        self.Entry_gender = ttk.Combobox(self.Frame_1, values=(' ', 'Male', 'Female', 'Others'),
                                         font=('arial', 8), width=21, textvariable=self.Gender)
        self.Entry_gender.place(x=190, y=100, width=145)

        self.Entry_date_of_birth = DateEntry(self.Frame_1, font=('arial', 10), date_pattern='dd/mm/yyyy',
                                             textvariable=self.DateOfBirth)
        self.Entry_date_of_birth.place(x=190, y=140, width=145)

        self.Entry_Birth_country = Entry(self.Frame_1, font=('arial', 10), textvariable=self.BirthCountry)
        self.Entry_Birth_country.place(x=190, y=180)

        self.Entry_Birth_city = Entry(self.Frame_1, font=('arial', 10), textvariable=self.BirthCity)
        self.Entry_Birth_city.place(x=190, y=220)

        self.Entry_Address = Entry(self.Frame_1, font=('arial', 10), textvariable=self.Address)
        self.Entry_Address.place(x=190, y=260)

        self.Entry_contact = Entry(self.Frame_1, font=('arial', 10), textvariable=self.PhoneNUmber)
        self.Entry_contact.place(x=190, y=300)

        self.Entry_email = Entry(self.Frame_1, font=('arial', 10), textvariable=self.Email)
        self.Entry_email.place(x=190, y=340)

        self.Entry_major = Entry(self.Frame_1, font=('arial', 10), textvariable=self.Major)
        self.Entry_major.place(x=190, y=380)

        self.Entry_blood_group = ttk.Combobox(self.Frame_1,
                                              values=(' ', 'A+', 'A-', 'B+', 'B-', 'AB+', 'AB-', 'O+', 'O-'),
                                              font=('arial', 8), width=21, textvariable=self.Blood_Group)
        self.Entry_blood_group.place(x=190, y=420, width=145)

        self.Entry_religion = Entry(self.Frame_1, font=('arial', 10), textvariable=self.Religion)
        self.Entry_religion.place(x=190, y=460)

        self.Entry_parent = Entry(self.Frame_1, font=('arial', 10), textvariable=self.Parent)
        self.Entry_parent.place(x=540, y=20)

        self.Entry_parent_name = Entry(self.Frame_1, font=('arial', 10), textvariable=self.Parent_Name)
        self.Entry_parent_name.place(x=540, y=60)

        self.Entry_parenr_address = Entry(self.Frame_1, font=('arial', 10), textvariable=self.Parent_Address)
        self.Entry_parenr_address.place(x=540, y=100)

        self.Entry_parent_contact = Entry(self.Frame_1, font=('arial', 10), textvariable=self.Parent_Contact)
        self.Entry_parent_contact.place(x=540, y=140)

        self.Entry_parent_email = Entry(self.Frame_1, font=('arial', 10), textvariable=self.Parent_Email)
        self.Entry_parent_email.place(x=540, y=180)

    # -------------------------------- SCROLL BAR -------------------------------------------------------
    def create_scroll_bar(self):
        global student_table
        self.scroll_x = Scrollbar(self.Frame_2, orient=HORIZONTAL)
        self.scroll_y = Scrollbar(self.Frame_2, orient=VERTICAL)

        self.student_table = tkinter.ttk.Treeview(self.Frame_2, column=('roll no',
                                                                        'last_name', 'first_name', 'gender',
                                                                        'date_of_birth',
                                                                        'birth_country', 'birth_city',
                                                                        'address', 'phone_number',
                                                                        'email',
                                                                        'major', 'blood_group', 'religion', 'id',
                                                                        'age',
                                                                        'username', 'parent', 'parent_name',
                                                                        'parent_address', 'parent_contact',
                                                                        'parent_email',
                                                                        'registration_date'),
                                                  xscrollcommand=self.scroll_x.set, yscrollcommand=self.scroll_y.set)

        self.scroll_x.pack(side=BOTTOM, fill=X)
        self.scroll_y.pack(side=RIGHT, fill=Y)

        self.scroll_x.config(command=self.student_table.xview)
        self.scroll_y.config(command=self.student_table.yview)

        self.student_table.heading('roll no', text='Roll No')
        self.student_table.heading('last_name', text='Last name')
        self.student_table.heading('first_name', text='First name')
        self.student_table.heading('gender', text='Gender')
        self.student_table.heading('date_of_birth', text='Date Of Birth')
        self.student_table.heading('birth_country', text='Birth Country')
        self.student_table.heading('birth_city', text='Birth City')
        self.student_table.heading('age', text='Age')
        self.student_table.heading('address', text='Address')
        self.student_table.heading('phone_number', text=' Phone Number')
        self.student_table.heading('email', text='Email')
        self.student_table.heading('major', text='Major')
        self.student_table.heading('blood_group', text='Blood Group')
        self.student_table.heading('religion', text='Religion')
        self.student_table.heading('id', text='ID')
        self.student_table.heading('username', text='Username')
        self.student_table.heading('parent', text='Parent')
        self.student_table.heading('parent_name', text='Parent Name')
        self.student_table.heading('parent_address', text='Parent Address')
        self.student_table.heading('parent_contact', text='Parent Contact')
        self.student_table.heading('parent_email', text='Parent Email')
        self.student_table.heading('registration_date', text='Registration Date')

        self.student_table['show'] = 'headings'
        self.student_table.column('roll no', width=50)
        self.student_table.pack(fill=BOTH, expand=1)
        self.student_table.bind('<Double-Button-1>', self.OneSelected)

    # -------------------------------- Button -------------------------------------------------------
    def create_button(self):
        self.button_add = Button(self.Frame_3, text="ADD", font=('Courier', 15, 'bold'), bg='aquamarine4', fg="White",
                                 width=12, command=self.add)
        self.button_add.place(x=5, y=2)
        self.button_add.config(activebackground="#41B77F", relief=RAISED)

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
                                    fg="White", width=12, command=self.DeleteData)
        self.button_delete.place(x=665, y=2)
        self.button_delete.config(activebackground="#41B77F", relief=RAISED)

        self.button_search = Button(self.Frame_3, text='SEARCH', font=('Courier', 15, 'bold'), bg='aquamarine4',
                                    fg="White", width=12)
        self.button_search.place(x=830, y=2)
        self.button_search.config(activebackground="#41B77F", relief=RAISED)

        self.button_exit = Button(self.Frame_3, text='EXIT', font=('Courier', 15, 'bold'), bg='aquamarine4',
                                  fg="White", width=12)
        self.button_exit.place(x=995, y=2)
        self.button_exit.config(activebackground="#41B77F", relief=RAISED, command=self.exit)

        self.button_open_file = Button(self.Frame_1, text='OPEN FILE', font=('Courier', 15, 'bold'), bg='aquamarine4',
                                       fg="White", width=10, command=self.open_file)
        self.button_open_file.place(x=450, y=440)
        self.button_open_file.config(activebackground="#41B77F", relief=RAISED)

    # -------------------------------- Canvas, Image And Time -------------------------------------------------------
    def create_canvas(self):
        global date2

        self.canvas = Canvas(self.Frame_1, width=180, height=120, bg='aquamarine4')
        self.canvas.place(x=420, y=310)
        self.img = PhotoImage()
        self.canvas.create_image(90, 70, image=self.img)

        self.localtime = time.asctime(time.localtime(time.time()))
        self.lbl_time = Label(self.master, text=self.localtime, fg="white", font=("Courier", 16), bg="aquamarine4")
        self.lbl_time.place(x=1017, y=50)

        self.date2 = DateEntry(self.master, date_pattern='dd/mm/yyyy')

    def open_file(self):
        global get_image
        self.get_image = filedialog.askopenfilename(initialdir="/version 2.0/images", title="Select Image",
                                                    filetypes=(("jpg files", "*.jpg"), ("png files", "*.png"),
                                                               ("all files", "*.*")))

    # ----------------------------------------- Age -----------------------------------------------
    def calculer_age(self):
        self.dob_date = (self.Entry_date_of_birth.get_date())
        self.curent_date = (self.date2.get_date())
        self.day = (abs((self.dob_date - self.curent_date).days))
        self.age = int(self.day / 365)
        return self.age

    # ----------------------------------------- Some Functions -----------------------------------------------
    def verifier_first_name(self, first_name):
        if not first_name.isalpha():
            tkinter.messagebox.showwarning('', 'The First Name Must Have Only Alphabet Characters',
                                           icon="warning")
            self.FirstName.set('')

    def verifier_last_name(self, last_name):
        if not last_name.isalpha():
            tkinter.messagebox.showwarning('', 'The Last Name Must Have Only Alphabet Characters',
                                           icon="warning")
            self.LastName.set('')

    def verifier_country(self, country):
        if not country.isalpha():
            tkinter.messagebox.showwarning('', 'The Birth Country Name Must Have Only Alphabet Characters',
                                           icon="warning")
            self.BirthCountry.set('')

    def verifier_city(self, city):
        if not city.isalpha():
            tkinter.messagebox.showwarning('', 'The Birth City Name Must Have Only Alphabet Characters',
                                           icon="warning")
            self.BirthCity.set('')

    def verifier_major(self, major):
        if not major.isalpha():
            tkinter.messagebox.showwarning('', 'The Major Must Have Only Alphabet Characters',
                                           icon="warning")
            self.Major.set('')

    def verifier_phone(self, phone):
        if not phone.isdigit():
            tkinter.messagebox.showwarning('', 'The Phone Number Must Have Only Digits',
                                           icon="warning")
            self.PhoneNUmber.set('')

    def verifier_parent(self, parent):
        if not parent.isalpha():
            tkinter.messagebox.showwarning('', 'Parent Must Have Only Alphabet Characters',
                                           icon="warning")
            self.Parent.set('')

    def verifier_parent_name(self, parent_name):
        if not parent_name.isalpha():
            tkinter.messagebox.showwarning('', 'The Parent Name Must Have Only Alphabet Characters',
                                           icon="warning")
            self.Parent_Name.set('')

    def verifier_contact_parent(self, contact_parent):
        if not contact_parent.isdigit():
            tkinter.messagebox.showwarning('', 'The Parent Contact Must Have Only Digits',
                                           icon="warning")
            self.Parent_Contact.set('')


root = tk.Tk()
root.geometry("1350x750")
root.resizable(False, False)
root.title("Université Espoir")
root.iconbitmap("logo1.ICO")
root.config(background="aquamarine4")

app = GuiStudent(master=root)
app.mainloop()
