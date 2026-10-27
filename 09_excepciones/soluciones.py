"""
SOLUCIONES - EXCEPCIONES EN PYTHON
===================================
"""

# ==============================================================================
# EJERCICIO 1
# ==============================================================================
print("="*60)
print("EJERCICIO 1: try/except básico")
print("="*60)

def dividir(a: int, b: int) -> float | None:
    try:
        return a / b
    except ZeroDivisionError:
        print("  Error: No se puede dividir por cero.")
        return None

print(f"\n  dividir(10, 2) = {dividir(10, 2)}")
print(f"  dividir(10, 0) = {dividir(10, 0)}")
print("\n" + "-"*60)


# ==============================================================================
# EJERCICIO 2
# ==============================================================================
print("\nEJERCICIO 2: ValueError en conversión")
print("="*60)

def convertir_a_entero(texto: str) -> int | None:
    try:
        return int(texto)
    except ValueError:
        print(f"  '{texto}' no es un entero válido.")
        return None

print("\nPruebas:")
print(f"  convertir_a_entero('42') = {convertir_a_entero('42')}")
convertir_a_entero("hola")
convertir_a_entero("3.14")
print("\n" + "-"*60)


# ==============================================================================
# EJERCICIO 3
# ==============================================================================
print("\nEJERCICIO 3: Múltiples excepciones")
print("="*60)

def acceder_a_lista(lista: list, indice) -> None:
    try:
        print(f"  lista[{indice}] = {lista[indice]}")
    except IndexError:
        print(f"  Error: Índice {indice} fuera de rango.")
    except TypeError:
        print(f"  Error: El índice debe ser un entero, se recibió {type(indice).__name__}.")

mi_lista: list = [1, 2, 3]
print("\nPruebas:")
acceder_a_lista(mi_lista, 1)
acceder_a_lista(mi_lista, 10)
acceder_a_lista(mi_lista, "a")
print("\n" + "-"*60)


# ==============================================================================
# EJERCICIO 4
# ==============================================================================
print("\nEJERCICIO 4: Cláusula `as`")
print("="*60)

print("\nIntentando abrir archivo inexistente:")
try:
    archivo = open("no_existe.txt", "r")
except FileNotFoundError as e:
    print(f"  Tipo de excepción: {type(e).__name__}")
    print(f"  Mensaje: {e}")
    print(f"  Argumentos: {e.args}")
print("\n" + "-"*60)


# ==============================================================================
# EJERCICIO 5
# ==============================================================================
print("\nEJERCICIO 5: try/except/else")
print("="*60)

def procesar_numero(texto: str) -> None:
    try:
        numero: float = float(texto)
    except ValueError:
        print(f"  '{texto}' no es un número válido.")
    else:
        cuadrado: float = numero ** 2
        print(f"  '{texto}' → {numero}, cuadrado: {cuadrado}")

print("\nPruebas:")
procesar_numero("25")
procesar_numero("abc")
procesar_numero("7.5")
print("\n" + "-"*60)


# ==============================================================================
# EJERCICIO 6
# ==============================================================================
print("\nEJERCICIO 6: try/except/finally")
print("="*60)

def leer_archivo_seguro(ruta: str) -> None:
    print(f"\n  Intentando leer '{ruta}':")
    try:
        with open(ruta, "r") as archivo:
            contenido: str = archivo.read()
            print(f"  Contenido: {contenido[:50]}...")
    except FileNotFoundError:
        print(f"  El archivo '{ruta}' no existe.")
    finally:
        print("  Operación de lectura finalizada.")

# Crear un archivo temporal para probar
with open("archivo_temporal.txt", "w") as f:
    f.write("Contenido de prueba para el ejercicio 6.")

leer_archivo_seguro("archivo_temporal.txt")
leer_archivo_seguro("no_existe.txt")

# Limpiar
import os
os.remove("archivo_temporal.txt")
print("\n" + "-"*60)


# ==============================================================================
# EJERCICIO 7
# ==============================================================================
print("\nEJERCICIO 7: Validación de entrada")
print("="*60)

def pedir_edad(texto: str) -> int | None:
    try:
        edad: int = int(texto)
        if edad < 0 or edad > 120:
            raise ValueError(f"Edad fuera de rango válido (0-120): {edad}")
        return edad
    except ValueError as e:
        print(f"  Error: {e}")
        return None

print("\nPruebas:")
print(f"  pedir_edad('25') = {pedir_edad('25')}")
pedir_edad("abc")
pedir_edad("150")
pedir_edad("-5")
print("\n" + "-"*60)


# ==============================================================================
# EJERCICIO 8
# ==============================================================================
print("\nEJERCICIO 8: KeyError en diccionarios")
print("="*60)

usuario: dict = {"nombre": "Ana", "edad": 30}

def obtener_valor(diccionario: dict, clave: str):
    try:
        return diccionario[clave]
    except KeyError:
        print(f"  La clave '{clave}' no existe.")
        return None

print("\nPruebas:")
print(f"  obtener_valor(usuario, 'nombre') = {obtener_valor(usuario, 'nombre')}")
obtener_valor(usuario, "telefono")
print(f"  obtener_valor(usuario, 'edad') = {obtener_valor(usuario, 'edad')}")
print("\n" + "-"*60)


# ==============================================================================
# EJERCICIO 9
# ==============================================================================
print("\nEJERCICIO 9: Excepción personalizada")
print("="*60)

class TemperaturaInvalidaError(Exception):
    """Excepción para temperaturas por debajo del cero absoluto."""
    def __init__(self, temperatura: float) -> None:
        self.temperatura: float = temperatura
        super().__init__(f"Temperatura {temperatura}°C es menor al cero absoluto (-273.15°C)")

def verificar_temperatura(temp: float) -> float:
    if temp < -273.15:
        raise TemperaturaInvalidaError(temp)
    return temp

print("\nPruebas:")
try:
    print(f"  verificar_temperatura(25.0) = {verificar_temperatura(25.0)}")
    print(f"  verificar_temperatura(-300.0) = {verificar_temperatura(-300.0)}")
except TemperaturaInvalidaError as e:
    print(f"  Error: {e}")
    print(f"  Temperatura inválida: {e.temperatura}")
print("\n" + "-"*60)


# ==============================================================================
# EJERCICIO 10
# ==============================================================================
print("\nEJERCICIO 10: Combinación completa")
print("="*60)

def procesar_lista_numeros(lista: list[str]) -> None:
    validos: int = 0
    invalidos: int = 0
    
    print("\nProcesando elementos:")
    for item in lista:
        try:
            numero: int = int(item)
            print(f"  ✓ '{item}' → {numero}")
            validos += 1
        except ValueError:
            print(f"  ✗ '{item}' no es un número válido")
            invalidos += 1
    
    print(f"\nResumen:")
    print(f"  Números válidos: {validos}")
    print(f"  Números inválidos: {invalidos}")

datos: list[str] = ["10", "abc", "20", "xyz", "30"]
procesar_lista_numeros(datos)
print("\n" + "="*60)
