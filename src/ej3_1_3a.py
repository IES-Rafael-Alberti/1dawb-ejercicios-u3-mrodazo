"""
Ejercicio 3.1.3
Escribir un programa que almacene las asignaturas de un curso (por ejemplo Matemáticas, Física, Química, Historia y Lengua) en una lista, pregunte al usuario la nota que ha sacado en cada asignatura, y después las muestre por pantalla con el mensaje En <asignatura> has sacado <nota> donde <asignatura> es cada una de las asignaturas de la lista y <nota> cada una de las correspondientes notas introducidas por el usuario.

Se usan 2 listas, una para Asignaturas y otra para Notas

"""

from ej3_1_2 import pedir_numero_asignaturas, crear_asignaturas, mostrar_lista

def pedir_notas (num_asignaturas: int) -> list:
    notas = []
    error = True
    while error:
        for i in range (0, num_asignaturas):
            try:
                notas[i] = int(input("Introduzca las notas de las asignaturas: "))
                if not (0<= i <= 10):
                    raise ValueError
                error = False
            except ValueError:
                print ("Error")



def main ():
    print ("Ejercicio 3.1.3")
    print ("----------------\n")

    num_asignaturas = pedir_numero_asignaturas()
    asignaturas = crear_asignaturas(num_asignaturas)
    notas = pedir_notas (num_asignaturas)
    mostrar_lista(asignaturas)
    print ()

if __name__ == "__main__":
    main()