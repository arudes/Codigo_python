# -*- coding: utf-8 -*-
"""
Created on Fri Apr  3 11:30:44 2020

@author: Maldonado
"""

from tkinter import *
from tkinter import messagebox as MB
from tkinter import colorchooser as CC
from tkinter import filedialog as FD

root = Tk()

def test():
    
    color = CC.askcolor(title="Elige un color")
    print(color)
    
    ficheror = FD.askopenfilename(title="Abrir archivo", initialdir="C:", 
                                  filetypes=(("Fichero de texto","*.txt"), ("Fichero python","*.py"), ("Todos los ficheros","*.*")))
    print(ficheror)
    
    ruta = FD.asksaveasfile(title="Guardar archivo")
    print(ruta)
    
Button(root, text="click", command=test).pack()

root.mainloop()