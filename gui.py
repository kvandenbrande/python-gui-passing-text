#!/bin/python
# -*- coding: utf-8 -*-
#__author__ = "Kevin Van den Brande"

import tkinter as tk
from tkinter import ttk
from main import printbericht

def doorgeven():
    bericht=inputnaam.get()
    printbericht(bericht)


#create instance
win = tk.Tk()

#create title
win.title ('Simple GUI with functions')

#create frame

#create inputbox
inputnaam=tk.StringVar()
nameEntered=ttk.Entry(win, width=20, textvariable=inputnaam)
nameEntered.grid(column=0, row=1)

#create buttons
action=ttk.Button(win, text='Print text', command=doorgeven)
action.grid(column=1,row=1)


#start GUI
win.mainloop()
