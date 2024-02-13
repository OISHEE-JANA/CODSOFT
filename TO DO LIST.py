from tkinter import *
from tkinter import messagebox

def newTask():
    task = my_entry.get()
    if task != "":
        lb.insert(END, task)
        my_entry.delete(0, "end")
    else:
        messagebox.showwarning("ERROR", "Please enter your task.")

def deleteTask():
    lb.delete(ANCHOR)
    
ws = Tk()
ws.geometry('800x500')
ws.title('TO DO LIST')
ws.config(bg='#000000')
ws.label = Label(text= "TO-DO-LIST",font='arial 15 bold', bg='grey' )
ws.label.pack(side='top', fill=BOTH)

frame = Frame(ws)
frame.pack(pady=10)

lb = Listbox(
    frame,
    width=60,
    height=10,
    font=("arial", 15, "bold"),
    highlightthickness=0,
    activestyle="none",
)
lb.pack(side=LEFT, fill=BOTH)

task_list = [
    
    ]

for item in task_list:
    lb.insert(END, item)

sb = Scrollbar(frame)
sb.pack(side=RIGHT, fill=BOTH)

lb.config(yscrollcommand=sb.set)
sb.config(command=lb.yview)

my_entry = Entry(
    ws,
    font=("arial", 15)
    )

my_entry.pack(padx=60,pady=20)

button_frame = Frame(ws)
button_frame.pack(pady=50)

addTask_btn = Button(
    button_frame,
    text='ADD YOUR TASK',
    font=("arial", 15, "bold"),
    padx=40,
    pady=30,
    command=newTask
)
addTask_btn.pack(fill=BOTH, expand=True, side=LEFT)

delTask_btn = Button(
    button_frame,
    text='DELETE YOUR TASK',
    font=("arial", 15, "bold"),
    padx=20,
    pady=10,
    command=deleteTask
)
delTask_btn.pack(fill=BOTH, expand=True, side=LEFT)


ws.mainloop()