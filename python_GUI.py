import numpy as np
import tkinter as tk
import math as ma
from tkinter import messagebox as tkMessageBox
from tkinter import *
import reading_excel_sheet as res

top = tk.Tk()
B=[]


for i in range(len(res.rowval)):
    def helloCallBack():
        val = 1
        tkMessageBox.showinfo( "Hello Python", res.rowval[i])
    B=tk.Button(top, text =res.rowval[i], command = helloCallBack)
    B.pack()

top.mainloop()

##
##root = Tk()
##
##eq1_ent = Entry( text = "", width=6)
##entry_name = eq1_ent.get()
##eq1_ent.grid(row = 11, sticky = W)
##
##mainloop()
