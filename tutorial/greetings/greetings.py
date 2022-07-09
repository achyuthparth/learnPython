from tkinter import *

root = Tk()

#creating the widget
myLabel = Label(root, text="hello")

#packs it to screen
#myLabel.pack()




#creates second label
myLabel2 = Label(root, text="wassup")

#puts the labels onto the grid

myLabel.grid(row=0, column=0)
myLabel2.grid(row=1, column=0)

def myClick():
    myLabel3 = Label(root, text="button is here")
    myLabel3.grid(row = 11, column = 0)

myButton = Button(root, text="click me", command=myClick)
myButton.grid(row = 10, column = 0)



root.mainloop() 