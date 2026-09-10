#   TUPLAS FIJAS

TIPOS = ("Computadora", "Monitor", "Celular")
ESTADOS = ("Disponible", "Asignado", "En reparación", "Fuera de servicio")

#   MATRIZ (3 filas = TIPOS, 4 columnas = ESTADOS)
#   Fila 0 = Computadora, Fila 1 = Monitor, Fila 2 = Celular
#   Columna 0 = Disponible, Columna 1 = Asignado, Columna 2 = En reparación, Columna 3 = Fuera de servicio

filas = 3
columnas = 4

matriz = [[0 for j in range(columnas)] for i in range(filas)]

#   ACTUALIZAR MATRIZ

"""
Recibe el tipo (Computadora, Monitor o Celular), le resta 1 a su estado anterior
(por si pasa de ser 'Disponible a Asignado') y suma 1 a su estado nuevo
"""

def actualizar_matriz(tipo, estado_anterior, estado_nuevo):
    fila = TIPOS.index(tipo)

    if estado_anterior is not None:
        columna_anterior = ESTADOS.index(estado_anterior)
        matriz[fila][columna_anterior] -= 1

    columna_nueva = ESTADOS.index(estado_nuevo)
    matriz[fila][columna_nueva] += 1

#   TOTAL POR TIPO

"Obtiene el índice donde se encuentra el 'tipo' recibido de parámetro y suma toda su fila"

def total_por_tipo(tipo):
    fila = TIPOS.index(tipo)
    return sum(matriz[fila])

#   OBTENER LA CANTIDAD POR ESTADO

"""
Obtiene el índice donde se encuentra el estado que se recibe como parámetro e inicializa 'total = 0'.
Luego recorre cada fila en la matriz y suma a 'total' el valor del elemento de 'fila[columna]'.
Retorna el total.
"""

def total_por_estado(estado):
    columna = ESTADOS.index(estado)
    total = 0

    for fila in matriz:
        total += fila[columna]

    return total

