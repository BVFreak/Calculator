# Calculator
from tkinter import *
import tkinter

print("\n     Calculator\n     Version 0.1\n     Made by BVFreak\n")

root = tkinter.Tk()  #sets the root

root.title("Calculator")  #sets the name of the root

root_width = 1920
root_height = 1080

# get the screen dimension
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# find the center point
center_x = int(screen_width / 2 - root_width / 2)
center_y = int(screen_height / 2 - root_height / 2)

# set the position of the root to the center of the screen
root.geometry(f'{root_width}x{root_height}+{center_x}+{center_y}')


def button_add():
  return


# buttons

button_1 = Button(root,
                  text="1",
                  padx=40,
                  pady=20,
                  command=button_add,
                  font="TkFixedFont")
button_2 = Button(root,
                  text="2",
                  padx=40,
                  pady=20,
                  command=button_add,
                  font="TkFixedFont")
button_3 = Button(root,
                  text="3",
                  padx=40,
                  pady=20,
                  command=button_add,
                  font="TkFixedFont")
button_4 = Button(root,
                  text="4",
                  padx=40,
                  pady=20,
                  command=button_add,
                  font="TkFixedFont")
button_5 = Button(root,
                  text="5",
                  padx=40,
                  pady=20,
                  command=button_add,
                  font="TkFixedFont")
button_6 = Button(root,
                  text="6",
                  padx=40,
                  pady=20,
                  command=button_add,
                  font="TkFixedFont")
button_7 = Button(root,
                  text="7",
                  padx=40,
                  pady=20,
                  command=button_add,
                  font="TkFixedFont")
button_8 = Button(root,
                  text="8",
                  padx=40,
                  pady=20,
                  command=button_add,
                  font="TkFixedFont")
button_9 = Button(root,
                  text="9",
                  padx=40,
                  pady=20,
                  command=button_add,
                  font="TkFixedFont")
button_0 = Button(root,
                  text="0",
                  padx=40,
                  pady=20,
                  command=button_add,
                  font="TkFixedFont")
button_decimalpoint = Button(root,
                             text=".",
                             padx=40,
                             pady=20,
                             command=button_add,
                             font="TkFixedFont")
button_equals = Button(root,
                       text="=",
                       padx=40,
                       pady=20,
                       command=button_add,
                       font="TkFixedFont")
button_add = Button(root,
                    text="+",
                    padx=40,
                    pady=20,
                    command=button_add,
                    font="TkFixedFont")
button_subtract = Button(root,
                         text="-",
                         padx=40,
                         pady=20,
                         command=button_add,
                         font="TkFixedFont")
button_multiply = Button(root,
                         text="x",
                         padx=40,
                         pady=20,
                         command=button_add,
                         font="TkFixedFont")
button_divide = Button(root,
                       text="÷",
                       padx=40,
                       pady=20,
                       command=button_add,
                       font="TkFixedFont")

# place buttons

button_1.grid(row=3, column=0)
button_2.grid(row=3, column=1)
button_3.grid(row=3, column=2)

button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)

button_7.grid(row=1, column=0)
button_8.grid(row=1, column=1)
button_9.grid(row=1, column=2)

button_0.grid(row=4, column=0)
button_decimalpoint.grid(row=4, column=1)
button_equals.grid(row=4, column=2)

button_add.grid(row=4, column=3)
button_subtract.grid(row=3, column=3)
button_multiply.grid(row=2, column=3)
button_divide.grid(row=1, column=3)

system = Entry(root, width=35, borderwidth=5)
system.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

root.mainloop()
