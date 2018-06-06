from tkinter import Frame, Entry, Tk, Label, Button
import openpyxl
import xlrd as xl


import reading_excel_sheet as res

'''def show_entry_fields():
        wb = openpyxl.load_workbook('example.xlsx')
        sheet = wb.active
        sheet['A1']=e1
        sheet['B1']=e2
        wb.save('example.xlsx')
        wb = openpyxl.load_workbook('example.xlsx')
        Stock = sheet['B1'].value
        print(Stock) '''




def Act1():
        master = Tk()
        frame1= Frame(master, highlightbackground="red", highlightcolor="green", highlightthickness=10, width=400, height = 50, bd= 0)
        frame1.pack()
        L1=Label(frame1, text="Product Name")
        L1.grid(row=0, column=3)
        L1e=Label(frame1, text=res.desired_cell.value)
        L1e.grid(row=int(L1.grid_info()['row'])+ 1  , column=int(L1.grid_info()['column']))


        L2=Label(frame1, text="Opening Stock")
        L2.grid(row=int(L1.grid_info()['row'])+ 2  , column=int(L1.grid_info()['column']))
        L2e=Label(frame1, text="43523")
        L2e.grid(row=int(L1.grid_info()['row'])+ 3  , column=int(L1.grid_info()['column']))



        L3=Label(frame1, text="Today")
        L3.grid(row=int(L1.grid_info()['row'])+ 4  , column=int(L1.grid_info()['column']) - 2)
        L3e=Label(frame1, text="2465")
        L3e.grid(row=int(L1.grid_info()['row'])+ 5  , column=int(L1.grid_info()['column']) -2)


        L4=Label(frame1, text="To Month")
        L4.grid(row=int(L1.grid_info()['row'])+ 4  , column=int(L1.grid_info()['column']))
        L4e=Label(frame1, text="6845")
        L4e.grid(row=int(L1.grid_info()['row'])+ 5 , column=int(L1.grid_info()['column']))


        L5=Label(frame1, text="To Date")
        L5.grid(row=int(L1.grid_info()['row'])+ 4  , column=int(L1.grid_info()['column']) +2)
        L5e=Label(frame1, text="45765")
        L5e.grid(row=int(L1.grid_info()['row'])+ 5 , column=int(L1.grid_info()['column']) + 2)



master1=Tk()

Heading=Label(frame1, text="Product Name")
Heading.grid(row=1, column=o)
for (1, i<int(max_row))
        b1 = Button(master1, text=res.desired_cell.value, command=None)
        b1.grid(row=0, column=i)

b2 = Button(master1, text="PAC-100S", command=Act1)
b2.grid(row=0, column=1)


#seperator=Frame(height=2, bd=1, relief=SUNKEN)
#seperator.pack(fill=X, padx=5, pady=5)


#Button(master, text='Quit', command=master.quit).grid(row=3, column=0, sticky=W, pady=4)
#Button(master, text='Show', command=show_entry_fields).grid(row=3, column=1, sticky=W, pady=4)

master1.mainloop()




