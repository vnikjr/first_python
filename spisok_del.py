from tkinter import *
root = Tk()
root.geometry('300x400')
def add():
    todo = text.get() + '\n'
    list.insert (END ,todo)
btn = Button(text = 'ok', command = add)
btn.pack()
text = Entry()
text.pack()
list = text
list.pack()
root.mainloop()
