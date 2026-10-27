"""
SOLUCIONES - MANEJO DE ARCHIVOS EN PYTHON
==========================================
"""

from pathlib import Path
import json
import csv

directorio: Path = Path("archivos_practica")
directorio.mkdir(exist_ok=True)

# ==============================================================================
# EJERCICIO 1
# ==============================================================================
print("="*60)
print("EJERCICIO 1: Crear y escribir archivo")
print("="*60)

ruta_notas: Path = directorio / "notas.txt"

with open(ruta_notas, "w", encoding="utf-8") as archivo:
    archivo.write("Nombre: Estudiante\n")
    archivo.write("Lenguaje favorito: Python\n")
    archivo.write("Objetivo: Dominar los fundamentos\n")

if ruta_notas.exists():
    print(f"\nArchivo creado: {ruta_notas.name}")
    print(f"Tamaño: {ruta_notas.stat().st_size} bytes")
print("\n" + "-"*60)


# ==============================================================================
# EJERCICIO 2
# ==============================================================================
print("\nEJERCICIO 2: Leer y contar líneas")
print("="*60)

with open(ruta_notas, "r", encoding="utf-8") as archivo:
    lineas: list[str] = archivo.readlines()

print(f"\nTotal de líneas: {len(lineas)}")
print("\nContenido numerado:")
for numero, linea in enumerate(lineas, start=1):
    print(f"  {numero}. {linea.strip()}")
print("\n" + "-"*60)


# ==============================================================================
# EJERCICIO 3
# ==============================================================================
print("\nEJERCICIO 3: Agregar contenido (append)")
print("="*60)

with open(ruta_notas, "a", encoding="utf-8") as archivo:
    archivo.write("Última actualización: 2026\n")

print("\nContenido actualizado:")
with open(ruta_notas, "r", encoding="utf-8") as archivo:
    for linea in archivo:
        print(f"  {linea.strip()}")
print("\n" + "-"*60)


# ==============================================================================
# EJERCICIO 4
# ==============================================================================
print("\nEJERCICIO 4: Procesar contenido (números)")
print("="*60)

ruta_numeros: Path = directorio / "numeros.txt"
numeros_a_escribir: list[int] = [10, 25, 30, 45, 50]

with open(ruta_numeros, "w", encoding="utf-8") as archivo:
    for numero in numeros_a_escribir:
        archivo.write(f"{numero}\n")

print(f"\nArchivo '{ruta_numeros.name}' creado con: {numeros_a_escribir}")

with open(ruta_numeros, "r", encoding="utf-8") as archivo:
    numeros_leidos: list[int] = [int(linea.strip()) for linea in archivo]

suma_total: int = sum(numeros_leidos)
promedio: float = suma_total / len(numeros_leidos)
maximo: int = max(numeros_leidos)

print(f"\nSuma total: {suma_total}")
print(f"Promedio: {promedio:.2f}")
print(f"Número más grande: {maximo}")
print("\n" + "-"*60)


# ==============================================================================
# EJERCICIO 5
# ==============================================================================
print("\nEJERCICIO 5: Crear archivo JSON")
print("="*60)

config: dict[str, str | int | bool] = {
    "app": "MiApp",
    "version": "1.0.0",
    "debug": False,
    "puerto": 8080
}

ruta_config: Path = directorio / "config.json"

with open(ruta_config, "w", encoding="utf-8") as archivo:
    json.dump(config, archivo, indent=4, ensure_ascii=False)

print(f"\nJSON creado: {ruta_config.name}")

with open(ruta_config, "r", encoding="utf-8") as archivo:
    config_leida: dict = json.load(archivo)

print(f"Contenido leído:")
for clave, valor in config_leida.items():
    print(f"  {clave}: {valor}")
print("\n" + "-"*60)


# ==============================================================================
# EJERCICIO 6
# ==============================================================================
print("\nEJERCICIO 6: Modificar archivo JSON")
print("="*60)

with open(ruta_config, "r", encoding="utf-8") as archivo:
    datos: dict = json.load(archivo)

datos["debug"] = True
datos["usuarios"] = 100

with open(ruta_config, "w", encoding="utf-8") as archivo:
    json.dump(datos, archivo, indent=4, ensure_ascii=False)

print(f"\nJSON modificado:")
with open(ruta_config, "r", encoding="utf-8") as archivo:
    datos_verificados: dict = json.load(archivo)

for clave, valor in datos_verificados.items():
    print(f"  {clave}: {valor}")
print("\n" + "-"*60)


# ==============================================================================
# EJERCICIO 7
# ==============================================================================
print("\nEJERCICIO 7: Crear archivo CSV")
print("="*60)

empleados: list[dict[str, str | int]] = [
    {"nombre": "Ana", "departamento": "Desarrollo", "salario": 3500},
    {"nombre": "Luis", "departamento": "Ventas", "salario": 3000},
    {"nombre": "María", "departamento": "Marketing", "salario": 3200}
]

ruta_empleados: Path = directorio / "empleados.csv"

with open(ruta_empleados, "w", newline="", encoding="utf-8") as archivo:
    campos: list[str] = ["nombre", "departamento", "salario"]
    writer = csv.DictWriter(archivo, fieldnames=campos)
    writer.writeheader()
    writer.writerows(empleados)

print(f"\nCSV creado: {ruta_empleados.name}")
print(f"Registros: {len(empleados)}")
print("\n" + "-"*60)


# ==============================================================================
# EJERCICIO 8
# ==============================================================================
print("\nEJERCICIO 8: Leer CSV y filtrar")
print("="*60)

print(f"\nEmpleados con salario > 3100:")

with open(ruta_empleados, "r", encoding="utf-8") as archivo:
    reader = csv.DictReader(archivo)
    for fila in reader:
        if int(fila["salario"]) > 3100:
            print(f"  {fila['nombre']} - {fila['departamento']} (${fila['salario']})")
print("\n" + "-"*60)


# ==============================================================================
# EJERCICIO 9
# ==============================================================================
print("\nEJERCICIO 9: Manejo de errores")
print("="*60)

ruta_inexistente: Path = directorio / "inexistente.txt"

try:
    with open(ruta_inexistente, "r", encoding="utf-8") as archivo:
        contenido = archivo.read()
except FileNotFoundError:
    print(f"\nError capturado: El archivo '{ruta_inexistente.name}' no existe.")
except Exception as e:
    print(f"\nError inesperado: {e}")
finally:
    print("Proceso finalizado.")
print("\n" + "-"*60)


# ==============================================================================
# EJERCICIO 10
# ==============================================================================
print("\nEJERCICIO 10: Respaldo de archivo")
print("="*60)

def crear_respaldo(ruta_original: Path) -> Path:
    """Crea una copia de respaldo con extensión .bak."""
    ruta_respaldo: Path = Path(str(ruta_original) + ".bak")
    with open(ruta_original, "r", encoding="utf-8") as archivo_origen:
        contenido: str = archivo_origen.read()
    with open(ruta_respaldo, "w", encoding="utf-8") as archivo_respaldo:
        archivo_respaldo.write(contenido)
    return ruta_respaldo

respaldo: Path = crear_respaldo(ruta_notas)
print(f"\nRespaldo creado: {respaldo.name}")
print(f"Existe: {respaldo.exists()}")
print(f"Tamaño: {respaldo.stat().st_size} bytes")
print("\n" + "="*60)
