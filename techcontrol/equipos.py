from empleados import (
    legajos_empleados, 
    registrar_empleado
)


from matriz import (
    TIPOS,
    ESTADOS,
    actualizar_matriz,
    matriz
)

codigos_equipos = []
tipos_equipos = []
marcas_equipos = []
modelos_equipos = []
estados_equipos = []
legajos_asignados = []

#  REGISTRAR EQUIPO

def registrar_equipo(codigo, tipo, marca, modelo):

    tipo = tipo.capitalize()

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





#  ASIGNAR EQUIPO

def asignar_equipo(codigo, legajo):

    if legajo not in legajos_empleados:

        print("Error: no existe un empleado con ese legajo.")

        return

    if codigo not in codigos_equipos:

        print("Error: no existe un equipo con ese código.")

        return

    posicion = codigos_equipos.index(codigo)

    if estados_equipos[posicion] != "Disponible":

        print("Error: el equipo no está Disponible, no se puede asignar.")

        return

    tipo = tipos_equipos[posicion]

    estados_equipos[posicion] = "Asignado"

    legajos_asignados[posicion] = legajo

    actualizar_matriz(tipo, "Disponible", "Asignado")

    print("Equipo asignado correctamente.")


#  DEVOLVER EQUIPO

def devolver_equipo(codigo):

    if codigo not in codigos_equipos:

        print("Error: no existe un equipo con ese código.")

        return

    posicion = codigos_equipos.index(codigo)

    if estados_equipos[posicion] != "Asignado":

        print("Error: el equipo no está Asignado, no se puede devolver.")

        return

    if legajos_asignados[posicion] == "":

        print("Error: el equipo no tiene un legajo asociado.")

        return

    tipo = tipos_equipos[posicion]

    estados_equipos[posicion] = "Disponible"

    legajos_asignados[posicion] = ""

    actualizar_matriz(tipo, "Asignado", "Disponible")

    print("Equipo devuelto correctamente.")


#  CAMBIAR ESTADO DE UN EQUIPO

def cambiar_estado_equipo(codigo, estado_nuevo):

    estado_nuevo = estado_nuevo.capitalize()

    if codigo not in codigos_equipos:

        print("Error: no existe un equipo con ese código.")

        return

    if estado_nuevo not in ESTADOS:

        print("Error: el estado ingresado no es válido.")

        return

    posicion = codigos_equipos.index(codigo)

    estado_actual = estados_equipos[posicion]

    transiciones_validas = [
        ("Disponible", "En reparación"),
        ("En reparación", "Disponible"),
        ("En reparación", "Fuera de servicio"),
        ("Disponible", "Fuera de servicio")
    ]

    if (estado_actual, estado_nuevo) not in transiciones_validas:

        print(f"Error: no se puede pasar de '{estado_actual}' a '{estado_nuevo}'.")

        return

    tipo = tipos_equipos[posicion]

    estados_equipos[posicion] = estado_nuevo

    actualizar_matriz(tipo, estado_actual, estado_nuevo)

    print("Estado del equipo actualizado correctamente.")