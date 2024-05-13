from tkinter import *

window = Tk()
window.title("My First GUI Program")
window.minsize(width=600, height=400)

# Label

my_label = Label(text="I am a Label", font=("Arial", 24))
my_label.grid(column=1, row=0)

my_label["text"] = "New text"
my_label.config(text="New text")

# Entry

input = Entry(width=12)
input.grid(column=1, row=1)

# Button

def button_click():
    new_label = input.get()
    my_label.config(text=new_label)

button = Button(text="Click me", command=button_click)
button.grid(column=1, row=2)


window.mainloop()
