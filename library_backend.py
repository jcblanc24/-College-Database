import sqlite3


def connect():
    con = sqlite3.connect('UE.db')
    cur = con.cursor()

    cur.execute('CREATE TABLE IF NOT EXISTS library(id INTEGER PRIMARY KEY, member_type text, reference_no integer, '
                'firstname text, lastname text, address text, mobile_no integer, ID_book text, title text,'
                ' author text, borrow integer, due integer, loan integer)')

    con.commit()
    con.close()


def insert(Member='', Reference='', FName='', LName='', Address='', Mobil='', ID_Book='',
           Book_Title='', Author='', Date_Borrowed='', Date_Due='', Day_Loan=''):
    conn = sqlite3.connect('UE.db')
    cur = conn.cursor()

    cur.execute("""INSERT INTO library(member_type, reference_no, firstname, lastname, address, 
    mobile_no, ID_book, title, author, borrow, due, loan) VALUES(?,?,?,?,?,?,?,?,?,?,?,?)""",
                (Member, Reference, FName, LName, Address, Mobil, ID_Book,
                 Book_Title, Author, Date_Borrowed, Date_Due, Day_Loan))

    cur.execute("""SELECT * FROM library""")
    rows = cur.fetchall()
    with open("C:\\Users\\Clayton\\Desktop\\School database\\Version 2.0\\Files "
              "Data\\Students\\Library_data.txt",
              "w") as fichier_texte:
        for row in rows:
            fichier_texte.write(
                f'{row[0]} : {row[1]}  |||   {row[2]}   |||   {row[3]}    |||   {row[4]}   |||   {row[5]}'
                f'  |||   {row[6]}   |||   {row[7]}   ||| {row[8]}   |||   {row[9]}  |||  {row[10]}  ||| '
                f'  {row[11]}   |||   {row[12]}.\n')

    conn.commit()
    conn.close()


def view():
    conn = sqlite3.connect('UE.db')
    cur = conn.cursor()

    cur.execute("""SELECT * FROM library""")
    rows = cur.fetchall()
    return rows


def delete(id):
    conn = sqlite3.connect('UE.db')
    cur = conn.cursor()

    cur.execute('DELETE FROM library WHERE id = ?', (id,))

    conn.commit()
    conn.close()


connect()
