import os
import time
from icrawler.builtin import BingImageCrawler

# Leer ingredientes desde archivo
def leer_ingredientes(archivo):
    with open(archivo, "r", encoding="utf-8") as f:
        return [linea.strip() for linea in f if linea.strip()]

# Descargar una sola imagen y renombrarla
def descargar_imagen(nombre, carpeta_destino):
    nombre_archivo = nombre.replace(",", "").replace(" ", "_").replace("(", "").replace(")", "") + ".jpg"
    ruta_final = os.path.join(carpeta_destino, nombre_archivo)

    if os.path.exists(ruta_final):
        print(f"⏭️ Ya existe: {nombre_archivo}")
        return

    # Carpeta temporal
    temp_dir = os.path.join(carpeta_destino, "temp")
    os.makedirs(temp_dir, exist_ok=True)

    crawler = BingImageCrawler(storage={"root_dir": temp_dir})
    crawler.crawl(keyword=nombre, max_num=1)

    # Buscar la imagen descargada
    archivos = os.listdir(temp_dir)
    if archivos:
        original = os.path.join(temp_dir, archivos[0])
        os.rename(original, ruta_final)
        print(f"✅ Descargado y renombrado: {ruta_final}")
    else:
        print(f"❌ No se encontró imagen para: {nombre}")

    # Limpiar carpeta temporal
    for f in os.listdir(temp_dir):
        os.remove(os.path.join(temp_dir, f))

# Configuración
CARPETA_IMAGENES = "imagenes_ingredientes"
os.makedirs(CARPETA_IMAGENES, exist_ok=True)

ingredientes = leer_ingredientes("Ingredientes.txt")

for ingrediente in ingredientes:
    print(f"🔍 Buscando imagen para: {ingrediente}")
    try:
        descargar_imagen(ingrediente, CARPETA_IMAGENES)
        time.sleep(1)  # Pausa breve para evitar bloqueos
    except Exception as e:
        print(f"❌ Error con {ingrediente}: {e}")

print("\n🎉 Descarga completa.")
