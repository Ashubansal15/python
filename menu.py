from tkinter import *
root=Tk()
def doNothing():
     print("I am nothing")
def doSomething():
     print("I am something")



menu=Menu(root)

root.configure(menu=menu)

submenu1=Menu(menu)


menu.add_cascade(label="File",menu=submenu1)




submenu1.add_command(label="New Project",command=doNothing)

submenu1.add_command(label="Open Project",command=doSomething)


submenu2=Menu(menu)

menu.add_cascade(label="Edit",menu=submenu2)


submenu2.add_command(label="Cut",command=doNothing)

submenu2.add_command(label="Copy",command=doSomething)




