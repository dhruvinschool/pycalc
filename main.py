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

if switch == False:
    switchdisp = 'Rad'
else:
    switchdisp = 'Deg'

#Below is an OOP implementation of numbers inside of the UI. Three attributes are made , value (number value) , textbox (the textbox of the calculator).

class NumberButton:
    def __init__(self, parent, value, textbox):
        self.value = value
        self.textbox = textbox
        self.button = Button(
            parent,
            text=str(value),
            font="Arial 23",
            relief="groove",
            bd=0,
            fg="white",
            bg="#1e1e2e",
            command=self.insert_value
        )
        self.button.pack(side=LEFT, expand=TRUE, fill=BOTH)

#I have also used 'parent' to ensure that each button will have the same UI properties in tkinter , theyll have the same font and colour.

    def insert_value(self):
        if self.textbox.get() == '0':
            self.textbox.delete(0, END)
        position = len(self.textbox.get())
        self.textbox.insert(position, str(self.value))
#This function actually puts the value inside of the textbox.

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

def cos():
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

def tan():
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
        tkinter.messagebox.showerror("Error" , "Error , check operand and operator")
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
        tkinter.messagebox.showerror("Error" , "Error , check operand and operator")
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
        tkinter.messagebox.showerror("Error" , "Error , check operand and operator")
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
    try:
        ans=(eval(textbox.get()))
        #The eval function takes the entire textbox as a string and evaluates it if its in mathematical terms
        if isinstance(ans,complex):
            raise ValueError("Complex result not allowed")
        textbox.delete(0, END)
        #The textbox is deleted
        textbox.insert(0, str(ans))
        #The answer to the evaluation is inputted into the start of the textbox
    except Exception:
        tkinter.messagebox.showerror("Error" , "Error , check operand and operator")

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

def sqrrt():
    position=len(textbox.get())
    textbox.insert(position,'**(1/2)')
    #Adds **(1/2) to the end of the textbox. The evaluate function interprets this as ^1/2 . aka sqrrt.


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
        tkinter.messagebox.showerror("Error" , "Error , check operand and operator")
    #If the textbox is not in integer form , or is a negative number , this error is reported.

textbox = Entry(win,font='Arial 20',fg="Black",bg="#cdd6f4",bd=4,justify=RIGHT)
#This is where the textbox itself is created , I used Arial font and black foreground for black text. The background colour has been chosen from a colorscheme online (Catppuccin mocha)
textbox.insert(0, '0')
#This makes the default textbox value 0
textbox.pack(expand=TRUE, fill=BOTH)
#This makes a textbox , which will afterwards be the answer box.

def angleswitcher():
    global switch
    if switch is False:
        switch = True
        degrad['text'] = "Deg"
    #If the switch is false , we set it to true and we change the switch button display to Deg.
    else:
        switch = False
        degrad['text'] = "Rad"
    #If the switch is not False , we set it to false and make the text Rad.

def euler():
    #This function adds a number to the textbox.
    if textbox.get() =='0':
        textbox.delete(0,END)
    #The above if function checks if the textbox contains only 0 , which is the base value. If so , it'll delete the 0 before inputting the number.
    position=len(textbox.get())
    eulerstr = 'e'
    #Here a string called eulerstr is made to hold eulers number , so that it can be put in the textbox (next line) , more on the first line outside of this function.
    textbox.insert(position,str(eulerstr))

e = math.e
#Here the euler constant symbol is used as a variable to hold the actual euler constant value. Hence , when used in eval function , it is interpreted as a variable and the euler value is used for calculation , whilst euler symbol is on the textbox.

def ln():
    try:
        ans=float(textbox.get())
        ans=math.log(ans)
        textbox.delete(0,END)
        textbox.insert(0,ans)
    #As stated earlier , try is used here so that the computer can verify that the value supplied has an an actual value on the sine graph.
    except Exception:
        tkinter.messagebox.showerror("Error" , "Error , check operand and operator")
    #An error is hence printed in the exception , so that the user is made aware that the input/operation is invalid.

def log():
    try:
        ans=float(textbox.get())
        ans=math.log(ans, 10)
        textbox.delete(0,END)
        textbox.insert(0,ans)
    #As stated earlier , try is used here so that the computer can verify that the value supplied has an an actual value on the sine graph.
    except Exception:
        tkinter.messagebox.showerror("Error" , "Error , check operand and operator")
    #An error is hence printed in the exception , so that the user is made aware that the input/operation is invalid.



#All the following blocks of code are in the same format. The first line makes a row , which is just a frame in the window. The row is made expandable , and buttons are all added to the row to make actual buttons for the calculator.

# --- row1 ---
row1=Frame(win,bg="#1e1e2e")
row1.pack(expand=TRUE, fill=BOTH)
NumberButton(row1, 1, textbox)
NumberButton(row1, 2, textbox)
NumberButton(row1, 3, textbox)

# Operator + Trig buttons using iteration
row1_buttons = [
    ("+", btnplus, "Arial 23"),
    ("sin", sin, "Arial 18"),
    ("cos", cos, "Arial 18"),
    ("tan", tan, "Arial 18"),
    ("(", open_parentheses, "Arial 18"),
    (")", closing_parentheses, "Arial 18"),
]
#For each button entry inside of my UI , I have designed each button to be held inside of a list. Each object in the list has 3 properties , the label (button display) , the function (function to be executed) and the font (scaling purposes.)

for label, func, font in row1_buttons:
    Button(row1, text=label, font=font, relief="groove", bd=0,
           command=func, fg="white", bg="#1e1e2e").pack(side=LEFT, expand=TRUE, fill=BOTH)
#This loop loops through each item in the list , iterating as many times as the size of the list is. It fetches the label , function , and font and defines a button in the row containing data from each item.

# --- row2 ---
row2=Frame(win,bg="#1e1e2e")
row2.pack(expand=TRUE, fill=BOTH)
NumberButton(row2, 4, textbox)
NumberButton(row2, 5, textbox)
NumberButton(row2, 6, textbox)

row2_buttons = [
    ("-", btnsub, "Arial 22"),
    ("sin-1", asin, "Arial 10 bold"),
    ("cos-1", acos, "Arial 10 bold"),
    ("tan-1", atan, "Arial 10 bold"),
    ("π", pi, "Arial 18"),
    ("x!", fact, "Arial 18"),
]

for label, func, font in row2_buttons:
    Button(row2, text=label, font=font, relief="groove", bd=0,
           command=func, fg="white", bg="#1e1e2e").pack(side=LEFT, expand=TRUE, fill=BOTH)

# --- row3 ---
row3=Frame(win,bg="#1e1e2e")
row3.pack(expand=TRUE, fill=BOTH)
NumberButton(row3, 7, textbox)
NumberButton(row3, 8, textbox)
NumberButton(row3, 9, textbox)

row3_buttons = [
    ("*", btnmult, "Arial 23"),
    ("x^2", sqr, "Arial 17"),
    ("log", log, "Arial 17"),
    ("ln", ln, "Arial 17"),
    ("√x", sqrrt, "Arial 17"),  # keep None if you haven’t written sqrroot function
    ("x^y", power, "Arial 17"),
]

for label, func, font in row3_buttons:
    Button(row3, text=label, font=font, relief="groove", bd=0,
           command=func, fg="white", bg="#1e1e2e").pack(side=LEFT, expand=TRUE, fill=BOTH)

# --- row4 ---
row4=Frame(win,bg="#1e1e2e")
row4.pack(expand=TRUE, fill=BOTH)
backbtn=Button(row4,text="⌫",font="Arial 15",relief="groove",bd=0, command=delete, fg="white",bg='#1e1e2e').pack(side=LEFT, expand=TRUE, fill=BOTH)    
NumberButton(row4, 0, textbox)
equalsbtn=Button(row4,text="=",font="Arial 18 bold",relief="groove",bd=0, command=equals, fg="white",bg='#89b4fa').pack(side=LEFT, expand=TRUE, fill=BOTH)

row4_buttons = [
    ("/", btndiv, "Arial 23"),
    ("AC", ac, "Arial 20"),
    (".", decimal, "Arial 20"),
    ("e", euler, "Arial 20"),
    ("n/a", None, "Arial 20"), 
]

for label, func, font in row4_buttons:
    Button(row4, text=label, font=font, relief="groove", bd=0,
           command=func, fg="white", bg="#1e1e2e").pack(side=LEFT, expand=TRUE, fill=BOTH)

degrad=Button(row4,text="Rad",font="Arial 20", relief="groove",bd=0,command=angleswitcher,fg="white",bg='#1e1e2e')
degrad.pack(side=LEFT, expand=TRUE, fill=BOTH)
win.mainloop()
#This is what actually starts the window
