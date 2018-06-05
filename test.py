from tkinter import Tk, Label, Button, LEFT, RIGHT, TOP, Entry, END
import openpyxl


#class Putting:
#    def __init__(self):
#        self.name="Name"

def Append1(entry1):
        wb = openpyxl.load_workbook('example.xlsx')
        sheet = wb.get_sheet_by_name('Sheet3')
        sheet['A1']=entry1.value
        return

def Append2(Arg2):
        wb = openpyxl.load_workbook('example.xlsx')
        sheet = wb.get_sheet_by_name('Sheet3')
        sheet['B1']=entry2.value
        return







#Loading Sheet



class MyFirstGUI:
    
    def __init__(self, master):
        self.master = master
        master.title("A simple GUI")
#Labels
        self.label = Label(master, text="Daily Product Report")
        self.label.pack()

#Entry Widget

        entry1 = Entry(master)
        entry1.grid(row=0, column=1)

        
        entry2 = Entry(master)
        entry2.grid(row=1, column=2)                
        
#buttons
        self.greet_button = Button(master, text="Append1", command=Append1(entry1.value))
        self.greet_button.pack()
           
        self.close_button = Button(master, text="Append2", command=Append2(entry2.value))
        self.close_button.pack()

        self.Get_data = Button(master, text="Stock", command=self.Get_data)
        self.Get_data.pack()




    def Get_data(self):
            a3 = sheet['C1'].value
            return
            print(a3)





root = Tk()
my_gui = MyFirstGUI(root)
root.mainloop()






        
  
        


    

    
