from tkinter import *
from tkinter import ttk
from random import randint

App = Tk()
App.title("Dice Roller")
App.geometry("220x220")
App.resizable(0, 0)

Dice = {
    0 : '🎲',
    1 : '⚀',
    2 : '⚁',
    3 : '⚂',
    4 : '⚃',
    5 : '⚄',
    6 : '⚅'
}

lbl = Label(App, text=Dice[0], font=('Times', 100))
lbl.grid(row=0, column=0, padx=40)


def roll():
    dice_choice = randint(1, 6)

    dice_lbl = Label(App, text=Dice[dice_choice], font=('Times', 100), width=2)
    dice_lbl.grid(row=0, column=0, padx=40)


roll_button = ttk.Button(App, text='Roll', command=roll, width=10)
roll_button.grid(pady=10)

App.mainloop()
