from matriz import TIPOS, actualizar_matriz

codigos_equipos = []
tipos_equipos = []
marcas_equipos = []
modelos_equipos = []
estados_equipos = []
legajos_asignados = []

#  REGISTRAR EQUIPO

def registrar_equipo(codigo, tipo, marca, modelo):

    if codigo == "":

        print("Error: el código no puede estar vacío.")

        return

    if codigo in codigos_equipos:

        print("Error: ya existe un equipo con ese código.")

        return

    if tipo not in TIPOS:

        print("Error: el tipo de equipo no es válido.")

        return

    if marca == "":

        print("Error: la marca no puede estar vacía.")

        return

    if modelo == "":

        print("Error: el modelo no puede estar vacío.")

        return

    codigos_equipos.append(codigo)

    tipos_equipos.append(tipo)

    marcas_equipos.append(marca)

    modelos_equipos.append(modelo)

    estados_equipos.append("Disponible")

    legajos_asignados.append("")

    actualizar_matriz(tipo, None, "Disponible")

    print("Equipo registrado correctamente.")

#  BUSCAR EQUIPO POR CÓDIGO

def buscar_equipo_por_codigo(codigo):

    if codigo not in codigos_equipos:

        print("Error: no existe un equipo con ese código.")

        return -1

    posicion = codigos_equipos.index(codigo)

    print("Equipo encontrado:")

    print("Código:", codigo)

    print("Tipo:", tipos_equipos[posicion])

    print("Marca:", marcas_equipos[posicion])

    print("Modelo:", modelos_equipos[posicion])

    print("Estado:", estados_equipos[posicion])

    if legajos_asignados[posicion] == "":

        print("Empleado: Sin empleado asignado")

    else:

        print("Legajo asignado:", legajos_asignados[posicion])

    return posicion

#  MOSTRAR INVENTARIO GENERAL

def mostrar_inventario_general():

    if len(codigos_equipos) == 0:

        print("No hay equipos registrados.")

        return

    print("          INVENTARIO GENERAL")

    for i in range(len(codigos_equipos)):

        print()

        print("Equipo", i + 1)

        print("Código:", codigos_equipos[i])

        print("Tipo:", tipos_equipos[i])

        print("Marca:", marcas_equipos[i])

        print("Modelo:", modelos_equipos[i])

        print("Estado:", estados_equipos[i])

        if legajos_asignados[i] == "":

            print("Empleado: Sin empleado asignado")

        else:

            print("Legajo asignado:", legajos_asignados[i])