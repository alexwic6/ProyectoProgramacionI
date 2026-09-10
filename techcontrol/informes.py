from equipos import (
    codigos_equipos,
    tipos_equipos,
    marcas_equipos,
    modelos_equipos,
    estados_equipos,
    legajos_asignados
)

from empleados import (
    legajos_empleados,
    nombres_empleados
)

from matriz import (
    matriz,
    total_general,
    total_por_estado,
    total_por_tipo,
    TIPOS,
    ESTADOS
)







def contar_por_estado(estado):
    contador = 0

    for estado_equipo in estados_equipos:
        if estado_equipo == estado:
            contador += 1

    return contador




def tipo_mas_asignado():
    columna_asignado = 1
    maximo = -1
    tipos_maximos = []

    for i in range(len(TIPOS)):
        cantidad = matriz[i][columna_asignado]

        if cantidad > maximo:
            maximo = cantidad
            tipos_maximos = [TIPOS[i]]

        elif cantidad == maximo:
            tipos_maximos.append(TIPOS[i])

    return tipos_maximos, maximo


def empleado_mas_asignado():
    maximo = -1
    empleados_maximos = []

    for i in range(len(legajos_empleados)):
        legajo = legajos_empleados[i]
        cantidad = 0

        for legajo_asignado in legajos_asignados:
            if legajo_asignado == legajo:
                cantidad += 1

        if cantidad > maximo:
            maximo = cantidad
            empleados_maximos = [nombres_empleados[i]]

        elif cantidad == maximo:
            empleados_maximos.append(nombres_empleados[i])

    return empleados_maximos, maximo



def porcentaje_utilizacion():
    total_equipos = total_general()
    total_asignados = contar_por_estado("Asignado")

    if total_equipos == 0:
        return 0

    porcentaje = (total_asignados / total_equipos) * 100

    return porcentaje


def ranking_empleados_utilizacion():
    ranking = []

    for i in range(len(legajos_empleados)):
        legajo = legajos_empleados[i]
        nombre = nombres_empleados[i]
        cantidad = 0

        for legajo_asignado in legajos_asignados:
            if legajo_asignado == legajo:
                cantidad += 1

        ranking.append((nombre, cantidad))

    ranking = sorted(ranking, key=lambda empleado: empleado[1], reverse=True)

    return ranking


def top_3_empleados():
    ranking = ranking_empleados_utilizacion()

    return ranking[0:3]


def equipos_en_reparacion():
    equipos = [
        codigos_equipos[i]
        for i in range(len(codigos_equipos))
        if estados_equipos[i] == "En reparación"
    ]

    return equipos



def alerta_baja_disponibilidad():
    tipos_baja_disponibilidad = []
    columna_disponible = 0

    for i in range(len(TIPOS)):
        cantidad_disponible = matriz[i][columna_disponible]

        if cantidad_disponible < 2:
            tipos_baja_disponibilidad.append(TIPOS[i])

    return tipos_baja_disponibilidad



def informe_inventario_general():
    print("\nINVENTARIO GENERAL DE EQUIPOS")

    if len(codigos_equipos) == 0:
        print("No hay equipos registrados.")
        return

    for i in range(len(codigos_equipos)):
        print("\nCódigo:", codigos_equipos[i])
        print("Tipo:", tipos_equipos[i])
        print("Marca:", marcas_equipos[i])
        print("Modelo:", modelos_equipos[i])
        print("Estado:", estados_equipos[i])

        if legajos_asignados[i] == "":
            print("Empleado: Sin empleado asignado")
        else:
            print("Legajo asignado:", legajos_asignados[i])


def informe_matriz_resumen():
    print("\nRESUMEN")

    print("Tipo | Disponible | Asignado | En reparación | Fuera de servicio | Total")

    for i in range(len(TIPOS)):
        total_tipo = total_por_tipo(TIPOS[i])

        print(
            TIPOS[i],
            "|",
            matriz[i][0],
            "|",
            matriz[i][1],
            "|",
            matriz[i][2],
            "|",
            matriz[i][3],
            "|",
            total_tipo
        )



    print("\nTOTALES POR ESTADO")

    for j in range(len(ESTADOS)):
        print(ESTADOS[j], ":", total_por_estado(ESTADOS[j]))

    print("\nTotal general:", total_general())


def informe_equipos_por_empleado(legajo):
    encontrado = False

    for i in range(len(legajos_empleados)):
        if legajos_empleados[i] == legajo:
            encontrado = True
            nombre = nombres_empleados[i]
            break

    if encontrado == False:
        print("El empleado no existe.")
        return

    print("\nEMPLEADO:", nombre)
    print("LEGAJO:", legajo)
    print("EQUIPOS ASIGNADOS:")

    tiene_equipos = False

    for i in range(len(codigos_equipos)):
        if legajos_asignados[i] == legajo:
            tiene_equipos = True

            print("\nCódigo:", codigos_equipos[i])
            print("Tipo:", tipos_equipos[i])
            print("Marca:", marcas_equipos[i])
            print("Modelo:", modelos_equipos[i])
            print("Estado:", estados_equipos[i])

    if tiene_equipos == False:
        print("No tiene equipos asignados.")



def informe_indicadores_generales():
    print("\nINDICADORES GENERALES")

    porcentaje = porcentaje_utilizacion()

    print("Porcentaje de utilización:", porcentaje, "%")

    tipos_maximos, cantidad_tipo = tipo_mas_asignado()

    print("\nTipo/s con mayor cantidad de equipos asignados:")

    for tipo in tipos_maximos:
        print("-", tipo)

    print("Cantidad asignada:", cantidad_tipo)

    empleados_maximos, cantidad_empleado = empleado_mas_asignado()

    print("\nEmpleado/s con mayor cantidad de equipos asignados:")

    for empleado in empleados_maximos:
        print("-", empleado)

    print("Cantidad de equipos:", cantidad_empleado)

    alertas = alerta_baja_disponibilidad()

    print("\nAlertas de baja disponibilidad:")

    if len(alertas) == 0:
        print("No hay alertas.")

    else:
        for tipo in alertas:
            print("-", tipo, "tiene menos de 2 equipos disponibles")



def informe_equipos_inoperativos():
    print("\nEQUIPOS EN REPARACIÓN O FUERA DE SERVICIO")

    encontrado = False

    for i in range(len(codigos_equipos)):
        if estados_equipos[i] == "En reparación" or estados_equipos[i] == "Fuera de servicio":
            encontrado = True

            print("\nCódigo:", codigos_equipos[i])
            print("Tipo:", tipos_equipos[i])
            print("Marca:", marcas_equipos[i])
            print("Modelo:", modelos_equipos[i])
            print("Estado:", estados_equipos[i])

    if encontrado == False:
        print("No hay equipos en reparación ni fuera de servicio.")



def informe_ranking_empleados_utilizacion():
    print("\nRANKING DE EMPLEADOS")

    ranking = ranking_empleados_utilizacion()

    if len(ranking) == 0:
        print("No hay empleados registrados.")
        return

    for i in range(len(ranking)):
        print(
            i + 1,
            "-",
            ranking[i][0],
            "-",
            ranking[i][1],
            "equipo/s"
        )

    print("\nTOP 3")

    top = ranking[0:3]

    for i in range(len(top)):
        print(
            i + 1,
            "-",
            top[i][0],
            "-",
            top[i][1],
            "equipo/s"
        )

