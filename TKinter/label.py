# -*- coding: utf-8 -*-
"""
Created on Sat Mar 28 11:14:29 2020

@author: Maldonado
"""

from tkinter import *

root = Tk()


# texto = StringVar()
# texto.set("Texto de prueba")

# #frame = Frame(root, width=480, height=320)
# #frame.pack() #usar both para x, y
# Label(root, text="Hola mundo").pack(anchor="nw")
# label = Label(root, text="en tkinter")
# label.pack(anchor="center")
# label.config(bg="green", fg="yellow", font=("verdana", 16))
# Label(root, text="inicios").pack(anchor="se")

# label.config(textvariable=texto)

iimagen = PhotoImage(file ="dragon.gif")
Label(root, image=iimagen).pack()

root.mainloop()