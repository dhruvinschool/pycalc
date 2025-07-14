import math
import tkinter.messagebox # type: ignore
from tkinter import *

switch = False
#this will be used in order to switch radians and degrees mode
win = Tk()
#this makes a window
win.geometry("650x400+300+300")
#define resolution
win.title('pyCalc')
#define window title

def btn1():
    #This function adds a number to the textbox.
    if textbox.get() =='0':
        textbox.delete(0,END)
    #The above if function checks if the textbox contains only 0 , which is the base value. If so , it'll delete the 0 before inputting the number.
    position=len(textbox.get())
    textbox.insert(position,'1')
#The other functions regarding numbers are pretty much identical , they all have the same purpose. Hence , they are repeated with little modifications to account for the numbers they represent.
def btn2():
    #This function adds a number to the textbox.
    if textbox.get() =='0':
        textbox.delete(0,END)
    #The above if function checks if the textbox contains only 0 , which is the base value. If so , it'll delete the 0 before inputting the number.
    position=len(textbox.get())
    textbox.insert(position,'2')

def btn3():
    #This function adds a number to the textbox.
    if textbox.get() =='0':
        textbox.delete(0,END)
    #The above if function checks if the textbox contains only 0 , which is the base value. If so , it'll delete the 0 before inputting the number.
    position=len(textbox.get())
    textbox.insert(position,'3')

def btn4():
    #This function adds a number to the textbox.
    if textbox.get() =='0':
        textbox.delete(0,END)
    #The above if function checks if the textbox contains only 0 , which is the base value. If so , it'll delete the 0 before inputting the number.
    position=len(textbox.get())
    textbox.insert(position,'4')

def btn5():
    #This function adds a number to the textbox.
    if textbox.get() =='0':
        textbox.delete(0,END)
    #The above if function checks if the textbox contains only 0 , which is the base value. If so , it'll delete the 0 before inputting the number.
    position=len(textbox.get())
    textbox.insert(position,'5')

def btn6():
    #This function adds a number to the textbox.
    if textbox.get() =='0':
        textbox.delete(0,END)
    #The above if function checks if the textbox contains only 0 , which is the base value. If so , it'll delete the 0 before inputting the number.
    position=len(textbox.get())
    textbox.insert(position,'6')

def btn7():
    #This function adds a number to the textbox.
    if textbox.get() =='0':
        textbox.delete(0,END)
    #The above if function checks if the textbox contains only 0 , which is the base value. If so , it'll delete the 0 before inputting the number.
    position=len(textbox.get())
    textbox.insert(position,'7')

def btn8():
    #This function adds a number to the textbox.
    if textbox.get() =='0':
        textbox.delete(0,END)
    #The above if function checks if the textbox contains only 0 , which is the base value. If so , it'll delete the 0 before inputting the number.
    position=len(textbox.get())
    textbox.insert(position,'8')

def btn9():
    #This function adds a number to the textbox.
    if textbox.get() =='0':
        textbox.delete(0,END)
    #The above if function checks if the textbox contains only 0 , which is the base value. If so , it'll delete the 0 before inputting the number.
    position=len(textbox.get())
    textbox.insert(position,'9')

def btn0():
    #This function adds a number to the textbox.
    if textbox.get() =='0':
        textbox.delete(0,END)
    #The above if function checks if the textbox contains only 0 , which is the base value. If so , it'll delete the 0 before inputting the number.
    position=len(textbox.get())
    textbox.insert(position,'0')

#You may have noticed that in the following operation functions , I have ommitted the if statement that deletes the base value of '0'. This is because for an operation , a base value is always needed , so when none is supplied it defaults to using 0.

def btnplus():
    position=len(textbox.get())
    #This finds the length of the textbox
    textbox.insert(position,'+')
    #This uses the length as a position to start with , so after the end of the textbox it will add the operator

def btnsub():
    if textbox.get() == '0':
        textbox.delete(0,END)
    #Clears textbox for negative numbers
    position=len(textbox.get())
    #This finds the length of the textbox
    textbox.insert(position,'-')
    #This uses the length as a position to start with , so after the end of the textbox it will add the operator

def btnmult():
    position=len(textbox.get())
    #This finds the length of the textbox
    textbox.insert(position,'*')
    #This uses the length as a position to start with , so after the end of the textbox it will add the operator

def btndiv():
    position=len(textbox.get())
    #This finds the length of the textbox
    textbox.insert(position,'/')
    #This uses the length as a position to start with , so after the end of the textbox it will add the operator

#The following 6 functions are all trigonometric functions. You may be thinking 'Why is the try function used..?' This is because of the fact that in trigonometry , values after a certain point are undefined. For instance , arcsin(12) has no value , so we use this to test if an operation can actually be performed.

def sin():
    try:
        ans=float(textbox.get())
        if switch == True:
            #Switch is what we used at the start to define degree or radians mode , if true its turned from degrees to radians. Unfortunately , due to conversion between degres and radians , some accuracy errors are capable of occuring , however the magnitude of these inconsistincies is relatively minimal , so it should not affect the performand by a large scale. But it is still noteworthy.
            ans=math.sin(math.radians(ans))
            #See? We use math.radians(ans) first to actually convert to radians , as the math library's sine function only inputs radians.
            textbox.delete(0,END)
            textbox.insert(0, str(ans))
        else:
            ans=math.sin(ans)
            textbox.delete(0,END)
            textbox.insert(0, str(ans))
    #As stated earlier , try is used here so that the computer can verify that the value supplied has an an actual value on the sine graph.
    except Exception:
        tkinter.messagebox.showerror("Error , check operand and operation")
    #An error is hence printed in the exception , so that the user is made aware that the input/operation is invalid.

def cos():
    try:
        ans=float(textbox.get())
        if switch == True:
            #Switch is what we used at the start to define degree or radians mode , if true its turned from degrees to radians. Unfortunately , due to conversion between degres and radians , some accuracy errors are capable of occuring , however the magnitude of these inconsistincies is relatively minimal , so it should not affect the performand by a large scale. But it is still noteworthy.
            ans=math.cos(math.radians(ans))
            #See? We use math.radians(ans) first to actually convert to radians , as the math library's sine function only inputs radians.
            textbox.delete(0,END)
            textbox.insert(0, str(ans))
        else:
            ans=math.cos(ans)
            textbox.delete(0,END)
            textbox.insert(0, str(ans))
    #As stated earlier , try is used here so that the computer can verify that the value supplied has an an actual value on the sine graph.
    except Exception:
        tkinter.messagebox.showerror("Error , check operand and operation")
    #An error is hence printed in the exception , so that the user is made aware that the input/operation is invalid.

def tan():
    try:
        ans=float(textbox.get())
        if switch == True:
            #Switch is what we used at the start to define degree or radians mode , if true its turned from degrees to radians. Unfortunately , due to conversion between degres and radians , some accuracy errors are capable of occuring , however the magnitude of these inconsistincies is relatively minimal , so it should not affect the performand by a large scale. But it is still noteworthy.
            ans=math.tan(math.radians(ans))
            #See? We use math.radians(ans) first to actually convert to radians , as the math library's sine function only inputs radians.
            textbox.delete(0,END)
            textbox.insert(0, str(ans))
        else:
            ans=math.tan(ans)
            textbox.delete(0,END)
            textbox.insert(0, str(ans))
    #As stated earlier , try is used here so that the computer can verify that the value supplied has an an actual value on the sine graph.
    except Exception:
        tkinter.messagebox.showerror("Error , check operand and operation")
    #An error is hence printed in the exception , so that the user is made aware that the input/operation is invalid.

def asin():
    try:
        ans=float(textbox.get())
        if switch == True:
            #Switch is what we used at the start to define degree or radians mode , if true its turned from degrees to radians. Unfortunately , due to conversion between degres and radians , some accuracy errors are capable of occuring , however the magnitude of these inconsistincies is relatively minimal , so it should not affect the performand by a large scale. But it is still noteworthy.
            ans=math.asin(ans)
            #In the case of arc trig functions , we must first find the inverse of the value , which doesnt need to be converted as its not an angle. After this , we convert the given answer from radians into degrees.
            ans=math.degrees(ans)
            textbox.delete(0,END)
            textbox.insert(0, str(ans))
        else:
            ans=math.asin(ans)
            textbox.delete(0,END)
            textbox.insert(0, str(ans))
    except Exception:
        tkinter.messagebox.showerror("Error , check operand and operation")
#An error is hence printed in the exception , so that the user is made aware that the input/operation is invalid.
#As stated earlier , try is used here so that the computer can verify that the value supplied has an an actual value on the sine graph.


def acos():
    try:
        ans=float(textbox.get())
        if switch == True:
            #Switch is what we used at the start to define degree or radians mode , if true its turned from degrees to radians. Unfortunately , due to conversion between degres and radians , some accuracy errors are capable of occuring , however the magnitude of these inconsistincies is relatively minimal , so it should not affect the performand by a large scale. But it is still noteworthy.
            ans=math.acos(ans)
            #In the case of arc trig functions , we must first find the inverse of the value , which doesnt need to be converted as its not an angle. After this , we convert the given answer from radians into degrees.
            ans=math.degrees(ans)
            textbox.delete(0,END)
            textbox.insert(0, str(ans))
        else:
            ans=math.acos(ans)
            textbox.delete(0,END)
            textbox.insert(0, str(ans))
    #As stated earlier , try is used here so that the computer can verify that the value supplied has an an actual value on the sine graph.
    except Exception:
        tkinter.messagebox.showerror("Error , check operand and operation")
    #An error is hence printed in the exception , so that the user is made aware that the input/operation is invalid.

def atan():
    try:
        ans=float(textbox.get())
        if switch == True:
            #Switch is what we used at the start to define degree or radians mode , if true its turned from degrees to radians. Unfortunately , due to conversion between degres and radians , some accuracy errors are capable of occuring , however the magnitude of these inconsistincies is relatively minimal , so it should not affect the performand by a large scale. But it is still noteworthy.
            ans=math.atan(ans)
            #In the case of arc trig functions , we must first find the inverse of the value , which doesnt need to be converted as its not an angle. After this , we convert the given answer from radians into degrees.
            ans=math.degrees(ans)
            textbox.delete(0,END)
            textbox.insert(0, str(ans))
        else:
            ans=math.atan(ans)
            textbox.delete(0,END)
            textbox.insert(0, str(ans))
    #As stated earlier , try is used here so that the computer can verify that the value supplied has an an actual value on the sine graph.
    except Exception:
        tkinter.messagebox.showerror("Error , check operand and operation")
    #An error is hence printed in the exception , so that the user is made aware that the input/operation is invalid.

def pi():
    #This function adds a number to the textbox.
    if textbox.get() =='0':
        textbox.delete(0,END)
    #The above if function checks if the textbox contains only 0 , which is the base value. If so , it'll delete the 0 before inputting the number.
    position=len(textbox.get())
    pistr = 'π'
    #Here a string called pistr is made to hold pi , so that it can be put in the textbox (next line) , more on the first line outside of this function.
    textbox.insert(position,str(pistr))

π = math.pi
#Here the pi symbol is used as a variable to hold the actual pi value. Hence , when used in eval function , it is interpreted as a variable and the pi value is used for calculation , whilst pi symbol is on the textbox.

def ac():
    textbox.delete(0,END)
    #Before inserting the 0 , we must clear the entire textbox
    textbox.insert(0, '0')
    #Now we insert 0 from the starting point of the box.

def equals():
    ans=(eval(textbox.get()))
    #The eval function takes the entire textbox as a string and evaluates it if its in mathematical terms
    textbox.delete(0, END)
    #The textbox is deleted
    textbox.insert(0, str(ans))
    #The answer to the evaluation is inputted into the start of the textbox

def open_parentheses():
    if textbox.get() == '0':
        textbox.delete(0,END)
    #This if statement checks for if the textbox is equal to zero , if it is it wipes it to add a parentheses.
    position=len(textbox.get())
    textbox.insert(position,'(')
    #A parentheses is added into the textbox.

def closing_parentheses():
    if textbox.get() == '0':
        textbox.delete(0,END)
    #This if statement checks for if the textbox is equal to zero , if it is it wipes it to add a parentheses.
    position=len(textbox.get())
    textbox.insert(position,')')
    #A parentheses is added into the textbox.


def delete():
    if textbox.get() == '0':
        textbox.delete(0,END)
        textbox.insert(0,'0')
    #In this if statement , we are checking to see if the textbox is equal to 0. If it is , we do NOT delete the 0 and we keep it as it is , as we do not want an empty textbox.
    else:
        position=len(textbox.get())
        textbox.delete(position-1,position)
    #In this else statement , since the textbox isnt equal to zero , the last digit on the textbox is deleted to shorted the textbox.
def decimal():
    position = len(textbox.get())
    textbox.insert(position,'.')
    #Here , a decimal is simply added to the end of the textbox.

def sqr():
    position=len(textbox.get())
    textbox.insert(position,'**2')
    #Adds **2 to the end of the textbox. The evaluate function interprets this as ^2.

def power():
    position=len(textbox.get())
    textbox.insert(position, '**')
    ##Adds ** to the end of the textbox. The evaluate function interprets this as ^ , so the next number is the exponent.

def fact():
    try:
        ans=textbox.get()
        ans = math.factorial(int(ans))
        textbox.delete(0,END)
        textbox.insert(0,str(ans))
    #This essentially finds the factorial of the textbox , with the entire textbox being interpreted as a single integer. This is then outputted into the box.
    except Exception:
        tkinter.messagebox.showerror("Error , check operand and operation")
    #If the textbox is not in integer form , or is a negative number , this error is reported.




textbox = Entry(win,font='Arial 20',fg="Black",bg="#cdd6f4",bd=4,justify=RIGHT)
#This is where the textbox itself is created , I used Arial font and black foreground for black text. The background colour has been chosen from a colorscheme online (Catppuccin mocha)
textbox.insert(0, '0')
#This makes the default textbox value 0
textbox.pack(expand=TRUE, fill=BOTH)
#This makes a textbox , which will afterwards be the answer box.

#All the following blocks of code are in the same format. The first line makes a row , which is just a frame in the window. The row is made expandable , and buttons are all added to the row to make actual buttons for the calculator.

row1=Frame(win,bg="#1e1e2e")
row1.pack(expand=TRUE, fill=BOTH)
onebtn=Button(row1,text="1",font="Arial 23",relief="groove", command=btn1, fg="white",bg='#1e1e2e').pack(side=LEFT, expand=TRUE, fill=BOTH)    
twobtn=Button(row1,text="2",font="Arial 23",relief="groove", command=btn2,fg="white",bg='#1e1e2e').pack(side=LEFT, expand=TRUE, fill=BOTH)
threebtn=Button(row1,text="3",font="Arial 23",relief="groove", command=btn3,fg="white",bg='#1e1e2e').pack(side=LEFT, expand=TRUE, fill=BOTH)
plusbtn=Button(row1,text="+",font="Arial 23",relief="groove", command=btnplus,fg="white",bg='#1e1e2e').pack(side=LEFT, expand=TRUE, fill=BOTH)
sinbtn=Button(row1,text="sin",font="Arial 18",relief="groove", command=sin,fg="white",bg='#1e1e2e').pack(side=LEFT, expand=TRUE, fill=BOTH)
cosbtn=Button(row1,text="cos",font="Arial 18",relief="groove", command=cos,fg="white",bg='#1e1e2e').pack(side=LEFT, expand=TRUE, fill=BOTH)
tanbtn=Button(row1,text="tan",font="Arial 18",relief="groove", command=tan,fg="white",bg='#1e1e2e').pack(side=LEFT, expand=TRUE, fill=BOTH)
openbtn=Button(row1,text="(",font="Arial 18",relief="groove", command=open_parentheses, fg="white",bg='#1e1e2e').pack(side=LEFT, expand=TRUE, fill=BOTH)
closebtn=Button(row1,text=")",font="Arial 18",relief="groove", command=closing_parentheses, fg="white",bg='#1e1e2e').pack(side=LEFT, expand=TRUE, fill=BOTH)

row2=Frame(win,bg="#1e1e2e")
row2.pack(expand=TRUE, fill=BOTH)
fourbtn=Button(row2,text="4",font="Arial 22",relief="groove", command=btn4,fg="white",bg='#1e1e2e').pack(side=LEFT, expand=TRUE, fill=BOTH)    
fivebtn=Button(row2,text="5",font="Arial 22",relief="groove", command=btn5,fg="white",bg='#1e1e2e').pack(side=LEFT, expand=TRUE, fill=BOTH)
sixbtn=Button(row2,text="6",font="Arial 22",relief="groove", command=btn6,fg="white",bg='#1e1e2e').pack(side=LEFT, expand=TRUE, fill=BOTH)
minusbtn=Button(row2,text="-",font="Arial 22",relief="groove", command=btnsub,fg="white",bg='#1e1e2e').pack(side=LEFT, expand=TRUE, fill=BOTH)
arcsinbtn=Button(row2,text="sin-1",font="Arial 10 bold",relief="groove", command=asin,fg="white",bg='#1e1e2e').pack(side=LEFT, expand=TRUE, fill=BOTH)
arccosbtn=Button(row2,text="cos-1",font="Arial 10 bold",relief="groove", command=acos,fg="white",bg='#1e1e2e').pack(side=LEFT, expand=TRUE, fill=BOTH)
arctanbtn=Button(row2,text="tan-1",font="Arial 10 bold",relief="groove", command=atan,fg="white",bg='#1e1e2e').pack(side=LEFT, expand=TRUE, fill=BOTH)
pibtn=Button(row2,text="π",font="Arial 18",relief="groove", command=pi,fg="white",bg='#1e1e2e').pack(side=LEFT, expand=TRUE, fill=BOTH)
factbtn=Button(row2,text="x!",font="Arial 18",relief="groove", command=fact, fg="white",bg='#1e1e2e').pack(side=LEFT, expand=TRUE, fill=BOTH)

row3=Frame(win,bg="#1e1e2e")
row3.pack(expand=TRUE, fill=BOTH)
sevenbtn=Button(row3,text="7",font="Arial 23", command=btn7,relief="groove",fg="white",bg='#1e1e2e').pack(side=LEFT, expand=TRUE, fill=BOTH)    
eightbtn=Button(row3,text="8",font="Arial 23", command=btn8,relief="groove",fg="white",bg='#1e1e2e').pack(side=LEFT, expand=TRUE, fill=BOTH)
ninebtn=Button(row3,text="9",font="Arial 23", command=btn9,relief="groove",fg="white",bg='#1e1e2e').pack(side=LEFT, expand=TRUE, fill=BOTH)
multiplybtn=Button(row3,text="*",font="Arial 23",relief="groove", command=btnmult,fg="white",bg='#1e1e2e').pack(side=LEFT, expand=TRUE, fill=BOTH)
sqrbtn=Button(row3,text="x^2",font="Arial 17",relief="groove", command=sqr, fg="white",bg='#1e1e2e').pack(side=LEFT, expand=TRUE, fill=BOTH)
logbtn=Button(row3,text="log",font="Arial 17",relief="groove",fg="white",bg='#1e1e2e').pack(side=LEFT, expand=TRUE, fill=BOTH)
lnbtn=Button(row3,text="ln",font="Arial 17",relief="groove",fg="white",bg='#1e1e2e').pack(side=LEFT, expand=TRUE, fill=BOTH)
sqrrootbtn=Button(row3,text="√x",font="Arial 17",relief="groove",fg="white",bg='#1e1e2e').pack(side=LEFT, expand=TRUE, fill=BOTH)
pwrbtn=Button(row3,text="x^y",font="Arial 17",relief="groove", command=power, fg="white",bg='#1e1e2e').pack(side=LEFT, expand=TRUE, fill=BOTH)

row4=Frame(win,bg="#1e1e2e")
row4.pack(expand=TRUE, fill=BOTH)
backbtn=Button(row4,text="⌫",font="Arial 15",relief="groove", command=delete, fg="white",bg='#1e1e2e').pack(side=LEFT, expand=TRUE, fill=BOTH)    
zerobtn=Button(row4,text="0",font="Arial 23",relief="groove", command=btn0,fg="white",bg='#1e1e2e').pack(side=LEFT, expand=TRUE, fill=BOTH)
equalsbtn=Button(row4,text="=",font="Arial 11 bold",relief="groove", command=equals, fg="white",bg='#89b4fa').pack(side=LEFT, expand=TRUE, fill=BOTH)
dividebtn=Button(row4,text="/",font="Arial 23",relief="groove", command=btndiv,fg="white",bg='#1e1e2e').pack(side=LEFT, expand=TRUE, fill=BOTH)
clearbtn=Button(row4,text="AC",font="Arial 20",relief="groove", command=ac,fg="white",bg='#1e1e2e').pack(side=LEFT, expand=TRUE, fill=BOTH)    
decimalbtn=Button(row4,text=".",font="Arial 20",relief="groove", command=decimal, fg="white",bg='#1e1e2e').pack(side=LEFT, expand=TRUE, fill=BOTH)    
ebtn=Button(row4,text="e",font="Arial 20",relief="groove",fg="white",bg='#1e1e2e').pack(side=LEFT, expand=TRUE, fill=BOTH)
placeholder2btn=Button(row4,text="n/a",font="Arial 20",relief="groove",fg="white",bg='#1e1e2e').pack(side=LEFT, expand=TRUE, fill=BOTH)
switcheroooo=Button(row4,text="d/r",font="Arial 20", relief="groove",fg="white",bg='#1e1e2e').pack(side=LEFT, expand=TRUE, fill=BOTH)

win.mainloop()
#This is what actually starts the window
