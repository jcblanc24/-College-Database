import sqlite3
from tkinter import filedialog


def insert(FirstName='', LastName='', Gender='', Date_Of_Birth='', Birth_Country='', Birth_City='', Age='',
           Address='', Phone_Number='', Email='', Major='', Blood_Group='', Religion='', stdID='', usernameStd='',
           Parent='', Parent_Name='', Parent_Address='', Parent_Contact='', Parent_Email='', Registration_Date='',
           image=''):
    conn = sqlite3.connect('UE.db')
    cur = conn.cursor()

    cur.execute("""INSERT INTO students(first_name, last_name, gender, date_of_birth, birth_country, birth_city, age, 
    address, phone_number, email, major, blood_group, religion, stdID, usernameStd, parent,
    Parent_Name, Parent_Address, Parent_Contact, Parent_Email, registration_date, image) VALUES(?,?,?,?,?,?,?,?,?,
    ?,?,?,?,?,?,?,?,?,?,?,?,?)""",
                (FirstName, LastName, Gender, Date_Of_Birth, Birth_Country, Birth_City, Age,
                 Address, Phone_Number, Email, Major, Blood_Group, Religion, stdID, usernameStd,
                 Parent, Parent_Name, Parent_Address, Parent_Contact, Parent_Email, Registration_Date,
                 image))

    cur.execute("""SELECT * FROM students""")
    rows = cur.fetchall()
    with open("C:\\Users\\Clayton\\Desktop\\School database\\Version 2.0\\Files "
              "Data\\Students\\Students_data.txt",
              "w") as fichier_texte:
        for row in rows:
            fichier_texte.write(
                f'{row[0]} : {row[1]}  |||   {row[2]}   |||   {row[3]}    |||   {row[4]}   |||   {row[5]}'
                f'|||   {row[6]} years old   |||   {row[7]}   ||| {row[8]}   |||   {row[9]}  |||  {row[10]}  ||| '
                f'  {row[11]}   |||   {row[12]}   |||   {row[13]}   |||  {row[14]}   |||   {row[15]}   ||| {row[16]}'
                f'   |||   {row[17]}  |||  {row[18]}  ||| {row[19]}   |||   {row[20]}   |||   {row[21]}   ||| '
                f' {row[22]}.\n')

    conn.commit()
    conn.close()


def view():
    conn = sqlite3.connect('UE.db')
    cur = conn.cursor()

    cur.execute("""SELECT * FROM students""")
    rows = cur.fetchall()
    return rows


def open_file():
    global get_image
    get_image = filedialog.askopenfilename(initialdir="/version 2.0/images", title="Select Image",
                                           filetypes=(("jpg files", "*.jpg"), ("png files", "*.png"),
                                                      ("all files", "*.*")))


def conver_image_to_bynary(filename):
    with open(filename, 'rb') as file:
        photo_image = file.read()
        return photo_image


