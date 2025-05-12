import pandas as pd
from pymongo import MongoClient

# Leer el archivo Excel
archivo_excel = "ingredientes_imagenes.xlsx"  # Cambia por la ruta real
df = pd.read_excel(archivo_excel)

# Conectar a MongoDB
cliente = MongoClient("mongodb://admin:Password1@127.0.0.1:27017/admin")  # Cambia si es necesario
db = cliente["tudespensa"]
coleccion = db["ingredientes"]

# Recorrer todas las filas
for index, fila in df.iterrows():
    nombre_ingrediente = fila[0].strip()
    nombre_imagen = fila[1].strip()

    resultado = coleccion.update_one(
        {"nombre": nombre_ingrediente},
        {"$set": {"imagen": nombre_imagen}}
    )

    if resultado.matched_count:
        print(f"✅ Actualizado: {nombre_ingrediente} -> {nombre_imagen}")
    else:
        print(f"❌ No encontrado en DB: {nombre_ingrediente}")
