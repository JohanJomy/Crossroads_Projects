from tkinter import *
import math

calc = Tk()
calc.geometry("300x480+450+100")
calc.resizable(0, 0)
calc.title("Calculator")

def show(a):
    # print(a)
    if isinstance(a, str):
        en.insert(END, a)
    else:
        en.insert(END, a.widget["text"])

def clear(a):
    if a == "b":
        temp = en.get()
        en.delete(0, END)
        en.insert(END, temp[0:-1])
    else:
        en.delete(0, END)

def operate():
    value = en.get()
    en.delete(0, END)
    en.insert(END, eval(str(value)))
    # lab.configure(text = eval(str(value)))

def hoverin(a):
    # print("kitti")
    numbtns[int(a.widget["text"])-1].configure(background="#a8dadc")
def hoverout(a):
    # print("poyi")
    numbtns[int(a.widget["text"])-1].configure(background="#f1faee")

enframe = Frame(calc, width=300, height=300)
enframe.pack(expand=True, fill="both", ipady=12)

en = Entry(enframe, font=("Helvetica", 25,'bold'), background="#264653", fg="#fff",justify=RIGHT)
en.pack(expand=True, fill="both", ipady=12)

btnframe = [Frame(calc) for i in range(6)]
for i in btnframe:
    i.pack(expand=True, fill="both")

numbtns = [Button(btnframe[4 - math.ceil(i / 3)], text=str(i), font=("Verdana", 22),
                  relief=GROOVE, border=0,background="#f1faee", fg="#000") for i in range(1, 10)]
for i in numbtns:
    i.pack(side=LEFT, expand=True, fill="both")
    i.bind('<Button-1>', show)
    i.bind('<Enter>', hoverin)
    i.bind('<Leave>', hoverout)

btn_clear = Button(btnframe[0], text="C", command=lambda : clear("c"), font=("Verdana", 22,'bold'), relief=GROOVE, border=0,background="#e63946", fg="#fff")
btn_clear.pack(side=LEFT, expand=True, fill="both",ipadx=3)
btn_back = Button(btnframe[0], text="\u2b05", command=lambda : clear("b"), font=("Verdana", 22,'bold'), relief=GROOVE, border=0,background="#f48c06", fg="#fff")
btn_back.pack(side=LEFT, expand=True, fill="both")
btn_sqr = Button(btnframe[0], text="x\u00b2", command=lambda: show("**2"), font=("Verdana", 22,'bold'), relief=GROOVE, border=0,background="#2a9d8f", fg="#fff")
btn_sqr.pack(side=LEFT, expand=True, fill="both",ipadx=2)
btn_div = Button(btnframe[0], text="/", command=lambda: show("/"), font=("Verdana", 22,'bold'), relief=GROOVE, border=0,background="#2a9d8f", fg="#fff")
btn_div.pack(side=LEFT, expand=True, fill="both",ipadx=3)
btn_multi = Button(btnframe[1], text="x", command=lambda: show("*"), font=("Verdana", 22,'bold'), relief=GROOVE, border=0,background="#2a9d8f", fg="#fff")
btn_multi.pack(side=LEFT, expand=True, fill="both",ipadx=3)
btn_minus = Button(btnframe[2], text="-", command=lambda: show("-"), font=("Verdana", 25,'bold'), relief=GROOVE, border=0,background="#2a9d8f", fg="#fff")
btn_minus.pack(side=LEFT, expand=True, fill="both",ipadx=2)
btn_plus = Button(btnframe[3], text="+", command=lambda: show("+"), font=("Verdana", 22,'bold'), relief=GROOVE, border=0,background="#2a9d8f", fg="#fff")
btn_plus.pack(side=LEFT, expand=True, fill="both")
# btn_dzero = Button(btnframe[4], text="00", command=lambda: show("00"), font=("Verdana", 22), relief=GROOVE, border=0,background="#f1faee", fg="#000")
# btn_dzero.pack(side=LEFT, expand=True, fill="both")
btn_zero = Button(btnframe[4], text="0", command=lambda: show("0"), font=("Verdana", 22), relief=GROOVE, border=0,background="#f1faee", fg="#000")
btn_zero.pack(side=LEFT, expand=True, fill="both")
btn_dot = Button(btnframe[4], text=".", command=lambda: show("."), font=("Verdana", 22), relief=GROOVE, border=0,background="#f1faee", fg="#000")
btn_dot.pack(side=LEFT, expand=True, fill="both",ipadx=2)
btn_equal = Button(btnframe[4], text="=", command=operate, font=("Verdana", 22,'bold'), relief=GROOVE, border=0,background="#aacc00", fg="#fff")
btn_equal.pack(side=LEFT, expand=True, fill="both",ipadx=36)

lab1 = Label(btnframe[5],text=("  Have A Nice Day"),background="#f1faee", fg="#505050",font=("Helvetica", 12,'bold'),anchor=W)
lab1.pack(side=LEFT, expand=True, fill="both")
lab2 = Label(btnframe[5],text=('\u00A9 Jijo'),background="#f1faee", fg="#505050",font=("Helvetica", 12,'bold'),anchor=CENTER)
lab2.pack(side=LEFT, expand=True, fill="both")
calc.mainloop()