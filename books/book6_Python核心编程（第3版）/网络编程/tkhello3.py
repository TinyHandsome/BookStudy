import tkinter as tk

top = tk.Tk()

hello = tk.Label(top, text='Hello World!')
hello.pack()

quit = tk.Button(top, text='QUIT', command=top.quit, bg='red', fg='white')
quit.pack(fill=tk.X, expand=1)
tk.mainloop()
