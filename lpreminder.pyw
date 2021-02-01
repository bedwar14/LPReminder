import tkinter as tk
from tkinter import ttk
import tkinter.font as font

class bgManager:
    def __init__(self):
        self.rval = 0
        self.gval = 0
        self.bval = 255
        self.BlueToRed = "toRed"
        self.RedToGreen = "toGreen"
        self.GreenToBlue = "toBlue"
        self.state= self.BlueToRed
        self.iter = 0
    def nextState(self):
        print(f'nextState {self.state}-> {self.rval},{self.gval},{self.bval}')
        if self.state == self.BlueToRed:
            return self.RedToGreen
        elif self.state == self.RedToGreen:
            return self.GreenToBlue
        else:
            return self.BlueToRed
    def resetRGB(self):
        print(f'resetRGB start {self.state}-> {self.rval},{self.gval},{self.bval}')
        self.rval = 0
        self.gval = 0
        self.bval = 0
        if self.state == self.BlueToRed:
            self.bval = 255
        elif self.state == self.RedToGreen:
            self.rval = 255
        else:
            self.gval = 255
        print(f'resetRGB End {self.state}-> {self.rval},{self.gval},{self.bval}')
    def moveNextState(self):
        self.state = self.nextState()
    def shiftColor(self):
        self.iter = self.iter + 1
        print(f'shiftColor {self.state}-> {self.rval},{self.gval},{self.bval}')
        if self.state == self.BlueToRed:
            self.bval = max(0,self.bval-5)
            self.rval = min(255,self.rval+5)
        elif self.state == self.RedToGreen:
            self.rval = max(0,self.rval-5)
            self.gval = min(255,self.gval+5)
        else:
            self.gval = max(0,self.gval-5)
            self.bval = min(255,self.bval+5)
    def getBGColor(self):
        return f'#{self.rval:02x}{self.gval:02x}{self.bval:02x}'
    def shouldChangeState(self):
        if self.state == self.BlueToRed:
            return self.rval >= 255
        elif self.state == self.RedToGreen:
            return self.gval >= 255
        else:
            return self.bval >= 255

root = tk.Tk()
root.geometry("600x400")
mgr = bgManager()
rfont = font.Font(family="Helvetica", size=24)
rect1 = tk.Label(root, text="put Your Hours into Liquid Planner!",font=rfont, bg="blue",fg="white")
rect1.pack(fill="both", expand=True)

def task():
    if mgr.iter > 3000:
        root.destroy()
    else:
        rect1["text"]="Enter Your Hours into Liquid Planner!"
        mgr.shiftColor()
        if mgr.shouldChangeState():
            mgr.moveNextState()
            mgr.resetRGB()
        rect1["bg"] = mgr.getBGColor()
        root.after(20, task)

root.after(20, task)
root.mainloop()
