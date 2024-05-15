from tkinter import *
import string
import random
import pyperclip

def generator():
    small_alphabet = string.ascii_lowercase
    capital_alphabet = string.ascii_uppercase
    numbers = string.digits
    special_characters = string.punctuation

    all = small_alphabet + capital_alphabet + numbers + special_characters
    password_length = int(length_box.get())

    if choice.get() == 1:
        passwordField.insert(0,random.sample(small_alphabet,password_length))

    if choice.get() == 2:
        passwordField.insert(0,random.sample(capital_alphabet + small_alphabet,password_length))

    if choice.get() == 3:
        passwordField.insert(0,random.sample(all,password_length))

def copy():
    random_password = passwordField.get()
    pyperclip.copy(random_password)

root = Tk()
root.config(background='black')
choice = IntVar()
Font = ('arial',13, 'bold')
passwordLabel = Label(root, text='Password Generator', font=('times new roman',20,'bold'),bg="gray20",fg = "white")
passwordLabel.grid(pady = 10)

weakRadioButton = Radiobutton(root,text='Weak',variable=choice,value=1,font=Font)
weakRadioButton.grid(pady = 5)

mediumRadioButton = Radiobutton(root,text='Medium',variable=choice,value=2,font=Font)
mediumRadioButton.grid(pady = 5)

strongRadioButton = Radiobutton(root,text='Strong',variable=choice,value=3,font=Font)
strongRadioButton.grid(pady = 5)

lengthLabel = Label(root, text='Password Length', font=Font,fg='white',bg="gray20")
lengthLabel.grid(pady = 5)

length_box = Spinbox(root,from_=5,to=20,font=Font,width=5)
length_box.grid(pady = 5)

generateButton = Button(root,text = "Generate", font=Font, command=generator)
generateButton.grid(pady = 5)

passwordField = Entry(root,font=Font,width=25,bd = 2)
passwordField.grid()

copyButton = Button(root,text = "Copy",bd = 2,font=Font,command=copy)
copyButton.grid()
root.mainloop()

