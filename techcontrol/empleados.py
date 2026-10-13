#   FUNCIÓN REGISTRAR EMPLEADO

def registrar_empleado(lista_legajos_empleados, lista_nombres_empleados, legajo, nombre):

    legajo = legajo.strip()
    nombre = nombre.strip()

    if legajo == "":
        print("El legajo no puede estar vacío.")
        return

    if legajo in lista_legajos_empleados:
        print(f"El legajo '{legajo}' ya existe.")
        return

    if nombre == "":
        print("El nombre no puede estar vacío.")
        return

    lista_legajos_empleados.append(legajo)
    lista_nombres_empleados.append(nombre)
    print("Empleado registrado correctamente.")


#   FUNCIÓN BUSCAR EMPLEADO POR LEGAJO

def buscar_empleado_por_legajo(lista_legajos_empleados, legajo_buscado):

    legajo_buscado = legajo_buscado.strip()
    posicion = None

    for i in range(len(lista_legajos_empleados)):
        if lista_legajos_empleados[i] == legajo_buscado:
            posicion = i

    return posicion