import tkinter as tk

top = tk.Tk()
quit = tk.Button(top, text='Hello World', command=top.quit)
quit.pack()
tk.mainloop()