import os

def leer_ingredientes(archivo):
    with open(archivo, "r", encoding="utf-8") as f:
        return [linea.strip() for linea in f if linea.strip()]

def normalizar_nombre(nombre):
    return nombre.replace(",", "").replace(" ", "_").replace("(", "").replace(")", "") + ".jpg"

# Rutas
archivo_ingredientes = "Ingredientes.txt"
carpeta_imagenes = "imagenes_ingredientes"

# Leer ingredientes
ingredientes = leer_ingredientes(archivo_ingredientes)

# Obtener nombres de archivos descargados
imagenes_existentes = set(os.listdir(carpeta_imagenes))

# Comparar
faltantes = []

for ingrediente in ingredientes:
    nombre_imagen = normalizar_nombre(ingrediente)
    if nombre_imagen not in imagenes_existentes:
        faltantes.append(ingrediente)

# Mostrar resultados
if faltantes:
    print("❌ Ingredientes sin imagen:\n")
    for f in faltantes:
        print("-", f)
else:
    print("✅ Todos los ingredientes tienen imagen.")

# Opcional: guardar en archivo
with open("imagenes_faltantes.txt", "w", encoding="utf-8") as f:
    for item in faltantes:
        f.write(item + "\n")
