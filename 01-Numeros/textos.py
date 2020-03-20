saludo = "Hola mundo"

#concatenar
mensaje = "Hola "+" "+"Mundo\n"
print(mensaje)

#multiplicar
cad1 = "Bienvenido "*3
cad2 = "a Komorebi Code\n"
print(cad1 + cad2)

#añadir
mensaje1 = "Bienvenidos"
mensaje1 += " a "
mensaje1 += "Komorebi Code\n"
print(mensaje1)

#metodos para cadenas de caracteres

mensaje2 = "Hola Mundo"
print("La longitud de la cadena es: " +str(len(mensaje2))+"\n")

mensaje3 = "hola mundo"
mensaje3 = mensaje3.find("mundo") # con find podemos busca una sub cadena dentro de una cadena
print(mensaje3) #devuelve la posicion donde inicia

mensaje4 = "Hola Mundo"
mensaje4 = mensaje4.find("gato")
print(mensaje4) #devuelve -1 ya que no se encontro la sub cadena

mensaje5 = "progra en python"
mesaje5 = mensaje5.replace("a", "ando")
print(mensaje5)

mensaje6 = "cortar el texto"
mensaje6 = mensaje6[2:8]
print(mensaje6)

mensaje7 = "HACER LETRA MINUSCULA"
print(mensaje7.lower())

mensaje8 = "Hola mundo"
print(mensaje8.upper())

mensaje9 = "hola mundo"
print(mensaje9.capitalize())

