# 🧹 CSV Cleaner – Limpieza Automática de Datos

Script en Python que automatiza la limpieza de archivos CSV.
Elimina duplicados, estandariza texto y ordena los datos por columna,
generando un archivo limpio listo para analizar.

---

## ✨ Funcionalidades

- Eliminación de filas duplicadas
- Normalización de texto (minúsculas, sin espacios extra)
- Ordenamiento por columna específica
- Genera archivo CSV limpio listo para usar

---

## 🛠️ Tecnologías utilizadas

- Python 3
- Pandas
- CSV

---

## ▶️ Cómo usarlo

1. Clonar el repositorio
git clone https://github.com/aixochoa/csv-cleaner-python

2. Instalar dependencias
pip install pandas

3. Ejecutar el script
python csv_cleaner.py

4. Ejemplo de uso
limpiar_csv("datos_originales.csv", "datos_limpios.csv", "nombre")

---

## 📄 Ejemplo de resultado

Antes:
Juan , juan@mail.com
juan , juan@mail.com   ← duplicado
María , maria@mail.com

Después:
juan, juan@mail.com
maría, maria@mail.com

---

## Autor
Aixo Ochoa
Estudiante de Medicina (UBA) & Análisis de Datos | Talento Tech
[github.com/aixochoa](https://github.com/aixochoa)
