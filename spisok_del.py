from tkinter import *
root = Tk()
root.geometry('300x400')
text = Entry()
list = Text()
def add():
    todo = text.get() + '\n'
    list.insert (END ,todo)
btn = Button(text = 'ok', command = add)
list.pack()
btn.pack()
text.pack()
root.mainloop()

