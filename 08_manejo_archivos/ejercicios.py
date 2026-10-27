"""
EJERCICIOS - MANEJO DE ARCHIVOS EN PYTHON
==========================================
Resuelve cada ejercicio. No mires las soluciones hasta terminar.
Todos los archivos se crean en la carpeta 'archivos_practica'.
"""

from pathlib import Path
import json
import csv

directorio: Path = Path("archivos_practica")
directorio.mkdir(exist_ok=True)

# ==============================================================================
# EJERCICIO 1: Crear y escribir archivo
# ==============================================================================
# Crea un archivo llamado 'notas.txt' en la carpeta 'archivos_practica'.
# Escribe 3 líneas: una con tu nombre, otra con tu lenguaje favorito,
# y otra con un objetivo de aprendizaje.
# Verifica que el archivo existe e imprime su tamaño en bytes.

# Tu código aquí:



# ==============================================================================
# EJERCICIO 2: Leer y contar líneas
# ==============================================================================
# Abre el archivo 'notas.txt' creado en el ejercicio anterior.
# Lee todas las líneas y cuenta cuántas líneas tiene el archivo.
# Imprime cada línea numerada (empezando desde 1).

# Tu código aquí:



# ==============================================================================
# EJERCICIO 3: Agregar contenido (append)
# ==============================================================================
# Abre 'notas.txt' en modo append ('a').
# Agrega una línea nueva con la fecha actual como string.
# Luego, lee el archivo completo e imprime todas las líneas para verificar.

# Tu código aquí:



# ==============================================================================
# EJERCICIO 4: Procesar contenido (números)
# ==============================================================================
# Crea un archivo 'numeros.txt' con estos números, uno por línea: 10, 25, 30, 45, 50
# Luego, lee el archivo y calcula:
# - La suma de todos los números
# - El promedio
# - El número más grande
# Imprime los tres resultados.

# Tu código aquí:



# ==============================================================================
# EJERCICIO 5: Crear archivo JSON
# ==============================================================================
# Tienes este diccionario de configuración:
# config = {"app": "MiApp", "version": "1.0.0", "debug": False, "puerto": 8080}
# Guárdalo como 'config.json' en la carpeta 'archivos_practica' con indentación de 4.
# Luego, léelo de vuelta e imprime el contenido.

config: dict[str, str | int | bool] = {
    "app": "MiApp",
    "version": "1.0.0",
    "debug": False,
    "puerto": 8080
}

# Tu código aquí:



# ==============================================================================
# EJERCICIO 6: Modificar archivo JSON
# ==============================================================================
# Abre el archivo 'config.json' del ejercicio anterior.
# Cambia el valor de 'debug' a True y agrega una nueva clave 'usuarios' con valor 100.
# Guarda los cambios en el mismo archivo y verifica imprimiendo el contenido.

# Tu código aquí:



# ==============================================================================
# EJERCICIO 7: Crear archivo CSV
# ==============================================================================
# Tienes esta lista de empleados:
# empleados = [
#     {"nombre": "Ana", "departamento": "Desarrollo", "salario": 3500},
#     {"nombre": "Luis", "departamento": "Ventas", "salario": 3000},
#     {"nombre": "María", "departamento": "Marketing", "salario": 3200}
# ]
# Guárdala como 'empleados.csv' en la carpeta 'archivos_practica'.
# Usa csv.DictWriter con las columnas: nombre, departamento, salario.

empleados: list[dict[str, str | int]] = [
    {"nombre": "Ana", "departamento": "Desarrollo", "salario": 3500},
    {"nombre": "Luis", "departamento": "Ventas", "salario": 3000},
    {"nombre": "María", "departamento": "Marketing", "salario": 3200}
]

# Tu código aquí:



# ==============================================================================
# EJERCICIO 8: Leer CSV y filtrar
# ==============================================================================
# Abre el archivo 'empleados.csv' del ejercicio anterior.
# Lee el contenido y filtra solo los empleados con salario mayor a 3100.
# Imprime el nombre y departamento de los empleados filtrados.

# Tu código aquí:



# ==============================================================================
# EJERCICIO 9: Manejo de errores
# ==============================================================================
# Intenta leer un archivo llamado 'inexistente.txt' en la carpeta 'archivos_practica'.
# Usa try/except para capturar el error FileNotFoundError e imprime un mensaje claro.
# Luego, usa try/finally para imprimir "Proceso finalizado" pase lo que pase.

# Tu código aquí:



# ==============================================================================
# EJERCICIO 10: Respaldo de archivo
# ==============================================================================
# Crea una función 'crear_respaldo' que reciba la ruta de un archivo (Path)
# y cree una copia del archivo con la extensión '.bak' agregada al nombre.
# Ejemplo: 'notas.txt' → 'notas.txt.bak'
# Prueba la función con 'notas.txt' y verifica que el respaldo existe.

# Tu código aquí:
