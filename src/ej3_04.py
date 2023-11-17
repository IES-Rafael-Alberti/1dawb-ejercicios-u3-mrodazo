"""
Ejercicio 3.1.4
Escribir un programa que pregunte al usuario los números ganadores de la lotería primitiva, los almacene en una lista y los muestre por pantalla ordenados de menor a mayor.

Primitiva: 6 números del 1 al 49 y 1 reintegro del 0 al 9.
Los números tienen que ser únicos.


Creamos primero una lista y después se pasa a Tupla con .sort
"""
#Con esta función pedimos los números de la primitiva, comprobando que se cumple 1-49
def comprobar_numeros_primitiva(num_p: int) -> tuple:
    error = True
    while error:
        try:
            num_p = int(input("Introduzca los números elegidos de la primitiva: "))
            error = False
            if not (1<= num_p <= 49):
                raise ValueError
        except ValueError:
            print("**Error** Introduzca un número entre el 1 y el 49: ")
    return num_p

#Con esta función pedimos el reintegro, comprobando que se cumple 0-9
def pedir_reintegro(num_r: int) -> int:
    error = True
    while error:
        try:
            num_r = int(input("Introduzca el reintegro: "))
            error = False
            if not (0<= num_r <= 9):
                raise ValueError
        except ValueError:
            print("**Error** Introduzca un número entre el 0 y el 9: ")
    return num_r


def crear_primitiva (num_p) -> tuple:
    print ("Introduzca los números elegidos: ")
    primitiva = list(f"{6}. ", comprobar_numeros_primitiva((i + 1) for i in range (6))) 

    


def main ():
    




if __name__ == "__main__":
    main()