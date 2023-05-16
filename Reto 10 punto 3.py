#Hacer un algoritmo que deje al final de un arreglo de números todos los ceros que aparezcan en dicho arreglo.
def ceros_al_final (num: int) -> list:
    for i in range (n):
        num = int(input("Insertar números del arreglo: "))
        lista.append(num)
    print("Lista original: " + str(lista))
    
    for i in lista:
        if i == 0:
            lista.remove(i)
            lista.append(i)
    print("Lista con ceros al final: "+str(lista))

if __name__ == "__main__":
    lista = []
    lista_de_ceros = []
    n = int(input("Inserte la cantidad de elementos para el arreglo: "))
    num = 0
    ceros_al_final (num)