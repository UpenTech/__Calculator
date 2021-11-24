#GUI Calculator Program
from tkinter import *

state_plu = ["O"]               #                 State Representation to check if operand button is pressed or not
state_sub = ["O"]               #              "X" representing pressed state while "O" representing not-pressed state
state_mul = ["O"]
state_div = ["O"]

top = Tk()                                                                             #Window Creation

top.title("Basic Calculator")
top.geometry("380x250")

bar = Entry(top, width=59, borderwidth=3)                                              #Calcuator's Working Screen (Input)
bar.grid(row=0, column=0, columnspan=4, padx=10, pady=5)

bar2 = Entry(top, width=12, borderwidth=3)                                             #Calcualor's Working Screen (Output)
bar2.grid(row=5, column=0)

pre_list = []
post_list = []


def button_clicked(number:int) -> None:
    """
    :Description: Updates the Working Screen with the digits pressed
    :type number: int
    """
    status = bar.get()
    bar.delete(0,END)
    store = status + str(number)
    bar.insert(0, store)


def button_ac() -> None:
    """Clears the screen and cache
    """
    bar.delete(0,END)
    pre_list.clear()


def button_add() -> None:
    """Add operand
    """
    if pre_list == []:
        pre_list.append(float(bar.get()))
    else:
        button_eq()
    state_plu[0] = "X"
    bar.delete(0,END)


def button_sub() -> None:

    if pre_list == []:
        pre_list.append(float(bar.get()))
    else:
        button_eq()
    state_sub[0] = "X"
    bar.delete(0,END)


def button_mul() -> None:
    
    if pre_list == []:
        pre_list.append(float(bar.get()))
    else:
        button_eq()
    state_mul[0] = "X"
    bar.delete(0,END)


def button_div() -> None:
    
    if pre_list == []:
        pre_list.append(float(bar.get()))
    else:
        button_eq()
    state_div[0] = "X"
    bar.delete(0,END)


def button_eq() -> None:

    bar2.delete(0,END)
    post_list.append(float(bar.get()))

    if state_plu[0] == "X":
        state_plu[0] = "O"
        pre_list[0] = pre_list[0] + post_list[0]
    elif state_sub[0] == "X":
        state_sub[0] = "O"
        pre_list[0] = pre_list[0] - post_list[0]
    elif state_mul[0] == "X":
        state_mul[0] = "O"
        pre_list[0] = pre_list[0] * post_list[0]
    elif state_div[0] == "X":
        state_div[0] = "O"
        pre_list[0] = pre_list[0] / post_list[0]
    post_list.clear()
    bar2.insert(0,pre_list[0])

def button_clear() -> None:
    bar.delete(len(bar.get()) - 1, END)


button1 = Button(top, text="1",width=12, height=2, fg="White", bg="#999944", command= lambda: button_clicked(1))
button1.grid(row=1, column=0)

button2 = Button(top, text="2",width=12, height=2, fg="White", bg="#999944", command= lambda: button_clicked(2))
button2.grid(row=1, column=1)

button3 = Button(top, text="3", width=12, height=2, fg="White", bg="#999944", command= lambda: button_clicked(3))
button3.grid(row=1, column=2)

buttonc = Button(top, text="AC", width=12, height=2, fg="White", bg="Crimson", command= button_ac)
buttonc.grid(row=1, column=3)



button4 = Button(top, text="4",width=12, height=2, fg="White", bg="#999944", command= lambda: button_clicked(4))
button4.grid(row=2, column=0)

button5 = Button(top, text="5",width=12, height=2, fg="White", bg="#999944", command= lambda: button_clicked(5))
button5.grid(row=2, column=1)

button6 = Button(top, text="6", width=12, height=2, fg="White", bg="#999944", command= lambda: button_clicked(6))
button6.grid(row=2, column=2)

buttonp = Button(top, text="+", width=12, height=2, fg="White", bg="#8899BB", command= button_add)
buttonp.grid(row=2, column=3)



button7 = Button(top, text="7",width=12, height=2, fg="White", bg="#999944", command= lambda: button_clicked(7))
button7.grid(row=3, column=0)

button8 = Button(top, text="8",width=12, height=2, fg="White", bg="#999944", command= lambda: button_clicked(8))
button8.grid(row=3, column=1)

button9 = Button(top, text="9", width=12, height=2, fg="White", bg="#999944", command= lambda: button_clicked(9))
button9.grid(row=3, column=2)

buttonm = Button(top, text="-", width=12, height=2, fg="White", bg="#8899BB", command= button_sub)
buttonm.grid(row=3, column=3)



buttonde = Button(top, text=".", width=12, height=2, fg="White", bg="#8899BB", command= lambda: button_clicked("."))
buttonde.grid(row=4, column=0)

button0 = Button(top, text="0", width=12, height=2, fg="White", bg="#999944", command= lambda: button_clicked(0))
button0.grid(row=4, column=1)

buttonmu = Button(top, text="x", width=12, height=2, fg="White", bg="#8899BB", command= button_mul)
buttonmu.grid(row=4, column=2)

buttond = Button(top, text="/", width=12, height=2, fg="White", bg="#8899BB", command= button_div)
buttond.grid(row=4, column=3)

buttoneq = Button(top, text="=", width = 12, height=2, fg="White", bg="#8899BB", command= button_eq)
buttoneq.grid(row=5, column=3)

buttonbk = Button(top, text="<Clear", width = 12, height=2, fg="White", bg="#8899BB", command= button_clear)
buttonbk.grid(row=5, column=2)

top.mainloop()
