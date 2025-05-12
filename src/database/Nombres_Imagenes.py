import os

# Carpeta donde están las imágenes
CARPETA_IMAGENES = "imagenes_ingredientes"
ARCHIVO_SALIDA = "nombres_imagenes.txt"

# Obtener lista de archivos en la carpeta
nombres_archivos = [
    archivo for archivo in os.listdir(CARPETA_IMAGENES)
    if os.path.isfile(os.path.join(CARPETA_IMAGENES, archivo))
]

# Guardar en archivo de texto
with open(ARCHIVO_SALIDA, "w", encoding="utf-8") as f:
    for nombre in nombres_archivos:
        f.write(nombre + "\n")

print(f"✅ Archivo generado: {ARCHIVO_SALIDA} con {len(nombres_archivos)} nombres.")
