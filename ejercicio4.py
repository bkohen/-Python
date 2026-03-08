def es_primo(numero):

    if numero <= 1:
        return False

    for i in range(2, numero):
        if numero % i == 0:
            return False

    return True


def calcular_factorial(numero):

    resultado = 1
    for i in range(1, numero + 1):
        resultado *= i

    return resultado


def contar_vocales(texto):

    vocales = {"a":0,"e":0,"i":0,"o":0,"u":0}

    texto = texto.lower()

    for letra in texto:
        if letra in vocales:
            vocales[letra] += 1

    return vocales


def main():

    print("1. Número primo")
    print("2. Factorial")
    print("3. Contar vocales")

    opcion = input("Seleccione opción: ")

    if opcion == "1":

        numero = int(input("Ingrese número: "))

        if es_primo(numero):
            print("El número es primo")
        else:
            print("El número no es primo")

    elif opcion == "2":

        numero = int(input("Ingrese número: "))
        print("Factorial:", calcular_factorial(numero))

    elif opcion == "3":

        texto = input("Ingrese texto: ")
        resultado = contar_vocales(texto)

        for vocal in resultado:
            print(vocal, ":", resultado[vocal])

    else:
        print("Opción inválida")


if __name__ == "__main__":
    main()