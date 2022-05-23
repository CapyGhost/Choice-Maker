from tkinter import *
import tkinter
import random

def make_choice():
    options = [choice1.get(), choice2.get()]
    choice = tkinter.Label(text=random.choice(options), font="Kristen_ITC: 14")
    choice.pack()
app = Tk()
app.title("Choice Maker")
app.geometry("800x600")

text1 = tkinter.Label(text="Welecome Enter a Choice \nEnter first choice", font="Kristen_ITC: 14")
text1.pack()

choice1 = tkinter.Entry(width="50", font="Kristen_ITC: 14")
choice1.pack()

text2 = tkinter.Label(text="Enter second choice", font="Kristen_ITC: 14")
text2.pack()

choice2 = tkinter.Entry(width="50", font="Kristen_ITC: 14")
choice2.pack()

space = tkinter.Label(text=" ", font="Kristen_ITC: 14")
space.pack()

button1 = tkinter.Button(text="Submit", font="Kristen_ITC: 14", bg="red", height="5", width="50", command=make_choice)
button1.pack()

app.mainloop()