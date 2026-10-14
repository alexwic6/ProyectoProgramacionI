from equipos import (
    registrar_equipo,
    buscar_equipo_por_codigo,
    asignar_equipo,
    devolver_equipo,
    cambiar_estado_equipo
)

from matriz import (
    crear_matriz
)

from empleados import (
    registrar_empleado,
    buscar_empleado_por_legajo
)

from informes import (
    informe_inventario_general,
    informe_matriz_resumen,
    informe_equipos_por_empleado,
    informe_indicadores_generales,
    informe_equipos_inoperativos,
    informe_ranking_empleados_utilizacion
)


def mostrar_menu():
    print("\n========================================")
    print("SISTEMA TECHCONTROL - MENÚ")
    print("========================================")
    print("1. Registrar nuevo equipo")
    print("2. Registrar nuevo empleado")
    print("3. Asignar equipo a empleado")
    print("4. Registrar devolución de equipo")
    print("5. Cambiar estado de un equipo")
    print("6. Buscar equipo por código")
    print("7. Buscar empleado y consultar sus equipos")
    print("8. Mostrar inventario general")
    print("9. Generar estadísticas e informes finales")
    print("10. Salir del sistema")
    print("========================================")


def submenu_informes(
        matriz, codigos_equipos, tipos_equipos, marcas_equipos, modelos_equipos,
        estados_equipos, legajos_asignados, legajos_empleados, nombres_empleados):

    print("\n--- ESTADÍSTICAS E INFORMES ---")
    print("1. Inventario general")
    print("2. Matriz resumen")
    print("3. Equipos por empleado")
    print("4. Indicadores generales")
    print("5. Equipos en reparación / fuera de servicio")
    print("6. Ranking de empleados")

    opcion = input("Elegir un informe: ")

    if opcion == "1":
        informe_inventario_general(codigos_equipos, tipos_equipos, marcas_equipos,
                                   modelos_equipos, estados_equipos, legajos_asignados)
    elif opcion == "2":
        informe_matriz_resumen(matriz)
    elif opcion == "3":
        legajo = input("Ingresar el legajo del empleado: ")
        informe_equipos_por_empleado(legajo, nombres_empleados, legajos_empleados,
                                     legajos_asignados, codigos_equipos, tipos_equipos,
                                     marcas_equipos, modelos_equipos, estados_equipos)
    elif opcion == "4":
        informe_indicadores_generales(matriz, estados_equipos, nombres_empleados,
                                      legajos_empleados, legajos_asignados)
    elif opcion == "5":
        informe_equipos_inoperativos(codigos_equipos, tipos_equipos, marcas_equipos,
                                     modelos_equipos, estados_equipos)
    elif opcion == "6":
        informe_ranking_empleados_utilizacion(nombres_empleados, legajos_empleados,
                                              legajos_asignados)
    else:
        print("Opción inválida.")


def iniciar_sistema():

    # Datos de empleados
    legajos_empleados = []
    nombres_empleados = []

    # Datos de equipos
    codigos_equipos = []
    tipos_equipos = []
    marcas_equipos = []
    modelos_equipos = []
    estados_equipos = []
    legajos_asignados = []

    # Matriz de resumen
    matriz = crear_matriz()

    programa_activo = True

    while programa_activo:

        mostrar_menu()
        opcion = input("Elegir una opción: ")

        if opcion == "1":
            codigo = input("Código (FORMATO: XX-000): ")
            tipo = input("Tipo (Computadora/Monitor/Celular): ")
            marca = input("Marca: ")
            modelo = input("Modelo: ")
            registrar_equipo(matriz, codigos_equipos, tipos_equipos, marcas_equipos,
                             modelos_equipos, estados_equipos, legajos_asignados,
                             codigo, tipo, marca, modelo)

        elif opcion == "2":
            legajo = input("Legajo: ")
            nombre = input("Nombre completo: ")
            registrar_empleado(legajos_empleados, nombres_empleados, legajo, nombre)

        elif opcion == "3":
            codigo = input("Código del equipo: ")
            legajo = input("Legajo del empleado: ")
            asignar_equipo(matriz, codigos_equipos, tipos_equipos, estados_equipos,
                           legajos_asignados, legajos_empleados,
                           codigo, legajo)

        elif opcion == "4":
            codigo = input("Código del equipo a devolver: ")
            devolver_equipo(matriz, codigos_equipos, tipos_equipos, estados_equipos,
                            legajos_asignados,
                            codigo)

        elif opcion == "5":
            codigo = input("Código del equipo: ")
            print("1. Disponible")
            print("2. En reparación")
            print("3. Fuera de servicio")
            estado_nuevo = input("Elegí el nuevo estado (número o texto): ")
            cambiar_estado_equipo(matriz, codigos_equipos, tipos_equipos, estados_equipos,
                                  codigo, estado_nuevo)

        elif opcion == "6":
            codigo = input("Código del equipo a buscar: ")
            buscar_equipo_por_codigo(codigos_equipos, tipos_equipos, marcas_equipos,
                                     modelos_equipos, estados_equipos, legajos_asignados,
                                     legajos_empleados, nombres_empleados,
                                     codigo)

        elif opcion == "7":
            legajo = input("Legajo del empleado a buscar: ")
            posicion = buscar_empleado_por_legajo(legajos_empleados, legajo)

            if posicion is None:
                print("Error: no existe un empleado con ese legajo.")
            else:
                informe_equipos_por_empleado(legajo, nombres_empleados, legajos_empleados,
                                             legajos_asignados, codigos_equipos, tipos_equipos,
                                             marcas_equipos, modelos_equipos, estados_equipos)

        elif opcion == "8":
            informe_inventario_general(codigos_equipos, tipos_equipos, marcas_equipos,
                                       modelos_equipos, estados_equipos, legajos_asignados)

        elif opcion == "9":
            submenu_informes(matriz, codigos_equipos, tipos_equipos, marcas_equipos,
                             modelos_equipos, estados_equipos, legajos_asignados,
                             legajos_empleados, nombres_empleados)

        elif opcion == "10":
            print("Cerrando el sistema...")
            programa_activo = False

        else:
            print("Opción inválida, intentá de nuevo.")


if __name__ == "__main__":
    iniciar_sistema()