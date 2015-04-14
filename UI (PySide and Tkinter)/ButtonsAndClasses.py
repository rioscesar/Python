from tkinter import *


class BButton(object):
    def __init__(self, master):
        frame = Frame(master)
        frame.pack()

        self.printbutton = Button(frame, text="Message", command=self.printMessage)
        self.printbutton.pack(side=LEFT)
        self.quitbutton = Button(frame, text="Quit", command=frame.quit)
        self.quitbutton.pack(side=LEFT)

    @staticmethod
    def printMessage():
        print("Message :p")

root = Tk()
b = BButton(root)


root.mainloop()