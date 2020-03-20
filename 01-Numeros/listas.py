#declarando lista
lista = [12,45,32,8,41,67]
print(lista)
datos = [6,"una cadena",5.67,"Hola mundo"]
print(datos)
#mostrar elementos
print(datos[0])
print(datos[-1])

#slicing en listas
print(datos[-2:])

#concatenarlo a una nueva lista
print(lista + [10,100,200])

#las listas no son inmutables
inpar = [1,3,5,7,10,11]
inpar[4] = 9
print(inpar)

#metodos de las listas
inpar.append(13)

#asignacion con slicing
lista1 = ["a","b","c","d","e"]
print(lista1[:3])
lista1[:3] = ["A","B","C"]
print(lista1)
#borrando las primeras 3 posiciones
lista1[:3] = []
print(lista1)

print(len(lista1))

#lista anidadas
l1 = [1,2,3]
l2 = [4,5,6]
l3 = [7,8,9]
r = [l1,l2,l3]
print(r)
print(r[0])

#accediendo al primer elemento de la lista
print(r[0][0])
print(r[-1][-1])
