"""
SOLUCIONES - TIPOS DE DATOS EN PYTHON
======================================
Código resuelto con explicaciones.
"""

# ==============================================================================
# EJERCICIO 1: Declaración básica con tipos
# ==============================================================================
producto: str = "Laptop"
precio: float = 999.99
stock: int = 15
disponible: bool = True

print("--- Ejercicio 1 ---")
print(f"producto: {producto}, tipo: {type(producto)}")
print(f"precio: {precio}, tipo: {type(precio)}")
print(f"stock: {stock}, tipo: {type(stock)}")
print(f"disponible: {disponible}, tipo: {type(disponible)}")
# Salida:
# producto: Laptop, tipo: <class 'str'>
# precio: 999.99, tipo: <class 'float'>
# stock: 15, tipo: <class 'int'>
# disponible: True, tipo: <class 'bool'>


# ==============================================================================
# EJERCICIO 2: Conversión de tipos (casting)
# ==============================================================================
texto_edad: str = "28"
texto_altura: str = "1.75"
texto_precio: str = "49.99"

edad: int = int(texto_edad)
altura: float = float(texto_altura)
precio: float = float(texto_precio)

resultado: float = edad * altura * precio

print("\n--- Ejercicio 2 ---")
print(f"Resultado: {resultado}")
# Salida: Resultado: 2449.515


# ==============================================================================
# EJERCICIO 3: Listas vs Tuplas (mutabilidad)
# ==============================================================================
frutas: list = ["manzana", "banana", "naranja"]
coordenadas: tuple = (10, 20, 30)

frutas.append("pera")  # Esto funciona porque list es mutable
# coordenadas[0] = 99  # ERROR: tuple es inmutable, esto causaría TypeError

print("\n--- Ejercicio 3 ---")
print(f"frutas: {frutas}")
print(f"coordenadas: {coordenadas}")
# Salida:
# frutas: ['manzana', 'banana', 'naranja', 'pera']
# coordenadas: (10, 20, 30)


# ==============================================================================
# EJERCICIO 4: Diccionarios
# ==============================================================================
estudiante: dict = {
    "nombre": "Carlos",
    "edad": 22,
    "cursos": ["Python", "JavaScript", "SQL"],
    "activo": True
}

nombre_estudiante: str = estudiante["nombre"]
cantidad_cursos: int = len(estudiante["cursos"])

print("\n--- Ejercicio 4 ---")
print(f"Nombre: {nombre_estudiante}")
print(f"Cantidad de cursos: {cantidad_cursos}")
# Salida:
# Nombre: Carlos
# Cantidad de cursos: 3


# ==============================================================================
# EJERCICIO 5: Sets y operaciones
# ==============================================================================
numeros_pares: set = {2, 4, 6, 8, 10}
numeros_primos: set = {2, 3, 5, 7, 11}

union: set = numeros_pares | numeros_primos  # o numeros_pares.union(numeros_primos)
interseccion: set = numeros_pares & numeros_primos  # o numeros_pares.intersection(numeros_primos)
diferencia: set = numeros_pares - numeros_primos  # o numeros_pares.difference(numeros_primos)

print("\n--- Ejercicio 5 ---")
print(f"Unión: {union}")
print(f"Intersección: {interseccion}")
print(f"Diferencia: {diferencia}")
# Salida:
# Unión: {2, 3, 4, 5, 6, 7, 8, 10, 11}
# Intersección: {2}
# Diferencia: {4, 6, 8, 10}


# ==============================================================================
# EJERCICIO 6: Range y conversión
# ==============================================================================
rango: range = range(1, 21, 3)  # 1, 4, 7, 10, 13, 16, 19

lista_desde_rango: list = list(rango)
tupla_desde_rango: tuple = tuple(rango)

print("\n--- Ejercicio 6 ---")
print(f"Lista: {lista_desde_rango}")
print(f"Tupla: {tupla_desde_rango}")
# Salida:
# Lista: [1, 4, 7, 10, 13, 16, 19]
# Tupla: (1, 4, 7, 10, 13, 16, 19)


# ==============================================================================
# EJERCICIO 7: Bytes y bytearray
# ==============================================================================
datos_bytes: bytes = b"Python"
datos_bytearray: bytearray = bytearray(b"Python")

datos_bytearray[0] = 80  # 80 es el código ASCII de 'P'

print("\n--- Ejercicio 7 ---")
print(f"bytes: {datos_bytes}, tipo: {type(datos_bytes)}")
print(f"bytearray: {datos_bytearray}, tipo: {type(datos_bytearray)}")
# Salida:
# bytes: b'Python', tipo: <class 'bytes'>
# bytearray: bytearray(b'Python'), tipo: <class 'bytearray'>
# Nota: El primer byte ya era 'P' (80), por eso no cambia visualmente


# ==============================================================================
# EJERCICIO 8: None y verificación
# ==============================================================================
resultado = None

if resultado is None:
    resultado = 42

es_none: bool = resultado is None

print("\n--- Ejercicio 8 ---")
print(f"Resultado: {resultado}")
print(f"Es None: {es_none}")
# Salida:
# Resultado: 42
# Es None: False


# ==============================================================================
# EJERCICIO 9: Tipos complejos anidados
# ==============================================================================
productos: list = [
    {
        "nombre": "Laptop",
        "precio": 999.99,
        "tags": {"electrónica", "computadora", "portátil"}
    },
    {
        "nombre": "Mouse",
        "precio": 29.99,
        "tags": {"periférico", "accesorio"}
    },
    {
        "nombre": "Teclado",
        "precio": 79.99,
        "tags": {"periférico", "input"}
    }
]

segundo_producto: dict = productos[1]
nombre_segundo: str = segundo_producto["nombre"]
tags_segundo: set = segundo_producto["tags"]

print("\n--- Ejercicio 9 ---")
print(f"Nombre: {nombre_segundo}")
print(f"Tags: {tags_segundo}")
# Salida:
# Nombre: Mouse
# Tags: {'periférico', 'accesorio'}


# ==============================================================================
# EJERCICIO 10: Conversión entre tipos de secuencia
# ==============================================================================
tupla_original: tuple = (1, 2, 3, 4, 5)

lista_convertida: list = list(tupla_original)
set_convertido: set = set(tupla_original)
string_convertido: str = "-".join(str(x) for x in tupla_original)

print("\n--- Ejercicio 10 ---")
print(f"Lista: {lista_convertida}")
print(f"Set: {set_convertido}")
print(f"String: {string_convertido}")
# Salida:
# Lista: [1, 2, 3, 4, 5]
# Set: {1, 2, 3, 4, 5}
# String: 1-2-3-4-5
