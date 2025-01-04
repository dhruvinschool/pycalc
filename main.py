import math
from tkinter import *

#Below is the first part of the project , making the base GUI. In this , I will also create the functions to be used. For now , a basic GUI will be made to work for the limited set of functions available as of now , in the future it will be expanded upon.

win = Tk()
win.geometry("650x400+300+300")
#define resolution
win.title('pyCalc')
textbox = Entry(win,font='Arial 20',fg="Black",bg="#cdd6f4",bd=4,justify=RIGHT).pack(expand=TRUE, fill=BOTH)
#This makes a textbox , which will afterwards be the answer box.
row1=Frame(win,bg="#1e1e2e")
row1.pack(expand=TRUE, fill=BOTH)
onebtn=Button(row1,text="1",font="Arial 23",relief="groove",fg="white",bg='#1e1e2e').pack(side=LEFT, expand=TRUE, fill=BOTH)    
twobtn=Button(row1,text="2",font="Arial 23",relief="groove",fg="white",bg='#1e1e2e').pack(side=LEFT, expand=TRUE, fill=BOTH)
threebtn=Button(row1,text="3",font="Arial 23",relief="groove",fg="white",bg='#1e1e2e').pack(side=LEFT, expand=TRUE, fill=BOTH)
plusbtn=Button(row1,text="+",font="Arial 23",relief="groove",fg="white",bg='#1e1e2e').pack(side=LEFT, expand=TRUE, fill=BOTH)
sinbtn=Button(row1,text="sin",font="Arial 18",relief="groove",fg="white",bg='#1e1e2e').pack(side=LEFT, expand=TRUE, fill=BOTH)
cosbtn=Button(row1,text="cos",font="Arial 18",relief="groove",fg="white",bg='#1e1e2e').pack(side=LEFT, expand=TRUE, fill=BOTH)
tanbtn=Button(row1,text="tan",font="Arial 18",relief="groove",fg="white",bg='#1e1e2e').pack(side=LEFT, expand=TRUE, fill=BOTH)
openbtn=Button(row1,text="(",font="Arial 18",relief="groove",fg="white",bg='#1e1e2e').pack(side=LEFT, expand=TRUE, fill=BOTH)
closebtn=Button(row1,text=")",font="Arial 18",relief="groove",fg="white",bg='#1e1e2e').pack(side=LEFT, expand=TRUE, fill=BOTH)




row2=Frame(win,bg="#1e1e2e")
row2.pack(expand=TRUE, fill=BOTH)
fourbtn=Button(row2,text="4",font="Arial 22",relief="groove",fg="white",bg='#1e1e2e').pack(side=LEFT, expand=TRUE, fill=BOTH)    
fivebtn=Button(row2,text="5",font="Arial 22",relief="groove",fg="white",bg='#1e1e2e').pack(side=LEFT, expand=TRUE, fill=BOTH)
sixbtn=Button(row2,text="6",font="Arial 22",relief="groove",fg="white",bg='#1e1e2e').pack(side=LEFT, expand=TRUE, fill=BOTH)
minusbtn=Button(row2,text="-",font="Arial 22",relief="groove",fg="white",bg='#1e1e2e').pack(side=LEFT, expand=TRUE, fill=BOTH)
arcsinbtn=Button(row2,text="sin-1",font="Arial 10 bold",relief="groove",fg="white",bg='#1e1e2e').pack(side=LEFT, expand=TRUE, fill=BOTH)
arccosbtn=Button(row2,text="cos-1",font="Arial 10 bold",relief="groove",fg="white",bg='#1e1e2e').pack(side=LEFT, expand=TRUE, fill=BOTH)
arctanbtn=Button(row2,text="tan-1",font="Arial 10 bold",relief="groove",fg="white",bg='#1e1e2e').pack(side=LEFT, expand=TRUE, fill=BOTH)
pibtn=Button(row2,text="π",font="Arial 18",relief="groove",fg="white",bg='#1e1e2e').pack(side=LEFT, expand=TRUE, fill=BOTH)
factbtn=Button(row2,text="x!",font="Arial 18",relief="groove",fg="white",bg='#1e1e2e').pack(side=LEFT, expand=TRUE, fill=BOTH)



row3=Frame(win,bg="#1e1e2e")
row3.pack(expand=TRUE, fill=BOTH)
sevenbtn=Button(row3,text="7",font="Arial 23",relief="groove",fg="white",bg='#1e1e2e').pack(side=LEFT, expand=TRUE, fill=BOTH)    
eightbtn=Button(row3,text="8",font="Arial 23",relief="groove",fg="white",bg='#1e1e2e').pack(side=LEFT, expand=TRUE, fill=BOTH)
ninebtn=Button(row3,text="9",font="Arial 23",relief="groove",fg="white",bg='#1e1e2e').pack(side=LEFT, expand=TRUE, fill=BOTH)
multiplybtn=Button(row3,text="*",font="Arial 23",relief="groove",fg="white",bg='#1e1e2e').pack(side=LEFT, expand=TRUE, fill=BOTH)
sqrbtn=Button(row3,text="x^2",font="Arial 17",relief="groove",fg="white",bg='#1e1e2e').pack(side=LEFT, expand=TRUE, fill=BOTH)
logbtn=Button(row3,text="log",font="Arial 17",relief="groove",fg="white",bg='#1e1e2e').pack(side=LEFT, expand=TRUE, fill=BOTH)
lnbtn=Button(row3,text="ln",font="Arial 17",relief="groove",fg="white",bg='#1e1e2e').pack(side=LEFT, expand=TRUE, fill=BOTH)
sqrrootbtn=Button(row3,text="√x",font="Arial 17",relief="groove",fg="white",bg='#1e1e2e').pack(side=LEFT, expand=TRUE, fill=BOTH)
sqrbtn=Button(row3,text="x^y",font="Arial 17",relief="groove",fg="white",bg='#1e1e2e').pack(side=LEFT, expand=TRUE, fill=BOTH)


row4=Frame(win,bg="#1e1e2e")
row4.pack(expand=TRUE, fill=BOTH)
backbtn=Button(row4,text="⌫",font="Arial 15",relief="groove",fg="white",bg='#1e1e2e').pack(side=LEFT, expand=TRUE, fill=BOTH)    
zerobtn=Button(row4,text="0",font="Arial 23",relief="groove",fg="white",bg='#1e1e2e').pack(side=LEFT, expand=TRUE, fill=BOTH)
equalsbtn=Button(row4,text="=",font="Arial 11 bold",relief="groove",fg="white",bg='#89b4fa').pack(side=LEFT, expand=TRUE, fill=BOTH)
dividebtn=Button(row4,text="/",font="Arial 23",relief="groove",fg="white",bg='#1e1e2e').pack(side=LEFT, expand=TRUE, fill=BOTH)
clearbtn=Button(row4,text="AC",font="Arial 20",relief="groove",fg="white",bg='#1e1e2e').pack(side=LEFT, expand=TRUE, fill=BOTH)    
decimalbtn=Button(row4,text=".",font="Arial 20",relief="groove",fg="white",bg='#1e1e2e').pack(side=LEFT, expand=TRUE, fill=BOTH)    
placeholder1btn=Button(row4,text="n/a",font="Arial 20",relief="groove",fg="white",bg='#1e1e2e').pack(side=LEFT, expand=TRUE, fill=BOTH)
placerholder2btn=Button(row4,text="n/a",font="Arial 20",relief="groove",fg="white",bg='#1e1e2e').pack(side=LEFT, expand=TRUE, fill=BOTH)

win.mainloop()
