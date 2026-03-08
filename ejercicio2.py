def main():

    valor_base = float(input("Ingrese el valor monetario: "))

    impuesto = valor_base * 0.19

    if valor_base >= 200000:
        descuento = valor_base * 0.10
    else:
        descuento = 0

    total_final = valor_base + impuesto - descuento

    print("\nResultados")
    print("Valor base:", valor_base)
    print("Impuesto (19%):", impuesto)
    print("Descuento:", descuento)
    print("Total final:", total_final)


if __name__ == "__main__":
    main()