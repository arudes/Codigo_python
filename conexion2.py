# -*- coding: utf-8 -*-
"""
Created on Sat Apr  4 18:41:01 2020

@author: Maldonado
"""

import sqlite3

conexion = sqlite3.connect("usuarios.db")
cursor = conexion.cursor()

cursor.execute(''' 
               create table usuarios(dni varchar(9) primary key,
                                     nombre varchar(100),
                                     edad integer,
                                     email varchar(100))
               ''')
usuarios = [('01','Mauricio',29, 'soporte@tecno.com'),
             ('02','Juan', 30, 'user@gmail.com'),
             ('03','Maria', 56, 'ventas@comensal.com'),]
cursor.executemany("insert into usuarios values(?,?,?,?)", usuarios)

conexion.commit()
conexion.close()