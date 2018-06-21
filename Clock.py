import tkinter
import time


class Clock(tkinter.Label):
    """ Class that contains the clock widget and clock refresh """

    def __init__(self, parent=None, seconds=True, colon=False):
       
        tkinter.Label.__init__(self, parent)

        self.display_seconds = seconds
        if self.display_seconds:
            self.time     = time.strftime('%H:%M:%S')
        else:
            self.time     = time.strftime('%I:%M %p').lstrip('0')
        self.display_time = self.time
        self.configure(text=self.display_time)

        if colon:
            self.blink_colon()

        self.after(200, self.tick)


    def tick(self):
        """ Updates the display clock every 200 milliseconds """
        if self.display_seconds:
            new_time = time.strftime('%H:%M:%S')
        else:
            new_time = time.strftime('%I:%M %p').lstrip('0')
        if new_time != self.time:
            self.time = new_time
            self.display_time = self.time
            self.config(text=self.display_time)
        self.after(200, self.tick)


    def blink_colon(self):
        """ Blink the colon every second """
        if ':' in self.display_time:
            self.display_time = self.display_time.replace(':',' ')
        else:
            self.display_time = self.display_time.replace(' ',':',1)
        self.config(text=self.display_time)
        self.after(1000, self.blink_colon)



if __name__ == "__main__":
    """
    Create a tkinter window and populate it with elements
    One of those elements merely happens to include the clocks.
    The clock widget can be configure()d like any other Label widget.
    Nothing special needs to be added to main(). The Clock class
      updates the widget automatically when you create the widget.
    """

    # Create window and frame

    window = tkinter.Tk()
    frame  = tkinter.Frame(window, width=400, height=400 )
    frame.pack()

    # Add the frame elements, including the clock like any other element

    tkinter.Label(frame, text="Clock with seconds:").pack()

    clock1 = Clock(frame)
    clock1.pack()
    clock1.configure(bg='green',fg='yellow',font=("helvetica",35))

    tkinter.Label(frame, text=" ").pack()

    tkinter.Label(frame, text="Clock with blinking colon:").pack()

    clock2 = Clock(frame, seconds=False, colon=True)
    clock2.pack()
    clock2.configure(bg='red',fg='white',font=("arial",20))

    tkinter.Label(frame, text=" ").pack()

    tkinter.Label(frame, text="Have a nice day.").pack()

    window.mainloop()
