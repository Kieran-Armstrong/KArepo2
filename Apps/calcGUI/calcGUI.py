
#import everything from Tkinter
from sqlite3 import Row
from tkinter import *

#globally declare expression variable
expression = ""

#function to update expression in text entry box 
def press(num):
    #point out global expression variable
    global expression 

    #concatenation of string
    expression = expression + str(num)

    #updqte expression using set method
    equation.set(expression)

#function to evaluate final expression
def equalPress():
    #Try and except statements used for handling errors e.g. zero, division errors

    try:
        global expression

        #evaluate expression and convert result into str
        total = str(eval(expression))

        equation.set(total)

        #initialize expression var by empty string
        expression = ""

    #if error is generated then handle
    except:
        equation.set(" error ")
        expression = ""

#function to clear contents
def clear():
    global expression
    expression = ""
    equation.set("")

#Driver code
if __name__ == "__main__":
    #create GUI window
    calcgui = Tk()

    #set background colour
    calcgui.configure(background="white")

    #set title of window
    calcgui.title("Simple Calculator")

    #set dimensions of window
    calcgui.geometry("270x150")

    #stringVar() is variable class
    equation = StringVar()

    #create text entry box 
    expression_field = Entry(calcgui, textvariable=equation)

    expression_field.grid(columnspan=4, ipadx=70)

    #create and place buttons to determine command or function
    btn1 = Button(calcgui, text=" 1 ", fg="white", bg="gray", command=lambda: press(1), height=1, width=7)
    btn1.grid(row=2, column=0)

    btn2 = Button(calcgui, text=" 2 ", fg="white", bg="gray", command=lambda: press(2), height=1, width=7)
    btn2.grid(row=2, column=1)

    btn3 = Button(calcgui, text=" 3 ", fg="white", bg="gray", command=lambda: press(3), height=1, width=7)
    btn3.grid(row=2, column=2)

    btn4 = Button(calcgui, text=" 4 ", fg="white", bg="gray", command=lambda: press(4), height=1, width=7)
    btn4.grid(row=3, column=0)

    btn5 = Button(calcgui, text=" 5 ", fg="white", bg="gray", command=lambda: press(5), height=1, width=7)
    btn5.grid(row=3, column=1)

    btn6 = Button(calcgui, text=" 6 ", fg="white", bg="gray", command=lambda: press(6), height=1, width=7)
    btn6.grid(row=3, column=2)
    
    btn7 = Button(calcgui, text=" 7 ", fg="white", bg="gray", command=lambda: press(7), height=1, width=7)
    btn7.grid(row=4, column=0)

    btn8 = Button(calcgui, text=" 8 ", fg="white", bg="gray", command=lambda: press(8), height=1, width=7)
    btn8.grid(row=4, column=1)

    btn9 = Button(calcgui, text=" 9 ", fg="white", bg="gray", command=lambda: press(9), height=1, width=7)  
    btn9.grid(row=4, column=2)

    btn0 = Button(calcgui, text=" 0 ", fg="white", bg="gray", command=lambda: press(0), height=1, width=7)
    btn0.grid(row=5, column=0)

    plus = Button(calcgui, text = " + ", fg="white", bg="gray", command=lambda: press("+"), height=1, width=7)
    plus.grid(row=2, column=3)

    minus = Button(calcgui, text = " - ", fg="white", bg="gray", command=lambda: press("-"), height=1, width=7)
    minus.grid(row=3, column=3)

    multiply = Button(calcgui, text = " X ", fg="white", bg="gray", command=lambda: press("*"), height=1, width=7)
    multiply.grid(row=4, column=3)

    divide = Button(calcgui, text = " / ", fg="white", bg="gray", command=lambda: press("/"), height=1, width=7)
    divide.grid(row=5, column=3)

    equals = Button(calcgui, text = " = ", fg="white", bg="gray", command=equalPress, height=1, width=7)
    equals.grid(row=5, column=2)

    clrBtn = Button(calcgui, text="Clear", fg="white", bg="gray", command=clear, height=1, width=7)
    clrBtn.grid(row=5, column=1)

    decBtn = Button(calcgui, text=" . ", fg="white", bg="gray", command=lambda: press("."), height=1, width=7)
    decBtn.grid(row=6, column=0)

    #start gui
    calcgui.mainloop()


    







