# 变量追踪：trace
from tkinter import *
window=Tk()
def callbackw(*args): #
	print("variable was written!")
 
def callbackr(*args):
	print("variable was read !")
 
def processButton1():
	var.set("hello,world!")
def processButton2():
	var.get()
def processButton3():
	var.trace_vdelete("r",vr)
 
var=StringVar()
# 追踪变量var的变化
vw=var.trace("w", callbackw) #当变量var被重设时提示
vr=var.trace("r", callbackr) #当变量var被读取时提示

Label(window,textvariable=var).pack()
Button(window,text="Button1",command=processButton1).pack() #重新设定变量var
Button(window,text="Button2",command=processButton2).pack() #读取变量var的值
Button(window,text="Button3",command=processButton3).pack() #不再追踪读取变量的操作
window.mainloop()