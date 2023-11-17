"""
Ejercicio 3.1.12¶
Escribir un programa que almacene las matrices A=(123456) y B=(−100111) en una lista y muestre por pantalla su producto. Nota: Para representar matrices mediante listas usar listas anidadas, representando cada vector fila en una lista.

A:
    1 2
    3 4
    5 6
B:
    -1 0
     0 1
     1 1
El restultado tiene que ser:
    -1 0
     0 4
     5 6

"""

def producto_fila (vector_1: tuple, vector_2: tuple) -> tuple:
    return tuple(vector_1[i])#Mirar foto


def main():

    #para definir las tuplas:
    matriz_1 = ((1,2), (3,4), (5,6))
    matriz_2 = ((-1,0), (0,1), (1,1))
    #Creamos lista vacía
    matriz_final = []

    for fila in range (3):#filas
        #le añadimos una lista para que tenga una lista dentro de la lista
        matriz_final.append(list()) 
        for columna in range (2): #columnas
            matriz_final[fila].append(matriz_1[fila][columna] * matriz_2[fila][columna])
            
    print(matriz_final)

if __name__ == "__main__":
    main()