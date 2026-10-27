"""
TIPOS DE DATOS EN PYTHON - GUÍA COMPLETA CON ANOTACIONES
=========================================================
Cada tipo explicado, con anotación de tipo explícita: variable: tipo = valor
"""

# ==============================================================================
# 1. TIPOS NUMÉRICOS
# ==============================================================================

# --- int ---
# Números enteros, sin decimales. No tienen límite de tamaño.
edad: int = 25
temperatura_negativa: int = -10
binario: int = 0b1010      # 10 en decimal
hexadecimal: int = 0x1F    # 31 en decimal

print("--- int ---")
print(f"edad: {edad}, tipo: {type(edad)}")
print(f"binario 0b1010: {binario}")
print(f"hexadecimal 0x1F: {hexadecimal}")


# --- float ---
# Números con decimales. Precisión de 64 bits (doble precisión).
pi: float = 3.14159
gravedad: float = -9.8
cientifico: float = 1.5e3  # 1500.0

print("\n--- float ---")
print(f"pi: {pi}, tipo: {type(pi)}")
print(f"1.5e3: {cientifico}")


# --- complex ---
# Números complejos con parte real e imaginaria. Usan 'j' para imaginaria.
complejo: complex = 3 + 4j
solo_imaginario: complex = 5j

print("\n--- complex ---")
print(f"complejo: {complejo}, tipo: {type(complejo)}")
print(f"Parte real: {complejo.real}, imaginaria: {complejo.imag}")


# --- bool ---
# Valores de verdad: True o False. En Python, bool es subtipo de int.
es_adulto: bool = True
es_menor: bool = False
comparacion: bool = 10 > 5

print("\n--- bool ---")
print(f"es_adulto: {es_adulto}, tipo: {type(es_adulto)}")
print(f"10 > 5: {comparacion}")
print(f"True como int: {int(True)}")


# ==============================================================================
# 2. TIPOS DE SECUENCIA
# ==============================================================================

# --- str ---
# Cadenas de texto Unicode. Inmutables (no se pueden cambiar después de crearlas).
nombre: str = "Python"
multilinea: str = """Línea 1
Línea 2"""
raw: str = r"C:\nueva"  # No interpreta \n como salto de línea

print("\n--- str ---")
print(f"nombre: {nombre}, tipo: {type(nombre)}")
print(f"raw string: {raw}")


# --- list ---
# Listas ordenadas y mutables. Permiten duplicados y mezcla de tipos.
numeros: list = [1, 2, 3, 4, 5]
mixta: list = [1, "texto", 3.14, True]
vacia: list = []

print("\n--- list ---")
print(f"numeros: {numeros}, tipo: {type(numeros)}")
print(f"mixta: {mixta}")


# --- tuple ---
# Tuplas ordenadas e inmutables. Más rápidas que listas, usadas para datos fijos.
coordenadas: tuple = (10, 20, 30)
un_elemento: tuple = (42,)  # Coma obligatoria para un solo elemento
vacia: tuple = ()

print("\n--- tuple ---")
print(f"coordenadas: {coordenadas}, tipo: {type(coordenadas)}")
print(f"un_elemento: {un_elemento}")


# --- range ---
# Secuencia inmutable de números enteros. Usada en loops y para generar secuencias.
rango: range = range(5)        # 0, 1, 2, 3, 4
rango_paso: range = range(0, 10, 2)  # 0, 2, 4, 6, 8

print("\n--- range ---")
print(f"range(5): {rango}, tipo: {type(rango)}")
print(f"Convertido a lista: {list(rango)}")
print(f"range(0, 10, 2): {list(rango_paso)}")


# --- bytes ---
# Secuencia inmutable de bytes (valores 0-255). Usada para datos binarios.
datos: bytes = b"Hola"
vacio: bytes = b""

print("\n--- bytes ---")
print(f"datos: {datos}, tipo: {type(datos)}")


# --- bytearray ---
# Como bytes, pero mutable. Puedes modificar los valores después de crearlo.
mutable: bytearray = bytearray(b"Hola")

print("\n--- bytearray ---")
print(f"mutable: {mutable}, tipo: {type(mutable)}")


# --- memoryview ---
# Vista de memoria de un objeto binario. Permite acceder a datos sin copiarlos.
datos_originales: bytes = b"Hola Mundo"
vista: memoryview = memoryview(datos_originales)

print("\n--- memoryview ---")
print(f"vista: {vista}, tipo: {type(vista)}")
print(f"Primeros 4 bytes: {list(vista[:4])}")


# ==============================================================================
# 3. TIPOS DE CONJUNTO
# ==============================================================================

# --- set ---
# Conjuntos mutables, no ordenados, sin duplicados. Útiles para operaciones de conjuntos.
numeros: set = {1, 2, 3, 4, 5}
vacio: set = set()  # {} crea dict, no set

print("\n--- set ---")
print(f"numeros: {numeros}, tipo: {type(numeros)}")


# --- frozenset ---
# Como set, pero inmutable. Puede usarse como clave en diccionarios.
inmutable: frozenset = frozenset([1, 2, 3])

print("\n--- frozenset ---")
print(f"inmutable: {inmutable}, tipo: {type(inmutable)}")


# ==============================================================================
# 4. TIPOS DE MAPEO
# ==============================================================================

# --- dict ---
# Diccionarios: pares clave-valor. Ordenados (Python 3.7+), mutables, claves únicas.
persona: dict = {"nombre": "Ana", "edad": 30}
vacio: dict = {}

print("\n--- dict ---")
print(f"persona: {persona}, tipo: {type(persona)}")


# ==============================================================================
# 5. TIPO NULO
# ==============================================================================

# --- NoneType ---
# Representa ausencia de valor. Solo existe un valor: None.
resultado: None = None

print("\n--- NoneType ---")
print(f"resultado: {resultado}, tipo: {type(resultado)}")


# ==============================================================================
# RESUMEN
# ==============================================================================
print("\n" + "="*60)
print("TIPOS DE DATOS EN PYTHON")
print("="*60)
print("Numéricos: int, float, complex, bool")
print("Secuencias: str, list, tuple, range, bytes, bytearray, memoryview")
print("Conjuntos: set, frozenset")
print("Mapeos: dict")
print("Nulo: NoneType")
print("="*60)
