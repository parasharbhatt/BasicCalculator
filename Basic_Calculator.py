"""
This is utility program to perform Basic Calculation.

Date of Initial code :  written on 7-Nov-2020
Author               : Parashar Bhatt



"""
import os
from tkinter import *

impath = os.path.join(os.getcwd(),'HandDrawCalculator.ico')
print(impath)


root = Tk()  # main window
root.title("Basic Calculator")

#root.iconbitmap("HandDrawCalculator.ico")

#root.iconbitmap(impath)

"""

if "nt" == os.name:
    root.wm_iconbitmap(bitmap = "HandDrawCalculator.ico")
else:
    root.wm_iconbitmap(bitmap = "HandDrawCalculator.xbm" )
    
"""




global opcode
e = Entry(root, width=35, borderwidth=5)

e.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

def button_click(number):
    current=e.get()
    current= str(current)+str(number)
    e.delete(0, END)
    e.insert(0, current)

def button_dot():
    val= e.get()
    val = str(val)+"."
    e.delete(0, END)
    e.insert(0,val)


def button_square():
    global opcode
    opcode = "square"
    first_number= e.get()
    global f_num
    f_num = float(first_number)
    global s_num
    s_num=2
    global result
    result=calculate()
    e.delete(0,END)
    e.insert(0,result)

    

def button_power():
    global opcode
    opcode="power"
    first_number= e.get()
    global f_num
    f_num = float(first_number)
    e.delete(0, END)

def button_add():
    global opcode
    opcode="+"
    first_number= e.get()
    global f_num
    f_num = float(first_number)
    e.delete(0, END)

def button_subtract():
    global opcode
    opcode="-"
    first_number= e.get()
    global f_num
    f_num = float(first_number)
    e.delete(0, END)

def button_multiply():
    global opcode
    opcode="*"
    first_number= e.get()
    global f_num
    f_num = float(first_number)
    e.delete(0, END)

def button_divide():
    global opcode
    opcode="/"
    first_number= e.get()
    global f_num
    f_num = float(first_number)
    e.delete(0, END)

def button_equal():
    global opcode
    if opcode !="square":
        second_number= e.get()
    elif opcode == "square":
        second_number=2

    global s_num
    s_num = float(second_number)
    e.delete(0, END)
    global result
    result=calculate()
    e.insert(0, result)

    



def button_clear():
    e.delete(0, END)

def calculate():
    global opcode
    global f_num
    global s_num
    global result
    if opcode == "+":
        result = f_num + s_num
    elif opcode =="-":
        result = f_num - s_num
    elif opcode =="*":
        result = f_num * s_num
    elif opcode =="/":
        if s_num != 0:
            result = f_num / s_num
        else:
            result = "ERR!!"
    elif opcode == "square":
        result = pow(f_num,s_num)
    elif opcode == "power":
        result = pow(f_num,s_num)
    
    if( result - int(result)) == 0:
        result=int(result)
    return result


# define button

button_1 = Button(root, text="1", padx=40, pady=10 , command=lambda: button_click(1))
button_2 = Button(root, text="2", padx=40, pady=10 , command=lambda: button_click(2))
button_3 = Button(root, text="3", padx=40, pady=10 , command=lambda: button_click(3))
button_4 = Button(root, text="4", padx=40, pady=10 , command=lambda: button_click(4))
button_5 = Button(root, text="5", padx=40, pady=10 , command=lambda: button_click(5))
button_6 = Button(root, text="6", padx=40, pady=10 , command=lambda: button_click(6))
button_7 = Button(root, text="7", padx=40, pady=10 , command=lambda: button_click(7))
button_8 = Button(root, text="8", padx=40, pady=10 , command=lambda: button_click(8))
button_9 = Button(root, text="9", padx=40, pady=10 , command=lambda: button_click(9))
button_10 = Button(root, text="0", padx=40, pady=10 , command=lambda: button_click(0))
button_clear = Button(root, text="Clear", padx=81, pady=10 , command=button_clear)

button_add = Button(root, text="+", padx=39, pady=10 , command=button_add)
button_multiply = Button(root, text="*", padx=41, pady=10 , command=button_multiply)
button_subtract = Button(root, text="-", padx=39, pady=10 , command=button_subtract)
button_divide = Button(root, text="/", padx=41, pady=10 , command=button_divide)

button_equal = Button(root, text="=", padx=91, pady=10 , command=button_equal)


button_11 = Button(root, text=".", padx=40, pady=10 , command=button_dot)
button_12 = Button(root, text="x^2", padx=35, pady=10 , command=button_square)
button_13 = Button(root, text="x^y", padx=35, pady=10 , command=button_power)


# put button on screen

button_1.grid(row=3,column=0)
button_2.grid(row=3,column=1)
button_3.grid(row=3,column=2)
button_4.grid(row=2,column=0)
button_5.grid(row=2,column=1)
button_6.grid(row=2,column=2)
button_7.grid(row=1,column=0)
button_8.grid(row=1,column=1)
button_9.grid(row=1,column=2)
button_10.grid(row=4,column=0)
button_clear.grid(row=4,column=1, columnspan=2)
button_add.grid(row=5,column=0)
button_equal.grid(row=5,column=1,columnspan=2)
button_subtract.grid(row=6,column=0)
button_multiply.grid(row=6,column=1)
button_divide.grid(row=6,column=2)
button_11.grid(row=7,column=0)
button_12.grid(row=7,column=1)
button_13.grid(row=7,column=2)
#button_.grid(row=1,column=0)



# event looping

root.mainloop()

