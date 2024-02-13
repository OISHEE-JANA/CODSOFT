import tkinter as tk
from tkinter import *

def click(event):
    global scvalue
    text = event.widget.cget("text")
    if text == "=":
        if scvalue.get().isdigit():
            value = int(scvalue.get())
        else:
            value = eval(screen.get())
        scvalue.set(value)
        screen.update()
    elif text == "C":
        clear()
    else:
        scvalue.set(scvalue.get() + text)
        screen.update()
def clear():
    scvalue.set("")
    screen.update()

root = Tk()
root.geometry("400x500")
root.title("Calculator")
scvalue = StringVar()
scvalue.set("")
screen = Entry(root, textvar=scvalue, font=("times new roman", 25, "bold"))
screen.pack(fill=X, ipadx=4, ipady=6, padx=10)

f = Frame(root, bg="grey")
b = Button(f, text="9", padx=28, pady=22, font=("times new roman", 15, "bold"))
b.pack(side=LEFT)
b.bind("<Button-1>", click)


b = Button(f, text="8", padx=28, pady=22, font=("times new roman", 15, "bold"))
b.pack(side=LEFT)
b.bind("<Button-1>", click)


b = Button(f, text="7", padx=28, pady=22, font=("times new roman", 15, "bold"))
b.pack(side=LEFT)
b.bind("<Button-1>", click)

b = Button(f, text="6", padx=28, pady=22, font=("times new roman", 15, "bold"))
b.pack(side=LEFT)
b.bind("<Button-1>", click)

f.pack()

f = Frame(root, bg="grey")
b = Button(f, text="5", padx=28, pady=22, font=("times new roman", 15, "bold"))
b.pack(side=LEFT)
b.bind("<Button-1>", click)

b = Button(f, text="4", padx=28, pady=22, font=("times new roman", 15, "bold"))
b.pack(side=LEFT)
b.bind("<Button-1>", click)

b = Button(f, text="3", padx=28, pady=22, font=("times new roman", 15, "bold"))
b.pack(side=LEFT)
b.bind("<Button-1>", click)

b = Button(f, text="2", padx=28, pady=22, font=("times new roman", 15, "bold"))
b.pack(side=LEFT)
b.bind("<Button-1>", click)

f.pack()

f = Frame(root, bg="grey")
b = Button(f, text="1", padx=28, pady=22, font=("times new roman", 15, "bold"))
b.pack(side=LEFT)
b.bind("<Button-1>", click)

b = Button(f, text="0", padx=28, pady=22, font=("times new roman", 15, "bold"))
b.pack(side=LEFT)
b.bind("<Button-1>", click)

b = Button(f, text=".", padx=28, pady=22, font=("times new roman", 15, "bold"))
b.pack(side=LEFT)
b.bind("<Button-1>", click)

b = Button(f, text="C", padx=28, pady=22, font=("times new roman", 15, "bold"))
b.pack(side=LEFT)
b.bind("<Button-1>", click)

f.pack()

f = Frame(root, bg="grey")
b = Button(f, text="+", padx=28, pady=22, font=("times new roman", 15, "bold"))
b.pack(side=LEFT)
b.bind("<Button-1>", click)

b = Button(f, text="-", padx=28, pady=22, font=("times new roman", 15, "bold"))
b.pack(side=LEFT)
b.bind("<Button-1>", click)

b = Button(f, text="/", padx=28, pady=22, font=("times new roman", 15, "bold"))
b.pack(side=LEFT)
b.bind("<Button-1>", click)

b = Button(f, text="*", padx=28, pady=22, font=("times new roman", 15, "bold"))
b.pack(side=LEFT)
b.bind("<Button-1>", click)

f.pack()

f = Frame(root, bg="grey")
b = Button(f, text="%", padx=28, pady=22, font=("times new roman", 15, "bold"))
b.pack(side=LEFT)
b.bind("<Button-1>", click)

b = Button(f, text="=", padx=28, pady=22, font=("times new roman", 15, "bold"))
b.pack(side=LEFT)
b.bind("<Button-1>", click)

f.pack()

root.mainloop()

