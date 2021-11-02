from tkinter import *
import matplotlib.pyplot as plt
import numpy as np


window = Tk()
window.title("Calculator")
window.geometry("200x372")
window.minsize(200, 372)
window.maxsize(200, 372)


operator = ""
text_input = StringVar()
textDisplay = Entry(window, textvariable=text_input, insertwidth=4, justify='right').grid(columnspan=4)


def btn(nombre):
    global operator
    operator = operator + str(nombre)
    text_input.set(operator)


def result():
    global operator
    res = str(eval(operator))
    text_input.set(res)


def clear():
    global operator
    operator = ""
    text_input.set(operator)


def x2():
    x = np.linspace(-100, 100, 100)
    y = x**2
    plt.plot(x, y, "pink")
    plt.title("f(x^2)")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.show()


def Vx():
    x = np.linspace(1, 10, 100)
    y = np.sqrt(x)
    plt.plot(x, y, "pink")
    plt.title("f(Vx)")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.show()


def LNx():
    x = np.linspace(0, 10, 100)
    y = np.log(x)
    plt.plot(x, y, "pink")
    plt.title("f(ln(x))")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.show()


def Ex():
    x = np.linspace(1, 10, 100)
    y = np.exp(x)
    plt.plot(x, y, "pink")
    plt.title("f(e^x)")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.show()


button_0 = Button(window, height=2, width=2, text="0", font=("Times", 16), command=lambda: btn(0)).grid(row=4, column=1)
button_1 = Button(window, height=2, width=2, text="1", font=("Times", 16), command=lambda: btn(1)).grid(row=1, column=0)
button_2 = Button(window, height=2, width=2, text="2", font=("Times", 16), command=lambda: btn(2)).grid(row=1, column=1)
button_3 = Button(window, height=2, width=2, text="3", font=("Times", 16), command=lambda: btn(3)).grid(row=1, column=2)
button_4 = Button(window, height=2, width=2, text="4", font=("Times", 16), command=lambda: btn(4)).grid(row=2, column=0)
button_5 = Button(window, height=2, width=2, text="5", font=("Times", 16), command=lambda: btn(5)).grid(row=2, column=1)
button_6 = Button(window, height=2, width=2, text="6", font=("Times", 16), command=lambda: btn(6)).grid(row=2, column=2)
button_7 = Button(window, height=2, width=2, text="7", font=("Times", 16), command=lambda: btn(7)).grid(row=3, column=0)
button_8 = Button(window, height=2, width=2, text="8", font=("Times", 16), command=lambda: btn(8)).grid(row=3, column=1)
button_9 = Button(window, height=2, width=2, text="9", font=("Times", 16), command=lambda: btn(9)).grid(row=3, column=2)
button_com = Button(window, height=2, width=2, text=",", font=("Times", 16), command=lambda: btn(".")).grid(row=4, column=2)
button_add = Button(window, height=2, width=2, text="+", font=("Times", 16), command=lambda: btn("+")).grid(row=1, column=3)
button_les = Button(window, height=2, width=2, text="-", font=("Times", 16), command=lambda: btn("-")).grid(row=2, column=3)
button_mul = Button(window, height=2, width=2, text="x", font=("Times", 16), command=lambda: btn("*")).grid(row=3, column=3)
button_div = Button(window, height=2, width=2, text="%", font=("Times", 16), command=lambda: btn("/")).grid(row=4, column=3)
button_res = Button(window, height=2, width=2, text="=", font=("Times", 16), command=result).grid(row=5, column=3)
button_clr = Button(window, height=2, width=2, text="C", font=("Times", 16), command=clear).grid(row=4, column=0)
button_x2 = Button(window, height=2, width=2, text="x2", font=("Times", 16), command=x2).grid(row=5, column=0)
button_Vx = Button(window, height=2, width=2, text="Vx", font=("Times", 16), command=Vx).grid(row=5, column=1)
button_LNx = Button(window, height=2, width=2, text="ln", font=("Times", 16), command=LNx).grid(row=6, column=0)
button_Ex = Button(window, height=2, width=2, text="eX", font=("Times", 16), command=Ex).grid(row=6, column=1)


window.mainloop()