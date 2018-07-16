'''Q1. Write a python program using tkinter interface to write Hello World and a exit button that closes the interface.'''
from tkinter import *
root =Tk()
theLabel=Label(root,text="hello this is neha ")
theLabel.pack()
root.mainloop()

'''. Write a python program using tkinter interface to write Hello World and a exit button that closes the interface.'''
from tkinter import*
root=Tk()
theLabel1=Label(root,text="My file_name_neha",fg="olive")
theLabel1.pack()

topFrame=Frame(root)
topFrame.pack()
bottomFrame=Frame(root)
bottomFrame.pack(side=BOTTOM)

button1=Button(topFrame,text="button1",fg="red")
button2=Button(topFrame,text="button2",fg="red")
button3=Button(topFrame,text="button3",fg="blue")
button4=Button(bottomFrame,text="button4",fg="pink")

button1.pack()
button2.pack()
button3.pack()
button4.pack()

root.mainloop()

'''
 Create a frame using tkinter with any label text and two buttons.One to exit and other to change the label to some other text.'''

from tkinter import*
root=Tk()
theLabel1=Label(root,text="My file_name_neha",fg="olive")
theLabel1.pack()

topFrame=Frame(root)
topFrame.pack()
bottomFrame=Frame(root)
bottomFrame.pack(side=BOTTOM)

button1=Button(topFrame,text="button1",fg="red")
button2=Button(topFrame,text="button2",fg="red")

button1.pack()
button2.pack()

root.mainloop()
