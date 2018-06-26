from tkinter import Frame, Entry, Tk, Label, Button, ttk, HORIZONTAL, RAISED, SUNKEN, S, W, E, N
import openpyxl
import Dashboard_Beta as DB

wb = openpyxl.load_workbook('Target_Entry.xlsx')
sheet = wb['Sheet1']

DB.tick()
#### Target Feed Butons
def Target_button(frameT):
    tgt_btn=Button(frameT, text="Feed target", bg="red", fg="white", width=10)
    tgt_btn.grid(row=1, column=20, sticky = N+S+W)
    tgt_btn.configure(command= lambda k=tgt_btn: TargetEntry())



    
#### Target Feed Butons

def TargetEntry():
    master2=Tk()
    master2.title("Feed target")
    master2.grid_columnconfigure(0, weight=1)
    frame3= Frame(master2, highlightbackground="green", highlightcolor="green", highlightthickness=2, bd= 0)
    frame3.grid(row=0, column=0)
    Heading=Label(frame3, text="DASHBOARD", font=("Courier", 44))
    Heading.grid(row=0, columnspan=2)


    L2=Label(frame3, text="PAC 18")
    L2.grid(row=1, column=1)

