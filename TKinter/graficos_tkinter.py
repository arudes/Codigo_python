# -*- coding: utf-8 -*-
"""
Created on Wed Feb 26 17:22:02 2020

@author: Maldonado
"""
from tkinter import *

principal = Tk() #se crea el marco
principal.title("Hola Mundo") # se le asigna un nombre al titulo de la ventana
principal.resizable(1,1) #se le asigna permisos para redimencionar
principal.iconbitmap('python.ico') #se fija un icono de pantalla

principal.mainloop() #se crea un bucle que permite ver la pantalla