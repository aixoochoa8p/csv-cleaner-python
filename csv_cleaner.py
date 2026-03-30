import csv

def limpiar_csv(archivo_entrada, archivo_salida, columna_orden):
    filas_unicas = set()
    datos_limpios = []

    # Leer y normalizar datos
    with open(archivo_entrada, "r", encoding="utf-8") as f:
        lector = csv.DictReader(f)
        for fila in lector:
            # Normalizar texto: quitar espacios y pasar a minúsculas
            fila_normalizada = {k: v.strip().lower() for k, v in fila.items()}

            # Convertir fila a tupla para detectar duplicados
            fila_tupla = tuple(fila_normalizada.items())

            if fila_tupla not in filas_unicas:
                filas_unicas.add(fila_tupla)
                datos_limpios.append(fila_normalizada)

    # Ordenar por la columna indicada
    datos_limpios.sort(key=lambda x: x[columna_orden])

    # Guardar archivo limpio
    with open(archivo_salida, "w", newline="", encoding="utf-8") as f:
        escritor = csv.DictWriter(f, fieldnames=datos_limpios[0].keys())
        escritor.writeheader()
        escritor.writerows(datos_limpios)

    print(f"Archivo limpio generado: {archivo_salida}")
