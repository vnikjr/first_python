from tkinter import *
from tkinter import messagebox
 
root = Tk()
root.title("викторина")
root.geometry("400x400")

def que_one():
    question = Label( root, text="висит груша нельзя скушать")
    answer = Entry()
    btn = Button (root, text="ответить", command=lambda: game_1(que_two))
    question.grid(row=0)
    answer.grid(row=1)
    btn.grid(row=2)
que_one()

    def game_1(que_two):
        if answer.get() == "лампочка":
            que_two()
        else:
            messagebox.showerror ("Error!", "попробуй ещё раз!")
def que_two():
    question_2 = Label( root, text="длинная залёная пахнет калбасой")
    answer_2 = Entry()
    btn_2 = Button (root, text="ответить" )
    question_2.grid(row=0)
    answer_2.grid(row=1)
    btn_2.grid(row=2)

root.mainloop()
