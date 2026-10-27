"""
EXCEPCIONES EN PYTHON - GUÍA COMPLETA
======================================
Manejo de errores, estructura try/except, excepciones personalizadas.
"""

# ==============================================================================
# 1. ESTRUCTURA BÁSICA try/except
# ==============================================================================
print("="*60)
print("1. ESTRUCTURA BÁSICA try/except")
print("="*60)

# Sin manejo de excepciones, un error detiene el programa.
# Con try/except, capturamos el error y el programa continúa.

try:
    resultado: float = 10 / 0
except ZeroDivisionError:
    print("\nError capturado: No se puede dividir por cero.")

print("El programa continúa ejecutándose.")
print("\n" + "-"*60)


# ==============================================================================
# 2. CAPTURAR EXCEPCIONES ESPECÍFICAS
# ==============================================================================
print("\n2. CAPTURAR EXCEPCIONES ESPECÍFICAS")
print("="*60)

# Es buena práctica capturar excepciones específicas, no genéricas.

try:
    numero: int = int("abc")
except ValueError:
    print("\nValueError: No se puede convertir 'abc' a entero.")

try:
    mi_lista: list = [1, 2, 3]
    elemento = mi_lista[10]
except IndexError:
    print("IndexError: El índice 10 no existe en la lista.")

try:
    mi_diccionario: dict = {"a": 1}
    valor = mi_diccionario["b"]
except KeyError:
    print("KeyError: La clave 'b' no existe en el diccionario.")
print("\n" + "-"*60)


# ==============================================================================
# 3. MÚLTIPLES EXCEPCIONES EN UN BLOQUE
# ==============================================================================
print("\n3. MÚLTIPLES EXCEPCIONES EN UN BLOQUE")
print("="*60)

# Forma 1: Varias excepciones en una sola tupla
try:
    valor = int("xyz")
except (ValueError, TypeError) as e:
    print(f"\nError capturado (tupla): {type(e).__name__} - {e}")

# Forma 2: Bloques except separados para manejo diferenciado
def dividir(a: int, b: int) -> None:
    try:
        resultado: float = a / b
        print(f"  {a} / {b} = {resultado}")
    except ZeroDivisionError:
        print(f"  Error: División por cero en {a}/{b}")
    except TypeError:
        print(f"  Error: Tipos inválidos en {a}/{b}")

print("\nPruebas de división:")
dividir(10, 2)
dividir(10, 0)
print("\n" + "-"*60)


# ==============================================================================
# 4. LA CLÁUSULA `as` (INFORMACIÓN DEL ERROR)
# ==============================================================================
print("\n4. LA CLÁUSULA `as`")
print("="*60)

# La cláusula 'as' captura la instancia de la excepción para inspeccionarla.

try:
    archivo = open("archivo_inexistente.txt", "r")
except FileNotFoundError as e:
    print(f"\nTipo de excepción: {type(e).__name__}")
    print(f"Mensaje del error: {e}")
    print(f"Argumentos: {e.args}")
print("\n" + "-"*60)


# ==============================================================================
# 5. ESTRUCTURA try/except/else
# ==============================================================================
print("\n5. ESTRUCTURA try/except/else")
print("="*60)

# El bloque 'else' se ejecuta SOLO si NO hubo excepciones en try.

def conversion_segura(texto: str) -> None:
    try:
        numero: int = int(texto)
    except ValueError:
        print(f"  '{texto}' no es un número válido.")
    else:
        print(f"  '{texto}' convertido exitosamente a {numero} (tipo: {type(numero).__name__})")

print("\nPruebas de conversión:")
conversion_segura("42")
conversion_segura("hola")
conversion_segura("3.14")
print("\n" + "-"*60)


# ==============================================================================
# 6. ESTRUCTURA try/except/else/finally
# ==============================================================================
print("\n6. ESTRUCTURA try/except/else/finally")
print("="*60)

# El bloque 'finally' se ejecuta SIEMPRE, haya error o no.
# Útil para liberar recursos (cerrar archivos, conexiones, etc.)

def operacion_con_recursos(divisor: int) -> None:
    recurso_abierto: bool = True
    print(f"\n  Intentando dividir 100 entre {divisor}...")
    try:
        if recurso_abierto:
            print("  Recurso abierto.")
        resultado: float = 100 / divisor
    except ZeroDivisionError:
        print("  Error: Divisor es cero.")
    else:
        print(f"  Resultado: {resultado}")
    finally:
        recurso_abierto = False
        print("  Recurso cerrado (finally siempre se ejecuta).")

operacion_con_recursos(5)
operacion_con_recursos(0)
print("\n" + "-"*60)


# ==============================================================================
# 7. EXCEPCIONES INTEGRADAS COMUNES
# ==============================================================================
print("\n7. EXCEPCIONES INTEGRADAS COMUNES")
print("="*60)

excepciones_comunes: list[tuple[str, str, str]] = [
    ("ValueError", "Valor incorrecto para el tipo", "int('abc')"),
    ("TypeError", "Operación con tipo incorrecto", "'2' + 2"),
    ("ZeroDivisionError", "División por cero", "1 / 0"),
    ("IndexError", "Índice fuera de rango", "[1,2][5]"),
    ("KeyError", "Clave no encontrada", "{'a':1}['b']"),
    ("FileNotFoundError", "Archivo no existe", "open('no.txt')"),
    ("AttributeError", "Atributo no existe", "'str'.metodo_falso()"),
    ("ImportError", "Módulo no disponible", "import modulo_falso"),
    ("OverflowError", "Resultado numérico muy grande", "Operación extrema"),
    ("RecursionError", "Recursión máxima excedida", "Función recursiva infinita"),
]

print("\nExcepción             | Causa                          | Ejemplo")
print("-"*85)
for nombre, causa, ejemplo in excepciones_comunes:
    print(f"{nombre:<21} | {causa:<30} | {ejemplo}")
print("\n" + "-"*60)


# ==============================================================================
# 8. JERARQUÍA DE EXCEPCIONES (BÁSICA)
# ==============================================================================
print("\n8. JERARQUÍA DE EXCEPCIONES")
print("="*60)

# Todas las excepciones heredan de BaseException.
# Exception es la clase base para excepciones "regulares".

jerarquia: str = """
BaseException
├── SystemExit
├── KeyboardInterrupt
├── GeneratorExit
└── Exception
    ├── ArithmeticError
    │   └── ZeroDivisionError
    ├── LookupError
    │   ├── IndexError
    │   └── KeyError
    ├── ValueError
    ├── TypeError
    ├── OSError
    │   └── FileNotFoundError
    └── ... (muchas más)
"""
print(jerarquia)
print("Nota: Capturar 'Exception' atrapa todas las excepciones regulares.")
print("Nota: Evitar capturar 'BaseException' (incluye SystemExit, KeyboardInterrupt).")
print("\n" + "-"*60)


# ==============================================================================
# 9. LANZAR EXCEPCIONES CON raise
# ==============================================================================
print("\n9. LANZAR EXCEPCIONES CON raise")
print("="*60)

# Se usa 'raise' para lanzar una excepción manualmente cuando se detecta
# una condición inválida.

def calcular_raiz(numero: float) -> float:
    """Calcula la raíz cuadrada. Lanza error si el número es negativo."""
    if numero < 0:
        raise ValueError(f"No se puede calcular la raíz de un negativo: {numero}")
    return numero ** 0.5

print("\nPruebas de calcular_raiz:")
try:
    print(f"  Raíz de 16: {calcular_raiz(16)}")
    print(f"  Raíz de -4: {calcular_raiz(-4)}")
except ValueError as e:
    print(f"  Error capturado: {e}")
print("\n" + "-"*60)


# ==============================================================================
# 10. EXCEPCIONES PERSONALIZADAS
# ==============================================================================
print("\n10. EXCEPCIONES PERSONALIZADAS")
print("="*60)

# Se crean heredando de Exception (o de una subclase más específica).

class SaldoInsuficienteError(Exception):
    """Excepción lanzada cuando el saldo es insuficiente para una operación."""
    def __init__(self, saldo: float, monto: float) -> None:
        self.saldo: float = saldo
        self.monto: float = monto
        super().__init__(f"Saldo insuficiente: se necesita {monto}, disponible {saldo}")

class CuentaBancaria:
    """Simulación simple de cuenta bancaria con excepción personalizada."""
    def __init__(self, saldo_inicial: float) -> None:
        self.saldo: float = saldo_inicial
    
    def retirar(self, monto: float) -> None:
        if monto > self.saldo:
            raise SaldoInsuficienteError(self.saldo, monto)
        self.saldo -= monto
        print(f"  Retiro de {monto}. Nuevo saldo: {self.saldo}")

print("\nPruebas con excepción personalizada:")
cuenta: CuentaBancaria = CuentaBancaria(100.0)
try:
    cuenta.retirar(30)
    cuenta.retirar(200)  # Esto lanzará la excepción personalizada
except SaldoInsuficienteError as e:
    print(f"  Error: {e}")
    print(f"  Saldo actual: {e.saldo}, monto intentado: {e.monto}")
print("\n" + "-"*60)


# ==============================================================================
# 11. RE-LANZAMIENTO Y ENCADENAMIENTO (from)
# ==============================================================================
print("\n11. RE-LANZAMIENTO Y ENCADENAMIENTO")
print("="*60)

# 'raise ... from ...' preserva la excepción original como contexto.

def procesar_dato(dato: str) -> int:
    try:
        return int(dato)
    except ValueError as e:
        raise TypeError(f"Se esperaba un número, se recibió: '{dato}'") from e

print("\nPrueba de encadenamiento:")
try:
    procesar_dato("no_soy_numero")
except TypeError as e:
    print(f"  Excepción capturada: {e}")
    print(f"  Causa original (__cause__): {e.__cause__}")
print("\n" + "-"*60)


# ==============================================================================
# 12. ASSERT (AFIRMACIONES)
# ==============================================================================
print("\n12. ASSERT (AFIRMACIONES)")
print("="*60)

# 'assert' verifica una condición en desarrollo.
# Si es False, lanza AssertionError. No usar para control de flujo en producción.

def aplicar_descuento(precio: float, descuento: float) -> float:
    assert 0 <= descuento <= 100, f"El descuento debe estar entre 0 y 100, recibido: {descuento}"
    return precio * (1 - descuento / 100)

print("\nPruebas con assert:")
try:
    print(f"  Precio con 20% descuento: {aplicar_descuento(100, 20)}")
    print(f"  Precio con 150% descuento: {aplicar_descuento(100, 150)}")
except AssertionError as e:
    print(f"  AssertionError: {e}")

print("\nNota: assert se puede desactivar con 'python -O' (modo optimizado).")
print("\n" + "-"*60)


# ==============================================================================
# 13. BUENAS PRÁCTICAS
# ==============================================================================
print("\n13. BUENAS PRÁCTICAS")
print("="*60)

buenas_practicas: list[str] = [
    "Capturar excepciones específicas, no 'except:' a secas.",
    "Evitar 'except Exception:' amplio salvo casos justificados.",
    "Usar else para código que solo debe ejecutarse si no hubo error.",
    "Usar finally para liberar recursos (cerrar archivos, conexiones).",
    "No usar excepciones para control de flujo normal.",
    "Documentar las excepciones que puede lanzar una función.",
    "Crear excepciones personalizadas para errores de dominio.",
    "Incluir mensajes descriptivos al lanzar excepciones.",
]

print("\nBuenas prácticas recomendadas:")
for i, practica in enumerate(buenas_practicas, start=1):
    print(f"  {i}. {practica}")

print("\n" + "="*60)
print("FIN DE LA GUÍA DE EXCEPCIONES")
print("="*60)
