from tkinter import *
import tkinter.messagebox

def doNothin():
    print("Message")

root = Tk()
root.geometry("200x200")

# ********** Menu ***********

menu = Menu(root)
root.config(menu=menu)

sub_menu = Menu(menu)
menu.add_cascade(label="File", menu=sub_menu)
sub_menu.add_command(label="New Project", command=doNothin)
sub_menu.add_command(label="New...", command=doNothin)
sub_menu.add_separator()
sub_menu.add_command(label="Exit", command=quit)

edit_menu = Menu(menu)
menu.add_cascade(label="Edit", menu=edit_menu)
edit_menu.add_command(label="Undo", command=doNothin)

# ********** Toolbar ***********

toolbar = Frame(root)
b1 = Button(toolbar, text="Insert", command=doNothin)
b1.pack(side=LEFT, padx=2, pady=2)
b2 = Button(toolbar, text="Print", command=doNothin)
b2.pack(side=LEFT, padx=2, pady=2)

toolbar.pack(side=TOP, fill=X)

# ********** Status Bar ***********

status = Label(root, text="Prepareing to do nothin'", bd=1, relief=SUNKEN, anchor=W)
status.pack(side=BOTTOM, fill=X)

'''# ********** Message box***********

#tkinter.messagebox.showinfo("Window Title", "Are you cool")
answer = tkinter.messagebox.askquestion("Question", "Are you cool")

if answer == 'yes':
    print(":D")'''

# ********** Canvas ***********

canvas = Canvas(root, width=200, height=100)
canvas.pack()

black_line = canvas.create_line(0, 0, 200, 50)
red_line = canvas.create_line(0, 0, 50, 200, fill='red')

green_box = canvas.create_rectangle(25, 25, 130, 60, fill="green")
canvas.delete(red_line)
canvas.delete(black_line)

root.mainloop()