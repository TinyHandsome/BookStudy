from tkinter import Tk
from time import sleep
from tkinter.messagebox import showwarning
import win32com.client as win32

warn = lambda app: showwarning(app, "Exit?")
RANGE = range(3, 8)

def ppoint():
    app = 'PowerPoint'
    ppoint = win32.gencache.EnsureDispatch('%s.Application' % app)
    pres = ppoint.Presentations.Add()
    ppoint.Visible = True

    sl = pres.Slides.Add(1, win32.constants.ppLayoutText)
    sleep(1)
    sla = sl.Shapes[0].TextFrame.TextRange
    sla.Text = 'Python-to-%s Demo' % app
    sleep(1)
    slb = sl.Shapes[1].TextFrame.TextRange
    for i in RANGE:
        slb.InsertAfter("Line %d\r\n" % i)
        sleep(1)
    slb.InsertAfter("\r\nTh-th-th-that's all folks!")

    warn(app)
    pres.Close()
    ppoint.Quit()

if __name__ == '__main__':
    Tk().withdraw()
    ppoint()
    

