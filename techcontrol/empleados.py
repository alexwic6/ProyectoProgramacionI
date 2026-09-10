legajos_empleados = []
nombres_empleados = []


#   FUNCIÓN REGISTRAR EMPLEADO

def registrar_empleado(legajo, nombre):
    if legajo == "" or legajo == None:
        print("El legajo no puede estar vacío.")
        return
    
    if legajo in legajos_empleados:
        print(f"El legajo '{legajo}' ya existe.")
        return
    
    if nombre == "" or nombre == None:
        print("El nombre no puede estar vacío")
        return

    legajos_empleados.append(legajo)
    nombres_empleados.append(nombre)




#   FUNCIÓN BUSCAR EMPLEADO POR LEGAJO

def buscar_empleado_por_legajo(legajo_buscado):
    for i in range(len(legajos_empleados)):
        if legajos_empleados[i] == legajo_buscado:
            return i