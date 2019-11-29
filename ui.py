import Spoof as njn
from tkinter import *
import os
path=os.path.dirname(os.path.abspath(__file__))

root= Tk()
root.title('BoringBrowser')
#imgicon = PhotoImage(file=os.path.join(path,'Boringbot.png'))
root.tk.call('wm', 'iconphoto', root._w, PhotoImage(file=path+'\\BoringBot.png'))
x=IntVar()
y=StringVar()
Label1=Label(root,text="Tasks")
Label2=Label(root,text="Site")

entry1 = Entry(root,textvariable=x)
entry2 = Entry(root,textvariable=y) 

Label1.grid(row=0,column=0)
entry1.grid(row=0,column=1)
Label2.grid(row=1,column=0)
entry2.grid(row=1,column=1)

    
button1 = Button(text='Launch', command=lambda:njn.thread(x.get(),y.get()))
button1.grid(row=2,column=0)

root.mainloop()