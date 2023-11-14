"""
Ejercicio 3.1.1
Escribir un programa que almacene las asignaturas de un curso (por ejemplo Matemáticas, Física, Química, Historia y Lengua) en una lista y la muestre por pantalla.

"""
def mostrar_lista (asignaturas):
    print (" - ".join(asignaturas))


def main ():
    print ("Ejercicio 3.1.1")
    print ("----------------\n")

    asignaturas = ("Matemáticas", "Física", "Química", "Historia", "Lengua")
    mostrar_lista(asignaturas)
    print ()


if __name__ == "__main__":
    main()