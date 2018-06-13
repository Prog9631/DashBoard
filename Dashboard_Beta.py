from tkinter import Frame, Entry, Tk, Label, Button, ttk, HORIZONTAL, RAISED, SUNKEN, S, W, E, N
import openpyxl
import xlrd as xl
import array as arr
import Dictionery as dic
from datetime import datetime
import time
from time import gmtime, strftime
import Excel_Display_Window
#from Target_Entry_Window import Target_button
import Target_Entry_Window as tew

import reading_excel_sheet as res
import readsheet_functions as rsf

master1=Tk()
master1.title("DashBoard")
master1.grid_columnconfigure(0,weight=1)

frame2= Frame(master1, highlightbackground="green", highlightcolor="green", highlightthickness=2, bd= 0)
frame2.grid_columnconfigure(0,weight=1)
frame2.grid_rowconfigure(0, weight=1)
frame2.grid_columnconfigure(0, weight=1)
frame2.grid(row=0, column=0)
Heading=Label(frame2, text="DASHBOARD", font=("Courier", 44))
Heading.grid(row=0, columnspan=2)


#### DATE
Date = Label(frame2, font=('Courier', 15), bg='grey', text = strftime("%d %b %Y", gmtime()))
Date.grid(row=0, column = 20, sticky = N+E+W)
#### DATE

#### CLOCK
time1 = ''
clock = Label(frame2, font=('Courier', 15), bg='grey')
clock.grid(row=0, column=20, sticky = E+W)
def tick():
    global time1
   
    time2 = time.strftime('%a,%H:%M:%S')
  
    if time2 != time1:
        time1 = time2
        clock.config(text=time2)

    clock.after(200, tick)

tick()
#### CLOCK
       
ttk.Separator(frame2, orient = HORIZONTAL).grid(row=1, columnspan = 5 , sticky ="sew")

arr = []





#### Prod BUTTONS
for i in range(1, res.worksheet.nrows - 1):
        button=Button(frame2, text=res.rowval[i], bg="red", fg="white", width=10)
        button.grid(row=2, column=i-1)
        button.configure(command= lambda k=button: Act1(k))
        
        arr.append(res.rowval[i])
#### Prod BUTTONS



tew.Target_button(frame2)
master1.resizable(False, False)

master1.mainloop()




