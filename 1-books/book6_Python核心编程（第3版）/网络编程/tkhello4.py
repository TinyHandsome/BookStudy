import tkinter as tk

def resize(ev=None):
    label.config(font='Helvetica -%d bold' % scale.get())

top = tk.Tk()
top.geometry('250x150')

label = tk.Label(top, text='Hello World!', font='Helvetica -12 bold')
label.pack()

scale = tk.Scale(top, from_=10, to=40, orient=tk.HORIZONTAL, command=resize)
scale.set(12)
scale.pack(fill=tk.X, expand=1)

quit = tk.Button(top, text='QUIT', command=top.quit, activeforeground='white', activebackground='red')
quit.pack()

tk.mainloop()
