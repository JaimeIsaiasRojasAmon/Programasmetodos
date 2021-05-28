#desarrolle en Python un programa para calcular la inversa de matrices de dimension 2x2, no olvide colocar
# comentarios en su programa

# Python program to inverse
# a matrix using numpy
#Programa que crea una matriz de dimensiones con los datos que ingresa el usuario
#Import required package
import numpy as np  #asignamos np para facillitar el codigo al escribir
filas = int(input("Introduce numero de filas: "))    #se crean las dimensiones de la mattriz
columnas = int(input("Introduce el nunero de columnas:"))

matriz = []
for i in range(filas):
    matriz.append([])   #añadimos la lista
    for j in range(columnas):
        valor = float(input("Fila{},Columna{} : ".format(i+1, j+1)))  #nos referimos a numeros de orden
        matriz[i].append(valor)   #añadimos el valor que introduce el usuario
print()
for fila in matriz:
    print("[",end=" ")
    for elemento in fila:
        print("{:8.2}".format(elemento), end=" ")  #creamos un formato adecuado
    print("]")
print()




print(" La matriz inversa es :")
# Calculamos la inversa de la matriz
print(np.linalg.inv(matriz)) #calculamos la inversa de la matriz creada y la imprimimos
