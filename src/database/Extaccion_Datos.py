import pandas as pd
import json
import numpy as np

# Diccionario de configuración para cada tipo de ingrediente
CONFIGURACIONES = {
    "Carnes": {
        "archivo": "src/database/Tabla/Carnes.xls",
        "columnas": "B:U",
        "n_filas": 82,
        "nombres_columnas": [
            "Alimento", "Género-especie-variedad","Columna Extra","Energía kj", "Energía_kcal", "Agua_g", "Proteínas_g",
            "Grasa Total_g", "Carbohidratos totales_g", "Cenizas_g", "Sodio_mg", "Potasio_mg", "Calcio_mg",
            "Fósforo_mg", "Hierro_mg", "Zinc_mg", "Tiamina_mg", "Rivoflavina_mg", "Niacina_mg", "Vitamina_C_mg"
        ]
    },
    "Cereales": {
        "archivo": "src/database/Tabla/Cereales.xls",
        "columnas": "B:W",
        "n_filas": 56,
        "nombres_columnas": [
            "Alimento", "Género-especie-variedad","Columna Extra", "Energía kj", "Energía_kcal", "Agua_g", "Proteínas_g",
            "Grasa Total_g", "Carbohidratos totales_g", "Carbohidratos disponibles_g", "Fibra dietética_g",
            "Cenizas_g", "Sodio_mg", "Potasio_mg", "Calcio_mg", "Fósforo_mg", "Hierro_mg", "Zinc_mg",
            "Tiamina_mg", "Rivoflavina_mg", "Niacina_mg", "Vitamina_C_mg"
        ]
    },
    "Frutas": {
        "archivo": "src/database/Tabla/Frutas.xls",
        "columnas": "B:U",
        "n_filas": 36,
        "nombres_columnas": [
            "Alimento", "Género-especie-variedad","Columna Extra", "Energía kj", "Energía_kcal", "Agua_g", "Proteínas_g",
            "Grasa Total_g", "Carbohidratos totales_g", "Cenizas_g", "Sodio_mg", "Potasio_mg", "Calcio_mg",
            "Fósforo_mg", "Hierro_mg", "Zinc_mg", "Tiamina_mg", "Rivoflavina_mg", "Niacina_mg", "Vitamina_C_mg"
        ]
    },
    "Grasas y Aceites": {
        "archivo": "src/database/Tabla/Grasas.xls",
        "columnas": "B:K",
        "n_filas": 16,
        "nombres_columnas": [
            "Alimento", "Género-especie-variedad","Columna Extra", "Energía kj", "Energía_kcal", "Agua_g",
            "Grasa Total_g", "Ac. grasos saturados_g", "Ac. grasos monoinsaturados_g", "Ac. grasos poliinsaturados_g"
        ]
    },
    "Huevos": {
        "archivo": "src/database/Tabla/Huevo.xls",
        "columnas": "B:Y",
        "n_filas": 7,
        "nombres_columnas": [
            "Alimento", "Género-especie-variedad","Columna Extra", "Energía kj", "Energía_kcal", "Agua_g", "Proteínas_g",
            "Grasa Total_g", "Carbohidratos totales_g", "Cenizas_g", "Ac. grasos saturados_g",
            "Ac. grasos monoinsaturados_g", "Ac. grasos poliinsaturados_g", "Colesterol_g", "Sodio_mg",
            "Potasio_mg", "Calcio_mg", "Fósforo_mg", "Hierro_mg", "Zinc_mg", "Tiamina_mg",
            "Rivoflavina_mg", "Niacina_mg", "Vitamina_C_mg"
        ]
    },
    "Lácteos": {
        "archivo": "src/database/Tabla/Leche.xls",
        "columnas": "B:U",
        "n_filas": 66,
        "nombres_columnas": [
            "Alimento", "Género-especie-variedad","Columna Extra", "Energía kj", "Energía_kcal", "Agua_g", "Proteínas_g",
            "Grasa Total_g", "Carbohidratos totales_g", "Cenizas_g", "Sodio_mg", "Potasio_mg", "Calcio_mg",
            "Fósforo_mg", "Hierro_mg", "Zinc_mg", "Tiamina_mg", "Rivoflavina_mg", "Niacina_mg", "Vitamina_C_mg"
        ]
    },
    "Pescados": {
        "archivo": "src/database/Tabla/Pescados.xls",
        "columnas": "B:X",
        "n_filas": 88,
        "nombres_columnas": [
            "Alimento", "Género-especie-variedad","Columna Extra", "Energía kj", "Energía_kcal", "Agua_g", "Proteínas_g",
            "Grasa Total_g", "Carbohidratos totales_g", "Cenizas_g", "Ac. grasos saturados_g",
            "Ac. grasos monoinsaturados_g", "Ac. grasos poliinsaturados_g", "Sodio_mg", "Potasio_mg",
            "Calcio_mg", "Fósforo_mg", "Hierro_mg", "Zinc_mg", "Tiamina_mg", "Rivoflavina_mg",
            "Niacina_mg", "Vitamina_C_mg"
        ]
    },
    "Vegetales": {
        "archivo": "src/database/Tabla/Vegetales.xls",
        "columnas": "B:W",
        "n_filas": 93,
        "nombres_columnas": [
            "Alimento", "Género-especie-variedad","Columna Extra", "Energía kj", "Energía_kcal", "Agua_g", "Proteínas_g",
            "Grasa Total_g", "Carbohidratos totales_g", "Carbohidratos disponibles_g", "Fibra dietética_g",
            "Cenizas_g", "Sodio_mg", "Potasio_mg", "Calcio_mg", "Fósforo_mg", "Hierro_mg", "Zinc_mg",
            "Tiamina_mg", "Rivoflavina_mg", "Niacina_mg", "Vitamina_C_mg"
        ]
    }
}

# Función general de guardado
def procesar_ingredientes(tipo):
    config = CONFIGURACIONES[tipo]
    df = pd.read_excel(
        config["archivo"],
        skiprows=7,
        usecols=config["columnas"],
        nrows=config["n_filas"],
        engine="xlrd"
    )
    df.columns = config["nombres_columnas"]

    ingredientes = []
    for _, fila in df.iterrows():
        ingrediente = {
            "nombre": fila.get("Alimento", np.nan),
            "tipo": tipo,
            "caloriasPor100g": fila.get("Energía_kcal", np.nan),
            "proteinas": fila.get("Proteínas_g", np.nan),
            "grasas": fila.get("Grasa Total_g", np.nan),
            "carbohidratos": fila.get("Carbohidratos totales_g", np.nan),
            "agua": fila.get("Agua_g", np.nan),
            "fibra": fila.get("Fibra dietética_g", None),
            "carbohidratosDisponibles": fila.get("Carbohidratos disponibles_g", None),
            "sodio": round(fila["Sodio_mg"] / 1000, 4) if pd.notna(fila.get("Sodio_mg")) else 0,
            "cenizas": fila.get("Cenizas_g", np.nan),
            "potasio": fila.get("Potasio_mg", np.nan),
            "calcio": fila.get("Calcio_mg", np.nan),
            "fosforo": fila.get("Fósforo_mg", np.nan),
            "hierro": fila.get("Hierro_mg", np.nan),
            "zinc": fila.get("Zinc_mg", np.nan),
            "tiamina": fila.get("Tiamina_mg", np.nan),
            "rivoflavina": fila.get("Rivoflavina_mg", np.nan),
            "niacina": fila.get("Niacina_mg", np.nan),
            "vitaminaC": fila.get("Vitamina_C_mg", np.nan),
            "acidosGrasosSaturados": fila.get("Ac. grasos saturados_g", np.nan),
            "acidosGrasosMonoinsaturados": fila.get("Ac. grasos monoinsaturados_g", np.nan),
            "acidosGrasosPoliinsaturados": fila.get("Ac. grasos poliinsaturados_g", np.nan),
            "colesterol": fila.get("Colesterol_g", np.nan)
        }
        ingredientes.append(ingrediente)

    salida = f"ingredientes_{tipo.lower().replace(' ', '_')}.txt"
    with open(salida, "w", encoding="utf-8") as f:
        json.dump(ingredientes, f, ensure_ascii=False, indent=2)

    print(f"✅ Ingredientes de '{tipo}' exportados en '{salida}'")

# Ejecutar todos automáticamente
if __name__ == "__main__":
    for tipo in CONFIGURACIONES.keys():
        procesar_ingredientes(tipo)
