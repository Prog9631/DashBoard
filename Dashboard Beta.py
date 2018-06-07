from tkinter import Frame, Entry, Tk, Label, Button
import openpyxl
import xlrd as xl
import array as arr


import reading_excel_sheet as res
import readsheet_functions as rsf
'''def show_entry_fields():
        wb = openpyxl.load_workbook('example.xlsx')
        sheet = wb.active
        sheet['A1']=e1
        sheet['B1']=e2
        wb.save('example.xlsx')
        wb = openpyxl.load_workbook('example.xlsx')
        Stock = sheet['B1'].value
        print(Stock) '''




def Act1(i):
        
        master = Tk()
        frame1= Frame(master, highlightbackground="red", highlightcolor="green", highlightthickness=10, width=400, height = 50, bd= 0)
        frame1.grid()
        
        L1=Label(frame1, text=i.cget('text'))
        L1.grid(row=0, column=3)
 

        L2=Label(frame1, text="Opening Stock")
        L2.grid(row=int(L1.grid_info()['row'])+ 2  , column=int(L1.grid_info()['column']))
        L2e=Label(frame1, text=rsf.find_val('data_sheet.xlsx', 'Sheet3',str(i.cget('text')),'Prodcution', 'OP stock'))
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
frame2= Frame(master1, highlightbackground="green", highlightcolor="green", highlightthickness=10, width=400, height = 50, bd= 0)
frame2.pack()
Heading=Label(frame2, text="DASHBOARD")
Heading.grid(row=1, column=1)

arr = []

def tst(k):
        print(k.cget('text'))

for i in range(1, res.worksheet.nrows - 1):
        button=Button(frame2, text=res.rowval[i])
        button.grid(row=2, column=i)
        button.configure(command= lambda k=button: Act1(k))
        button.grid(row=2, column=i)
        arr.append(res.rowval[i])







#seperator=Frame(height=2, bd=1, relief=SUNKEN)
#seperator.pack(fill=X, padx=5, pady=5)


#Button(master, text='Quit', command=master.quit).grid(row=3, column=0, sticky=W, pady=4)
#Button(master, text='Show', command=show_entry_fields).grid(row=3, column=1, sticky=W, pady=4)

master1.mainloop()




