'''
Internship Task - 1
Creator :: Avijit Dey
Title :: To-Do List in Python using Tkinter
Date :: 05/09/2023
'''
from tkinter import *
import tkinter.font as toft

root = Tk()

# Configure Window
root.title("Do-IT")
SizeWindow = "400x500"

root.geometry(SizeWindow)
root.resizable(False,False)
root.iconbitmap("addicon.ico")

root.configure(
    bg = "#7393B3"
)

#Label Header
HeaderFrame = Frame(root)
HeaderFrame.pack()

TextHeader = StringVar()
TextHeader.set("Do-IT")
Header = Label(HeaderFrame, 
    textvariable= TextHeader
)

Header.configure(
    bg="#7393B3",
    fg = "#ffffff",
    font =toft.Font(
        family = "Verdana",
        size= 30,
        weight = "bold"
    )
)
Header.pack()

Input = Frame(root)

#Entry Text Box
InputToDo = Entry(Input,
    relief = "ridge",
    bd = 5,
    bg= "#c8d4e8",
    width = 50,
    justify= "center",
    borderwidth=10,
    font =toft.Font(
        family = "courier")
)

InputToDo.pack()
Input.pack(pady=10, padx=20)

#Button
BtnFrame = Frame(root)

def add_task():
    todo.insert(END, "> " + InputToDo.get())
    InputToDo.delete(0,END)
    
def delete_task():
    todo.delete(ANCHOR)



add = Button(BtnFrame,text = "Add",command=add_task)

delete = Button(BtnFrame,text = "Delete",command=delete_task)

add_image = PhotoImage(file='check.png')
add_label = Label(image = add_image)

add.configure(bg = "#AFE1AF",relief = "ridge", width = 7, height =1,font =toft.Font(
        family = "Verdana", size =12))
delete.configure(bg = "#AFE1AF",relief = "ridge", width = 7, height =1,font =toft.Font(
        family = "Verdana", size =12))


add.grid(row = 0, column = 0, padx = 15)
delete.grid(row = 0, column = 1, padx = 15)


BtnFrame.configure(bg = "#7393b3")
BtnFrame.pack(pady = 10)

#todo list

ListFrame = Frame(root)

data = []

todo = Listbox(ListFrame)
for do in data:
    x = "> " + do
    todo.insert(END,x)
todo.configure(
    width = 32,
    height = 100,
    font = toft.Font(
        family = "courier",
        size = 12,
        weight = "bold"
    )
)
scroll = Scrollbar(ListFrame)

todo.configure(yscrollcommand=scroll.set,
    bg= "#c8d4e8",
    highlightthickness=0,
    selectbackground= "#ffffff",
    selectforeground= "#7393B3",
    activestyle= "none"
)
todo.pack(side=LEFT, fill=BOTH)
scroll.configure(command = todo.yview)
scroll.pack(side=RIGHT,fill = BOTH)

ListFrame.configure(
    pady = 20,
    padx = 20,
    bg = "#7393B3"
)
ListFrame.pack()

root.mainloop()
