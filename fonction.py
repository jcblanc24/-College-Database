import random
import tkinter
from tkinter import messagebox
from tkinter import *


def create_id_s(last_name):
    cle_name = last_name[:3].title()
    cle = "STD"
    tiret = "-"
    num = str(random.randint(1000, 9999))

    id_s = cle + tiret + cle_name + num
    return id_s


# Create username for each students
def create_username_s(first_name, last_name):
    first_name = first_name.lower()
    last_name = last_name.lower()

    f_name = first_name.split()
    if len(f_name) < 2:
        f_name1 = f_name[0]
        username = f_name1[0] + last_name
        return username
    else:
        f_name1 = f_name[0]
        f_name2 = f_name[1]
        username = f_name1[0] + f_name2[0] + last_name
        return username


# ------------------------------------------------- Professors --------------------------------------------------------
# Create username for each professors
def creer_username_p(first_name, last_name):
    first_name = first_name.lower()
    last_name = last_name.lower()

    f_name = first_name.split()
    if len(f_name) < 2:
        f_name1 = f_name[0]
        username = f_name1[0] + last_name
        return username
    else:
        f_name1 = f_name[0]
        f_name2 = f_name[1]
        username = f_name1[0] + f_name2[0] + last_name
        return username


# Create id for each professor
def creer_id_p(last_name):
    cle_name = last_name[:3].title()
    cle = "PROF"
    tiret = "-"
    num = str(random.randint(1000, 9999))

    id_p = cle + tiret + cle_name + num
    return id_p


# ------------------------------------------------ Secretary ----------------------------------------------------------
# Create username for each secretary
def creer_username_sec(first_name, last_name):
    first_name = first_name.lower()
    last_name = last_name.lower()

    f_name = first_name.split()
    if len(f_name) < 2:
        f_name1 = f_name[0]
        username = f_name1[0] + last_name
        return username
    else:
        f_name1 = f_name[0]
        f_name2 = f_name[1]
        username = f_name1[0] + f_name2[0] + last_name
        return username


# Create id for each secretary
def creer_id_sec(last_name):
    cle_name = last_name[:3].title()
    cle = "SEC"
    tiret = "-"
    num = str(random.randint(1000, 9999))

    id_sec = cle + tiret + cle_name + num
    return id_sec


# --------------------------------------------------- Verify ---------------------------------------------------
# Verify if data is alpha
def verifier_alpha(n):
    if not n.isalpha():
        tkinter.messagebox.showwarning('', 'The First Name And Last Name, Birth Country, Birth City, Address, '
                                           'Major Must Have Only Alphabet Characters',
                                       icon="warning")


# Verify if data is float
def verifier_float(y):
    if type(y) != float:
        tkinter.messagebox.showwarning('', 'This data must have only float',
                                       icon="warning")


# Verify if phone number is digit
def verifier_phone(z):
    if not z.isdigit():
        tkinter.messagebox.showwarning('', 'The Phone Number Must Have Only Digits',
                                       icon="warning")



