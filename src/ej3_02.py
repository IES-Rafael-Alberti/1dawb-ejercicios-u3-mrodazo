"""
Ejercicio 3.1.2
Escribir un programa que almacene las asignaturas de un curso (por ejemplo Matemáticas, Física, Química, Historia y Lengua) en una lista y la muestre por pantalla el mensaje Yo estudio <asignatura>, donde <asignatura> sobre cada una de las asignaturas de la lista.

"""

def pedir_numero_asignaturas() -> int:
    error = True
    while error:
        try:
            num = int(input("Introduzca el número de asignaturas: "))
            if not (1<= num <= 10):
                raise ValueError
            error = False
        except ValueError:
            print ("Error")
    return num

def pedir_asignatura (indice: int) -> str:
    return input (f"{indice}. ")


def crear_asignaturas (num_asignaturas) -> tuple:
    print ("Introduzca sus asignaturas: ")
    asignaturas = tuple(pedir_asignatura(i + 1) for i in range (num_asignaturas))

    return asignaturas


def mostrar_lista(asignaturas):
    for asignatura in asignaturas:
        print (f"Yo estudio {asignatura}")


def main ():
    print ("Ejercicio 3.1.2")
    print ("----------------\n")

    num_asignaturas = pedir_numero_asignaturas()
    asignaturas = crear_asignaturas(num_asignaturas)
    mostrar_lista(asignaturas)
    print ()


if __name__ == "__main__":
    main()