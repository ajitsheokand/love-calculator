from tkinter import *
import random
root=None
text=None
name=None
root=Tk()

def showResult():
    global root
    global svalue
    temp=random.randint(0,100)
    result= str(temp)+"% love"
    if name.get()=="jaspreet":
        result="100% love"
    text.set(result)

def show(root):
    global text
    text = StringVar()
    text.set("")
    label = Label(root,textvariable=text)
    label.pack()
name=StringVar()
label=Label(root,text="Love calculator")
label.pack()
label1=Label(root,text="your name:")
label1.pack()
entry1=Entry(root,textvariable=name)
entry1.pack()
label2=Label(root,text="your crush name:")
label2.pack()
entry2=Entry(root)
entry2.pack()
button=Button(root,text="result",command=showResult)
button.pack()
show(root)

root.mainloop()




