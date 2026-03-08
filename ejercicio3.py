def main():

    inicio = int(input("Ingrese número inicial: "))
    iteraciones = int(input("Número de iteraciones: "))

    if iteraciones < 0:
        print("Error: el número de iteraciones no puede ser negativo")
        return

    fibonacci = [inicio]

    a = 0
    b = inicio

    for i in range(iteraciones - 1):
        siguiente = a + b
        fibonacci.append(siguiente)
        a = b
        b = siguiente

    print("\nSerie generada:", fibonacci)
    print("Cantidad de términos:", len(fibonacci))
    print("Último valor:", fibonacci[-1])


if __name__ == "__main__":
    main() 