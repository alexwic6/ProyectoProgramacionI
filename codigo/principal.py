from perfil_equipo import (
    contiene_digitos,
    generar_sigla,
    normalizar_nombre,
    convertir_mayusculas,
    cantidad_caracteres
)


def main():
    equipo = input("Nombre del equipo: ")
    comision = input("Comisión: ")

    cantidad = int(input("Cantidad de integrantes: "))

    integrantes = []

    for i in range(cantidad):
        nombre = input(f"Nombre del integrante {i + 1}: ")
        rol = input(f"Rol de {nombre}: ")

        integrantes.append({
            "nombre": normalizar_nombre(nombre),
            "rol": normalizar_nombre(rol)
        })

    equipo = normalizar_nombre(equipo)

    equipo_mayusculas = convertir_mayusculas(equipo)
    cantidad_equipo = cantidad_caracteres(equipo)
    sigla = generar_sigla(equipo)
    tiene_digitos = contiene_digitos(equipo)

    print("\nPERFIL DEL EQUIPO")
    print(f"Nombre del equipo: {equipo_mayusculas}")
    print(f"Cantidad de caracteres: {cantidad_equipo}")
    print(f"Sigla: {sigla}")
    print(f"Contiene dígitos?: {tiene_digitos}")
    print(f"Comisión: {comision}")

    print("\nIntegrantes:")

    for integrante in integrantes:
        print(f"- {integrante['nombre']} | Rol: {integrante['rol']}")


main()