"""
Ejercicio 3.1.3
Escribir un programa que almacene las asignaturas de un curso (por ejemplo Matemáticas, Física, Química, Historia y Lengua) en una lista, pregunte al usuario la nota que ha sacado en cada asignatura, y después las muestre por pantalla con el mensaje En <asignatura> has sacado <nota> donde <asignatura> es cada una de las asignaturas de la lista y <nota> cada una de las correspondientes notas introducidas por el usuario.

"""

from ej3_02 import mostrar_lista


def pedir_nota (asignaturas: tuple) -> str:
    error = True
    while error:
        try:
            num = int(input(f"Introduzca la nota de la asignatura: {asignaturas[0][0]}"))
            if not (0<= num <= 10):
                raise ValueError
            error = False
        except ValueError:
            print ("Error")
    return num





def main ():
    print ("Ejercicio 3.1.3")
    print ("----------------\n")

    #Se crea Tupla de listas, para poder modificar su contenido
    asignaturas = (["Matemáticas", 0], ["Física", 0], ["Química", 0])
    mostrar_lista(asignaturas)
    print ()


if __name__ == "__main__":
    main()