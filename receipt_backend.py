import sqlite3


def connect():
    con = sqlite3.connect('UE.db')
    cur = con.cursor()

    cur.execute('CREATE TABLE IF NOT EXISTS fee(id INTEGER PRIMARY KEY, receipts integer, name text, admin text, date'
                ' integer, branch text, semester text, total integer, paid integer, due integer)')

    con.commit()
    con.close()


def insert(Receipt='', Student_Name='', Admission='', Date='', Branch='', Semester='', Total_amount='',
           Paid='', Balance=''):
    conn = sqlite3.connect('UE.db')
    cur = conn.cursor()

    cur.execute("""INSERT INTO fee(receipts, name, admin, date, branch, semester, total, 
    paid, due) VALUES(?,?,?,?,?,?,?,?,?)""",
                (Receipt, Student_Name, Admission, Date, Branch, Semester, Total_amount,
                 Paid, Balance))

    cur.execute("""SELECT * FROM fee""")
    rows = cur.fetchall()
    with open("C:\\Users\\Clayton\\Desktop\\School database\\Version 2.0\\Files "
              "Data\\Students\\Students_Receipt.txt",
              "w") as fichier_texte:
        for row in rows:
            fichier_texte.write('\t\tRECEIPT' + '\n\n')
            fichier_texte.write(f'\tReceipt No.   : {row[0]} \n')
            fichier_texte.write(f'\tStudent Name  : {row[2]} \n')
            fichier_texte.write(f'\tAdmission No. : {row[3]} \n')
            fichier_texte.write(f'\tDate          : {row[4]} \n')
            fichier_texte.write(f'\tBranch        : {row[5]} \n')
            fichier_texte.write(f'\tSemester      : {row[6]} \n\n')

            fichier_texte.write(f'\tTotal Amount  : {row[7]} \n')
            fichier_texte.write(f'\tPaid Amount   : {row[8]} \n')
            fichier_texte.write(f'\tBalance       : {row[7] - row[8]} \n\n\n')

    conn.commit()
    conn.close()


def view():
    conn = sqlite3.connect('UE.db')
    cur = conn.cursor()

    cur.execute("""SELECT * FROM fee""")
    rows = cur.fetchall()
    return rows


def delete(id):
    con = sqlite3.connect('UE.db')
    cur = con.cursor()

    cur.execute('DELETE FROM fee WHERE id = ?', (id,))

    con.commit()
    con.close()


connect()
