from tkinter import *
from math import *
import tkinter

root = tkinter.Tk()
root.title("Calculator")
root.resizable(width=False, height=False)

screen = StringVar()
screen.set("0")



# Widgets

calculation = Entry(root, textvariable = screen, font=("Verdana", 15, ), bd = 12,
                    insertwidth=4, width=14, justify=RIGHT)
calculation.grid(columnspan=4)
#   Numbers
button1 = Button(root, text='1', bg="gainsboro",
                 bd=3, padx=12, pady=5, font=("Helvetica", 14, "bold"))
button1.grid(row=2, column=0, sticky=W)
button2 = Button(root, text='2', bg="gainsboro",
                 bd=3, padx=12, pady=5, font=("Helvetica", 14, "bold"))
button2.grid(row=2, column=1, sticky=W)
button3 = Button(root, text='3', bg="gainsboro",
                 bd=3, padx=12, pady=5, font=("Helvetica", 14, "bold"))
button3.grid(row=2, column=2, sticky=W)
button4 = Button(root, text='4',  bg="gainsboro",
                 bd=3, padx=12, pady=5, font=("Helvetica", 14, "bold"))
button4.grid(row=3, column=0, sticky=W)
button5 = Button(root, text='5', bg="gainsboro",
                 bd=3, padx=12, pady=5, font=("Helvetica", 14, "bold"))
button5.grid(row=3, column=1, sticky=W)
button6 = Button(root, text='6',  bg="gainsboro",
                 bd=3, padx=12, pady=5, font=("Helvetica", 14, "bold"))
button6.grid(row=3, column=2, sticky=W)
button7 = Button(root, text='7',  bg="gainsboro",
                 bd=3, padx=12, pady=5, font=("Helvetica", 14, "bold"))
button7.grid(row=4, column=0, sticky=W)
button8 = Button(root, text='8',  bg="gainsboro",
                 bd=3, padx=12, pady=5, font=("Helvetica", 14, "bold"))
button8.grid(row=4, column=1, sticky=W)
button9 = Button(root, text='9',bg="gainsboro",
                 bd=3, padx=12, pady=5, font=("Helvetica", 14, "bold"))
button9.grid(row=4, column=2, sticky=W)
button0 = Button(root, text='0', bg="gainsboro",
                 bd=3, padx=12, pady=5, font=("Helvetica", 14, "bold"))
button0.grid(row=5, column=0, sticky=W)
button_float = Button(root, text='.', bg="gainsboro",
                      bd=3, padx=15, pady=5, font=("Helvetica", 14, "bold"))
button_float.grid(row=5, column=1)

#   Math signs
button_plus = Button(root, text='+', bg="gray70",
                     bd=3, padx=11, pady=5, font=("Helvetica", 14, "bold"))
button_plus.grid(row=2, column=3, sticky=W)
button_minus = Button(root, text='-', bg="gray70",
                      bd=3, padx=11, pady=4, font=("Verdana", 14, "bold"))
button_minus.grid(row=3, column=3, sticky=W)
button_multiply = Button(root, text='*', bg="gray70",
                         bd=3, padx=13, pady=5, font=("Helvetica", 14, "bold"))
button_multiply.grid(row=4, column=3, )
button_division = Button(root, text='/',  bg="gray70",
                         bd=3, padx=14, pady=5, font=("Helvetica", 14, "bold"))
button_division.grid(row=5, column=3, )
button_equal = Button(root, text='=',  bg='orange',
                      bd=3, padx=12, pady=5, font=("Arial", 14))
button_equal.grid(row=5, column=2, )

button_percent = Button(root, text='%',  bg="gray70",
                         bd=3, padx=8, pady=5, font=("Helvetica", 14, "bold"))
button_percent.grid(row=1, column=3, )

button_clear = Button(root, text='C',  bg='gray70',
                      bd=3, padx=11, pady=5, font=("Helvetica", 14))
button_clear.grid(row=1, column=0)
button_sqrt = Button(root, text='√', bg="gray70",
                        bd=3, padx=12, pady=5, font=("Helvetica", 14, "bold"))
button_sqrt.grid(row=1, column=1, sticky=W)
button_x = Button(root, text='x^y', bg="gray70",
                  bd=3, padx=6, pady=5, font=("Helvetica", 14))
button_x.grid(row=1, column=2, sticky=W)

root.mainloop()