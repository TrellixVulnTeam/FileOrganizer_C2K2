import os
import tkinter
from pathlib import Path
from tkinter import *
from tkinter import filedialog

from filesorting import *
from renameutility import *

def getDir():
    currentDir = filedialog.askdirectory()
    currentDir = currentDir.replace("/","\\")
    os.chdir(currentDir)
def singleRename(filenames,change):
    object = renameUtil(filenames,change)
    object.renameSingle()

def bulkRename(filenames,change):
    object = renameUtil(filenames, change)
    object.renameBulk()

def renameFunc(currentDir):
    filenames = []
    top = Toplevel()
    canvas = tkinter.Canvas(top, width=600, height=300)
    canvas.grid(columnspan=4, rowspan=3)
    top.title("Rename Activity")
    title = Label(top, text="File Sorter",font = "Tahoma",fg="black",height=2,width=15)
    inst = Label(top, text="Enter new name: ",font = "Tahoma",fg="black",height=2,width=15)
    current = filedialog.askopenfilenames(initialdir=currentDir)
    changed = Entry(top)
    for file in current:
        temp = Path(file)
        filenames.append(temp.name)
    print(filenames)
    single = Button(top, text="Single Rename", command=lambda: singleRename(filenames,changed.get()),font = "Tahoma",bg="#20bebe",fg="black",height=2,width=15)
    bulk = Button(top, text="Bulk Rename", command=lambda: bulkRename(filenames,changed.get()),font = "Tahoma",bg="#20bebe",fg="black",height=2,width=15)
    title.grid(row=0, column=1)
    inst.grid(row=1, column=1)
    changed.grid(row=2, column=1)
    single.grid(row = 3, column=0)
    bulk.grid(row=3, column=3)




root = Tk()
canvas = tkinter.Canvas(root,width = 600,height=300)
canvas.grid(columnspan=3,rowspan=3)
root.title("File Sorter")
title = Label(root,text="File Sorter",font = "Tahoma",fg="black",height=2,width=15)
select = Button(root,text="Select a folder: ",command= lambda : getDir(),font = "Tahoma",bg="#20bebe",fg="black",height=2,width=15)
sort = Button(root,text="Sort",command= lambda : filesort(currentDir),font = "Tahoma",bg="#20bebe",fg="black",height=2,width=15)
rename = Button(root,text="Rename",command=lambda : renameFunc(currentDir),font = "Tahoma",bg="#20bebe",fg="black",height=2,width=15)

title.grid(row=0,column=1)
select.grid(row=1,column=1)
sort.grid(row=2,column=0)
rename.grid(row=2,column=3)

root.mainloop()