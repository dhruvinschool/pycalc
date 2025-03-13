import math
import tkinter.messagebox # type: ignore
from tkinter import *

switch = False
win = Tk()
win.geometry("650x400+300+300")
#define resolution
win.title('pyCalc')

colour = '#f38ba8'

def angle(switch, colour):
    if switch == False:
        switch == True
        colour = '#f38ba8'
    else:
        switch == False
        colour = '#89b4fa'


def btn1():
    #This function adds a number to the textbox.
    if textbox.get() =='0':
        textbox.delete(0,END)
    #The above if function checks if the textbox contains only 0 , which is the base value. If so , it'll delete the 0 before inputting the number.
    position=len(textbox.get())
    textbox.insert(position,'1')
#The other functions regarding numbers are pretty much identical , they all have the same purpose. Hence , they are repeated with little modifications to account for the numbers they represent.
def btn2():
    if textbox.get() =='0':
        textbox.delete(0,END)
    position=len(textbox.get())
    textbox.insert(position,'2')

def btn3():
    if textbox.get() =='0':
        textbox.delete(0,END)
    position=len(textbox.get())
    textbox.insert(position,'3')

def btn4():
    if textbox.get() =='0':
        textbox.delete(0,END)
    position=len(textbox.get())
    textbox.insert(position,'4')

def btn5():
    if textbox.get() =='0':
        textbox.delete(0,END)
    position=len(textbox.get())
    textbox.insert(position,'5')

def btn6():
    if textbox.get() =='0':
        textbox.delete(0,END)
    position=len(textbox.get())
    textbox.insert(position,'6')

def btn7():
    if textbox.get() =='0':
        textbox.delete(0,END)
    position=len(textbox.get())
    textbox.insert(position,'7')

def btn8():
    if textbox.get() =='0':
        textbox.delete(0,END)
    position=len(textbox.get())
    textbox.insert(position,'8')

def btn9():
    if textbox.get() =='0':
        textbox.delete(0,END)
    position=len(textbox.get())
    textbox.insert(position,'9')

def btn0():
    if textbox.get() =='0':
        textbox.delete(0,END)
    position=len(textbox.get())
    textbox.insert(position,'0')

#You may have noticed that in the following operation functions , I have ommitted the if statement that deletes the base value of '0'. This is because for an operation , a base value is always needed , so when none is supplied it defaults to using 0.

def btnplus():
    position=len(textbox.get())
    textbox.insert(position,'+')

def btnsub():
    position=len(textbox.get())
    textbox.insert(position,'-')

def btnmult():
    position=len(textbox.get())
    textbox.insert(position,'*')

def btndiv():
    position=len(textbox.get())
    textbox.insert(position,'/')

#The following 6 functions are all trigonometric functions. You may be thinking 'Why is the try function used..?' This is because of the fact that in trigonometry , values after a certain point are undefined. For instance , arcsin(12) has no value , so we use this to test if an operation can actually be performed.

def sin():
    try:
        ans=float(textbox.get())
        if switch == True:
            ans=math.sin(math.radians(ans))
            textbox.delete(0,END)
            textbox.insert(0, str(ans))
        else:
            ans=math.sin(ans)
            textbox.delete(0,END)
            textbox.insert(0, str(ans))
    except Exception:
        tkinter.messagebox.showerror("Error , check operand and operation")

def cos():
    try:
        ans=float(textbox.get())
        if switch == True:
            ans=math.cos(math.radians(ans))
            textbox.delete(0,END)
            textbox.insert(0, str(ans))
        else:
            ans=math.cos(ans)
            textbox.delete(0,END)
            textbox.insert(0, str(ans))
    except Exception:
        tkinter.messagebox.showerror("Error , check operand and operation")

def tan():
    try:
        ans=float(textbox.get())
        if switch == True:
            ans=math.tan(math.radians(ans))
            textbox.delete(0,END)
            textbox.insert(0, str(ans))
        else:
            ans=math.tan(ans)
            textbox.delete(0,END)
            textbox.insert(0, str(ans))
    except Exception:
        tkinter.messagebox.showerror("Error , check operand and operation")

def asin():
    try:
        ans=float(textbox.get())
        if switch == True:
            ans=math.degrees(math.asin(ans))
            textbox.delete(0,END)
            textbox.insert(0, str(ans))
        else:
            ans=math.asin(ans)
            textbox.delete(0,END)
            textbox.insert(0, str(ans))
    except Exception:
        tkinter.messagebox.showerror("Error , check operand and operation")

def acos():
    try:
        ans=float(textbox.get())
        if switch == True:
            ans=math.degrees(math.acos(ans))
            textbox.delete(0,END)
            textbox.insert(0, str(ans))
        else:
            ans=math.acos(ans)
            textbox.delete(0,END)
            textbox.insert(0, str(ans))
    except Exception:
        tkinter.messagebox.showerror("Error , check operand and operation")

def atan():
    try:
        ans=float(textbox.get())
        if switch == True:
            ans=math.degrees(math.atan(ans))
            textbox.delete(0,END)
            textbox.insert(0, str(ans))
        else:
            ans=math.atan(ans)
            textbox.delete(0,END)
            textbox.insert(0, str(ans))
    except Exception:
        tkinter.messagebox.showerror("Error , check operand and operation")


textbox = Entry(win,font='Arial 20',fg="Black",bg="#cdd6f4",bd=4,justify=RIGHT)
textbox.insert(0, '0')
#This makes the default textbox value 0
textbox.pack(expand=TRUE, fill=BOTH)
#This makes a textbox , which will afterwards be the answer box.
row1=Frame(win,bg="#1e1e2e")
row1.pack(expand=TRUE, fill=BOTH)
onebtn=Button(row1,text="1",font="Arial 23",relief="groove", command=btn1, fg="white",bg='#1e1e2e').pack(side=LEFT, expand=TRUE, fill=BOTH)    
twobtn=Button(row1,text="2",font="Arial 23",relief="groove", command=btn2,fg="white",bg='#1e1e2e').pack(side=LEFT, expand=TRUE, fill=BOTH)
threebtn=Button(row1,text="3",font="Arial 23",relief="groove", command=btn3,fg="white",bg='#1e1e2e').pack(side=LEFT, expand=TRUE, fill=BOTH)
plusbtn=Button(row1,text="+",font="Arial 23",relief="groove", command=btnplus,fg="white",bg='#1e1e2e').pack(side=LEFT, expand=TRUE, fill=BOTH)
sinbtn=Button(row1,text="sin",font="Arial 18",relief="groove", command=sin,fg="white",bg='#1e1e2e').pack(side=LEFT, expand=TRUE, fill=BOTH)
cosbtn=Button(row1,text="cos",font="Arial 18",relief="groove", command=cos,fg="white",bg='#1e1e2e').pack(side=LEFT, expand=TRUE, fill=BOTH)
tanbtn=Button(row1,text="tan",font="Arial 18",relief="groove", command=tan,fg="white",bg='#1e1e2e').pack(side=LEFT, expand=TRUE, fill=BOTH)
openbtn=Button(row1,text="(",font="Arial 18",relief="groove",fg="white",bg='#1e1e2e').pack(side=LEFT, expand=TRUE, fill=BOTH)
closebtn=Button(row1,text=")",font="Arial 18",relief="groove",fg="white",bg='#1e1e2e').pack(side=LEFT, expand=TRUE, fill=BOTH)

row2=Frame(win,bg="#1e1e2e")
row2.pack(expand=TRUE, fill=BOTH)
fourbtn=Button(row2,text="4",font="Arial 22",relief="groove", command=btn4,fg="white",bg='#1e1e2e').pack(side=LEFT, expand=TRUE, fill=BOTH)    
fivebtn=Button(row2,text="5",font="Arial 22",relief="groove", command=btn5,fg="white",bg='#1e1e2e').pack(side=LEFT, expand=TRUE, fill=BOTH)
sixbtn=Button(row2,text="6",font="Arial 22",relief="groove", command=btn6,fg="white",bg='#1e1e2e').pack(side=LEFT, expand=TRUE, fill=BOTH)
minusbtn=Button(row2,text="-",font="Arial 22",relief="groove", command=btnsub,fg="white",bg='#1e1e2e').pack(side=LEFT, expand=TRUE, fill=BOTH)
arcsinbtn=Button(row2,text="sin-1",font="Arial 10 bold",relief="groove", command=asin,fg="white",bg='#1e1e2e').pack(side=LEFT, expand=TRUE, fill=BOTH)
arccosbtn=Button(row2,text="cos-1",font="Arial 10 bold",relief="groove", command=acos,fg="white",bg='#1e1e2e').pack(side=LEFT, expand=TRUE, fill=BOTH)
arctanbtn=Button(row2,text="tan-1",font="Arial 10 bold",relief="groove", command=atan,fg="white",bg='#1e1e2e').pack(side=LEFT, expand=TRUE, fill=BOTH)
pibtn=Button(row2,text="π",font="Arial 18",relief="groove",fg="white",bg='#1e1e2e').pack(side=LEFT, expand=TRUE, fill=BOTH)
factbtn=Button(row2,text="x!",font="Arial 18",relief="groove",fg="white",bg='#1e1e2e').pack(side=LEFT, expand=TRUE, fill=BOTH)

row3=Frame(win,bg="#1e1e2e")
row3.pack(expand=TRUE, fill=BOTH)
sevenbtn=Button(row3,text="7",font="Arial 23", command=btn7,relief="groove",fg="white",bg='#1e1e2e').pack(side=LEFT, expand=TRUE, fill=BOTH)    
eightbtn=Button(row3,text="8",font="Arial 23", command=btn8,relief="groove",fg="white",bg='#1e1e2e').pack(side=LEFT, expand=TRUE, fill=BOTH)
ninebtn=Button(row3,text="9",font="Arial 23", command=btn9,relief="groove",fg="white",bg='#1e1e2e').pack(side=LEFT, expand=TRUE, fill=BOTH)
multiplybtn=Button(row3,text="*",font="Arial 23",relief="groove", command=btnmult,fg="white",bg='#1e1e2e').pack(side=LEFT, expand=TRUE, fill=BOTH)
sqrbtn=Button(row3,text="x^2",font="Arial 17",relief="groove",fg="white",bg='#1e1e2e').pack(side=LEFT, expand=TRUE, fill=BOTH)
logbtn=Button(row3,text="log",font="Arial 17",relief="groove",fg="white",bg='#1e1e2e').pack(side=LEFT, expand=TRUE, fill=BOTH)
lnbtn=Button(row3,text="ln",font="Arial 17",relief="groove",fg="white",bg='#1e1e2e').pack(side=LEFT, expand=TRUE, fill=BOTH)
sqrrootbtn=Button(row3,text="√x",font="Arial 17",relief="groove",fg="white",bg='#1e1e2e').pack(side=LEFT, expand=TRUE, fill=BOTH)
sqrbtn=Button(row3,text="x^y",font="Arial 17",relief="groove",fg="white",bg='#1e1e2e').pack(side=LEFT, expand=TRUE, fill=BOTH)

row4=Frame(win,bg="#1e1e2e")
row4.pack(expand=TRUE, fill=BOTH)
backbtn=Button(row4,text="⌫",font="Arial 15",relief="groove",fg="white",bg='#1e1e2e').pack(side=LEFT, expand=TRUE, fill=BOTH)    
zerobtn=Button(row4,text="0",font="Arial 23",relief="groove", command=btn0,fg="white",bg='#1e1e2e').pack(side=LEFT, expand=TRUE, fill=BOTH)
equalsbtn=Button(row4,text="=",font="Arial 11 bold",relief="groove",fg="white",bg='#89b4fa').pack(side=LEFT, expand=TRUE, fill=BOTH)
dividebtn=Button(row4,text="/",font="Arial 23",relief="groove", command=btndiv,fg="white",bg='#1e1e2e').pack(side=LEFT, expand=TRUE, fill=BOTH)
clearbtn=Button(row4,text="AC",font="Arial 20",relief="groove",fg="white",bg='#1e1e2e').pack(side=LEFT, expand=TRUE, fill=BOTH)    
decimalbtn=Button(row4,text=".",font="Arial 20",relief="groove",fg="white",bg='#1e1e2e').pack(side=LEFT, expand=TRUE, fill=BOTH)    
placeholder1btn=Button(row4,text="n/a",font="Arial 20",relief="groove",fg="white",bg='#1e1e2e').pack(side=LEFT, expand=TRUE, fill=BOTH)
switcheroooo=Button(row4,text="Angle",font="Arial 20", command=angle, relief="groove",fg="white",bg=colour).pack(side=LEFT, expand=TRUE, fill=BOTH)

win.mainloop()
