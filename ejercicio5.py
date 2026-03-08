def validar_nombre():

    while True:
        nombre = input("Ingrese nombre: ")

        if len(nombre) >= 3:
            return nombre
        else:
            print("El nombre debe tener mínimo 3 caracteres")


def validar_edad():

    while True:
        edad = int(input("Ingrese edad: "))

        if 0 <= edad <= 120:
            return edad
        else:
            print("Edad inválida")


def validar_correo():

    while True:
        correo = input("Ingrese correo: ")

        if "@" in correo and (".com" in correo or "edu.co" in correo):
            return correo
        else:
            print("Correo inválido")


def main():

    usuarios = []

    nombre = validar_nombre()
    edad = validar_edad()
    correo = validar_correo()

    usuario = [nombre, edad, correo]
    usuarios.append(usuario)

    print("\nUsuario guardado:")
    print(usuarios)


if __name__ == "__main__":
    main()