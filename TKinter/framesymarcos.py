# -*- coding: utf-8 -*-
"""
Created on Tue Mar 24 14:52:36 2020

@author: Maldonado
"""

from tkinter import *

root = Tk()
root.title("Hola Mundo")
root.resizable(1,1) #ancho, alto
root.iconbitmap('radar.ico')

frame = Frame(root, width=480, height=320)
frame.pack(fill="x")
frame.config(cursor="pirate")
frame.config(bg="lightblue")
frame.config(bd=25)
frame.config(relief="sunken")

root.config(cursor="arrow")
root.config(bg="blue")
root.config(bd=15)
root.config(relief="ridge")

root.mainloop()
