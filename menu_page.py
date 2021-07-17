import tkinter as tk
from tkinter import *


class Menu(tk.Frame):
    def __init__(self, master=None, **kw):
        super().__init__(master, **kw)
        self.master = master

        self.create_frame()
        self.create_label()
        self.create_button()

    def student_info(self):
        self.master.destroy()
        import College_FrontEnd

    def fee_report(self):
        self.master.destroy()
        import receipt_frontend

    def lybrary(self):
        self.master.destroy()
        import library_frontend

    def mark_sheet(self):
        self.master.destroy()
        import marksheet_fontend

    def create_frame(self):
        self.title_Frame = LabelFrame(root, font=('arial', 50, 'bold'), width=1000, height=100, bg='aquamarine4',
                                      relief='raise', bd=13)
        self.title_Frame.grid(row=0, column=0, pady=50)

        self.Frame_1 = LabelFrame(root, font=('arial', 17, 'bold'), width=1000, height=100, bg='aquamarine4',
                                  relief='ridge', bd=10)
        self.Frame_1.grid(row=1, column=0, padx=280)

        self.Frame_2 = LabelFrame(root, font=('arial', 17, 'bold'), width=1000, height=100, bg='aquamarine4',
                                  relief='ridge', bd=10)
        self.Frame_2.grid(row=2, column=0, padx=130, pady=7)

        self.Frame_3 = LabelFrame(root, font=('arial', 17, 'bold'), width=1000, height=100, bg='aquamarine4',
                                  relief='ridge', bd=10)
        self.Frame_3.grid(row=3, column=0, pady=7)

        self.Frame_4 = LabelFrame(root, font=('arial', 17, 'bold'), width=1000, height=100, bg='aquamarine4',
                                  relief='ridge', bd=10)
        self.Frame_4.grid(row=4, column=0, pady=7)

    def create_label(self):
        self.title_Label = Label(self.title_Frame, text='MENU', font=('Courier', 30, 'bold'), bg='aquamarine4')
        self.title_Label.grid(row=0, column=0, padx=150)

        self.student_info_label = Label(self.Frame_1, text='STUDENT PROFILE', font=('Courier', 25, 'bold'),
                                        bg='aquamarine4')
        self.student_info_label.grid(row=0, column=0, padx=50, pady=5)

        self.fee_report_label = Label(self.Frame_2, text='FEE REPORT', font=('Courier', 25, 'bold'), bg='aquamarine4')
        self.fee_report_label.grid(row=0, column=0, padx=100, pady=5)

        self.library_label = Label(self.Frame_3, text='LIBRARY SYSTEM', font=('Courier', 25, 'bold'), bg='aquamarine4')
        self.library_label.grid(row=0, column=0, padx=60, pady=5)

        self.marksheet_label = Label(self.Frame_4, text='MARK SHEET', font=('Courier', 25, 'bold'), bg='aquamarine4')
        self.marksheet_label.grid(row=0, column=0, padx=101, pady=5)

    def create_button(self):
        self.button_student = Button(self.Frame_1, text='VIEW', font=('Courier', 16, 'bold'), width=8,
                                     bg='aquamarine4', command=self.student_info)
        self.button_student.config(activebackground="#41B77F", relief=RAISED)
        self.button_student.grid(row=0, column=3, padx=50)

        self.button_fee = Button(self.Frame_2, text='VIEW', font=('Courier', 16, 'bold'), width=8,
                                 bg='aquamarine4', command=self.fee_report)
        self.button_fee.config(activebackground="#41B77F", relief=RAISED)
        self.button_fee.grid(row=0, column=3, padx=50)

        self.button_library = Button(self.Frame_3, text='VIEW', font=('Courier', 16, 'bold'), width=8,
                                     bg='aquamarine4', command=self.lybrary)
        self.button_library.config(activebackground="#41B77F", relief=RAISED)
        self.button_library.grid(row=0, column=3, padx=50)

        self.button_mark = Button(self.Frame_4, text='VIEW', font=('Courier', 16, 'bold'), width=8,
                                  bg='aquamarine4', command=self.mark_sheet)
        self.button_mark.config(activebackground="#41B77F", relief=RAISED)
        self.button_mark.grid(row=0, column=3, padx=50)


root = tk.Tk()
root.geometry("1350x750")
root.resizable(False, False)
root.title("Université Espoir")
root.iconbitmap("logo1.ICO")
root.config(background="aquamarine4")

app = Menu(master=root)
app.mainloop()
