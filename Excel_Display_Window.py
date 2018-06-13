from tkinter import Frame, Entry, Tk, Label, Button, ttk, HORIZONTAL, RAISED, SUNKEN, S, W, E, N
import openpyxl
import xlrd as xl
import array as arr
import Dictionery as dic

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
