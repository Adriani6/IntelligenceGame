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
from tkinter import Label, Entry, Button
from countries import XML
from towns import City_XML
# Define tkinter
gui = tkinter.Tk()


def main():
    # Start the GUI
    GUI()

def GUI():
    gui.title("Intelligence Game")
    gui.minsize(700, 20)

    Label(gui, text="Country").grid(row=0, column=0)
    Label(gui, text="Town").grid(row=0, column=1)
    Label(gui, text="Plant").grid(row=0, column=2)
    Label(gui, text="Name").grid(row=0, column=3)
    Label(gui, text="Points").grid(row=0, column=4)
    Label(gui, text="Status: No Opponent").grid(row=8, column=0)

    Label(gui, text="").grid(row=1, column=0, rowspan=5, columnspan=5, pady=50)

    entry_country = Entry(gui)
    entry_country.grid(row=7, column=0, padx=5)
    entry_town = Entry(gui)
    entry_town.grid(row=7, column=1, padx=5)
    entry_plant = Entry(gui)
    entry_plant.grid(row=7, column=2, padx=5)
    entry_name = Entry(gui)
    entry_name.grid(row=7, column=3, padx=5)

    button = Button(gui, text="Finish Round", command=lambda: finished(entry_country.get())).grid(row=7, column=4)


    gui.mainloop()

def finished(country):
    XML.searchCountryInDB(country)
    City_XML.searchCityInDB("city")
if __name__ == '__main__':
    main()