import parser
from tkinter import *
root=Tk()
root.title("calculator")
display=Entry(root)
i=0
def getvar(num):
    global i
    display.insert(i,num)
    i+=1

def clear():
    display.delete(0,END)

def undo():
    entare_string=display.get()
    if len(entare_string):
        new_string=entare_string[:-1]
        clear()
        display.insert(0,new_string)
    else:
        clear()
        display.insert(0,"error")
def operation(opr):
    global i
    length=len(opr)
    display.insert(i,opr)
    i+=length

def calculate():
    entair_string=display.get()
    try:
        a=parser.expr(entair_string).compile()
        result=eval(a)
        clear()
        display.insert(0,result)
    except EXCEPTION:
        clear()
        display.insert(0,"error")



#adding button to the calculator

display.grid(row=1,columnspan=6,sticky=W+E)
Button(root,text="1",command=lambda : getvar(1)).grid(row=2,column=0)
Button(root,text="2",command=lambda : getvar(2)).grid(row=2,column=1)
Button(root,text="3",command=lambda : getvar(3)).grid(row=2,column=2)
Button(root,text="4",command=lambda : getvar(4)).grid(row=3,column=0)
Button(root,text="5",command=lambda : getvar(5)).grid(row=3,column=1)
Button(root,text="6",command=lambda : getvar(6)).grid(row=3,column=2)
Button(root,text="7",command=lambda : getvar(7)).grid(row=4,column=0)
Button(root,text="8",command=lambda : getvar(8)).grid(row=4,column=1)
Button(root,text="9",command=lambda : getvar(9)).grid(row=4,column=2)
Button(root,text="0",command=lambda : getvar(0)).grid(row=5,column=0)
Button(root,text="Ac",command=lambda :clear()).grid(row=5,column=1)
Button(root,text="=",command=lambda :calculate()).grid(row=5,column=2)
Button(root,text="+",command=lambda :operation('+')).grid(row=5,column=5)
Button(root,text="->",command=lambda :undo()).grid(row=2,column=3)
Button(root,text="_",command=lambda :operation('-')).grid(row=3,column=3)
Button(root,text="*",command=lambda :operation('*')).grid(row=4,column=3)
Button(root,text="/",command=lambda :operation('/')).grid(row=5,column=3)
Button(root,text="pi",command=lambda :operation("3.14")).grid(row=2,column=4)
Button(root,text="%",command=lambda :operation('%')).grid(row=3,column=4)
Button(root,text="(",command=lambda :operation('(')).grid(row=4,column=4)
Button(root,text=")").grid(row=5,column=4)
Button(root,text="exp",command=lambda :operation('**')).grid(row=2,column=5)
Button(root,text="x!").grid(row=3,column=5)
Button(root,text="^2",command=lambda :operation('**2')).grid(row=4,column=5)








root.mainloop()