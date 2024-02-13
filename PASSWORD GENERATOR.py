from tkinter import *
import string
import random

def generator():
    small_alphabets = string.ascii_lowercase
    capital_alphabets = string.ascii_uppercase
    numbers = string.digits
    special_characters = string.punctuation

    all_characters = small_alphabets + capital_alphabets + numbers + special_characters
    password_length = int(length_Box.get())

    if choice.get() == 1:
        generated_password = ''.join(random.sample(small_alphabets, password_length))

    elif choice.get() == 2:
        generated_password = ''.join(random.sample(small_alphabets + capital_alphabets, password_length))

    elif choice.get() == 3:
        generated_password = ''.join(random.sample(all_characters, password_length))

    passwordField.delete(0, END) 
    passwordField.insert(0, generated_password)

def copy():
    random_password = passwordField.get()
    root.clipboard_clear() 
    root.clipboard_append(random_password)
    root.update()

root = Tk()
root.config(bg='gray20')
choice = IntVar()
Font = ('Times New Roman', 13, 'bold') 

passwordLabel = Label(root, text='Password Generator', font=('Times New Roman', 20, 'bold'), bg='gray20', fg='white')
passwordLabel.grid(pady=10)

weakRadioButton = Radiobutton(root, text='Weak', value=1, variable=choice, font=Font)
weakRadioButton.grid(pady=5)

mediumRadioButton = Radiobutton(root, text='Medium', value=2, variable=choice, font=Font)
mediumRadioButton.grid(pady=5)

strongRadioButton = Radiobutton(root, text='Strong', value=3, variable=choice, font=Font)
strongRadioButton.grid(pady=5)

lengthLabel = Label(root, text='Password Length', font=Font, bg='gray20', fg='white')
lengthLabel.grid(pady=5)

length_Box = Spinbox(root, from_=5, to_=18, width=5, font=Font)
length_Box.grid(pady=5)

generateButton = Button(root, text='Generate', font=Font, command=generator)
generateButton.grid(pady=5)

passwordField = Entry(root, width=25, bd=2, font=Font)
passwordField.grid()

copyButton = Button(root, text='Copy', font=Font, command=copy)
copyButton.grid(pady=5)

root.mainloop()
