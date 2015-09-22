#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Adrian
#
# Created:     22/09/2015
# Copyright:   (c) Adrian 2015
# Licence:     <your licence>
#-------------------------------------------------------------------------------
# Note: In Python 3 + Tkinter has been renamed to tkinter (lower case). When compiling on a machine with Python 2 or < make sure to change to a capital letter.
# Import tkinter
import tkinter
from tkinter import Label, Entry
# Define tkinter
gui = tkinter.Tk()

def main():
    # Start the GUI
    GUI()

def GUI():
    gui.title("Intelligence Game")
    gui.minsize(700, 300)

    Label(gui, text="Country").grid(row=0, column=0)
    Label(gui, text="Town").grid(row=0, column=1)
    Label(gui, text="Plant").grid(row=0, column=2)
    Label(gui, text="Name").grid(row=0, column=3)
    Label(gui, text="Points").grid(row=0, column=4)

    entry_country = Entry(gui).grid(row=1, column=0)
    entry_town = Entry(gui).grid(row=1, column=1)
    entry_plant = Entry(gui).grid(row=1, column=2)
    entry_name = Entry(gui).grid(row=1, column=3)
    gui.mainloop()

if __name__ == '__main__':
    main()