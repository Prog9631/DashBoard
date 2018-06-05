from tkinter import *
import openpyxl

def show_entry_fields():
        wb = openpyxl.load_workbook('example.xlsx')
        sheet = wb.active
        sheet['A1']=e1
        sheet['B1']=e2
        wb.save('example.xlsx')
        wb = openpyxl.load_workbook('example.xlsx')
        Stock = sheet['B1'].value
        print(Stock)

master = Tk()
Label(master, text="First Name").grid(row=0)
Label(master, text="Last Name").grid(row=1)

e1 = Entry(master)
e2 = Entry(master)

e1.grid(row=0, column=1)
e2.grid(row=1, column=1)

Button(master, text='Quit', command=master.quit).grid(row=3, column=0, sticky=W, pady=4)
Button(master, text='Show', command=show_entry_fields).grid(row=3, column=1, sticky=W, pady=4)

mainloop( )
