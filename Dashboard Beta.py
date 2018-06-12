from tkinter import Frame, Entry, Tk, Label, Button, ttk, HORIZONTAL, RAISED, SUNKEN, S, W, E, N
import openpyxl
import xlrd as xl
import array as arr
import Dictionery as dic
from datetime import datetime
import time
from time import gmtime, strftime


DayDate =  print(strftime("%A, %d %b %Y  +0000", gmtime()))
print(strftime("%H:%M:%S"))


import reading_excel_sheet as res
import readsheet_functions as rsf


def Act1(i):
        
        master = Tk()
        frame1= Frame(master, highlightbackground="red", highlightcolor="green", highlightthickness=2, width=400, height = 50, bd= 0)
        frame1.grid()
        
        L1=Label(frame1, text=i.cget('text'))
        L1.grid(row=0, column=3)
 

        L2=Label(frame1, text="Opening Stock")
        L2.grid(row=int(L1.grid_info()['row'])+ 2  , column=int(L1.grid_info()['column']))
        L2e=Label(frame1, text=rsf.find_val('data_sheet.xlsx','Sheet3', str(i.cget('text')), 'OP stock'))
        L2e.grid(row=int(L1.grid_info()['row'])+ 3  , column=int(L1.grid_info()['column']))

      

        L3=Label(frame1,text="Today")
        L3.grid(row=int(L1.grid_info()['row'])+ 4  , column=int(L1.grid_info()['column']) - 2)
        L3e=Label(frame1, text=rsf.find_val('data_sheet.xlsx','Sheet3', str(i.cget('text')), 'Production', 'today'))
        L3e.grid(row=int(L1.grid_info()['row'])+ 5  , column=int(L1.grid_info()['column']) -2)


        L4=Label(frame1, text="To Month")
        L4.grid(row=int(L1.grid_info()['row'])+ 4  , column=int(L1.grid_info()['column']))
        L4e=Label(frame1, text = str(rsf.find_val('data_sheet.xlsx','Sheet3', str(i.cget('text')), 'Production', 'to month')) + \
                  '/' + \
                  str(rsf.find_val('data_sheet.xlsx','Sheet3', str(i.cget('text')), 'Dispatch/Sales', 'to month')))
        L4e.grid(row=int(L1.grid_info()['row'])+ 5 , column=int(L1.grid_info()['column']))

 
        L5=Label(frame1, text="To Date")
        L5.grid(row=int(L1.grid_info()['row'])+ 4  , column=int(L1.grid_info()['column']) +2)
        L5e=Label(frame1, text=rsf.find_val('data_sheet.xlsx','Sheet3', str(i.cget('text')), 'Production', 'to date'))
        L5e.grid(row=int(L1.grid_info()['row'])+ 5 , column=int(L1.grid_info()['column']) + 2)



master1=Tk()
master1.title("DashBoard")
master1.grid_columnconfigure(0,weight=1)





frame2= Frame(master1, highlightbackground="green", highlightcolor="green", highlightthickness=2, bd= 0)
frame2.grid_columnconfigure(0,weight=1)
frame2.grid_rowconfigure(0, weight=1)
frame2.grid_columnconfigure(0, weight=1)
frame2.grid(row=0, column=0)
Heading=Label(frame2, text="DASHBOARD", font=("Courier", 44))
Heading.grid(row=0, columnspan=3)


#### DATE
Date = Label(frame2, font=('Courier', 15), bg='grey', text = strftime("%d %b %Y", gmtime()))
Date.grid(row=0, column = 20, sticky = N)

Day = Label(frame2, font=('Courier', 15), bg='grey', text = strftime("%A", gmtime()))
Day.grid(row=0, column=20)



#### DATE

#### CLOCK
time1 = ''
clock = Label(frame2, font=('Courier', 15), bg='grey')
clock.grid(row=2, column=20)

def tick():
    global time1
    # get the current local time from the PC
    time2 = time.strftime('%a, %H:%M:%S')
    # if time string has changed, update it
    if time2 != time1:
        time1 = time2
        clock.config(text=time2)

    clock.after(200, tick)
tick()

#### CLOCK
       
ttk.Separator(frame2, orient = HORIZONTAL).grid(row=1, columnspan=5, sticky ="ew")

arr = []


for i in range(1, res.worksheet.nrows - 1):
        button=Button(frame2, text=res.rowval[i], bg="red", fg="white", width=10)
        button.grid(row=2, column=i-1)
        button.configure(command= lambda k=button: Act1(k))
        
        arr.append(res.rowval[i])
        
master1.resizable(False, False)

master1.mainloop()




