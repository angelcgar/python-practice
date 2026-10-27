"""
SOLUCIONES - OPERADORES EN PYTHON
==================================
"""

# ==============================================================================
# EJERCICIO 1
# ==============================================================================
a: int = 25
b: int = 7

suma: int = a + b
resta: int = a - b
mult: int = a * b
div: float = a / b
div_ent: int = a // b
mod: int = a % b
pot: int = a ** b

print("--- Ejercicio 1 ---")
print(f"Suma: {suma} ({type(suma).__name__})")
print(f"Resta: {resta} ({type(resta).__name__})")
print(f"Multiplicación: {mult} ({type(mult).__name__})")
print(f"División: {div} ({type(div).__name__})")
print(f"División entera: {div_ent} ({type(div_ent).__name__})")
print(f"Módulo: {mod} ({type(mod).__name__})")
print(f"Potencia: {pot} ({type(pot).__name__})")
# Salida: 32, 18, 175, 3.571..., 3, 4, 6103515625


# ==============================================================================
# EJERCICIO 2
# ==============================================================================
total_segundos: int = 7380

horas: int = total_segundos // 3600
resto: int = total_segundos % 3600
minutos: int = resto // 60
segundos: int = resto % 60

print("\n--- Ejercicio 2 ---")
print(f"{horas} horas, {minutos} minutos, {segundos} segundos")
# Salida: 2 horas, 3 minutos, 0 segundos


# ==============================================================================
# EJERCICIO 3
# ==============================================================================
persona1: int = 17
persona2: int = 25
persona3: int = 30

pueden_entrar: bool = (persona1 >= 18) and (persona2 >= 18) and (persona3 >= 18)
alguno_mayor: bool = (persona1 > 25) or (persona2 > 25) or (persona3 > 25)

print("\n--- Ejercicio 3 ---")
print(f"Pueden entrar: {pueden_entrar}")
print(f"Alguno mayor de 25: {alguno_mayor}")
# Salida: False, True


# ==============================================================================
# EJERCICIO 4
# ==============================================================================
saldo: int = 1000

saldo += 500      # 1500
saldo -= 200      # 1300
saldo *= 2        # 2600
saldo //= 4       # 650
saldo **= 2       # 422500

print("\n--- Ejercicio 4 ---")
print(f"Saldo final: {saldo}")
# Salida: 422500


# ==============================================================================
# EJERCICIO 5
# ==============================================================================
lista_1: list = [1, 2, 3]
lista_2: list = [1, 2, 3]
lista_3: list = lista_1

print("\n--- Ejercicio 5 ---")
print(f"lista_1 is lista_2: {lista_1 is lista_2}")      # False
print(f"lista_1 is lista_3: {lista_1 is lista_3}")      # True
print(f"lista_1 == lista_2: {lista_1 == lista_2}")      # True
print(f"id lista_1: {id(lista_1)}")
print(f"id lista_2: {id(lista_2)}")
print(f"id lista_3: {id(lista_3)}")
# Salida: False, True, True, ids: 1 y 3 iguales, 2 distinto


# ==============================================================================
# EJERCICIO 6
# ==============================================================================
texto: str = "Desarrollo Web con Python"
lenguajes: list = ["Python", "JavaScript", "Go", "Rust"]
versiones: dict = {"Python": "3.11", "JS": "ES2024"}

print("\n--- Ejercicio 6 ---")
print(f"'Python' en texto: {'Python' in texto}")
print(f"'Java' no en lenguajes: {'Java' not in lenguajes}")
print(f"'Python' en versiones: {'Python' in versiones}")
print(f"'3.11' no en versiones: {'3.11' not in versiones}")
# Salida: True, True, True, True


# ==============================================================================
# EJERCICIO 7
# ==============================================================================
x: int = 60
y: int = 13

and_bit: int = x & y
or_bit: int = x | y
xor_bit: int = x ^ y
not_bit: int = ~x
shift_izq: int = x << 2
shift_der: int = x >> 2

print("\n--- Ejercicio 7 ---")
print(f"60 & 13 = {and_bit} ({bin(and_bit)})")
print(f"60 | 13 = {or_bit} ({bin(or_bit)})")
print(f"60 ^ 13 = {xor_bit} ({bin(xor_bit)})")
print(f"~60 = {not_bit} ({bin(not_bit)})")
print(f"60 << 2 = {shift_izq} ({bin(shift_izq)})")
print(f"60 >> 2 = {shift_der} ({bin(shift_der)})")
# Salida: 12, 61, 49, -61, 240, 15


# ==============================================================================
# EJERCICIO 8
# ==============================================================================
numeros: list = [5, 12, 8, 20, 3, 15]

print("\n--- Ejercicio 8 ---")
if len(filtrados := [n for n in numeros if n > 10]) > 2:
    print(f"Filtrados: {filtrados}, Suma: {sum(filtrados)}")
# Salida: Filtrados: [12, 20, 15], Suma: 47


# ==============================================================================
# EJERCICIO 9
# ==============================================================================
palabra: str = "Python"

concatenada: str = palabra + " es genial"
repetida: str = (palabra + "-") * 4
repetida = repetida.rstrip("-")  # Quita el guion final
py_in: bool = "Py" in palabra
java_not_in: bool = "Java" not in palabra

print("\n--- Ejercicio 9 ---")
print(f"Concatenada: {concatenada}")
print(f"Repetida: {repetida}")
print(f"'Py' in palabra: {py_in}")
print(f"'Java' not in palabra: {java_not_in}")
# Salida: Python es genial, Python-Python-Python-Python, True, True


# ==============================================================================
# EJERCICIO 10
# ==============================================================================
expresion_1: int = 2 + 3 * 4           # 2 + 12 = 14
expresion_2: int = (2 + 3) * 4         # 5 * 4 = 20
expresion_3: int = 2 ** 3 ** 2         # 2 ** 9 = 512 (asociativo derecha)
expresion_4: int = 10 - 2 * 3 + 1      # 10 - 6 + 1 = 5
expresion_5: bool = True or False and False  # True or False = True

print("\n--- Ejercicio 10 ---")
print(f"2 + 3 * 4 = {expresion_1}")
print(f"(2 + 3) * 4 = {expresion_2}")
print(f"2 ** 3 ** 2 = {expresion_3}")
print(f"10 - 2 * 3 + 1 = {expresion_4}")
print(f"True or False and False = {expresion_5}")
# Salida: 14, 20, 512, 5, True
