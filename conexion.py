# -*- coding: utf-8 -*-
"""
Created on Fri Apr  3 19:09:37 2020

@author: Maldonado
"""

import sqlite3 

conexion = sqlite3.connect("ejemplo.db")
cursor = conexion.cursor()
#cursor.execute("create table usuarios (nombre varchar(100), edad integer, email varchar(100))")
#cursor.execute("insert into usuarios values('Alberto', 29, 'soporte@email.com')")
# cursor.execute("select * from usuarios")
# print(cursor)

# usuario = cursor.fetchone()
# print(usuario)
# print(usuario[2])

# usuarios = [('Mauricio',29, 'soporte@tecno.com'),
#             ('Juan', 30, 'user@gmail.com'),
#             ('Maria', 56, 'ventas@comensal.com'),]
# cursor.executemany("insert into usuarios values(?,?,?)", usuarios)

cursor.execute("select * from usuarios")
usuarios = cursor.fetchall()
for usuario in usuarios:
    print(usuario)

conexion.commit()

conexion.close()