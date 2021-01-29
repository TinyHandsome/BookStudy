from tkinter import Tk
from tkinter.messagebox import showwarning
import win32com.client as win32


def warn(app): return showwarning(app, 'Exit?')


RANGE = range(3, 8)


def outlook():
    app = 'Outlook'
    olook = win32.gencache.EnsureDispatch('%s.Application' % app)

    mail = olook.CreateItem(win32.constants.olMailItem)
    recip = mail.Recipients.Add('you@127.0.0.1')
    subj = mail.Subject = 'Python-to-%s Demo' % app
    body = ["Line %d" % i for i in RANGE]
    body.insert(0, '%s\r\n' % subj)
    body.append("\r\nTh-th-th-that's all folks!")
    mail.Body = '\r\n'.join(body)
    mail.send()

    ns = olook.GetNamespace("MAPI")
    obox = ns.GetDefaultFolder(win32.constants.olFolderOutbox)
    obox.Display()

    warn(app)
    olook.Quit()

if __name__ == '__main__':
    Tk().withdraw()
    outlook()
    
