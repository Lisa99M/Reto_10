#Desarrollar un algoritmo que calcule el producto punto de dos arreglos de números enteros (reales) de igual tamaño.
from operator import mul
def Producto_punto (lista1: list, lista2: list) -> float:
   
    for i in range (n):
        num1 = float(input("Insertar elementos reales para el arreglo 1: "))
        lista1.append(num1)
    for i in range (n):
        num2 = float(input("Insertar elementos reales para el arreglo 2: "))
        lista2.append(num2)
    producto = sum([i*j for (i,j) in zip(lista1, lista2)])
    return producto

if __name__ == "__main__":
    n = int(input("Insertar cantidad de elementos para los arreglos 1 y 2: "))
    num1 = 0
    num2 = 0
    lista1 = []
    lista2 = []
    Llamado = Producto_punto (lista1, lista2)
    print("El producto punto de los arreglos: " + str(lista1) + " y " + str(lista2) + " es: " + str(Llamado))
    
