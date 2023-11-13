"""
Ejercicio 3.1.2
Escribir un programa que almacene las asignaturas de un curso (por ejemplo Matemáticas, Física, Química, Historia y Lengua) en una lista y la muestre por pantalla el mensaje Yo estudio <asignatura>, donde <asignatura> sobre cada una de las asignaturas de la lista.

"""


from EjerciciosU2.Ptact2_2.ej2_2_01 import borrarConsola

def pedir_numero_asignaturas() -> int:
    error = True
    while error:
        try:
            num = int(input("Introduzca el número de asignaturas: "))
            if not (1<= num <= 10):
                raise ValueError
        except:


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
    borrarConsola()
    print ("Ejercicio 3.1.3")
    print ("----------------\n")

    num_asignaturas = pedir_numero_asignaturas()

    #Se crea Tupla de listas, para poder modificar su contenido
    asignaturas = (["Matemáticas", 0], ["Física", 0], ["Química", 0])
    mostrar_lista(asignaturas)
    print ()


if __name__ == "__main__":
    main()