
def calculo(v1: int, v2: int) -> int:
    if v1 * v2 < 0:
        return 0 #Para que en lugar de devolver números negativos, devuelva 0
    else:
        return v1 * v2


def producto_vectorial (v1: tuple, v2: tuple) -> tuple:
    return tuple(calculo(v1[i] * v2[i]) for i in range (len(v1)))


def pedir_numero()-> int:
    todo_ok = False
    while not todo_ok:
        try:
            num = int (input("Introduzca los números del vector: "))
            todo_ok = True
        except Exception as e:
            print(f"*Error* {e}")


def pedir_vector(total = 3) -> tuple: #Si no decimos cuál es la long del vector, va a ser 3
    return tuple(pedir_numero() for _ in range(total))


def main ():
    v1 = pedir_vector()
    v2 = pedir_vector()

    v3 = producto_vectorial(v1, v2)

    print(v3)

    #v3 = (-2, 8, 4) este es el resultado que debería dar



if __name__ == "__main__":
    main()