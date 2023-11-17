"""
Ejercicio 3.1.4
Escribir un programa que pregunte al usuario los números ganadores de la lotería primitiva, los almacene en una lista y los muestre por pantalla ordenados de menor a mayor.

Primitiva: 6 números del 1 al 49 y 1 reintegro del 0 al 9.
Los números tienen que ser únicos.

"""


def pedir_numero (indice: int, numeros_loteria: list):
    error = True
    try:
        numero = int(input(f"{indice}"))


def introducir_numeros_loteria()-> tuple:
    numeros_loteria = []
    for i in range (1,7):
        pedir_numero (i, numeros_loteria)

def main ():
    print ()



if __name__ == "__main__":
    main()