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


def normalizar_nombre(nombre):
    return nombre.title()


def convertir_mayusculas(texto):
    return texto.upper()


def cantidad_caracteres(texto):
    return len(texto)