

def calcular_promedio(notas):
    return sum(notas.values()) / len(notas)


def analizar_estudiante(estudiante):
    notas = estudiante["notas"]

    promedio = calcular_promedio(notas)
    mejor_materia = max(notas, key=notas.get)
    peor_materia = min(notas, key=notas.get)

    print("\n--- Información del Estudiante ---")
    print("Nombre:", estudiante["nombre"])
    print("Edad:", estudiante["edad"])
    print("Estado:", estudiante["estado"])
    print("Promedio:", round(promedio, 2))
    print("Mejor materia:", mejor_materia, "-", notas[mejor_materia])
    print("Peor materia:", peor_materia, "-", notas[peor_materia])

    if promedio >= 3.0:
        print("Aprueba")
    else:
        print("No aprueba")


def main():

    nombre = input("Nombre del estudiante: ")
    edad = int(input("Edad: "))
    estado = input("Estado (activo/inactivo): ")

    materias = []
    notas = {}

    cantidad = int(input("Cantidad de materias (mínimo 3): "))

    while cantidad < 3:
        print("Debe ingresar al menos 3 materias.")
        cantidad = int(input("Cantidad de materias: "))

    for i in range(cantidad):
        materia = input(f"Materia {i+1}: ")

        nota = float(input("Nota (0.0 a 5.0): "))
        while nota < 0 or nota > 5:
            print("Nota inválida")
            nota = float(input("Nota (0.0 a 5.0): "))

        materias.append(materia)
        notas[materia] = nota

    estudiante = {
        "nombre": nombre,
        "edad": edad,
        "estado": estado,
        "materias": materias,
        "notas": notas
    }

    analizar_estudiante(estudiante)


if __name__ == "__main__":
    main()