import csv

def leer_archivo(archivo):
    datos = {}

    arch = open(archivo, "r", encoding="utf-8")

    lector = csv.DictReader(arch)

    for columna in lector.fieldnames:
        datos[columna] = []

    for fila in lector:
        for columna in datos:
            datos[columna].append(fila[columna])

    arch.close()

    return datos