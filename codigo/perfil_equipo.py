#Punto 8 - Orientador 3
def contiene_digitos(texto):
    for caracter in texto:
        if caracter.isdigit():
            return True
    return False


def generar_sigla(nombre):
    palabras = nombre.split()
    sigla = ""

    for palabra in palabras:
        sigla += palabra[0].upper()

    return sigla


def main():
    equipo = input("Nombre del equipo: ")
    comision = input("Comisión: ")

    cantidad = int(input("Cantidad de integrantes: "))

    integrantes = []

    for i in range(cantidad):
        nombre = input(f"Nombre del integrante {i + 1}: ")
        rol = input(f"Rol de {nombre}: ")

        integrantes.append({
            "nombre": nombre.title(),
            "rol": rol.title()
        })

    equipo_mayusculas = equipo.upper()
    cantidad_caracteres = len(equipo)
    sigla = generar_sigla(equipo)
    tiene_digitos = contiene_digitos(equipo)

    print("PERFIL DEL EQUIPO")
    print(f"Nombre del equipo: {equipo_mayusculas}")
    print(f"Cantidad de caracteres: {cantidad_caracteres}")
    print(f"Sigla: {sigla}")
    print(f"Contiene dígitos?: {tiene_digitos}")
    print(f"Comisión: {comision}")

    print("\nIntegrantes:")

    for integrante in integrantes:
        print(f"- {integrante['nombre']} | Rol: {integrante['rol']}")


main()