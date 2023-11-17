"""
Ejercicio 3.2.1
Escribir un programa que guarde en una variable el diccionario {'Euro':'€', 'Dollar':'$', 'Yen':'¥'}, pregunte al usuario por una divisa y muestre su símbolo o un mensaje de aviso si la divisa no está en el diccionario.

"""
def clean_terminal():
    os.system("cls")

def pedir_divisa():
    divisa = input('Pedir divisa -> ')

    return divisa.title()


def main():
    clean_terminal()
    d = {'Euro':'€', 'Dollar':'$', 'Yen':'¥'}
    divisa = pedir_divisa()

    try:
        print (d[divisa])

    except ValueError:
        print ('Tu divisa no es reconocida')
"""
    if divisa in d:
        print (d[divisa])
    else:
        print ('Tu divisa no es reconocida')

"""     

if __name__ == "__main__":
    main()