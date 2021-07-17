import sqlite3


def connect():
    con = sqlite3.connect('UE.db')
    cur = con.cursor()

    cur.execute('CREATE TABLE IF NOT EXISTS marks (id INTEGER PRIMARY KEY, name text, ID_s text, branch text, date \
                     text, session text, address text, contact text, email text, marks1 integer, marks2 integer, marks3 integer, marks4 integer, \
                     marks5 integer, grand_tot integer, percentage integer, cgpa integer, grade text, division text, result text)')

    con.commit()
    con.close()


def insert(id, name=' ', ID_s=' ', branch=' ', date=' ', session=' ', address=' ', contact=' ',
           email=' ', marks1=' ', marks2=' ',
           marks3=' ', marks4=' ', marks5=' ', grand_tot=' ', percentage=' ', cgpa=' ', grade=' ', division=' ',
           result=' '):
    con = sqlite3.connect('UE.db')
    cur = con.cursor()

    cur.execute('INSERT INTO marks VALUES (NULL,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)',
                (id, name, ID_s, branch, date, session, address,
                 contact, email, marks1, marks2, marks3, marks4, marks5, grand_tot, percentage,
                 cgpa, grade, division, result))

    con.commit()
    con.close()


def view():
    conn = sqlite3.connect('UE.db')
    cur = conn.cursor()

    cur.execute("""SELECT * FROM marks""")
    rows = cur.fetchall()
    return rows


connect()
