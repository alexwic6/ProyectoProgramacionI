#   FUNCIÓN REGISTRAR EMPLEADO

def registrar_empleado(legajos_empleados, nombres_empleados, legajo, nombre):

    legajo = legajo.strip()
    nombre = nombre.strip()

    if legajo == "":
        print("El legajo no puede estar vacío.")
        return

    if legajo in legajos_empleados:
        print(f"El legajo '{legajo}' ya existe.")
        return

    if nombre == "":
        print("El nombre no puede estar vacío.")
        return

    legajos_empleados.append(legajo)
    nombres_empleados.append(nombre)
    print("Empleado registrado correctamente.")


#   FUNCIÓN BUSCAR EMPLEADO POR LEGAJO

def buscar_empleado_por_legajo(legajos_empleados, legajo_buscado):

    legajo_buscado = legajo_buscado.strip()
    posicion = None

    for i in range(len(legajos_empleados)):
        if legajos_empleados[i] == legajo_buscado:
            posicion = i

    return posicion